#!/usr/bin/env python3
"""Universe of Frynance — CPI, the Consumed Potato Index.

What share of a country's dietary energy comes from potatoes — and from fries
specifically? Plus a US income-decile breakdown. Reads `consumed_potato_index`.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"


def bar(pct, scale=1.4):
    return "#" * round(pct * scale)


def main() -> None:
    d = json.loads(DATA.read_text())
    cpi = d["consumed_potato_index"]
    w = cpi["world"]

    print("=" * 70)
    print("UNIVERSE OF FRYNANCE — CPI (Consumed Potato Index)")
    print("=" * 70)
    print(f"  Potato share of dietary energy supply. World: "
          f"{w['potato_kcal_pct']}% potato / {w['fry_kcal_pct']}% fries.\n")

    by_potato = sorted(cpi["countries"], key=lambda c: c["potato_kcal_pct"], reverse=True)
    print("  Ranked by POTATO calorie share:")
    print(f"  {'country':<10}{'potato%':>8}{'fry%':>7}   share of calories")
    for c in by_potato:
        print(f"  {c['country']:<10}{c['potato_kcal_pct']:>7.1f}%{c['fry_kcal_pct']:>6.1f}%   {bar(c['potato_kcal_pct'])}")

    top_potato = by_potato[0]
    top_fry = max(cpi["countries"], key=lambda c: c["fry_kcal_pct"])
    print(f"\n  The staple-vs-fry divide:")
    print(f"    Most potato-dependent : {top_potato['country']} "
          f"({top_potato['potato_kcal_pct']}% of calories) — but mostly boiled/fresh.")
    print(f"    Most FRY-dependent    : {top_fry['country']} "
          f"({top_fry['fry_kcal_pct']}% from fries) — {top_fry.get('note','')}")
    print(f"    -> highest potato-dependence is NOT highest fry-dependence.")

    # Income deciles
    dec = cpi["income_deciles"]
    print(f"\n  Income deciles — {dec['country']} (D1 = poorest, D10 = richest):")
    print(f"  {'decile':<8}{'potato%':>8}{'fry%':>7}")
    for row in dec["deciles"]:
        print(f"  D{row['d']:<7}{row['potato_pct']:>7.1f}%{row['fry_pct']:>6.1f}%")
    d1, d10 = dec["deciles"][0], dec["deciles"][-1]
    print(f"\n  Potato-calorie share falls {d1['potato_pct']}% (D1) -> {d10['potato_pct']}% (D10):"
          f" the cheap staple is leaned on more at the bottom.")
    print(f"  Fry share is flatter ({d1['fry_pct']}% -> {d10['fry_pct']}%): the rich eat fast")
    print(f"  food more OFTEN, but it's a smaller slice of their larger, more varied diet.\n")


if __name__ == "__main__":
    main()

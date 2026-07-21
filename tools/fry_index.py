#!/usr/bin/env python3
"""Universe of Frynance — the Fry Index (international PPC) + fry-flation.

Two views built on PPC (pennies per calorie):
  * Fry Index  — a McDonald's medium fries (320 cal) priced across countries,
                 à la the Big Mac Index. Where is a fry calorie cheapest?
  * Fry-flation — US McDonald's medium fries PPC over time.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"


def main() -> None:
    d = json.loads(DATA.read_text())

    # --- Fry Index (international) ---
    fi = d["fry_index"]
    cal = fi["calories"]
    rows = []
    for c in fi["countries"]:
        c["ppc"] = c["usd"] * 100 / cal
        rows.append(c)
    rows.sort(key=lambda c: c["ppc"])

    print("=" * 68)
    print("UNIVERSE OF FRYNANCE — THE FRY INDEX (international PPC)")
    print("=" * 68)
    print(f"  A McDonald's medium fries ({cal} cal), priced across the world.\n")
    print(f"  {'#':>2}  {'country':<14}{'local':>10}{'USD':>8}{'¢/cal':>8}")
    for i, c in enumerate(rows, 1):
        tag = f"  <- {c['note']}" if c.get("note") else ""
        print(f"  {i:>2}  {c['country']:<14}{c['local']:>10}{c['usd']:>8.2f}{c['ppc']:>8.2f}{tag}")
    lo, hi = rows[0], rows[-1]
    print(f"\n  A McD fry calorie costs {hi['ppc']/lo['ppc']:.1f}x more in {hi['country']} "
          f"than in {lo['country']}")
    print(f"  ({lo['ppc']:.2f} vs {hi['ppc']:.2f} ¢/cal).")

    print("\n  Local fry icons (not McD, for colour):")
    for li in fi["local_icons"]:
        ppc = li["usd"] * 100 / li["calories"]
        print(f"    {li['item']:<26}{li['usd']:>6.2f} / {li['calories']:>4} cal = {ppc:.2f} ¢/cal  ({li['note']})")

    # --- Fry-flation (over time) ---
    ff = d["fry_flation"]
    fcal = ff["calories"]
    s = ff["series"]
    print("\n" + "=" * 68)
    print("FRY-FLATION — US McDonald's medium fries over time")
    print("=" * 68)
    base_year = ff.get("base_year", s[-1]["year"])
    cpi_base = next((r["cpi_index"] for r in s if r["year"] == base_year), s[-1]["cpi_index"])
    print(f"  {'year':>6}{'nominal$':>10}{'real$ (' + str(base_year) + ')':>14}{'¢/cal':>8}")
    for r in s:
        real = r["usd"] * cpi_base / r["cpi_index"]
        ppc = r["usd"] * 100 / fcal
        bar = "#" * round(r["usd"] / s[-1]["usd"] * 24)
        print(f"  {r['year']:>6}{r['usd']:>10.2f}{real:>14.2f}{ppc:>8.2f}  {bar}")
    first, last = s[0], s[-1]
    yrs = last["year"] - first["year"]
    real_first = first["usd"] * cpi_base / first["cpi_index"]
    print(f"\n  {first['year']}->{last['year']}: ${first['usd']:.2f} -> ${last['usd']:.2f} "
          f"= {last['usd']/first['usd']:.1f}x NOMINAL over {yrs} yrs.")
    print(f"  In real {base_year} dollars: ${real_first:.2f} -> ${last['usd']:.2f} "
          f"= {last['usd']/real_first:.1f}x REAL — the fry got dearer even after inflation,")
    print(f"  most of it since 2020.\n")


if __name__ == "__main__":
    main()

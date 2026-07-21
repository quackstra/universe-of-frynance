#!/usr/bin/env python3
"""Universe of Frynance — PPC (Pennies Per Calorie).

Where is a fry calorie cheapest to buy?

    PPC = price_in_cents / calories   [US cents per calorie]

PPC is a ratio, so it is portion-independent: a medium chain fry and a whole
retail bag compare directly. Reads the `ppc` block of the dataset.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"

TIER_ICON = {"home": "🏠", "qsr": "🍔", "fast_casual": "🍟",
             "casual_dining": "🍽️", "fine_dining": "✨"}


def main() -> None:
    d = json.loads(DATA.read_text())
    entries = d["ppc"]["entries"]
    for e in entries:
        e["ppc"] = e["price_usd"] * 100 / e["calories"]
    entries.sort(key=lambda e: e["ppc"])

    print("=" * 70)
    print("UNIVERSE OF FRYNANCE — PPC (Pennies Per Calorie for a fry)")
    print("=" * 70)
    print("  Cheapest fry calorie first.\n")
    print(f"  {'#':>2}  {'source':<26}{'$':>7}{'kcal':>7}{'¢/cal':>8}  tier")
    for i, e in enumerate(entries, 1):
        icon = TIER_ICON.get(e["tier"], "  ")
        print(f"  {i:>2}  {e['source']:<26}{e['price_usd']:>7.2f}{e['calories']:>7}"
              f"{e['ppc']:>8.2f}  {icon} {e['tier']}")

    cheapest = entries[0]
    dearest = entries[-1]
    restaurants = [e for e in entries if e["tier"] != "home"]
    home = [e for e in entries if e["tier"] == "home"]
    cheap_rest = min(restaurants, key=lambda e: e["ppc"])
    home_mean = sum(e["ppc"] for e in home) / len(home)

    print(f"\n  Cheapest overall : {cheapest['source']} @ {cheapest['ppc']:.2f} ¢/cal")
    print(f"  Priciest overall : {dearest['source']} @ {dearest['ppc']:.2f} ¢/cal "
          f"({dearest['ppc']/cheapest['ppc']:.1f}x the cheapest)")
    print(f"\n  🍟 Cheapest RESTAURANT fry calorie: {cheap_rest['source']} "
          f"@ {cheap_rest['ppc']:.2f} ¢/cal")
    print(f"     — the big-portion paradox: {cheap_rest['source']} feels pricey but its")
    print(f"       huge {cheap_rest['calories']}-cal portion makes each calorie the cheapest out.")
    mcd = next((e for e in restaurants if "McDonald" in e["source"]), None)
    if mcd:
        print(f"     For contrast, McDonald's is {mcd['ppc']/cheap_rest['ppc']:.1f}x pricier per calorie.")
    print(f"\n  🏠 Home wins outright: ~{home_mean:.2f} ¢/cal, about "
          f"{cheap_rest['ppc']/home_mean:.1f}x cheaper than the best restaurant and "
          f"{dearest['ppc']/home_mean:.0f}x cheaper than fine dining.\n")


if __name__ == "__main__":
    main()

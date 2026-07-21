#!/usr/bin/env python3
"""Universe of Frynance — The Fry Bill (induced supply chain).

Two questions:
  1. How much potato demand exists ONLY because of the fry? (counterfactual)
  2. What does the world spend, sector by sector, to keep eating potatoes as
     fries — oil, salt, energy, water, labor, packaging, carbon?
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"
WORLD_PRODUCTION_MT = 375.0
FTE_HOURS = 2000.0  # full-time-equivalent hours / yr


def main() -> None:
    d = json.loads(DATA.read_text())
    fb = d["fry_bill"]
    raw = fb["fries_raw_mt"]
    finished_kg = fb["finished_fries_mt"] * 1e9
    servings = fb["servings_billion"] * 1e9

    print("=" * 70)
    print("UNIVERSE OF FRYNANCE — THE FRY BILL (the induced supply chain)")
    print("=" * 70)

    # 1. Induced potato demand
    rev = fb["induced_demand"]["revert_to_fresh_share"]
    reverted = raw * rev
    induced = raw * (1 - rev)
    print("\n  1. INDUCED POTATO DEMAND (counterfactual: if the fry didn't exist)")
    print(f"     Fries stream (raw potato)     : {raw:.1f} Mt/yr")
    print(f"     ...reverts to fresh boiled    : {reverted:.1f} Mt ({rev*100:.0f}%)")
    print(f"     ...simply not eaten (induced) : {induced:.1f} Mt ({(1-rev)*100:.0f}%)")
    print(f"     -> ~{induced:.0f} Mt of potato demand (~{induced/WORLD_PRODUCTION_MT*100:.1f}% of ALL")
    print(f"        world production) exists ONLY because we fry. The fry keeps")
    print(f"        income-elastic eaters buying potatoes (see MCE-PF).")

    # 2. Sector input bill
    print("\n  2. THE SECTOR BILL — inputs to fry the world's potatoes")
    print(f"     ({fb['finished_fries_mt']:.1f} Mt finished fries, ~{fb['servings_billion']:.0f}B servings/yr)\n")
    print(f"     {'sector':<26}{'global total':>16}   context")
    for i in fb["inputs"]:
        basis = i["basis"]
        val = i["intensity"]
        if basis == "per_kg_finished":
            total = val * finished_kg  # in the input's own kg/kWh/L units
        elif basis == "sec_per_serving":
            total = val / 3600 * servings  # hours
        elif basis == "kg_per_serving":
            total = val * servings  # kg
        else:
            total = val * finished_kg

        unit = i["unit"]
        if unit == "Mt":
            disp = f"{total/1e9:,.2f} Mt"
        elif unit == "TWh":
            disp = f"{total/1e9:,.1f} TWh"
        elif unit == "km3":
            disp = f"{total/1e12:,.1f} km3"
        elif unit == "billion_hr":
            disp = f"{total/1e9:,.2f} B hours"
        else:
            disp = f"{total:,.0f}"
        print(f"     {i['sector']:<26}{disp:>16}   {i['context']}")

    # Labor -> jobs highlight
    labor = next(x for x in fb["inputs"] if x["sector"] == "Labor")
    hours = labor["intensity"] / 3600 * servings
    print(f"\n     Labor alone = {hours/1e9:.2f} billion hours = ~{hours/FTE_HOURS/1e3:,.0f}k full-time jobs")
    oil = next(x for x in fb["inputs"] if x["sector"] == "Frying oil")
    print(f"     Oil alone   = {oil['intensity']*finished_kg/1e9:.2f} Mt — ~0.9% of all the vegetable")
    print(f"                   oil humanity produces, just to make fries crispy.\n")


if __name__ == "__main__":
    main()

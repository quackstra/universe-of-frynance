#!/usr/bin/env python3
"""Universe of Frynance — The Fry Economy (total economic impact).

The entire economic footprint of the effort to fry potatoes and keep people
eating them as incomes rise: direct + indirect (suppliers) + induced (the
spending of those workers' wages), IMPLAN / Type-II style.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"
FTE = 2000.0


def _v(x):
    return x["value"] if isinstance(x, dict) else x


def main() -> None:
    d = json.loads(DATA.read_text())
    fe = d["fry_economy"]

    fd = _v(fe["final_demand_usd_b"])
    om = _v(fe["output_multiplier"])
    vas = _v(fe["value_added_share"])
    direct = _v(fe["direct_jobs"])
    induced = _v(fe["induced_jobs"])
    suppliers = fe["supplier_jobs"]
    indirect = sum(s["jobs"] for s in suppliers)
    total_jobs = direct + indirect + induced
    emp_mult = total_jobs / direct

    total_output = fd * om
    gdp = total_output * vas

    print("=" * 68)
    print("UNIVERSE OF FRYNANCE — THE FRY ECONOMY (total economic impact)")
    print("=" * 68)

    print("\n  OUTPUT")
    print(f"    Final demand (consumer fry spend) : ${fd:,.0f} B/yr")
    print(f"    x output multiplier {om:.1f}            : ${total_output:,.0f} B total economic output")
    print(f"    Value-added (GDP contribution)    : ${gdp:,.0f} B  ({vas*100:.0f}% of output)")

    print("\n  JOBS — the fry economy's employment pyramid")
    print(f"    Direct   (fry + serve + process)  : {direct/1e6:>5.2f} M")
    print(f"    Indirect (suppliers, below)       : {indirect/1e6:>5.2f} M")
    print(f"    Induced  (worker wage-spending)   : {induced/1e6:>5.2f} M")
    print(f"    {'-'*44}")
    print(f"    TOTAL jobs                        : {total_jobs/1e6:>5.2f} M   (x{emp_mult:.1f} the direct)")

    print("\n  DOWNSTREAM SUPPLIER (INDIRECT) JOBS")
    for s in sorted(suppliers, key=lambda x: x["jobs"], reverse=True):
        bar = "#" * round(s["jobs"] / 12000)
        print(f"    {s['sector']:<38}{s['jobs']/1e3:>6.0f}k  {bar}")

    print(f"\n  In one line: keeping the world eating potatoes as fries is a")
    print(f"  ~${total_output:,.0f}B economic engine employing ~{total_jobs/1e6:.1f} million people —")
    print(f"  a workforce the size of a mid-large city's entire population,")
    print(f"  all so an inferior good stays on richer tables (see MCE-PF).\n")


if __name__ == "__main__":
    main()

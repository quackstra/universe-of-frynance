#!/usr/bin/env python3
"""Universe of Frynance — TPS (Taters Per Second).

The rate at which Earth produces potatoes, counted as whole tubers.
A cross-universe nod to Universe of Finance's TPS (transactions/second).

    TPS(annual) = production / avg_potato_weight / seconds_per_year

Monthly TPS applies a Northern-Hemisphere-weighted seasonality index. The index
is normalised by its DAY-WEIGHTED mean so the 12 monthly rates reconcile to the
annual TPS (a longer month at the same index carries more taters, but the *rate*
scales with the index alone).
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"

# Universe of Finance Big Number, for the easter egg (transactions/second).
UOF_TPS = 73_750

DAYS = {"Jan": 31, "Feb": 28.25, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
        "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}
MONTHS = list(DAYS)


def _v(x):
    return x["value"] if isinstance(x, dict) else x


def main() -> None:
    d = json.loads(DATA.read_text())
    production_mt = _v(d["big_number"]["production_mt"])
    tps = d["tps"]
    g = _v(tps["avg_potato_weight_g"])
    secs = tps["seconds_per_year"]

    production_g = production_mt * 1e6 * 1e6
    potatoes_yr = production_g / g
    annual_tps = potatoes_yr / secs

    print("=" * 62)
    print("UNIVERSE OF FRYNANCE — TPS (Taters Per Second)")
    print("=" * 62)
    print(f"\n  Production        : {production_mt:,.0f} Mt/yr")
    print(f"  Avg potato        : {g:.0f} g  ->  {potatoes_yr/1e12:,.2f} trillion taters/yr")
    print(f"\n  TPS (annual avg)  : {annual_tps:,.0f} taters / second")

    # Easter egg
    ratio = annual_tps / UOF_TPS
    print(f"\n  🥔 vs 💸  Earth grows potatoes at ~{annual_tps/1e3:,.0f}k TPS — about "
          f"{ratio:.2f}x the ~{UOF_TPS/1e3:.1f}k transactions/second")
    print(f"          of the whole global financial system (Universe of Finance).")

    # Monthly — normalise index by its day-weighted mean so rates reconcile.
    idx = tps["monthly_index"]["values"]
    dw_mean = sum(idx[m] * DAYS[m] for m in MONTHS) / sum(DAYS.values())
    print("\n  Monthly TPS (day-weighted mean of index normalised to annual):")
    print(f"  {'month':<6}{'index':>7}{'TPS':>12}   {'vs annual':>10}")
    rows = []
    for m in MONTHS:
        month_tps = annual_tps * idx[m] / dw_mean
        rows.append((m, idx[m], month_tps))
        bar = "#" * round((idx[m] / dw_mean) * 20)
        print(f"  {m:<6}{idx[m]:>7.2f}{month_tps:>12,.0f}   {(idx[m]/dw_mean-1)*100:>+9.1f}%  {bar}")

    peak = max(rows, key=lambda r: r[2])
    trough = min(rows, key=lambda r: r[2])
    # sanity: day-weighted average of monthly TPS should equal annual TPS
    check = sum(t * DAYS[m] for m, _, t in rows) / sum(DAYS.values())
    print(f"\n  Peak   : {peak[0]} @ {peak[2]:,.0f} TPS (holiday mash)")
    print(f"  Trough : {trough[0]} @ {trough[2]:,.0f} TPS (post-holiday dip)")
    print(f"  Reconciliation: day-weighted monthly mean = {check:,.0f} TPS "
          f"(annual {annual_tps:,.0f})  {'✅' if abs(check-annual_tps) < 1 else '❌'}\n")


if __name__ == "__main__":
    main()

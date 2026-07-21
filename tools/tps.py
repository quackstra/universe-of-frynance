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

    # Monthly — normalise each index by its day-weighted mean so rates reconcile.
    mi = tps["monthly_index"]
    nh = mi["values"]
    glob = mi.get("global_values", nh)

    def norm(idx):
        m0 = sum(idx[m] * DAYS[m] for m in MONTHS) / sum(DAYS.values())
        return {m: annual_tps * idx[m] / m0 for m in MONTHS}, m0

    nh_tps, nh_mean = norm(nh)
    gl_tps, gl_mean = norm(glob)

    print("\n  Monthly TPS — NH-weighted vs both-hemisphere GLOBAL (Run 4):")
    print(f"  {'month':<6}{'NH TPS':>11}{'GLOBAL TPS':>13}   {'NH vs avg':>10}")
    for m in MONTHS:
        bar = "#" * round((nh[m] / nh_mean) * 18)
        print(f"  {m:<6}{nh_tps[m]:>11,.0f}{gl_tps[m]:>13,.0f}   {(nh[m]/nh_mean-1)*100:>+9.1f}%  {bar}")

    nh_peak = max(MONTHS, key=lambda m: nh_tps[m]); nh_tr = min(MONTHS, key=lambda m: nh_tps[m])
    nh_swing = (nh_tps[nh_peak] - nh_tps[nh_tr]) / annual_tps * 100
    gl_swing = (max(gl_tps.values()) - min(gl_tps.values())) / annual_tps * 100
    check = sum(nh_tps[m] * DAYS[m] for m in MONTHS) / sum(DAYS.values())
    print(f"\n  NH   : peak {nh_peak} {nh_tps[nh_peak]:,.0f} / trough {nh_tr} {nh_tps[nh_tr]:,.0f}"
          f"  (swing {nh_swing:.0f}% of annual)")
    print(f"  GLOBAL: far flatter — swing only {gl_swing:.0f}% (SH offsets the North; holiday")
    print(f"          spike is a Northern/Western thing).")
    print(f"  Reconciliation: day-weighted monthly mean = {check:,.0f} TPS "
          f"(annual {annual_tps:,.0f})  {'✅' if abs(check-annual_tps) < 1 else '❌'}\n")


if __name__ == "__main__":
    main()

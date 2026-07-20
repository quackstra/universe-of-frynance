#!/usr/bin/env python3
"""Universe of Frynance — mass-balance reconciliation (the integrity gate).

Loads data/global_massbalance.json and:
  1. Prints the Big Number (production, per-capita).
  2. Prints the Tier-1 fate Sankey in Mt and % of production.
  3. ENFORCES the 100% gate: Tier-1 fate shares must sum to 100% (+/- tolerance).
  4. Expands Tier-2 processing and the fries stream.
  5. Reports Food Loss & Waste as a separate overlay (never summed into Tier-1).

Exit code is non-zero if the 100% gate fails — usable as a pre-publish check.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"
TOLERANCE_PCT = 0.5

CONF_ICON = {"high": "🟢", "medium": "🟡", "low": "🔴"}


def _v(x):
    return x["value"] if isinstance(x, dict) else x


def main() -> None:
    d = json.loads(DATA.read_text())
    bn = d["big_number"]
    production = _v(bn["production_mt"])

    print("=" * 66)
    print("UNIVERSE OF FRYNANCE — MASS BALANCE (the 100% gate)")
    print("=" * 66)
    print(f"\n  Big Number       : {production:,.1f} Mt potato / yr")
    print(f"  Per-capita       : {_v(bn['per_capita_kg']):.1f} kg/person/yr")

    fates = d["tier1_fates"]
    total_pct = sum(f["share_pct"] for f in fates)

    print("\n  Tier-1 fates (must sum to 100% of production):")
    print(f"  {'fate':<28}{'share':>8}{'Mt':>10}   conf")
    for f in sorted(fates, key=lambda x: x["share_pct"], reverse=True):
        mt = production * f["share_pct"] / 100
        icon = CONF_ICON.get(f.get("confidence", ""), "  ")
        print(f"  {f['name']:<28}{f['share_pct']:>7}%{mt:>10.1f}   {icon}")
    print(f"  {'-'*54}")
    print(f"  {'TOTAL':<28}{total_pct:>7}%{production:>10.1f}")

    ok = abs(total_pct - 100.0) <= TOLERANCE_PCT
    gate = "PASS ✅" if ok else f"FAIL ❌ (off by {total_pct-100:+.1f} pts)"
    print(f"\n  100% MASS-BALANCE GATE: {gate}")

    # Tier 2: processing split
    proc_pct = next(f["share_pct"] for f in fates if f["slug"] == "processing")
    proc_mt = production * proc_pct / 100
    print(f"\n  Tier-2 processing split (of {proc_mt:.1f} Mt processed):")
    p_total = sum(p["share_of_processing_pct"] for p in d["tier2_processing"])
    for p in sorted(d["tier2_processing"], key=lambda x: x["share_of_processing_pct"], reverse=True):
        mt = proc_mt * p["share_of_processing_pct"] / 100
        icon = CONF_ICON.get(p.get("confidence", ""), "  ")
        print(f"    {p['name']:<32}{p['share_of_processing_pct']:>6}%{mt:>9.1f} Mt  {icon}")
    if abs(p_total - 100) > TOLERANCE_PCT:
        print(f"    ⚠️  processing split sums to {p_total}% (should be 100)")

    # Fries stream
    frozen_pct = next(p["share_of_processing_pct"] for p in d["tier2_processing"] if p["slug"] == "frozen")
    fries_share = _v(d["fries_within_frozen_pct"])
    fries_mt = proc_mt * frozen_pct / 100 * fries_share / 100
    print(f"\n  Fries stream     : {fries_mt:.1f} Mt  "
          f"({fries_mt/production*100:.1f}% of all production) -> feeds Real MUSHT")

    # FLW overlay — reported, NOT summed
    flw = d["food_loss_waste_overlay"]
    flw_pct = _v(flw["chain_loss_pct"])
    print(f"\n  Conscience Number (FLW overlay, NOT in the 100% total):")
    print(f"    ~{flw_pct}% of the harvest lost/wasted field->consumer "
          f"(~{production*flw_pct/100:.0f} Mt).")
    print(f"    {flw['note']}\n")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

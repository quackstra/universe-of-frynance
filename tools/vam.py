#!/usr/bin/env python3
"""Universe of Frynance — the Value-Add Battery (VAM + MCE-PF).

How many ways can we measure the value of turning a potato into a fry?

  * MCE-PF — Marginal Consumption Elasticity of Processing a Fry:
             the income elasticity ADDED by processing (inferior -> normal).
  * VAM    — Value-Add Multiplier: the fry's price over the farm-gate value of
             the potato it contains (and the farmer's share of the fry dollar).
  * plus calorie-density and willingness-to-pay multipliers.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    va = d["value_add"]
    fg = va["farm_gate_usd_per_kg"]["value"]

    print("=" * 70)
    print("UNIVERSE OF FRYNANCE — THE VALUE-ADD BATTERY (potato -> fry)")
    print("=" * 70)

    # A. MCE-PF (elasticity)
    ep = va["elasticity"]["potato"]
    ef = va["elasticity"]["fry"]
    mce = ef["central"] - ep["central"]
    cands = [mce, ef["low"] - ep["low"], ef["high"] - ep["high"]]
    print("\n  A. MCE-PF — Marginal Consumption Elasticity of Processing a Fry")
    print(f"     income elasticity:  raw potato {ep['central']:+.1f} (inferior)  |  "
          f"fry {ef['central']:+.1f} (normal)")
    print(f"     MCE-PF = e_fry - e_potato = {mce:+.1f}  (range {min(cands):+.1f} to {max(cands):+.1f})")
    print(f"     -> processing ADDS ~{mce:+.1f} of income-elasticity: it turns an")
    print(f"        inferior good into a normal one. THIS is the value-add.")

    # B. VAM ladder
    print("\n  B. VAM — Value-Add Multiplier (price vs farm-gate potato inside it)")
    print(f"     farm-gate potato: ${fg:.2f}/kg\n")
    print(f"     {'venue':<30}{'price':>8}{'potato$':>9}{'VAM':>8}{'farm share':>12}")
    for v in va["venues"]:
        potato_cost = v["raw_input_g"] / 1000 * fg
        vam = v["price_usd"] / potato_cost
        share = potato_cost / v["price_usd"] * 100
        print(f"     {v['venue']:<30}{v['price_usd']:>8.2f}{potato_cost:>9.3f}{vam:>7.0f}x{share:>11.1f}%")
    qsr = next(v for v in va["venues"] if "QSR" in v["venue"])
    qsr_cost = qsr["raw_input_g"] / 1000 * fg
    qsr_vam = qsr["price_usd"] / qsr_cost
    print(f"\n     A QSR fry is worth ~{qsr_vam:.0f}x the farm-gate potato in it — the farmer")
    print(f"     keeps ~{qsr_cost/qsr['price_usd']*100:.1f}% (~{qsr_cost*100:.0f} cents of a ${qsr['price_usd']:.2f} fry).")

    # C. Calorie multiplier
    cd = va["calorie_density_kcal_per_kg"]
    print("\n  C. CTM — Caloric Transformation Multiplier")
    print(f"     {cd['raw']} -> {cd['fried']} kcal/kg = {cd['fried']/cd['raw']:.1f}x energy density (added oil).")

    # D. WTP premium
    p = va["ppc_ref"]
    print("\n  D. WTP — willingness-to-pay premium (pennies per calorie)")
    print(f"     DIY raw {p['raw_home']} -> QSR {p['qsr_mcd']} -> fine dining {p['fine_dining']} c/cal")
    print(f"     = up to {p['fine_dining']/p['raw_home']:.0f}x more paid per calorie for the served fry.")

    print("\n  Every lens measures the same thing: the fry is what a potato becomes")
    print("  to survive rising income. MCE-PF is why the processing industry exists.\n")


if __name__ == "__main__":
    main()

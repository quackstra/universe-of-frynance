#!/usr/bin/env python3
"""Universe of Frynance — MUSHT calculator (Make Underutilized Spuds Have Taste).

MUSHT is the hero/fun number: if every potato Earth grows in a year were extruded
into one perfectly straight french fry, 0.75 cm x 0.75 cm square, how long is the
line?

    Volume   = production_mass / potato_density        [cm^3]
    Length   = Volume / fry_cross_section_area          [cm]
    MUSHT    = Length converted to miles

We report two figures on the same raw-potato-volume basis:
  * Idealized MUSHT — 100% of production.
  * Real MUSHT      — only the spuds that actually become fries, derived from the
                      mass balance (Tier-1 processing x Tier-2 frozen x fries share).

All inputs come from data/global_massbalance.json so the number stays sourced.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "global_massbalance.json"

# Geometry / conversions
FRY_SIDE_CM = 0.75
FRY_AREA_CM2 = FRY_SIDE_CM * FRY_SIDE_CM          # 0.5625 cm^2
MI_PER_KM = 0.621371
KM_PER_AU = 1.495978707e8                          # astronomical unit
EARTH_EQUATOR_KM = 40075.0
EARTH_MOON_KM = 384400.0
EARTH_SUN_KM = 1.495978707e8
LIGHT_KM_PER_S = 299792.458
PLUTO_AVG_AU = 39.5


def _v(x):
    return x["value"] if isinstance(x, dict) else x


def fry_length_km(mass_mt: float, density_g_cm3: float) -> float:
    """Length of a 0.75cm-square fry from `mass_mt` million tonnes of potato."""
    mass_g = mass_mt * 1e6 * 1e6            # Mt -> tonnes -> grams
    volume_cm3 = mass_g / density_g_cm3
    length_cm = volume_cm3 / FRY_AREA_CM2
    return length_cm / 1e5                  # cm -> km


def fries_fraction(d: dict) -> float:
    """Fraction of total production that becomes fries, from the mass balance."""
    proc = next(f for f in d["tier1_fates"] if f["slug"] == "processing")["share_pct"] / 100
    frozen = next(p for p in d["tier2_processing"] if p["slug"] == "frozen")["share_of_processing_pct"] / 100
    fries = _v(d["fries_within_frozen_pct"]) / 100
    return proc * frozen * fries


def _wow(length_km: float) -> list[str]:
    miles = length_km * MI_PER_KM
    au = length_km / KM_PER_AU
    return [
        f"{length_km / EARTH_EQUATOR_KM:,.0f} times around the equator",
        f"{miles / (EARTH_MOON_KM * MI_PER_KM):,.0f} one-way trips to the Moon",
        f"{miles / (2 * EARTH_SUN_KM * MI_PER_KM):,.1f} round-trips to the Sun",
        f"{au:,.1f} AU — " + (f"past Pluto's average orbit (~{PLUTO_AVG_AU} AU)" if au > PLUTO_AVG_AU else f"out to ~{au:.0f} AU"),
        f"a photon needs {length_km / LIGHT_KM_PER_S / 3600:,.1f} hours to travel its length",
    ]


def main() -> None:
    d = json.loads(DATA.read_text())
    production = _v(d["big_number"]["production_mt"])
    density = _v(d["density_g_per_cm3"])

    ideal_km = fry_length_km(production, density)
    frac = fries_fraction(d)
    real_km = ideal_km * frac

    def report(title, km):
        miles = km * MI_PER_KM
        print(f"\n  {title}")
        print(f"    length : {km:,.0f} km  =  {miles/1e9:,.2f} billion miles")

    print("=" * 66)
    print("UNIVERSE OF FRYNANCE — MUSHT (Make Underutilized Spuds Have Taste)")
    print("=" * 66)
    print(f"\n  Big Number : {production:,.0f} Mt potato / yr  (density {density} g/cm^3)")
    print(f"  Fry cut    : {FRY_SIDE_CM} x {FRY_SIDE_CM} cm  (area {FRY_AREA_CM2} cm^2)")

    report("IDEALIZED MUSHT (100% of production):", ideal_km)
    for line in _wow(ideal_km):
        print(f"      - {line}")

    report(f"REAL MUSHT (only fries — {frac*100:.1f}% of production):", real_km)
    for line in _wow(real_km):
        print(f"      - {line}")

    print(f"\n  The gap ({(ideal_km-real_km)*MI_PER_KM/1e9:,.2f} billion miles of 'fry we never make')")
    print("  is itself a headline: most of the spud is not a fry.\n")


if __name__ == "__main__":
    main()

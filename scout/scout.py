#!/usr/bin/env python3
"""Universe of Frynance — Scout. Prints the ranked research backlog.

Run 0 is a lightweight reader: it surfaces the backlog and source registry so an
Elf (or a human) sees what to work next, inside-out. Later runs can score
priority = mass_share × sourcing_confidence_gap automatically.
"""
from __future__ import annotations

import pathlib

import yaml  # PyYAML; fall back to a tiny parser message if unavailable.

HERE = pathlib.Path(__file__).resolve().parent


def main() -> None:
    backlog = yaml.safe_load((HERE / "backlog.yaml").read_text())["backlog"]
    active = [b for b in backlog if b.get("status") != "parked"]
    active.sort(key=lambda b: b["priority"])
    print("UNIVERSE OF FRYNANCE — SCOUT BACKLOG (inside-out)")
    print("=" * 60)
    for b in active:
        print(f"  [{b['priority']:>2}] {b['id']:<10} {b['fate']:<26} {b['status']}")
        print(f"       {b['task']}")
    parked = [b for b in backlog if b.get("status") == "parked"]
    if parked:
        print("\n  Parked (Run-2 stretch):")
        for b in parked:
            print(f"    - {b['id']}: {b['task']}")


if __name__ == "__main__":
    main()

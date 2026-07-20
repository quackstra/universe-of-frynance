# Universe of Frynance — Claude Operating Notes

Sister project to Universe of Finance and Universe of Movement. Read
[BRIEF.md](BRIEF.md) and [TAXONOMY.md](TAXONOMY.md) before non-trivial work.

## What this project is

An open, reproducible mass balance of the world's potatoes: the Big Number
(~375 Mt/yr production) partitioned into fates, plus the MUSHT hero number
(miles of french fry).

## Non-negotiable rules

- **The 100 % gate is sacred.** Tier-1 fate shares in
  `data/global_massbalance.json` must always sum to 100 % of production. If you
  change one share, re-balance the others. `tools/massbalance.py` exits non-zero
  if the gate fails — treat that as a blocker.
- **Never sum Food Loss & Waste into the Tier-1 total.** FLW is a cross-cutting
  overlay (it spans several fates). Summing it double-counts. Report it separately
  as the Conscience Number.
- **Fresh-weight basis** for all fate shares unless a capsule explicitly states a
  product-weight → fresh-weight conversion (and shows the math in `workings/`).
- **MUSHT is raw-potato volume** (ρ ≈ 1.08 g/cm³), 0.75 cm × 0.75 cm cut. Don't
  silently switch to cooked/finished-fry volume — that's a different number.
- **Categories, not brands, in Run 1.** Chain-level fry cuts (curly/crinkle by
  restaurant) are a Run-2 stretch.
- **Cite everything, confidence-tag everything** (🟢/🟡/🔴). Show all math in
  `workings/`.

## Workflow

`Scout → Architect → Elves → Publish`. After any data edit, run
`python3 tools/massbalance.py && python3 tools/musht.py` and confirm the gate
passes before committing. Commit prefix: `[UoFry]`.

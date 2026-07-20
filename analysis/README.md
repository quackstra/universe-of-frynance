# Universe of Frynance — Research Index

The Big Number and its fates. Each fate becomes a capsule under
`analysis/<fate>/<category>/` with a `REPORT.md`, `data.json`, `workings/`, and
charts. Run-0 shares are 🔴 placeholders that reconcile to 100 % by construction.

## Fate Leaderboard (Run 0 — placeholders)

| # | Fate | Mt/yr | Share | Confidence |
|---|------|-------|-------|------------|
| 1 | Fresh / table food | 165.0 | 44.0 % | 🔴 |
| 2 | Processing (food) | 75.0 | 20.0 % | 🔴 |
| 3 | Animal feed | 41.2 | 11.0 % | 🔴 |
| 4 | Waste & loss (accounted) | 37.5 | 10.0 % | 🔴 |
| 5 | Seed (replanting) | 33.8 | 9.0 % | 🔴 |
| 6 | Industrial (non-food) | 22.5 | 6.0 % | 🔴 |
| | **TOTAL** | **375.0** | **100 %** | — |

**Processing (Tier 2) →** Frozen 37.5 · Crisps 16.5 · Dehydrated 11.2 ·
Canned/other 9.8 Mt. **Fries stream ≈ 31.9 Mt (8.5 % of all production).**

**Conscience overlay (not in the 100 %):** ~33 % FLW ≈ 124 Mt lost/wasted.

## Aggregate

- [**The Big Number + MUSHT**](aggregate/BIG_NUMBER.md) — production, per-capita,
  and the miles-of-fry hero number.

## Capsules (to be written — inside-out)

- [ ] `fresh_food/` — FRY-002
- [ ] `processing/` — FRY-003 (+ Tier-2 split)
- [ ] `processing/frozen_fries/` — FRY-004 (total fries + cut mix)
- [ ] `waste_loss/` — FRY-005 (FLW overlay)
- [ ] `feed/` — FRY-006
- [ ] `seed/` — FRY-007
- [ ] `industrial/` — FRY-008

Reproduce the headline numbers any time:

```bash
python3 tools/massbalance.py   # Big Number + 100% gate
python3 tools/musht.py         # MUSHT
```

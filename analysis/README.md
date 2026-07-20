# Universe of Frynance — Research Index

The Big Number and its fates. Each fate becomes a capsule under
`analysis/<fate>/<category>/` with a `REPORT.md`, `data.json`, `workings/`, and
charts. Run-1 shares are sourced (FAO / CIP / FAOSTAT) and reconcile to 100 %.

## Fate Leaderboard (Run 1 — sourced)

| # | Fate | Mt/yr | Share | Confidence |
|---|------|-------|-------|------------|
| 1 | [Fresh / table food](fresh_food/REPORT.md) | 195.0 | 52.0 % | 🟡 |
| 2 | [Processing (food)](processing/REPORT.md) | 52.5 | 14.0 % | 🟡 |
| 3 | Animal feed | 45.0 | 12.0 % | 🔴 |
| 4 | Seed (replanting) | 33.8 | 9.0 % | 🔴 |
| 5 | [Waste & loss (accounted)](waste_loss/REPORT.md) | 30.0 | 8.0 % | 🔴 |
| 6 | Industrial (non-food) | 18.8 | 5.0 % | 🔴 |
| | **TOTAL** | **375.0** | **100 %** | — |

**Processing (Tier 2) →** Frozen 26.2 · Crisps 12.6 · Dehydrated 7.3 ·
Canned/other 6.3 Mt. **[Fries stream](processing/frozen_fries/REPORT.md) ≈ 22.3 Mt
(5.9 % of all production).**

**Conscience overlay (not in the 100 %):** ~45 % full-chain FLW ≈ 169 Mt
lost/wasted (range 25–60 %). See [waste_loss](waste_loss/REPORT.md).

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

# Universe of Frynance — Research Index

The Big Number and its fates. Each fate becomes a capsule under
`analysis/<fate>/<category>/` with a `REPORT.md`, `data.json`, `workings/`, and
charts. Run-1 shares are sourced (FAO / CIP / FAOSTAT) and reconcile to 100 %.

## Fate Leaderboard (Run 2 — country-weighted)

| # | Fate | Mt/yr | Share | Confidence |
|---|------|-------|-------|------------|
| 1 | [Fresh / table food](fresh_food/REPORT.md) | 183.8 | 49.0 % | 🟡 |
| 2 | [Processing (food)](processing/REPORT.md) | 63.8 | 17.0 % | 🟡 |
| 3 | Animal feed | 45.0 | 12.0 % | 🔴 |
| 4 | Seed (replanting) | 33.8 | 9.0 % | 🔴 |
| 5 | [Waste & loss (accounted)](waste_loss/REPORT.md) | 30.0 | 8.0 % | 🔴 |
| 6 | Industrial (non-food) | 18.8 | 5.0 % | 🔴 |
| | **TOTAL** | **375.0** | **100 %** | — |

**Processing (Tier 2) →** Frozen 35.1 · Crisps 14.0 · Dehydrated 8.3 ·
Canned/other 6.4 Mt. **[Fries stream](processing/frozen_fries/REPORT.md) ≈ 29.8 Mt
(7.9 % of all production).**

**Deep dive:** [Fry cuts by geometry & chain](deep-dives/fry-cuts-by-chain/REPORT.md)
— straight 72 % · curly 4 % (**≈ 12 M miles/yr, mostly Arby's**) · waffle 5 %
(Chick-fil-A).

**Conscience overlay (not in the 100 %):** ~45 % full-chain FLW ≈ 169 Mt
lost/wasted (range 25–60 %). See [waste_loss](waste_loss/REPORT.md).

## Aggregate

- [**The Big Number + MUSHT**](aggregate/BIG_NUMBER.md) — production, per-capita,
  and the miles-of-fry hero number.
- [**TPS — Taters Per Second**](aggregate/TPS.md) — the rate number (~79,000/s),
  annual + month-by-month; 🥔 > global finance 💸.

## Deep dives

- [**Fry cuts by geometry, chain & tier**](deep-dives/fry-cuts-by-chain/REPORT.md)
  — straight/curly/waffle + QSR→fast-casual→casual→fine→independent tiers.
- [**Fry companions tracker**](deep-dives/fry-companions/REPORT.md) — what's most
  often sold with a fry (burger #1).
- [**PPC — Pennies Per Calorie**](deep-dives/ppc/REPORT.md) — where a fry calorie
  is cheapest (home ~0.24 ¢/cal; Five Guys beats McDonald's 2:1).
- [**The Fry Index & fry-flation**](deep-dives/fry-index/REPORT.md) — PPC across
  countries (4.7× Zurich vs Mumbai) and over time (3.9× nominal / 2.1× real).
- [**CPI — the Consumed Potato Index**](deep-dives/consumed-potato-index/REPORT.md)
  — potato & fry share of calories by country and US income decile.
- [**The Value-Add Battery (MCE-PF & VAM)**](deep-dives/value-add/REPORT.md) — how
  many ways to measure the value of turning a potato into a fry (elasticity +0.5,
  price 74×, calories 4×, WTP 8×).
- [**The Fry Bill (induced supply chain)**](deep-dives/fry-bill/REPORT.md) —
  potatoes existing only because we fry (~18 Mt) + the sector input bill (oil,
  salt, energy, water, labor, packaging, CO₂e).
- [**The Fry Economy (total economic impact)**](deep-dives/fry-economy/REPORT.md)
  — ~$285 B output, ~$128 B GDP, ~2.25 M jobs (direct + indirect + induced), with
  a downstream supplier-jobs breakdown.

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

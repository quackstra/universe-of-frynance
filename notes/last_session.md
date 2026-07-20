# Last Session — Universe of Frynance

## Run 1 — sourced mass balance + dashboard (2026-07-20)

Pushed to GitHub (private) and ran a research pass replacing Run-0 placeholders
with sourced figures.

### Data locked (with citations in data/global_massbalance.json)
- **Production 375 Mt** (FAOSTAT 2022; China 95.5 Mt / 25.5 %, India 56 Mt /
  15 %). 🟢
- **Tier-1 fates** (sum to 100 %): Fresh 52 % 🟡 · Processing 14 % 🟡 · Feed 12 %
  🔴 · Seed 9 % 🔴 · Waste(accounted) 8 % 🔴 · Industrial 5 % 🔴.
- **Tier-2 processing**: Frozen 50 · Crisps 24 · Dehydrated 14 · Canned/other 12
  (% of processing). Fries = frozen × 85 % = **22.3 Mt = 5.9 % of production**.
- **FLW overlay ~45 %** (~169 Mt, range 25–60 %) — reported separately, NOT in
  the 100 % (anti-double-count vs the 8 % FBS losses line).

### MUSHT (verified via tools/musht.py)
- Idealized **3.84 B miles** (41 AU, past Pluto).
- Real **0.23 B miles** (fries only). Gap ≈ 3.6 B miles → "~1 potato in 17 is a
  fry."

### Capsules written
fresh_food, processing (+ frozen_fries), waste_loss — each REPORT.md with sources.

### Dashboard
Self-contained `index.html` (Chart.js, potato/fry palette) forked from the
Movement template: hero (Production / MUSHT / Waste), fate leaderboard, fate
doughnut + processing bar, MUSHT deep-dive, insights.

## ⚠️ Open decision for Ferg
**GitHub Pages is blocked because the repo is private** ("plan does not support
Pages for this repository"). The sibling sites (Finance, Movement) are **public**.
To publish at `quackstra.github.io/universe-of-frynance`, the repo must be flipped
public (or the plan upgraded). Did NOT flip it — public is a one-way door and
needs Ferg's explicit OK. The dashboard is committed and ready the moment it goes
public.

## Next (Run 2)
Country-weighted FBS rebuild (China+India+EU+US) to move Tier-1 to 🟡/🟢; USDA
ERS + Eurostat processing tonnages; stage-resolved FLW; Sankey chart; parked
chain-level fry-cut deep dive (FRY-R2-001).

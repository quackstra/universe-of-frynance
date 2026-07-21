# Last Session — Universe of Frynance

## Run 3 — TPS, restaurant tiers & fry-companions tracker (2026-07-20)

Live at quackstra.github.io/universe-of-frynance.

### New metric: TPS — Taters Per Second (`tools/tps.py`, `analysis/aggregate/TPS.md`)
- **Annual TPS ≈ 79,220/s** (375 Mt ÷ 150 g avg potato ÷ 31,557,600 s = 2.5 T
  taters/yr). Easter egg: ~1.07× the Universe of Finance Big Number (~73,750
  transactions/s) — 🥔 > 💸.
- **Monthly TPS**: NH consumption-seasonality index, normalised by its
  DAY-WEIGHTED mean so the 12 months reconcile exactly to annual (verified ✅).
  Peak Nov 89,216 (Thanksgiving), trough Jan 69,821 (post-holiday dip).
- Avg potato weight 150 g is 🟡 (US medium russet ~170-180 g; sensitivity: 130 g
  → 91k TPS, 180 g → 66k TPS).

### Restaurant-tier fry mapping (expanded fry-cuts deep dive)
QSR / fast-casual / casual-dining / fine-dining / **independent (non-chain)**.
Key finding: independents (~half of units) are the largest, most varied
fry-volume tier — chains are the short head anchoring signatures (waffle=CFA,
curly=Arby's, crinkle=Shake Shack/Culver's, steak fries=Red Robin, hand-cut=Five
Guys); the long tail fills the rest. Data in `restaurant_tiers` (🔴).

### Fry-companions tracker (`analysis/deep-dives/fry-companions/`)
Share of fry-accompanied orders: burger 38 · chicken 24 · sandwich 12 · fish 8 ·
hot dog 7 · wings 5 · steak 3 · solo 3 %. Ubiquitous: soda + ketchup (regional
dips: mayo/vinegar/poutine). v1 estimates 🔴 — Run-4 to ground with POS/menu-mix.

### Dashboard
Added a **TPS section** (annual stat grid + monthly line chart with Nov peak
marker + annual-average dashed line), a **companions bar**, a **restaurant-tier**
note, a 4th hero stat (TPS), nav link, and 3 new insight cards. Run 3 badge/footer.

## Data structures added to global_massbalance.json
`tps` (avg_potato_weight_g, seconds_per_year, monthly_index+drivers),
`restaurant_tiers`, `fry_companions`. Mass-balance gate still PASS (unchanged
Tier-1).

## Next (Run 4)
- Ground fry-companion attach with POS/menu-mix panels; split by tier.
- Quantify per-tier fry volume (independents vs chains) for a true global cut mix.
- Processor-reported fry volumes (McCain/Lamb Weston/Simplot) → fries toward 🟢.
- Global (both-hemisphere) TPS seasonality vs the current NH-weighted index.

# Last Session — Universe of Frynance

## Run 4 — grounding pass (2026-07-20)

Put sourced numbers on the Run-3 scaffolds. Live at
quackstra.github.io/universe-of-frynance.

### Processor corroboration (fries tonnage 🟡, better corroborated)
- **McCain ~1 in 4 fries worldwide** (~$9B, world #1); Lamb Weston #2 (NA leader);
  Simplot ~3 Mt potatoes/yr. `fry_processors` block + frozen_fries capsule table.
- Raw vs finished: 29.8 Mt **raw** (MUSHT basis) ≈ **14.9 Mt finished** at ~50 %
  yield. McCain's "1 in 4" of ~15 Mt finished is the right order of magnitude, so
  ~30 Mt raw holds.

### Chain vs independent foodservice split (now 🟡)
- US: ~422,001 independent vs ~263,000 chain units (2024); independents ~67 % of
  sales. Chains over-index on fries (~45 % of fry volume) but the **independent
  tail still carries ~55 %**. `restaurant_fry_volume` block; capsule table +
  dashboard stacked bar. (Retail/home fries are a separate slice.)

### Both-hemisphere GLOBAL TPS (new second curve)
- `global_index = 1 + 0.4 × (NH index − 1)` — damped for SH offset + weak-
  seasonality populations. Holiday swing **24 % NH → ~10 % global**. `tools/tps.py`
  prints NH and GLOBAL side by side (both reconcile ✅). Dashboard TPS chart now
  has both lines.

### Data blocks added
`fries_finished`, `fry_processors`, `restaurant_fry_volume`, and
`tps.monthly_index.global_values`. Mass-balance gate unchanged (PASS).

### Gotcha fixed this run
An Edit anchored on `food_loss_waste_overlay` created an orphan key (assumed it
followed `fries_within_frozen_pct`; it didn't). Caught by the JSON parse check
before commit. Lesson: verify the anchor's neighbour, don't assume ordering.

## Next (Run 5)
- Exact processor tonnages from McCain/Lamb Weston/Simplot filings + frozen-fry
  trade flows → push fries toward 🟢.
- Ground fry-companion attach with POS/menu-mix panels; split by tier.
- Hemisphere-resolved TPS damping from real consumption data (replace the 0.4).
- Feed / seed / industrial still 🔴 — direct FAO FBS pull.

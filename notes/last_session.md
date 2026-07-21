# Last Session — Universe of Frynance

## Run 2 — country-weighted rebuild + fry-cut deep dive (2026-07-20)

Public repo live at github.com/quackstra/universe-of-frynance; dashboard at
quackstra.github.io/universe-of-frynance.

### Data upgrades (confidence 🔴 → 🟡 on the headline fates)
- **Processing 14 % → 17 %**, now a country-weighted rebuild (weighted mean
  17.2 %): US 70 % · EU ~45 % · China 15 % · India 7 % · RoW ~8 %, weighted by
  production share. See `country_processing` in the data file.
- **Fresh 52 % → 49 %** (residual after processing rose).
- **Tier-2 frozen 50 % → 55 %**, USDA-grounded: US used 176 M cwt raw for frozen
  (61 % of US processing) vs 57.8 M cwt for chips/shoestrings in 2022.
- **Fries 22.3 → 29.8 Mt = 7.9 %** of production. Real MUSHT **0.23 → 0.30 B mi**.
  "~1 potato in 13 becomes a fry."

### Fry-cut deep dive (FRY-R2-001 — the fun one)
`analysis/deep-dives/fry-cuts-by-chain/`. Cut mix of the fries stream (straight
72 · crinkle 8 · wedge 6 · waffle 5 · tots 5 · curly 4 %). Headline:
**🌀 curly fry ≈ 12 M straight-equivalent miles/yr (~26 round-trips to the Moon),
almost all Arby's**; waffle (~15 M mi) is Chick-fil-A (fastest-growing cut,
+14 % 2024). `tools/musht.py` now prints the per-cut table. Geometry caveat noted
(curly/waffle aren't literal 0.75 cm straight lines).

### Dashboard
Upgraded to Run 2: new numbers everywhere, a **Sankey** (production → fate →
processing → fries, via chartjs-chart-sankey) and a **fry-cut bar**. Curly-fry
insight card added.

## Sources added this run
USDA NASS Potatoes 2022/23; USDA ERS "Fries on the rise"; global-agriculture &
freshplaza on China 15 %; Springer China/India potato review; Coherent Market
Insights fry-cut market; AJC Chick-fil-A ~$24B; chefstandards chain fries.

## Next (Run 3)
- Processor-reported fry volumes (McCain / Lamb Weston / Simplot) + frozen-fry
  trade data to move fries from 🟡 toward 🟢.
- Stage-resolved FLW (field/storage/processing/retail/consumer).
- Feed / seed / industrial still 🔴 — need a direct FAO FBS pull.
- Historic arc: rise of the frozen fry (mid-20thC → now).

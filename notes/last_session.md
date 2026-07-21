# Last Session — Universe of Frynance

## Run 7 — CPI (Consumed Potato Index) + real fry-flation (2026-07-20)

Live at quackstra.github.io/universe-of-frynance.

### CPI — Consumed Potato Index (`tools/cpi.py`, `consumed_potato_index` block)
- Potato's share of a country's dietary energy supply (as-eaten, incl. fry oil),
  with a fries sub-share.
- Country ranking (potato% / fry%): Rwanda 11/0.2 · Belarus 11/1.0 · Ukraine
  9/0.8 · Peru 6/0.6 · Poland 6/1.0 · UK 5.5/2.5 · Ireland 5/1.8 · USA 3.5/2.0 ·
  China 2.5/0.5 · India 2/0.3 · World 2.4/0.4.
- **Headline: most potato-dependent ≠ most fry-dependent.** Rwanda/Belarus lean
  hardest on the potato but as fresh/boiled staple; the UK & US are the FRY
  nations (highest fried-potato calorie share).
- **Income deciles (US):** potato-calorie share falls 4.6% (D1) → 2.4% (D10) —
  cheap staple feeds tight budgets (ties to PPC). Fry curve flatter (2.4→1.7) —
  the honest nuance: fast-food FREQUENCY rises with income (CDC 31.7%→42.0%) but
  lower-income diets draw a higher SHARE of FAFH calories from cheap fried food
  (ERS 16.4% vs 15.3%). Modeled 🔴.

### Real fry-flation (Run-7 base item)
- Added cpi_index (US CPI-U) to fry_flation; fry_index.py now prints nominal +
  real(2025$). **2000→2025: 3.9× nominal but ~2.1× REAL** — the fry doubled even
  after inflation, almost all post-2020 ($3.58→$4.29 real). Dashboard fry-flation
  chart now has nominal + real lines.

### Dashboard
New **CPI section**: country grouped bar (potato vs fry %) + income-decile line.
Real-$ line added to fry-flation. 3 new insight cards, nav link, Run 7 badge.

## Full metric stack
Big Number · per-capita · MUSHT · TPS · PPC · Fry Index (+fry-flation nominal &
real) · **CPI (Consumed Potato Index)** · Conscience. Tools: massbalance, musht,
tps, ppc, fry_index, cpi, scout. Gate PASS.

## Next (Run 8)
- PPP-adjust the Fry Index (still nominal FX); "minutes of median wage per fry".
- Ground the CPI with real FAO FBS potato-DES-share numbers (replace modeled).
- Direct potato-by-income-decile survey data (replace the modeled deciles).
- Still-open: exact processor tonnages; POS companion attach; FBS feed/seed pull;
  ground casual/fine-dining PPC rows.

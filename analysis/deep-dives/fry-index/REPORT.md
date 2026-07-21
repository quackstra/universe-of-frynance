# Deep Dive — The Fry Index (international PPC & fry-flation)

**Run 6 · Confidence 🟡**

Two extensions of [PPC](../ppc/REPORT.md): across **space** (countries) and across
**time** (years), using a McDonald's medium fries (320 cal) as a common unit — the
Big Mac Index's starchy cousin.

## The Fry Index — where a fry calorie is cheapest on Earth

| # | Country | McD medium | USD | **¢/cal** |
|---|---------|-----------|-----|-----------|
| 1 | 🇮🇳 India | ₹110 | $1.32 | **0.41** ← cheapest |
| 2 | 🇯🇵 Japan | ¥330 | $2.21 | 0.69 |
| 3 | 🇬🇧 UK | £1.79 | $2.27 | 0.71 |
| 4 | 🇪🇺 Eurozone | €3.20 | $3.49 | 1.09 |
| 5 | 🇺🇸 USA | $3.56 | $3.56 | 1.11 |
| 6 | 🇨🇭 Switzerland | CHF 5.60 | $6.16 | **1.93** ← priciest |

**A McDonald's fry calorie costs ~4.7× more in Zurich than in Mumbai** (1.93 vs
0.41 ¢/cal). Like the Big Mac Index, this partly reflects local wages and price
levels, not just "fry value."

### Local fry icons (for colour, not McD)
- **UK chippy chips** — ~£3 for a big portion (~700 cal) → **0.55 ¢/cal**; the
  chip shop is one of the best fry-calorie deals in the rich world.
- **Belgian friterie frites** — €3.20 cone (~468 cal) → **0.75 ¢/cal**.

## Fry-flation — the fry over time (US McDonald's medium)

| Year | Price | ¢/cal | vs 2000 |
|------|-------|-------|---------|
| 2000 | $1.09 | 0.34 | — |
| 2010 | $1.49 | 0.47 | +37 % |
| 2014 | $1.79 | 0.56 | +64 % |
| 2019 | $2.29 | 0.72 | +110 % |
| 2020 | $2.89 | 0.90 | +165 % |
| 2024 | $4.19 | 1.31 | +284 % |
| 2025 | $4.29 | 1.34 | +294 % |

**A US McDonald's fry has gone ~3.9× since 2000** (0.34 → 1.34 ¢/cal). McDonald's
prices rose ~100 % in the decade to 2024 — **nearly double general inflation**.

**Run-7 — real vs nominal.** Deflating by US CPI-U to 2025 dollars, the fry went
from **$2.03 (2000) → $4.29 (2025) = ~2.1× in real terms.** So even after stripping
out general inflation the fry roughly *doubled* — and almost all of the real rise
is **post-2020** ($3.58 → $4.29). The dashboard plots nominal and real together.

## Method & caveats
FX at 2025 rates (₹83, ¥150, £0.79, €0.92, CHF 0.91 per USD). Country prices are
representative franchise prices (they vary widely — McDonald's franchisees set
their own). Nominal (not inflation-adjusted) time series. 🟡 overall; a future run
would add PPP adjustment and more countries. Reproduce: `python3 tools/fry_index.py`.

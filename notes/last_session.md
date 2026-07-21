# Last Session — Universe of Frynance

## Run 5 — PPC: Pennies Per Calorie (2026-07-20)

New value metric answering "where is a fry calorie cheapest to buy?" Live at
quackstra.github.io/universe-of-frynance.

### PPC (`tools/ppc.py`, `analysis/deep-dives/ppc/`, `ppc` data block)
- **PPC = price_cents / calories** (portion-independent ratio).
- Ranking (¢/cal): Raw potato 0.24 · Retail frozen 0.28 · **Five Guys 0.54** ·
  In-N-Out 0.58 · Burger King 0.71 · Chick-fil-A 0.74 · Arby's 0.75 · Wendy's
  0.85 · Casual 1.00 · **McDonald's 1.11** · **Fine dining 2.00**.
- Three findings: (1) **home wins ~2-8×** (cheapest calorie is DIY); (2) the
  **big-portion paradox** — Five Guys is the cheapest RESTAURANT fry/cal despite
  feeling pricey (953-cal portion); (3) **McDonald's ~2× Five Guys**, fine dining
  ~8× home.
- Confidence: prices 🟡 (US 2025, vary a lot by location — McD alone $1.89-5.90),
  calories 🟢; casual/fine-dining rows 🔴.
- Dashboard: PPC section + horizontal bar coloured by tier (home/fc/qsr/fine),
  nav link, insight card. Run 5 badge/footer.

### Data source anchors
menupricetracker (McD medium avg $3.56); fastfoodnutrition.org (calories: McD
320, Five Guys 953, CFA medium 420, BK 380); Walmart Great Value 32oz $2.97;
myfooddata raw potato 77 cal/100g.

## Metric stack so far
Big Number (375 Mt) · per-capita · MUSHT (3.84B mi) · TPS (~79k/s, NH+global) ·
**PPC (0.24-2.00 ¢/cal)** · Conscience (~45% waste). Trackers: fry cuts, tiers,
companions, PPC. Mass-balance gate PASS (unchanged).

## Next (Run 6)
- Non-US / international PPC (UK chippy, Belgian frites, global McD price parity).
- PPC vs the Big Mac Index (fry-flation over time).
- Ground casual/fine-dining PPC rows (currently 🔴).
- Still-open: exact processor tonnages; POS companion attach; FBS feed/seed pull.

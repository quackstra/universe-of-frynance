# Deep Dive — Fry Cuts by Geometry & Chain (FRY-R2-001)

**Run 2 · Confidence 🔴 (structured estimate)**

The fun deep dive: of the ~**29.8 Mt** of potato that becomes fries each year,
what *shape* is it, and which chains drive each cut? MUSHT miles below are
**straight-line-equivalent** (curly and waffle are not literal 0.75 cm straight
lines — the mileage is "if this tonnage were drawn out as one straight fry").

## Cut mix (share of the fries stream)

| Cut | Share | Mt/yr | Straight-equiv miles | Exemplar chains |
|-----|-------|-------|----------------------|-----------------|
| Straight / shoestring | 72 % | 21.5 | 219.5 M | McDonald's, Burger King, Wendy's, Five Guys, In-N-Out |
| Crinkle-cut | 8 % | 2.4 | 24.4 M | retail frozen, Sonic "Groovy Fries" (2024) |
| Wedge / steak | 6 % | 1.8 | 18.3 M | KFC, pubs, retail |
| Waffle / lattice | 5 % | 1.5 | 15.2 M | **Chick-fil-A** (fastest-growing cut, +14 % in 2024) |
| Tots / hash | 5 % | 1.5 | 15.2 M | Sonic, retail |
| **Curly** | 4 % | 1.2 | **12.2 M** | **Arby's**, Jack in the Box, Hardee's |

## Headline findings

- **Straight cut rules.** Straight/shoestring is ~**48 %** of the whole
  product-type market and higher still within QSR fries — McDonald's, the world's
  largest fry buyer, is straight ([market][mkt]).
- **🌀 Curly fry ≈ 12 million miles** of straight-equivalent fry a year —
  roughly **26 round-trips to the Moon** — and it's **mostly one chain, Arby's**
  (9th-largest US chain, 3,398 restaurants, curly is its signature) ([chains][ch]).
- **Waffle is the momentum cut.** Chick-fil-A — now the **3rd-largest US
  fast-food chain (~$24 B system sales)** — put waffle fries on the map; waffle
  was the fastest-growing cut in 2024 (+14 % in high-end QSR) ([market][mkt],
  [CFA][cfa]).
- **Geometry caveat:** MUSHT's 0.75 cm square line is a straight-fry idealization.
  Curly, waffle and crinkle add surface area without adding length, so their
  "miles" are notional — reported as straight-equivalent for comparability.

## Method
Cut shares are US-foodservice-weighted estimates anchored to (a) the straight-cut
~48 % market share, (b) which cut each major chain serves, and (c) chain scale
(system sales / unit counts). Applied to the global fries tonnage from the
[frozen fries capsule](../../processing/frozen_fries/REPORT.md). 🔴 — a true
figure needs processor cut-mix data + chain-level fry volumes (the public-data
wall). Reproduce: `python3 tools/musht.py` (prints the cut table).

[mkt]: https://www.coherentmarketinsights.com/market-insight/french-fries-market-3093
[ch]: https://chefstandards.com/fast-food-chains-fries/
[cfa]: https://www.ajc.com/business/2026/04/chick-fil-a-grew-us-sales-to-nearly-24b-last-year/

# Deep Dive — Fry Companions Tracker

**Run 3 · Confidence 🔴 (v1 estimate)**

What food is most frequently sold *with* a fry? The fry is rarely a solo act — it
is the great supporting side. This tracker ranks the main dish that shares the
plate.

## The companion ranking (share of fry-accompanied orders)

| # | Companion | Attach share |
|---|-----------|--------------|
| 1 | 🍔 Burger / cheeseburger | 38 % |
| 2 | 🍗 Chicken (sandwich / tenders / nuggets) | 24 % |
| 3 | 🥪 Sandwich / wrap / gyro | 12 % |
| 4 | 🐟 Fish (fish & chips) | 8 % |
| 5 | 🌭 Hot dog | 7 % |
| 6 | 🍖 Wings | 5 % |
| 7 | 🥩 Steak (steak frites) | 3 % |
| 8 | 🍟 Solo / other | 3 % |

## Findings
- **The burger is the fry's soulmate.** The burger–fries–soda trio is the defining
  American combo; the fry "adapts to every flavor and style," which is why it
  became the default burger side ([why the combo works][iceberg]).
- **Chicken is surging.** Chick-fil-A's rise (now the #3 US chain) and the chicken-
  sandwich wars push chicken to a strong #2 companion.
- **Fish & chips is the great regional anchor** — in the UK/Ireland the fry (chip)
  is defined *by* its companion, not the other way around.

## Ubiquitous pairings (not "main dish", but almost always present)
- **Beverage:** soda / soft drink — near-universal in combo meals.
- **Top dip:** ketchup. **Regional dips:** mayo (Belgium/Netherlands), malt
  vinegar (UK/Ireland), gravy + cheese curds = **poutine** (Canada), aioli, ranch.

## Method & roadmap
v1 shares are structured estimates anchored to combo-meal composition and chain
menu mix — a scaffold for the tracker, not measured attach data. **Run-4:**
ground with POS/menu-mix datasets (e.g. foodservice panels) and split by
restaurant tier — QSR attach skews burger/chicken; gastropubs skew steak/fish.
Cross-links to the [restaurant-tier fry mapping](../fry-cuts-by-chain/REPORT.md).

[iceberg]: https://icebergdriveinn.com/blogs/news/why-a-burger-fries-and-soda-make-the-perfect-combo

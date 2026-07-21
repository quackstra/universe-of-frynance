# The Big Number + MUSHT

## Big Number — ~375 million tonnes of potato / year

Global fresh-weight potato production, all varieties and sizes, all countries
(FAOSTAT, ~2022: 374.8 Mt). At a world population of ~8.1 billion that is
**~46 kg per person per year**.

This anchors the whole project: every fate below is a slice of these 375 Mt, and
the slices must sum back to 100 % (the mass-balance gate).

## MUSHT — Make Underutilized Spuds Have Taste

> If **100 % of every potato Earth grows** were extruded into one perfectly
> straight french fry, **0.75 cm × 0.75 cm** in cross-section, how long is it?

### The math (raw-potato-volume basis)

```
mass    = 375 Mt              = 3.75 × 10¹⁴ g
density ≈ 1.08 g/cm³          → volume = 3.47 × 10¹⁴ cm³
fry cross-section = 0.75 × 0.75 cm = 0.5625 cm²
length  = volume ÷ area       = 6.17 × 10¹⁴ cm
        = 6.17 × 10⁹ km       ≈ 3.84 billion miles
```

### Idealized MUSHT ≈ **3.84 billion miles**

- **41.3 AU — past Pluto's average orbit** (~39.5 AU). One fry, Earth to beyond
  Pluto.
- **154,000×** around the equator.
- **20.6** round-trips to the Sun · **16,000** one-way trips to the Moon.
- A photon needs **5.7 hours** to travel its length.

### Real MUSHT ≈ **0.30 billion miles**

Only the ~**7.9 %** of production that actually becomes fries (Processing 17 % ×
Frozen 55 % × fries-within-frozen 85 % ≈ 29.8 Mt). Still **3.3 AU** — out past the
asteroid belt — and **12,000×** around the equator. Put differently: **only about
1 potato in 13 becomes a fry.**

Broken down by cut (straight-line-equivalent miles): straight/shoestring 219.5 M ·
crinkle 24.4 M · wedge 18.3 M · waffle 15.2 M · tots 15.2 M · **curly 12.2 M
(≈ 26 round-trips to the Moon, mostly Arby's).** See the
[fry-cuts deep dive](../deep-dives/fry-cuts-by-chain/REPORT.md).

### The gap is the story

The **~3.5-billion-mile difference** between Idealized and Real MUSHT is a
headline in its own right: **most of the spud is not a fry.** Fries dominate the
cultural imagination but are a thin slice of what Earth grows.

## Assumptions & confidence

| Input | Value | Confidence |
|-------|-------|------------|
| Production | 375 Mt/yr | 🟢 FAOSTAT 2022 |
| Potato density | 1.08 g/cm³ | 🟡 raw specific gravity 1.05–1.09 |
| Fry cut | 0.75 cm square (≈ classic 3/8″) | 🟢 definitional |
| Fries fraction of production | 7.9 % | 🟡 derived (Proc 17% × Frozen 55% × 85%) |

Reproduce: `python3 tools/musht.py`. Recompute the fate split and the 100 %
gate: `python3 tools/massbalance.py`.

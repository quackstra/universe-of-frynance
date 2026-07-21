# Deep Dive — The Fry Bill (the induced supply chain)

**Run 9 · Confidence 🔴 (modeled from MCE-PF + input intensities)**

The fry doesn't just add value ([MCE-PF](../value-add/REPORT.md)) — it *induces* a
whole supply chain. Two questions: how many potatoes exist only because we fry,
and what does frying the world cost, sector by sector?

## 1. Induced potato demand — the counterfactual

If the fry format vanished, how much of the 29.8 Mt fries stream would still be
eaten? Some reverts to fresh boiled potato; the rest is **income-elastic demand
the fry alone sustains** (the whole point of [MCE-PF](../value-add/REPORT.md)) and
would simply exit to other foods.

| | Mt raw potato |
|---|---|
| Fries stream | 29.8 |
| …reverts to fresh boiled (40 %) | 11.9 |
| **…induced — vanishes without the fry (60 %)** | **17.9** |

> **~18 Mt of annual potato demand — ~4.8 % of *all* world production — exists
> only because we turn potatoes into fries.** That is the incremental farm demand
> the fry format creates, and everything below is the supply chain built to serve
> it.

## 2. The sector bill — what it takes to fry the world

Per **14.9 Mt of finished fries** (~135 billion servings/yr):

| Sector | Global total / yr | In context |
|--------|-------------------|------------|
| 🛢️ **Frying oil** | **1.94 Mt** | ~0.9 % of *all* the vegetable oil humanity produces (~220 Mt) |
| 🧂 Salt | 0.18 Mt | ~180,000 t of edible salt on the world's fries |
| ⚡ Energy (proc + cold-chain + cook) | 44.7 TWh | ~1.4× Ireland's annual electricity |
| 💧 Water footprint | 8.6 km³ | 574 L per kg — mostly green (rain) crop water |
| 👷 **Labor** | 1.80 B hours | **~900,000 full-time-equivalent jobs** frying & serving |
| 📦 Packaging | 2.02 Mt | cartons, bags and boxes |
| 🌍 CO₂e emissions | 67 Mt | a small nation's footprint; frozen fries are the highest-emission potato product |

### The two headline sector facts
- **Oil:** keeping the world in fries absorbs **~1.9 Mt of vegetable oil a year —
  about 0.9 % of everything humanity presses** — just to make potatoes crispy.
- **Labor:** the fry sustains **~900,000 full-time jobs** across processing and
  foodservice — a city's worth of people whose work exists because we fry.

## Method & caveats
Finished fries 14.9 Mt (Run 4). Input intensities: oil 13 % of finished weight,
salt 1.2 %, water 574 L/kg (waterfootprint.org), CO₂e ~4.5 kg/kg, energy ~3 kWh/kg,
labor ~48 s/serving, packaging ~15 g/serving. The **induced-demand split (40 %
revert / 60 % induced) is a modeled scenario** grounded in MCE-PF, not a measured
counterfactual — the single biggest 🔴. Sensitivity: at 25 % revert, induced rises
to ~22 Mt; at 55 %, ~13 Mt. Reproduce: `python3 tools/fry_bill.py`.

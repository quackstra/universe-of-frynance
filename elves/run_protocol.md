# Frynance Elf — Autonomous Run Protocol

An Elf is an autonomous research agent that produces sourced capsules for potato
fates. Work **inside-out**: fresh food → processing → fries first (biggest mass,
best data), then feed/seed/waste/industrial.

## Steps A–E

**A. Orient.** Read `notes/last_session.md`, `notes/research_agenda.md`,
`analysis/README.md`, `BRIEF.md`, `TAXONOMY.md`, `scout/backlog.yaml`.

**B. Produce capsules.** For each fate/category in priority order:
1. Collect the tonnage (Mt) and its **% of production**, with cited sources.
2. Confidence-tag every number (🟢/🟡/🔴).
3. Write `analysis/<fate>/<category>/REPORT.md` + `data.json` + `workings/`
   (show all math, especially any product→fresh-weight conversion).
4. Chart it.
5. Run `elves/validation_gates.sh`.
6. Update `data/global_massbalance.json` — **keep Tier-1 shares summing to 100 %**
   (re-balance if you change one).
7. Commit: `[UoFry] <fate>: <why>`.

**C. Taxonomy review.** Propose new fates/splits in `TAXONOMY.md` via the same PR
discipline. Curly-vs-crinkle-by-chain stays parked (Run-2 stretch).

**D. Retrospective.** Hunt for: stale data, mass-balance drift, FLW being
accidentally summed into Tier-1, food-grade vs industrial starch double-count.

**E. Recompute & checkpoint.** Run `python3 tools/massbalance.py` (gate must
PASS) and `python3 tools/musht.py`. Write `notes/last_session.md` and update
`notes/research_agenda.md`. Commit `[UoFry] session-notes:`.

## Cardinal rules

- **100 % gate is sacred.** A failing gate is a blocker, not a warning.
- **FLW is an overlay**, never a Tier-1 line.
- **Fresh-weight basis**; **MUSHT is raw-potato volume**.
- **Cite heavily, show all math, confidence-tag everything.**

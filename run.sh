#!/usr/bin/env bash
# Universe of Frynance Runner — orchestrates Scout → Architect → Elves → Publish
#
# Usage:
#   ./run.sh                # scout + bignumber
#   ./run.sh scout          # refresh scout/backlog.yaml
#   ./run.sh bignumber      # mass-balance gate + MUSHT
#   ./run.sh elf-run        # full autonomous research run
set -euo pipefail

FRY_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="${FRY_DIR}/logs"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"; }

run_scout() {
    log "=== SCOUT: ranking potato fates/categories ==="
    cd "${FRY_DIR}/scout" && python3 scout.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
}

run_bignumber() {
    log "=== BIG NUMBER: mass-balance gate + MUSHT ==="
    cd "${FRY_DIR}" && python3 tools/massbalance.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
    cd "${FRY_DIR}" && python3 tools/musht.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
}

run_elf_run() {
    log "=== ELF RUN: full autonomous research session ==="
    local elf_prompt
    elf_prompt="$(cat <<'PROMPT'
You are a Universe of Frynance research Elf executing a full autonomous run.
Follow elves/run_protocol.md exactly.

Step A: Read notes/last_session.md, notes/research_agenda.md, analysis/README.md,
        BRIEF.md, TAXONOMY.md.
Step B: Work inside-out (fresh food, processing, fries first). For each fate:
        collect Mt + % of production, cite sources, confidence-tag, write
        REPORT.md + data.json + workings/, chart, run elves/validation_gates.sh,
        commit ([UoFry] <fate>: ...). Keep Tier-1 shares summing to 100%.
Step C: Review TAXONOMY.md for new fates/splits.
Step D: Retrospective — stale data, mass-balance drift, FLW-vs-utilisation
        double-count risks.
Step E: Recompute python3 tools/massbalance.py && python3 tools/musht.py; write
        notes/last_session.md + notes/research_agenda.md; commit.

Rules: THE 100% GATE IS SACRED. Never sum FLW into Tier-1. Fresh-weight basis.
MUSHT is raw-potato volume. Cite heavily, show all math, confidence-tag.
PROMPT
)"
    cd "${FRY_DIR}" && claude -p "$elf_prompt" 2>&1 | tee -a "${LOG_DIR}/elf_run_${TIMESTAMP}.log"
}

main() {
    local mode="${1:-all}"
    log "Universe of Frynance Runner — mode: ${mode}"
    case "$mode" in
        scout)     run_scout ;;
        bignumber) run_bignumber ;;
        elf-run)   run_elf_run ;;
        all)       run_bignumber ;;
        *) echo "Usage: $0 [scout|elf-run|bignumber|all]"; exit 1 ;;
    esac
    log "Runner complete."
}

main "$@"

#!/usr/bin/env bash
# Universe of Frynance — pre-publish validation gates for a capsule / the dataset.
# Usage: elves/validation_gates.sh [path/to/data.json]
set -euo pipefail

FRY_DIR="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

say() { echo "  $*"; }
bad() { echo "  ❌ $*"; fail=1; }

echo "== Frynance validation gates =="

# 1. The global 100% mass-balance gate (authoritative).
if python3 "${FRY_DIR}/tools/massbalance.py" >/dev/null 2>&1; then
    say "✅ mass-balance 100% gate passes"
else
    bad "mass-balance 100% gate FAILS — Tier-1 shares must sum to 100%"
fi

# 2. Optional per-capsule checks if a data.json path was given.
if [[ "${1:-}" != "" ]]; then
    f="$1"
    [[ -f "$f" ]] || { bad "no such file: $f"; }
    if [[ -f "$f" ]]; then
        python3 -c "import json,sys; json.load(open('$f'))" \
            && say "✅ $f is valid JSON" || bad "$f is not valid JSON"
        grep -q '"confidence"' "$f" && say "✅ has confidence tags" \
            || bad "$f missing confidence tags"
        grep -q '"source"' "$f" && say "✅ has sources" \
            || bad "$f missing sources"
    fi
fi

# 3. MUSHT still computes.
python3 "${FRY_DIR}/tools/musht.py" >/dev/null 2>&1 \
    && say "✅ MUSHT computes" || bad "MUSHT failed to compute"

[[ $fail -eq 0 ]] && echo "== ALL GATES PASS ==" || { echo "== GATES FAILED =="; exit 1; }

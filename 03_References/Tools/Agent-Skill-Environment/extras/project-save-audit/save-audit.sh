#!/bin/bash
# Wrapper for /save-audit skill
# Usage: ./save-audit.sh [topic]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="c:/Users/shiva/obsidian"

cd "$VAULT_ROOT"

# Run Python implementation
python3 "$SCRIPT_DIR/save_audit.py" "$@"

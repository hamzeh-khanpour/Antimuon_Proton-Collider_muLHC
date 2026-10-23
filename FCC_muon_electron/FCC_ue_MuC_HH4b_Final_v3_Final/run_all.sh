#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Select a Python interpreter compatible with your existing MG5 installation.
PYTHON="${PYTHON:-python3}"
exec "$PYTHON" "$ROOT/run_workflow.py" "$@"

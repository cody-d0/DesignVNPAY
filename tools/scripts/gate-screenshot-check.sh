#!/bin/bash
# ============================================================
# Gate A: Screenshot Existence Check
# Purpose: Verify {prd_folder}/ui/ has ≥1 PNG (flat structure)
# Usage:   bash tools/scripts/gate-screenshot-check.sh <prd_folder>
# Exit:    0 = pass, 1 = missing or empty ui/
# ============================================================

set -euo pipefail

PRD_FOLDER="${1:?Usage: gate-screenshot-check.sh <prd_folder>}"

if [ ! -d "$PRD_FOLDER" ]; then
  echo "❌ GATE-A FAIL: Folder not found: $PRD_FOLDER" >&2
  exit 1
fi

UI_DIR="$PRD_FOLDER/ui"

if [ ! -d "$UI_DIR" ]; then
  echo "❌ GATE-A FAILED: ui/ folder not found at $UI_DIR" >&2
  echo '{"gate":"A","status":"FAIL","reason":"no_ui_dir","total_png":0}'
  exit 1
fi

TOTAL_PNG=$(find "$UI_DIR" -maxdepth 1 -name "*.png" -type f 2>/dev/null | wc -l | tr -d ' ')

echo "" >&2
echo "━━━ Gate A: Screenshot Existence ━━━" >&2
echo "UI folder: $UI_DIR" >&2
echo "Total PNGs: $TOTAL_PNG" >&2

if [ "$TOTAL_PNG" -eq 0 ]; then
  echo "❌ GATE-A FAILED: ui/ folder is empty (0 PNGs)" >&2
  echo "{\"gate\":\"A\",\"status\":\"FAIL\",\"total_png\":0}"
  exit 1
fi

echo "✅ GATE-A PASSED ($TOTAL_PNG PNGs)" >&2
echo "{\"gate\":\"A\",\"status\":\"PASS\",\"total_png\":$TOTAL_PNG}"
exit 0

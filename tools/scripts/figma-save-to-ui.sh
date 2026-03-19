#!/bin/bash
# ============================================================
# figma-save-to-ui.sh — Wrapper: Tải ảnh từ Figma → move vào ui/
# Purpose: Giải quyết path mismatch giữa script output và workflow
# Usage:   bash tools/scripts/figma-save-to-ui.sh <file_key> <node_id> <target_ui_dir>
# Example: bash tools/scripts/figma-save-to-ui.sh kPft93N2A3g 5197:5929 project/section/ui
# Exit:    0 = success (≥1 PNG in target_ui), 1 = failure
# Env:     FAT or FIGMA_ACCESS_TOKEN (required)
# ============================================================

set -euo pipefail

FILE_KEY="${1:?Usage: figma-save-to-ui.sh <file_key> <node_id> <target_ui_dir>}"
NODE_ID="${2:?Usage: figma-save-to-ui.sh <file_key> <node_id> <target_ui_dir>}"
TARGET_UI="${3:?Usage: figma-save-to-ui.sh <file_key> <node_id> <target_ui_dir>}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SAVE_SCRIPT="$SCRIPT_DIR/save-figma-section-screenshots.js"

# ─── Pre-checks ──────────────────────────────────────────────
if [ ! -f "$SAVE_SCRIPT" ]; then
  echo "❌ Script not found: $SAVE_SCRIPT" >&2
  exit 1
fi

# Source .env if available (tokens)
if [ -f .env ]; then
  set -a && . ./.env && set +a
fi

if [ -z "${FAT:-}" ] && [ -z "${FIGMA_ACCESS_TOKEN:-}" ]; then
  echo "❌ Figma token not found. Set FAT or FIGMA_ACCESS_TOKEN in .env" >&2
  exit 1
fi

# ─── Create temp dir for raw output ─────────────────────────
TMPDIR=$(mktemp -d "${TMPDIR:-/tmp}/figma-save-XXXXXX")
trap 'rm -rf "$TMPDIR"' EXIT

echo "📥 Downloading artboards from Figma..." >&2
echo "   file_key: $FILE_KEY" >&2
echo "   node_id:  $NODE_ID" >&2
echo "   temp_dir: $TMPDIR" >&2

# ─── Run save script ────────────────────────────────────────
if ! node "$SAVE_SCRIPT" "$FILE_KEY" "$NODE_ID" "$TMPDIR" 2>&1; then
  echo "❌ Save script failed" >&2
  exit 1
fi

# ─── Collect all PNGs (script creates nested dirs) ───────────
PNG_COUNT=$(find "$TMPDIR" -name "*.png" -type f 2>/dev/null | wc -l | tr -d ' ')

if [ "$PNG_COUNT" -eq 0 ]; then
  echo "❌ Script ran but produced 0 PNGs" >&2
  echo "   Check: node ID correct? Figma token valid? Artboards exist?" >&2
  exit 1
fi

echo "📦 Found $PNG_COUNT PNGs in temp output" >&2

# ─── Move all PNGs to target ui/ ────────────────────────────
mkdir -p "$TARGET_UI"

find "$TMPDIR" -name "*.png" -type f -exec mv {} "$TARGET_UI/" \;

FINAL_COUNT=$(find "$TARGET_UI" -maxdepth 1 -name "*.png" -type f 2>/dev/null | wc -l | tr -d ' ')

echo "" >&2
echo "✅ SUCCESS: $FINAL_COUNT PNGs → $TARGET_UI/" >&2

# List files saved
find "$TARGET_UI" -maxdepth 1 -name "*.png" -type f -exec basename {} \; | sort | while read f; do
  echo "   📄 $f" >&2
done

# JSON output to stdout
echo '{"status":"OK","count":'$FINAL_COUNT',"target":"'$TARGET_UI'"}'
exit 0

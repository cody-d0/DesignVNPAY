#!/bin/bash
# ============================================================
# Gate C: Vision File Check (before Skill C)
# Purpose: Verify all images referenced in .md files exist on disk
# Usage:   bash tools/scripts/gate-vision-files.sh <prd_folder>
# Exit:    0 = all images exist, 1 = missing images
# ============================================================

set -euo pipefail

PRD_FOLDER="${1:?Usage: gate-vision-files.sh <prd_folder>}"

if [ ! -d "$PRD_FOLDER" ]; then
  echo "❌ GATE-C FAIL: Folder not found: $PRD_FOLDER" >&2
  exit 1
fi

FOUND=0
MISSING=0
TOTAL=0
MISSING_LIST=""

# Find all .md files, extract image references, check existence
while IFS= read -r md_file; do
  md_dir=$(dirname "$md_file")
  
  # Extract image paths from markdown: ![...](path)
  while IFS= read -r img_ref; do
    [ -z "$img_ref" ] && continue
    TOTAL=$((TOTAL + 1))
    
    # Resolve relative to .md file location
    if [[ "$img_ref" == /* ]]; then
      img_path="$img_ref"
    else
      img_path="$md_dir/$img_ref"
    fi
    
    if [ -f "$img_path" ]; then
      FOUND=$((FOUND + 1))
    else
      MISSING=$((MISSING + 1))
      MISSING_LIST="${MISSING_LIST}\n  ❌ ${md_file##*/} → $img_ref"
      echo "❌ MISSING: $img_path (referenced in ${md_file##*/})" >&2
    fi
  done < <(sed -n 's/.*!\[[^]]*\](\([^)]*\)).*/\1/p' "$md_file" 2>/dev/null || true)
  
done < <(find "$PRD_FOLDER" -name "*.md" -type f -not -name "ux-review-report.md" -not -name "*overview*")

echo "" >&2
echo "━━━ Gate C: Vision File Check ━━━" >&2
echo "Found: $FOUND | Missing: $MISSING | Total refs: $TOTAL" >&2

if [ "$MISSING" -gt 0 ]; then
  echo -e "\nMissing files:$MISSING_LIST" >&2
  echo "❌ GATE-C FAILED: $MISSING image(s) referenced but not found on disk" >&2
  echo "⚠️  Skill C CANNOT run vision review without images" >&2
  echo '{"gate":"C","status":"FAIL","found":'$FOUND',"missing":'$MISSING',"total":'$TOTAL'}'
  exit 1
fi

if [ "$TOTAL" -eq 0 ]; then
  echo "⚠️  GATE-C WARNING: No image references found in .md files" >&2
  echo '{"gate":"C","status":"WARN","found":0,"missing":0,"total":0}'
  exit 1
fi

echo "✅ GATE-C PASSED: All $FOUND images exist" >&2
echo '{"gate":"C","status":"PASS","found":'$FOUND',"missing":0,"total":'$TOTAL'}'
exit 0

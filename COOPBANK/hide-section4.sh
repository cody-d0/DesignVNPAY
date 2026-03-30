#!/bin/bash
# Hide Section 4 (04 · Đánh giá theo danh mục heuristic) from all 28 pitch deck HTMLs
# Method: Add display:none to the scorecard section + hide its nav link

FINAL_DIR="/Users/dataism/Documents/UXtool/COOPBANK/final"
count=0
errors=0

for html_file in "$FINAL_DIR"/*/*pitch-deck*.html; do
  if [ ! -f "$html_file" ]; then
    continue
  fi
  
  module=$(basename "$(dirname "$html_file")")
  
  # 1. Hide the nav link for Scorecard
  # Replace <a href="#scorecard">Scorecard</a> with hidden version
  sed -i '' 's|<a href="#scorecard">Scorecard</a>|<a href="#scorecard" style="display:none">Scorecard</a>|g' "$html_file"
  
  # 2. Hide the entire section with id="scorecard" 
  # The section starts with <section class="section" id="scorecard">
  # Add style="display:none" to it
  sed -i '' 's|<section class="section" id="scorecard">|<section class="section" id="scorecard" style="display:none">|g' "$html_file"
  
  # Verify
  hidden_section=$(grep -c 'id="scorecard" style="display:none"' "$html_file")
  hidden_nav=$(grep -c 'href="#scorecard" style="display:none"' "$html_file")
  
  if [ "$hidden_section" -gt 0 ] && [ "$hidden_nav" -gt 0 ]; then
    echo "✅ $module — section hidden, nav hidden"
    count=$((count + 1))
  else
    echo "❌ $module — section=$hidden_section nav=$hidden_nav"
    errors=$((errors + 1))
  fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Success: $count modules"
echo "❌ Errors: $errors modules"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

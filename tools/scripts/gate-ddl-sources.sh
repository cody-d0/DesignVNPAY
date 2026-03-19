#!/usr/bin/env bash
# ────────────────────────────────────────────────────────
# Gate DDL Sources: Verify all UX review data sources exist
# MUST PASS before Bước 4 (UX Review Pipeline)
# Exit 0 = all sources present
# Exit 1 = missing critical sources
# ────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

echo ""
echo "━━━ Gate DDL Sources: UX Review Data Verification ━━━"

FOUND=0
MISSING=0
WARN=0
ERRORS=""

# ─── Critical Sources (HARD-FAIL) ──────────────────────

check_critical() {
  local label="$1"
  local path="$2"
  if [[ -f "$path" ]]; then
    local size=$(wc -c < "$path" | tr -d ' ')
    echo -e "  ${GREEN}✅${NC} $label ($size bytes)"
    FOUND=$((FOUND + 1))
  else
    echo -e "  ${RED}❌${NC} $label — NOT FOUND: $path"
    MISSING=$((MISSING + 1))
    ERRORS="${ERRORS}\n  MISSING: $label ($path)"
  fi
}

check_dir() {
  local label="$1"
  local path="$2"
  if [[ -d "$path" ]]; then
    echo -e "  ${GREEN}✅${NC} $label (directory exists)"
    FOUND=$((FOUND + 1))
  else
    echo -e "  ${RED}❌${NC} $label — NOT FOUND: $path"
    MISSING=$((MISSING + 1))
    ERRORS="${ERRORS}\n  MISSING: $label ($path)"
  fi
}

check_optional() {
  local label="$1"
  local path="$2"
  if [[ -f "$path" ]]; then
    local size=$(wc -c < "$path" | tr -d ' ')
    echo -e "  ${GREEN}✅${NC} $label ($size bytes)"
    FOUND=$((FOUND + 1))
  else
    echo -e "  ${YELLOW}⚠️${NC}  $label — optional, not found"
    WARN=$((WARN + 1))
  fi
}

echo ""
echo "1. UX Guidelines & Laws (ui-ux-pro-max skill):"
check_critical "ux-guidelines.csv (99 rules)" \
  "$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/data/ux-guidelines.csv"
check_critical "ux-laws.csv (20+ laws)" \
  "$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/data/ux-laws.csv"
check_critical "search.py (skill CLI)" \
  "$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/scripts/search.py"
check_critical "SKILL.md" \
  "$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/SKILL.md"

echo ""
echo "2. DDL Database Layer:"
check_critical "ddl.db (SQLite)" \
  "$PROJECT_ROOT/DDL/design-data-layer/ddl.db"
check_critical "ddl-api.js (Query API)" \
  "$PROJECT_ROOT/DDL/scripts/ddl-api.js"
check_critical "DDL-AGENT-PROTOCOL.md" \
  "$PROJECT_ROOT/DDL/design-data-layer/DDL-AGENT-PROTOCOL.md"

echo ""
echo "3. Scoring Tool:"
check_critical "ux-score-calculator.js" \
  "$PROJECT_ROOT/tools/ux-score-calculator.js"

echo ""
echo "4. Optional Sources:"
check_optional "ddl-registry.json" \
  "$PROJECT_ROOT/DDL/design-data-layer/ddl-registry.json"
check_optional "ddl-schema.json" \
  "$PROJECT_ROOT/DDL/design-data-layer/ddl-schema.json"

# ─── Validate CSV content ──────────────────────────────
echo ""
echo "5. Data Integrity:"
UXG_CSV="$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/data/ux-guidelines.csv"
if [[ -f "$UXG_CSV" ]]; then
  LINES=$(wc -l < "$UXG_CSV" | tr -d ' ')
  if [[ "$LINES" -ge 50 ]]; then
    echo -e "  ${GREEN}✅${NC} ux-guidelines.csv has $LINES rows (≥ 50)"
  else
    echo -e "  ${YELLOW}⚠️${NC}  ux-guidelines.csv has only $LINES rows (expected ≥ 50)"
    WARN=$((WARN + 1))
  fi
fi

UXL_CSV="$PROJECT_ROOT/.agents/skills/ui-ux-pro-max/data/ux-laws.csv"
if [[ -f "$UXL_CSV" ]]; then
  LINES=$(wc -l < "$UXL_CSV" | tr -d ' ')
  if [[ "$LINES" -ge 10 ]]; then
    echo -e "  ${GREEN}✅${NC} ux-laws.csv has $LINES rows (≥ 10)"
  else
    echo -e "  ${YELLOW}⚠️${NC}  ux-laws.csv has only $LINES rows (expected ≥ 10)"
    WARN=$((WARN + 1))
  fi
fi

# ─── Summary ───────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Found: $FOUND | Missing: $MISSING | Warnings: $WARN | Total refs: $((FOUND + MISSING))"

if [[ $MISSING -gt 0 ]]; then
  echo -e "${RED}❌ GATE-DDL FAILED: $MISSING critical source(s) missing${NC}"
  echo -e "$ERRORS"
  echo ""
  echo "Agent MUST NOT proceed with UX Review without these sources."
  echo "Agent MUST NOT fabricate DDL references."
  exit 1
else
  echo -e "${GREEN}✅ GATE-DDL PASSED: All $FOUND sources verified${NC}"
fi

# ─── JSON output ───────────────────────────────────────
echo "{\"gate\":\"DDL\",\"status\":\"$([ $MISSING -eq 0 ] && echo PASS || echo FAIL)\",\"found\":$FOUND,\"missing\":$MISSING,\"warnings\":$WARN}"
exit 0

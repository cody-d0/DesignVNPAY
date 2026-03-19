#!/usr/bin/env bash
# ============================================================
# Quality Gate — Automated checklist for automation scripts
# Author: AI-assisted (automation-scripts skill)
# Usage: bash quality-gate.sh <script-path>
# Exit codes: 0=grade A/B/C, 1=FAIL
# ============================================================
set -euo pipefail

readonly SCRIPT_PATH="${1:?Usage: $0 <script-path>}"
readonly SCRIPT_NAME="$(basename "$SCRIPT_PATH")"

# ─── Colors ──────────────────────────────────────────────────
if [[ -t 1 ]]; then
  readonly GREEN='\033[0;32m' RED='\033[0;31m' YELLOW='\033[1;33m'
  readonly CYAN='\033[0;36m' DIM='\033[2m' BOLD='\033[1m' NC='\033[0m'
else
  readonly GREEN='' RED='' YELLOW='' CYAN='' DIM='' BOLD='' NC=''
fi

# ─── Validation ──────────────────────────────────────────────
[[ ! -f "$SCRIPT_PATH" ]] && echo -e "${RED}File not found: $SCRIPT_PATH${NC}" && exit 1

CONTENT=$(cat "$SCRIPT_PATH")
LINE_COUNT=$(wc -l < "$SCRIPT_PATH" | tr -d ' ')
PASS=0
FAIL=0
WARN=0

check() {
  local label="$1" status="$2" detail="${3:-}"
  case "$status" in
    pass) echo -e "  ${GREEN}✅${NC} $label"; PASS=$((PASS + 1)) ;;
    fail) echo -e "  ${RED}❌${NC} $label ${DIM}$detail${NC}"; FAIL=$((FAIL + 1)) ;;
    warn) echo -e "  ${YELLOW}⚠️${NC}  $label ${DIM}$detail${NC}"; WARN=$((WARN + 1)) ;;
  esac
}

# ─── Detect Language ─────────────────────────────────────────
LANG_TYPE="unknown"
EXT="${SCRIPT_PATH##*.}"
case "$EXT" in
  sh|bash) LANG_TYPE="bash" ;;
  js|mjs|cjs) LANG_TYPE="node" ;;
  py) LANG_TYPE="python" ;;
  ts) LANG_TYPE="typescript" ;;
esac

# Also check shebang
FIRST_LINE=$(head -1 "$SCRIPT_PATH")
case "$FIRST_LINE" in
  *bash*|*sh*) LANG_TYPE="bash" ;;
  *node*) LANG_TYPE="node" ;;
  *python*) LANG_TYPE="python" ;;
esac

echo -e "\n${CYAN}━━━ Quality Gate: $SCRIPT_NAME ($LANG_TYPE, ${LINE_COUNT} LOC) ━━━${NC}\n"

# ═══════════════════════════════════════════════════════════
# CHECK 1: HEADER — Shebang + description
# ═══════════════════════════════════════════════════════════
echo -e "${CYAN}1. Header & Metadata${NC}"

if echo "$FIRST_LINE" | grep -qE '^#!'; then
  check "Shebang line" "pass"
else
  check "Shebang line" "fail" "Missing #!/usr/bin/env ..."
fi

if echo "$CONTENT" | head -20 | grep -qiE '(purpose|description|usage|script:|quality.?grade)'; then
  check "Description comment" "pass"
else
  check "Description comment" "warn" "No description found in first 20 lines"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 2: STRICT MODE — Error policy
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}2. Strict Mode${NC}"

case "$LANG_TYPE" in
  bash)
    if echo "$CONTENT" | grep -q 'set -.*e' && echo "$CONTENT" | grep -q 'pipefail'; then
      check "Strict mode (set -euo pipefail)" "pass"
    elif echo "$CONTENT" | grep -q 'set -.*e'; then
      check "Strict mode (partial)" "warn" "Has -e but missing -u or pipefail"
    else
      check "Strict mode" "fail" "Missing set -euo pipefail"
    fi
    ;;
  node)
    if echo "$CONTENT" | grep -qE "'use strict'|\"use strict\""; then
      check "use strict" "pass"
    else
      check "use strict" "warn" "Missing 'use strict'"
    fi
    if echo "$CONTENT" | grep -q 'unhandledRejection'; then
      check "Unhandled rejection handler" "pass"
    else
      check "Unhandled rejection handler" "warn" "No process.on('unhandledRejection')"
    fi
    ;;
  python)
    if echo "$CONTENT" | grep -qE '(try|except|logging\.)'; then
      check "Error handling (try/except or logging)" "pass"
    else
      check "Error handling" "warn" "No try/except or logging found"
    fi
    ;;
esac

# ═══════════════════════════════════════════════════════════
# CHECK 3: INPUT VALIDATION
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}3. Input Validation${NC}"

if echo "$CONTENT" | grep -qiE '(validate|validation|check.*input|required|missing.*arg|usage error|\{1:\?|:?Usage)'; then
  check "Input validation" "pass"
else
  check "Input validation" "warn" "No clear input validation found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 4: LOGGING — Timestamps + levels
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}4. Logging${NC}"

if echo "$CONTENT" | grep -qiE '(console\.(log|error|warn)|logging\.|log\(|echo.*INFO|echo.*ERROR|_log|\.info\()'; then
  check "Logging output" "pass"
else
  check "Logging output" "fail" "No logging found"
fi

if echo "$CONTENT" | grep -qiE '(date|timestamp|toISOString|asctime|%H:%M:%S|\.slice\(11)'; then
  check "Timestamps in logs" "pass"
else
  check "Timestamps in logs" "warn" "No timestamp formatting found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 5: IDEMPOTENT — Run 2x = same result
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}5. Idempotency${NC}"

if echo "$CONTENT" | grep -qiE '(idempoten|skip.*exist|already.*done|already.*exist|md5sum|hash.*check|-nt |\.tmp.*rename|\.tmp.*mv)'; then
  check "Idempotency patterns" "pass"
else
  check "Idempotency patterns" "warn" "No idempotency checks found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 6: DRY-RUN — Preview mode
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}6. Dry-Run${NC}"

if echo "$CONTENT" | grep -qiE '(dry.?run|preview|simulate|DRY_RUN)'; then
  check "Dry-run support" "pass"
else
  check "Dry-run support" "warn" "No --dry-run flag found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 7: CLEANUP — trap/finally
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}7. Cleanup${NC}"

if echo "$CONTENT" | grep -qiE '(trap.*EXIT|finally|cleanup\(\)|process\.on.*exit|atexit|CLEANUP_FILES)'; then
  check "Cleanup handler" "pass"
else
  check "Cleanup handler" "warn" "No cleanup/trap handler found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 8: SELF-TEST — --test flag
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}8. Self-Test${NC}"

if echo "$CONTENT" | grep -qiE '(--test|--check|self.?test|selfTest|self_test)'; then
  check "Self-test flag" "pass"
else
  check "Self-test flag" "warn" "No --test or --check flag found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 9: HELP — Usage text
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}9. Help${NC}"

if echo "$CONTENT" | grep -qiE '(--help|-h.*help|usage\(\)|show.*help|showHelp|USAGE:|Examples:)'; then
  check "Help / usage text" "pass"
else
  check "Help / usage text" "warn" "No --help flag found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 10: EXIT CODES — Semantic meaning
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}10. Exit Codes${NC}"

if echo "$CONTENT" | grep -qiE '(exit [0-9]|process\.exit\([0-9]|sys\.exit\([0-9]|process\.exitCode|exit code)'; then
  check "Semantic exit codes" "pass"
else
  check "Semantic exit codes" "warn" "No explicit exit codes"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 11: EXECUTION TRACE — Start/end/duration/counts
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}11. Execution Trace${NC}"

if echo "$CONTENT" | grep -qiE '(trace_start|trace_end|START.*━|Summary|duration|elapsed|processed.*failed|success.*fail)'; then
  check "Execution tracing" "pass"
else
  check "Execution tracing" "warn" "No execution trace summary found"
fi

# ═══════════════════════════════════════════════════════════
# CHECK 12: SECURITY — No hardcoded secrets
# ═══════════════════════════════════════════════════════════
echo -e "\n${CYAN}12. Security${NC}"

if echo "$CONTENT" | grep -vE '(^\s*#|^\s*//|grep|regex|pattern|check|example|placeholder)' | grep -qiE '(password|secret|api_key|token|credential)\s*=\s*["'\''"][a-zA-Z0-9]{8,}'; then
  check "No hardcoded secrets" "fail" "Possible hardcoded credential found!"
else
  check "No hardcoded secrets" "pass"
fi

if [[ "$LANG_TYPE" == "bash" ]]; then
  UNQUOTED=$(echo "$CONTENT" | grep -nE '\$[a-zA-Z_][a-zA-Z0-9_]*[^"]' | grep -vE '(^\s*#|".*\$|readonly|local|export|declare|if \[\[|\$\{|\$\()' | head -3 || true)
  if [[ -n "$UNQUOTED" ]]; then
    check "Quoted variables" "warn" "Possible unquoted variables"
  else
    check "Quoted variables" "pass"
  fi
fi

# ═══════════════════════════════════════════════════════════
# CHECK 13: SHELLCHECK (bash only)
# ═══════════════════════════════════════════════════════════
if [[ "$LANG_TYPE" == "bash" ]]; then
  echo -e "\n${CYAN}13. Static Analysis${NC}"
  if command -v shellcheck &>/dev/null; then
    SC_RESULT=$(shellcheck -S warning "$SCRIPT_PATH" 2>&1 || true)
    SC_COUNT=$(echo "$SC_RESULT" | grep -c 'SC[0-9]' || true)
    if [[ $SC_COUNT -eq 0 ]]; then
      check "ShellCheck" "pass"
    else
      check "ShellCheck" "warn" "$SC_COUNT warning(s)"
    fi
  else
    check "ShellCheck" "warn" "shellcheck not installed (brew install shellcheck)"
  fi
fi

# ═══════════════════════════════════════════════════════════
# GRADING
# ═══════════════════════════════════════════════════════════
TOTAL=$((PASS + FAIL + WARN))
SCORE=$((PASS))  # Only full passes count

echo -e "\n${CYAN}━━━ Results ━━━${NC}"
echo -e "  ${GREEN}Pass: $PASS${NC}  ${RED}Fail: $FAIL${NC}  ${YELLOW}Warn: $WARN${NC}  Total: $TOTAL"

# Grade calculation
GRADE="FAIL"
GRADE_COLOR="$RED"
if [[ $FAIL -eq 0 ]]; then
  if [[ $SCORE -ge 12 && $WARN -le 1 ]]; then
    GRADE="A"
    GRADE_COLOR="$GREEN"
  elif [[ $SCORE -ge 10 ]]; then
    GRADE="B"
    GRADE_COLOR="$GREEN"
  elif [[ $SCORE -ge 8 ]]; then
    GRADE="C"
    GRADE_COLOR="$YELLOW"
  fi
fi

echo -e "\n  ${BOLD}Grade: ${GRADE_COLOR}${GRADE}${NC}"

case "$GRADE" in
  A)    echo -e "  ${GREEN}Exemplary — production-ready${NC}" ;;
  B)    echo -e "  ${GREEN}Good — ready to deliver${NC}" ;;
  C)    echo -e "  ${YELLOW}Acceptable — minimum viable${NC}" ;;
  FAIL) echo -e "  ${RED}Must fix $FAIL failure(s) before delivering${NC}" ;;
esac

echo ""

if [[ "$GRADE" == "FAIL" ]]; then
  exit 1
else
  exit 0
fi

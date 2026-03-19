# Moderate Script Patterns (100-300 LOC)

CLI tools, multi-step workflows, scripts cần argument parsing & progress.

## Bash Template — CLI Tool

```bash
#!/usr/bin/env bash
# ============================================================
# Script: <name>.sh
# Purpose: <description>
# Usage: ./<name>.sh <command> [options] <args>
# Exit codes: 0=success, 1=error, 2=usage, 3=partial
# ============================================================
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"
readonly VERSION="1.0.0"
readonly LOG_FILE="${TMPDIR:-/tmp}/${SCRIPT_NAME%.*}-$(date +%Y%m%d).log"

# ─── Color Output ───────────────────────────────────────────
if [[ -t 1 ]]; then
  readonly RED='\033[0;31m' GREEN='\033[0;32m' YELLOW='\033[1;33m'
  readonly BLUE='\033[0;34m' CYAN='\033[0;36m' NC='\033[0m'
else
  readonly RED='' GREEN='' YELLOW='' BLUE='' CYAN='' NC=''
fi

# ─── Logging (tee to file + stderr) ─────────────────────────
_log() {
  local level="$1" color="$2"; shift 2
  local msg="$(date '+%H:%M:%S') [$SCRIPT_NAME] $level $*"
  echo -e "${color}${msg}${NC}" >&2
  echo "$msg" >> "$LOG_FILE"
}
log()  { _log "INFO " "$GREEN"  "$@"; }
warn() { _log "WARN " "$YELLOW" "$@"; }
err()  { _log "ERROR" "$RED"    "$@"; }
die()  { err "$@"; exit 1; }

# ─── Progress Bar ───────────────────────────────────────────
progress() {
  local current="$1" total="$2" label="${3:-Processing}"
  local pct=$((current * 100 / total))
  local filled=$((pct / 2))
  local empty=$((50 - filled))
  printf "\r${CYAN}%s${NC} [%s%s] %d/%d (%d%%)" \
    "$label" \
    "$(printf '#%.0s' $(seq 1 $filled 2>/dev/null) )" \
    "$(printf '.%.0s' $(seq 1 $empty 2>/dev/null) )" \
    "$current" "$total" "$pct" >&2
  [[ "$current" -eq "$total" ]] && echo "" >&2
}

# ─── Help ───────────────────────────────────────────────────
usage() {
  cat <<EOF
${CYAN}$SCRIPT_NAME${NC} v$VERSION — <description>

${YELLOW}USAGE:${NC}
  $SCRIPT_NAME <command> [options] <args>

${YELLOW}COMMANDS:${NC}
  run         Execute the main operation
  check       Validate inputs without executing
  status      Show current state

${YELLOW}OPTIONS:${NC}
  -h, --help       Show this help
  -v, --version    Show version
  -n, --dry-run    Preview without side effects
  -q, --quiet      Errors only
  -o, --output DIR Output directory (default: ./output)
  --verbose        Debug-level logging
  --no-color       Disable colored output

${YELLOW}EXAMPLES:${NC}
  $SCRIPT_NAME run data.json
  $SCRIPT_NAME run --dry-run --output /tmp/out data/
  $SCRIPT_NAME check input.csv

${YELLOW}ENVIRONMENT:${NC}
  ${SCRIPT_NAME^^}_CONFIG    Config file path (default: ./${SCRIPT_NAME}.conf)
EOF
  exit 0
}

# ─── Args Parsing ────────────────────────────────────────────
COMMAND=""
DRY_RUN=false
QUIET=false
VERBOSE=false
OUTPUT_DIR="./output"
INPUTS=()

parse_args() {
  [[ $# -eq 0 ]] && usage

  COMMAND="${1:-}"; shift || true

  case "$COMMAND" in
    run|check|status) ;;
    -h|--help) usage ;;
    -v|--version) echo "$VERSION"; exit 0 ;;
    *) die "Unknown command: $COMMAND. Use --help." ;;
  esac

  while [[ $# -gt 0 ]]; do
    case "$1" in
      -h|--help)     usage ;;
      -n|--dry-run)  DRY_RUN=true ;;
      -q|--quiet)    QUIET=true ;;
      -o|--output)   OUTPUT_DIR="${2:?--output requires a value}"; shift ;;
      --verbose)     VERBOSE=true ;;
      --no-color)    ;; # already handled by -t check
      -*)            die "Unknown option: $1" ;;
      *)             INPUTS+=("$1") ;;
    esac
    shift
  done
}

# ─── Validation ──────────────────────────────────────────────
validate() {
  local errors=0

  # Check dependencies
  for cmd in jq node; do
    if ! command -v "$cmd" &>/dev/null; then
      err "Missing dependency: $cmd"
      ((errors++))
    fi
  done

  # Check inputs
  if [[ ${#INPUTS[@]} -eq 0 ]]; then
    err "No input files specified"
    ((errors++))
  fi

  for input in "${INPUTS[@]}"; do
    if [[ ! -e "$input" ]]; then
      err "Input not found: $input"
      ((errors++))
    fi
  done

  # Check output dir
  if [[ "$COMMAND" == "run" ]]; then
    mkdir -p "$OUTPUT_DIR" 2>/dev/null || die "Cannot create output dir: $OUTPUT_DIR"
  fi

  [[ $errors -gt 0 ]] && die "$errors validation error(s). Fix and retry."
  log "✅ Validation passed"
}

# ─── Cleanup ────────────────────────────────────────────────
CLEANUP_FILES=()
cleanup() {
  local exit_code=$?
  for f in "${CLEANUP_FILES[@]}"; do
    [[ -f "$f" ]] && rm -f "$f"
  done
  if [[ $exit_code -ne 0 ]]; then
    warn "Script exited with code $exit_code. Log: $LOG_FILE"
  fi
}
trap cleanup EXIT

# ─── Commands ────────────────────────────────────────────────
cmd_run() {
  log "Processing ${#INPUTS[@]} input(s) → $OUTPUT_DIR"

  local total=${#INPUTS[@]}
  local success=0 failed=0

  for i in "${!INPUTS[@]}"; do
    local input="${INPUTS[$i]}"
    local idx=$((i + 1))
    progress "$idx" "$total" "Processing"

    if [[ "$DRY_RUN" == true ]]; then
      log "[DRY-RUN] Would process: $input"
      ((success++))
      continue
    fi

    # Process each input
    if process_one "$input"; then
      ((success++))
    else
      warn "Failed to process: $input"
      ((failed++))
    fi
  done

  # Summary
  echo "" >&2
  log "━━━ Summary ━━━"
  log "  Total:   $total"
  log "  Success: $success"
  [[ $failed -gt 0 ]] && warn "  Failed:  $failed"
  log "  Output:  $OUTPUT_DIR"
  log "  Log:     $LOG_FILE"

  [[ $failed -gt 0 ]] && return 3 # partial failure
  return 0
}

cmd_check() {
  log "Checking ${#INPUTS[@]} input(s)..."
  for input in "${INPUTS[@]}"; do
    if [[ -f "$input" ]]; then
      local size=$(wc -c < "$input" | tr -d ' ')
      log "  ✅ $input ($size bytes)"
    else
      warn "  ❌ $input (not found)"
    fi
  done
}

cmd_status() {
  log "Output dir: $OUTPUT_DIR"
  if [[ -d "$OUTPUT_DIR" ]]; then
    local count=$(find "$OUTPUT_DIR" -type f | wc -l | tr -d ' ')
    log "  Files: $count"
  else
    log "  (not created yet)"
  fi
}

# ─── Business Logic ─────────────────────────────────────────
process_one() {
  local input="$1"
  # ... implement per-item processing ...
  return 0
}

# ─── Main ────────────────────────────────────────────────────
parse_args "$@"
validate

case "$COMMAND" in
  run)    cmd_run ;;
  check)  cmd_check ;;
  status) cmd_status ;;
esac
```

## Node.js Template — Multi-Step CLI

```javascript
#!/usr/bin/env node
// @ts-check
'use strict';

/**
 * <name> — <description>
 * Usage: node <name>.js <command> [options] <args>
 */

const fs = require('fs');
const path = require('path');
const { parseArgs } = require('util');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

// ─── Logging ────────────────────────────────────────────────
const isTTY = process.stderr.isTTY;
const c = {
  red: isTTY ? '\x1b[31m' : '', green: isTTY ? '\x1b[32m' : '',
  yellow: isTTY ? '\x1b[33m' : '', cyan: isTTY ? '\x1b[36m' : '',
  dim: isTTY ? '\x1b[2m' : '', reset: isTTY ? '\x1b[0m' : '',
};
const ts = () => new Date().toISOString().slice(11, 19);

const log = Object.assign(
  (...args) => console.error(`${c.dim}${ts()}${c.reset} ${c.green}INFO${c.reset} `, ...args),
  {
    warn: (...args) => console.error(`${c.dim}${ts()}${c.reset} ${c.yellow}WARN${c.reset} `, ...args),
    error: (...args) => console.error(`${c.dim}${ts()}${c.reset} ${c.red}ERROR${c.reset}`, ...args),
    die: (...args) => { log.error(...args); process.exit(1); },
  }
);

// ─── Progress ───────────────────────────────────────────────
function progress(current, total, label = 'Processing') {
  if (!isTTY) return;
  const pct = Math.round((current / total) * 100);
  const filled = Math.round(pct / 2);
  const bar = '#'.repeat(filled) + '.'.repeat(50 - filled);
  process.stderr.write(`\r${c.cyan}${label}${c.reset} [${bar}] ${current}/${total} (${pct}%)`);
  if (current === total) process.stderr.write('\n');
}

// ─── Args ───────────────────────────────────────────────────
function parseCliArgs() {
  const { values, positionals } = parseArgs({
    allowPositionals: true,
    options: {
      help:      { type: 'boolean', short: 'h' },
      version:   { type: 'boolean', short: 'v' },
      'dry-run': { type: 'boolean', short: 'n' },
      quiet:     { type: 'boolean', short: 'q' },
      output:    { type: 'string',  short: 'o', default: './output' },
      verbose:   { type: 'boolean' },
    },
  });

  if (values.help || positionals.length === 0) {
    console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION}

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js <command> [options] <inputs...>

${c.yellow}COMMANDS:${c.reset}
  run     Execute the main operation
  check   Validate inputs

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show help
  -v, --version    Show version
  -n, --dry-run    Preview mode
  -o, --output     Output directory
  -q, --quiet      Errors only
`);
    process.exit(0);
  }

  if (values.version) { console.log(VERSION); process.exit(0); }

  const [command, ...inputs] = positionals;
  return { command, inputs, ...values, output: values.output || './output' };
}

// ─── Validation ─────────────────────────────────────────────
function validate(config) {
  const errors = [];

  if (!['run', 'check'].includes(config.command)) {
    errors.push(`Unknown command: ${config.command}`);
  }

  if (config.inputs.length === 0) {
    errors.push('No input files specified');
  }

  for (const input of config.inputs) {
    if (!fs.existsSync(input)) errors.push(`Input not found: ${input}`);
  }

  if (errors.length > 0) {
    errors.forEach(e => log.error(e));
    log.die(`${errors.length} validation error(s)`);
  }

  log('✅ Validation passed');
}

// ─── Business Logic ─────────────────────────────────────────
async function processOne(input, outputDir, dryRun) {
  if (dryRun) {
    log(`[DRY-RUN] Would process: ${input}`);
    return { status: 'skipped', input };
  }

  // ... implement processing ...

  return { status: 'success', input };
}

// ─── Commands ───────────────────────────────────────────────
async function cmdRun(config) {
  const { inputs, output: outputDir } = config;
  fs.mkdirSync(outputDir, { recursive: true });

  log(`Processing ${inputs.length} input(s) → ${outputDir}`);
  const results = { success: 0, failed: 0, errors: [] };

  for (let i = 0; i < inputs.length; i++) {
    progress(i + 1, inputs.length);
    try {
      const result = await processOne(inputs[i], outputDir, config['dry-run']);
      if (result.status === 'success' || result.status === 'skipped') results.success++;
      else results.failed++;
    } catch (err) {
      log.warn(`Failed: ${inputs[i]} — ${err.message}`);
      results.failed++;
      results.errors.push({ input: inputs[i], error: err.message });
    }
  }

  // Summary
  log('━━━ Summary ━━━');
  log(`  Total:   ${inputs.length}`);
  log(`  Success: ${results.success}`);
  if (results.failed > 0) log.warn(`  Failed:  ${results.failed}`);
  log(`  Output:  ${outputDir}`);

  // Write manifest
  const manifest = {
    _generated: new Date().toISOString(),
    _version: VERSION,
    total: inputs.length,
    ...results,
  };
  fs.writeFileSync(
    path.join(outputDir, 'manifest.json'),
    JSON.stringify(manifest, null, 2)
  );

  process.exitCode = results.failed > 0 ? 3 : 0;
}

async function cmdCheck(config) {
  for (const input of config.inputs) {
    const stat = fs.statSync(input);
    log(`  ✅ ${input} (${stat.size} bytes)`);
  }
}

// ─── Main ───────────────────────────────────────────────────
async function main() {
  const config = parseCliArgs();
  validate(config);

  switch (config.command) {
    case 'run':   await cmdRun(config); break;
    case 'check': await cmdCheck(config); break;
  }
}

main().catch(err => log.die(err.message));
```

## Key Patterns — Moderate

### 1. Retry with Exponential Backoff
```javascript
async function withRetry(fn, { maxAttempts = 3, baseDelay = 1000 } = {}) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt === maxAttempts) throw err;
      const delay = baseDelay * Math.pow(2, attempt - 1);
      log.warn(`Attempt ${attempt}/${maxAttempts} failed. Retry in ${delay}ms...`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
}
```

### 2. Concurrent Processing with Limit
```javascript
async function processPool(items, worker, { concurrency = 5 } = {}) {
  const results = [];
  const executing = new Set();

  for (const item of items) {
    const p = worker(item).then(r => {
      executing.delete(p);
      return r;
    });
    executing.add(p);
    results.push(p);

    if (executing.size >= concurrency) {
      await Promise.race(executing);
    }
  }

  return Promise.allSettled(results);
}
```

### 3. File Lock (bash, prevent concurrent runs)
```bash
LOCKFILE="/tmp/${SCRIPT_NAME}.lock"

acquire_lock() {
  if ! mkdir "$LOCKFILE" 2>/dev/null; then
    local pid
    pid=$(cat "$LOCKFILE/pid" 2>/dev/null)
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
      die "Already running (PID $pid). Lock: $LOCKFILE"
    else
      warn "Stale lock found. Removing."
      rm -rf "$LOCKFILE"
      mkdir "$LOCKFILE"
    fi
  fi
  echo $$ > "$LOCKFILE/pid"
}

release_lock() {
  rm -rf "$LOCKFILE"
}

trap release_lock EXIT
acquire_lock
```

### 4. Config File Support
```bash
# Load config (source only known-safe files)
CONFIG_FILE="${SCRIPT_NAME}.conf"
if [[ -f "$CONFIG_FILE" ]]; then
  log "Loading config: $CONFIG_FILE"
  # shellcheck source=/dev/null
  source "$CONFIG_FILE"
fi
```

### 5. Parallel Processing (bash, with GNU parallel or xargs)
```bash
process_parallel() {
  local input_list="$1"
  local max_jobs="${2:-4}"

  if command -v parallel &>/dev/null; then
    parallel -j "$max_jobs" --bar process_one {} :::: "$input_list"
  else
    xargs -P "$max_jobs" -I {} bash -c 'process_one "$@"' _ {} < "$input_list"
  fi
}
export -f process_one  # Required for xargs/parallel
```

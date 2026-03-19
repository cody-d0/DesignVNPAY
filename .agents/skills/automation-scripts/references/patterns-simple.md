# Simple Script Patterns (< 100 LOC)

Script đơn giản nhưng vẫn đủ safety nets.

## Bash Template — Simple

```bash
#!/usr/bin/env bash
# ============================================================
# Script: <name>.sh
# Purpose: <one-line description>
# Usage: ./<name>.sh [options] <args>
# Exit codes: 0=success, 1=error, 2=usage error
# ============================================================
set -euo pipefail

# ─── Configuration ──────────────────────────────────────────
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"
readonly VERSION="1.0.0"
readonly LOG_PREFIX="[$SCRIPT_NAME]"

# ─── Logging ────────────────────────────────────────────────
log()  { echo "$(date '+%H:%M:%S') $LOG_PREFIX INFO  $*"; }
warn() { echo "$(date '+%H:%M:%S') $LOG_PREFIX WARN  $*" >&2; }
die()  { echo "$(date '+%H:%M:%S') $LOG_PREFIX ERROR $*" >&2; exit 1; }

# ─── Help ───────────────────────────────────────────────────
usage() {
  cat <<EOF
Usage: $SCRIPT_NAME [options] <input>

Options:
  -h, --help       Show this help
  -v, --version    Show version
  -n, --dry-run    Show what would be done without doing it
  -q, --quiet      Suppress non-error output

Examples:
  $SCRIPT_NAME data.json
  $SCRIPT_NAME --dry-run /path/to/folder
EOF
  exit 0
}

# ─── Args ───────────────────────────────────────────────────
DRY_RUN=false
QUIET=false
INPUT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)    usage ;;
    -v|--version) echo "$VERSION"; exit 0 ;;
    -n|--dry-run) DRY_RUN=true; shift ;;
    -q|--quiet)   QUIET=true; shift ;;
    -*)           die "Unknown option: $1. Use --help for usage." ;;
    *)            INPUT="$1"; shift ;;
  esac
done

# ─── Validation ─────────────────────────────────────────────
[[ -z "$INPUT" ]] && die "Missing required argument: <input>. Use --help."
[[ ! -e "$INPUT" ]] && die "Input not found: $INPUT"

# ─── Cleanup handler ────────────────────────────────────────
cleanup() {
  # Remove temp files, release locks, etc.
  [[ -n "${TMPFILE:-}" ]] && rm -f "$TMPFILE"
}
trap cleanup EXIT

# ─── Core Logic ─────────────────────────────────────────────
main() {
  log "Starting with input: $INPUT"

  if [[ "$DRY_RUN" == true ]]; then
    log "[DRY-RUN] Would process: $INPUT"
    return 0
  fi

  # ... actual logic here ...

  log "✅ Done"
}

main "$@"
```

## Node.js Template — Simple

```javascript
#!/usr/bin/env node
// @ts-check
'use strict';

/**
 * <name> — <one-line description>
 *
 * Usage: node <name>.js [options] <input>
 * Exit codes: 0=success, 1=error, 2=usage error
 */

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

// ─── Logging ────────────────────────────────────────────────
const ts = () => new Date().toISOString().slice(11, 19);
const log = (...args) => console.log(`${ts()} [${SCRIPT_NAME}] INFO `, ...args);
const warn = (...args) => console.warn(`${ts()} [${SCRIPT_NAME}] WARN `, ...args);
const die = (...args) => { console.error(`${ts()} [${SCRIPT_NAME}] ERROR`, ...args); process.exit(1); };

// ─── Unhandled rejection safety net ─────────────────────────
process.on('unhandledRejection', (err) => die('Unhandled rejection:', err));

// ─── Args ───────────────────────────────────────────────────
const args = process.argv.slice(2);
const flags = new Set(args.filter(a => a.startsWith('-')));
const positional = args.filter(a => !a.startsWith('-'));

if (flags.has('-h') || flags.has('--help')) {
  console.log(`
Usage: ${SCRIPT_NAME} [options] <input>

Options:
  -h, --help       Show this help
  -v, --version    Show version
  -n, --dry-run    Show what would be done
  -q, --quiet      Suppress info output

Examples:
  node ${SCRIPT_NAME}.js data.json
  node ${SCRIPT_NAME}.js --dry-run ./folder
`);
  process.exit(0);
}

if (flags.has('-v') || flags.has('--version')) {
  console.log(VERSION);
  process.exit(0);
}

const DRY_RUN = flags.has('-n') || flags.has('--dry-run');
const QUIET = flags.has('-q') || flags.has('--quiet');
const INPUT = positional[0];

// ─── Validation ─────────────────────────────────────────────
if (!INPUT) die('Missing required argument: <input>. Use --help.');
if (!fs.existsSync(INPUT)) die(`Input not found: ${INPUT}`);

// ─── Core Logic ─────────────────────────────────────────────
function main() {
  log(`Starting with input: ${INPUT}`);

  if (DRY_RUN) {
    log(`[DRY-RUN] Would process: ${INPUT}`);
    return;
  }

  // ... actual logic here ...

  log('✅ Done');
}

main();
```

## Python Template — Simple

```python
#!/usr/bin/env python3
"""<name> — <one-line description>.

Usage: python <name>.py [options] <input>
Exit codes: 0=success, 1=error, 2=usage error
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# ─── Logging ────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(Path(__file__).stem)

# ─── Args ───────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("input", help="Input file or directory")
    p.add_argument("-n", "--dry-run", action="store_true", help="Show what would be done")
    p.add_argument("-q", "--quiet", action="store_true", help="Suppress info output")
    p.add_argument("-v", "--version", action="version", version="1.0.0")
    return p.parse_args()


# ─── Core Logic ─────────────────────────────────────────────
def main() -> int:
    args = parse_args()

    if args.quiet:
        log.setLevel(logging.WARNING)

    input_path = Path(args.input)
    if not input_path.exists():
        log.error("Input not found: %s", input_path)
        return 1

    log.info("Starting with input: %s", input_path)

    if args.dry_run:
        log.info("[DRY-RUN] Would process: %s", input_path)
        return 0

    # ... actual logic here ...

    log.info("✅ Done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Key Patterns cho Simple Scripts

### 1. Guard Clauses (Fail Fast)
```bash
# Check dependencies before doing anything
command -v jq >/dev/null 2>&1 || die "jq is required. Install: brew install jq"
command -v node >/dev/null 2>&1 || die "Node.js is required"
```

### 2. Safe Temp Files
```bash
TMPFILE=$(mktemp /tmp/${SCRIPT_NAME}.XXXXXX)
trap 'rm -f "$TMPFILE"' EXIT
```

### 3. Atomic Write (prevent partial output)
```bash
# Write to temp → rename atomically
echo "$content" > "${OUTPUT}.tmp"
mv "${OUTPUT}.tmp" "$OUTPUT"
```

### 4. Idempotent Check
```bash
if [[ -f "$OUTPUT" ]]; then
  existing_hash=$(md5sum "$OUTPUT" | cut -d' ' -f1)
  new_hash=$(echo "$content" | md5sum | cut -d' ' -f1)
  if [[ "$existing_hash" == "$new_hash" ]]; then
    log "Output unchanged, skipping"
    exit 0
  fi
fi
```

### 5. Self-Test (--test flag)
```bash
self_test() {
  local passed=0 failed=0
  _t() {
    local label="$1"; shift
    if eval "$@" >/dev/null 2>&1; then
      echo "  ✅ $label"; ((passed++))
    else
      echo "  ❌ $label"; ((failed++))
    fi
  }
  _t "Dependencies" "command -v jq >/dev/null 2>&1"
  _t "Input readable" "[[ -r \"${INPUT:-/dev/null}\" ]]"
  _t "Output writable" "touch \"${OUTPUT_DIR:-.}/.test\" && rm \"${OUTPUT_DIR:-.}/.test\""
  echo ""
  log "Self-test: $passed passed, $failed failed"
  [[ $failed -eq 0 ]] && exit 0 || exit 1
}
[[ "${1:-}" == "--test" ]] && self_test
```

```javascript
// Node.js equivalent
if (process.argv.includes('--test')) {
  const tests = [
    ['Dependencies', () => { require('fs'); require('path'); }],
    ['Output writable', () => {
      const t = require('path').join(OUTPUT_DIR || '.', '.test');
      require('fs').writeFileSync(t, ''); require('fs').unlinkSync(t);
    }],
  ];
  let p = 0, f = 0;
  for (const [n, fn] of tests) {
    try { fn(); console.log(`  ✅ ${n}`); p++; }
    catch { console.log(`  ❌ ${n}`); f++; }
  }
  console.log(`\nSelf-test: ${p} passed, ${f} failed`);
  process.exit(f > 0 ? 1 : 0);
}
```

### 6. Execution Trace
```bash
TRACE_START=$(date +%s)
TRACE_OK=0 TRACE_FAIL=0

trace_end() {
  local d=$(( $(date +%s) - TRACE_START ))
  log "━━━ Done (${d}s) ━━━  OK: $TRACE_OK  Fail: $TRACE_FAIL  Exit: $?"
}
trap trace_end EXIT
```

```javascript
// Node.js equivalent
const _trace = { start: Date.now(), ok: 0, fail: 0 };
process.on('exit', () => {
  const d = ((Date.now() - _trace.start) / 1000).toFixed(1);
  console.error(`━━━ Done (${d}s) ━━━  OK: ${_trace.ok}  Fail: ${_trace.fail}`);
});
```

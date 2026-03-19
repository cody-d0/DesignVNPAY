# Template: File Processor

Script xử lý batch files với progress reporting và error tracking.

## Khi nào dùng

- Đổi format hàng loạt (CSV → JSON, MD → HTML)
- Resize/optimize nhiều images
- Parse và extract data từ nhiều files
- Rename/reorganize file structure

## Bash Skeleton

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0")"

# ─── Config ──────────────────────────────────────────────────
INPUT_DIR="${1:?Usage: $SCRIPT_NAME <input-dir> [output-dir]}"
OUTPUT_DIR="${2:-${INPUT_DIR}_processed}"
PATTERN="${3:-*.json}"         # File glob
PARALLEL=${PARALLEL:-1}        # Parallel jobs (1 = sequential)

# ─── Logging ────────────────────────────────────────────────
log()  { echo "$(date '+%H:%M:%S') INFO  $*"; }
warn() { echo "$(date '+%H:%M:%S') WARN  $*" >&2; }
die()  { echo "$(date '+%H:%M:%S') ERROR $*" >&2; exit 1; }

# ─── Validate ───────────────────────────────────────────────
[[ ! -d "$INPUT_DIR" ]] && die "Input dir not found: $INPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Count files
FILE_COUNT=$(find "$INPUT_DIR" -name "$PATTERN" -type f | wc -l | tr -d ' ')
[[ $FILE_COUNT -eq 0 ]] && die "No files matching $PATTERN in $INPUT_DIR"

log "Found $FILE_COUNT files matching '$PATTERN'"

# ─── Process function ───────────────────────────────────────
process_file() {
  local input="$1"
  local relative="${input#$INPUT_DIR/}"
  local output="$OUTPUT_DIR/$relative"

  # Create output subdirectory
  mkdir -p "$(dirname "$output")"

  # Skip if output exists and is newer (idempotent)
  if [[ -f "$output" && "$output" -nt "$input" ]]; then
    return 0
  fi

  # ── Your transform logic here ──
  # Example: copy with modification
  # sed 's/old/new/g' "$input" > "${output}.tmp"
  # mv "${output}.tmp" "$output"

  cp "$input" "$output"  # Placeholder
}
export -f process_file
export INPUT_DIR OUTPUT_DIR

# ─── Execute ────────────────────────────────────────────────
ERRORS=0
PROCESSED=0

if [[ $PARALLEL -gt 1 ]] && command -v parallel &>/dev/null; then
  log "Processing with $PARALLEL parallel jobs..."
  find "$INPUT_DIR" -name "$PATTERN" -type f -print0 |
    parallel -0 -j "$PARALLEL" --bar process_file {} 2>/dev/null || ERRORS=$?
else
  while IFS= read -r -d '' file; do
    ((PROCESSED++))
    printf "\r  Processing: %d/%d" "$PROCESSED" "$FILE_COUNT" >&2
    if ! process_file "$file"; then
      warn "Failed: $file"
      ((ERRORS++))
    fi
  done < <(find "$INPUT_DIR" -name "$PATTERN" -type f -print0 | sort -z)
  echo "" >&2
fi

# ─── Summary ────────────────────────────────────────────────
OUTPUT_COUNT=$(find "$OUTPUT_DIR" -type f | wc -l | tr -d ' ')
log "━━━ Summary ━━━"
log "  Input:  $FILE_COUNT files"
log "  Output: $OUTPUT_COUNT files → $OUTPUT_DIR"
[[ $ERRORS -gt 0 ]] && warn "  Errors: $ERRORS"

exit $([[ $ERRORS -gt 0 ]] && echo 3 || echo 0)
```

## Node.js Skeleton — Stream-Based

```javascript
#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const { pipeline } = require('stream/promises');

async function processFile(inputPath, outputDir) {
  const relative = path.relative(INPUT_DIR, inputPath);
  const outputPath = path.join(outputDir, relative);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });

  // Skip if output is newer (idempotent)
  if (fs.existsSync(outputPath)) {
    const inStat = fs.statSync(inputPath);
    const outStat = fs.statSync(outputPath);
    if (outStat.mtimeMs > inStat.mtimeMs) return 'skipped';
  }

  // Stream-based transform (memory-efficient for large files)
  const { Transform } = require('stream');
  const transform = new Transform({
    transform(chunk, enc, cb) {
      // Your transform logic here
      cb(null, chunk);
    }
  });

  await pipeline(
    fs.createReadStream(inputPath),
    transform,
    fs.createWriteStream(outputPath + '.tmp'),
  );

  fs.renameSync(outputPath + '.tmp', outputPath); // Atomic
  return 'processed';
}
```

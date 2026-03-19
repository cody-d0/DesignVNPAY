# Template: Data Pipeline

Multi-stage pipeline với checkpoint, resume, và data validation.

## Khi nào dùng

- ETL (Extract → Transform → Load)
- Data migration giữa formats
- Multi-step data enrichment
- Large dataset processing

## Xem Pipeline Engine

→ Đọc `references/patterns-complex.md` Section "Pipeline Pattern — Node.js"
cho engine hoàn chỉnh với checkpoint/resume.

## Quick Pipeline — Bash

```bash
#!/usr/bin/env bash
# ============================================================
# Data Pipeline: <name>
# Purpose: ETL pipeline with checkpoint/resume
# Usage: ./<name>.sh [--resume] [--stage <name>] <input>
# Exit codes: 0=success, 1=error, 3=partial
# ============================================================
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0" .sh)"
readonly WORK_DIR="${WORK_DIR:-.pipeline-work}"
readonly STATE_FILE="$WORK_DIR/.state"

# ─── Logging ────────────────────────────────────────────────
log()  { echo "$(date '+%H:%M:%S') [$SCRIPT_NAME] INFO  $*"; }
warn() { echo "$(date '+%H:%M:%S') [$SCRIPT_NAME] WARN  $*" >&2; }
die()  { echo "$(date '+%H:%M:%S') [$SCRIPT_NAME] ERROR $*" >&2; exit 1; }

# ─── State Management (checkpoint/resume) ───────────────────
mkdir -p "$WORK_DIR"

get_state()  { cat "$STATE_FILE" 2>/dev/null || echo "init"; }
set_state()  { echo "$1" > "$STATE_FILE"; log "  Checkpoint: $1"; }

# ─── Validation ─────────────────────────────────────────────
INPUT="${1:?Usage: $SCRIPT_NAME <input-file>}"
[[ ! -f "$INPUT" ]] && die "Input not found: $INPUT"

# ─── Stages ─────────────────────────────────────────────────
stage_extract() {
  log "📥 Stage 1: Extract"
  local count
  # Example: count lines/records
  count=$(wc -l < "$INPUT" | tr -d ' ')
  log "  Found $count records"

  # ... extract logic, output to work dir ...
  cp "$INPUT" "$WORK_DIR/extracted.json"  # Placeholder
  set_state "extracted"
}

stage_transform() {
  log "🔄 Stage 2: Transform"
  [[ ! -f "$WORK_DIR/extracted.json" ]] && die "Missing extract output. Re-run from init."

  # ... transform logic ...
  cp "$WORK_DIR/extracted.json" "$WORK_DIR/transformed.json"  # Placeholder
  set_state "transformed"
}

stage_load() {
  log "📤 Stage 3: Load"
  [[ ! -f "$WORK_DIR/transformed.json" ]] && die "Missing transform output. Re-run from extracted."

  # ... load logic (write output, call API, etc) ...
  cp "$WORK_DIR/transformed.json" "$WORK_DIR/output.json"  # Placeholder
  set_state "complete"
}

# ─── Runner with Resume ─────────────────────────────────────
current=$(get_state)
log "Pipeline: $SCRIPT_NAME"
log "  State:  $current"
log "  Input:  $INPUT"

case "$current" in
  init)         stage_extract;  ;&  # fall through
  extracted)    stage_transform; ;& 
  transformed)  stage_load ;;
  complete)     log "✅ Already complete. Delete $STATE_FILE to re-run." ;;
  *)            die "Unknown state: $current" ;;
esac

log "🎉 Pipeline done"
```

## Node.js Pipeline — With Validation Between Stages

```javascript
#!/usr/bin/env node
'use strict';

/**
 * Data Pipeline — ETL with stage validation and checkpoint
 * Usage: node pipeline.js <input> [--resume] [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const WORK_DIR = '.pipeline-work';
const STATE_FILE = path.join(WORK_DIR, '.state.json');

// ─── State ──────────────────────────────────────────────────
function loadState() {
  try { return JSON.parse(fs.readFileSync(STATE_FILE, 'utf-8')); }
  catch { return { stage: 'init', results: {} }; }
}

function saveState(state) {
  fs.mkdirSync(WORK_DIR, { recursive: true });
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

// ─── Stage Validators ───────────────────────────────────────
// Validate output of each stage BEFORE proceeding to next
const validators = {
  extract(result) {
    if (!result || !result.records || result.records.length === 0)
      throw new Error('Extract produced no records');
    return true;
  },
  transform(result) {
    if (!result || !result.transformed)
      throw new Error('Transform produced no output');
    return true;
  },
};

// ─── Stages ─────────────────────────────────────────────────
const stages = [
  {
    name: 'extract',
    description: 'Read and parse input data',
    async run(ctx) {
      const raw = fs.readFileSync(ctx.input, 'utf-8');
      const data = JSON.parse(raw);
      const records = Array.isArray(data) ? data : [data];
      console.log(`  📥 Extracted ${records.length} records`);
      return { records, count: records.length };
    },
  },
  {
    name: 'transform',
    description: 'Apply business logic transformations',
    async run(ctx) {
      const { records } = ctx.results.extract;
      // ... transform logic ...
      const transformed = records.map(r => ({ ...r, _transformed: true }));
      console.log(`  🔄 Transformed ${transformed.length} records`);
      return { transformed, count: transformed.length };
    },
  },
  {
    name: 'load',
    description: 'Write output files',
    async run(ctx) {
      const { transformed } = ctx.results.transform;
      const outputPath = path.join(WORK_DIR, 'output.json');
      fs.writeFileSync(outputPath, JSON.stringify(transformed, null, 2));
      console.log(`  📤 Loaded ${transformed.length} records → ${outputPath}`);
      return { outputPath, count: transformed.length };
    },
  },
];

// ─── Main ───────────────────────────────────────────────────
async function main() {
  const args = process.argv.slice(2);
  const input = args.find(a => !a.startsWith('-'));
  const resume = args.includes('--resume');
  const dryRun = args.includes('--dry-run');

  if (!input) {
    console.log('Usage: node pipeline.js <input> [--resume] [--dry-run]');
    process.exit(2);
  }

  if (!fs.existsSync(input)) {
    console.error(`Input not found: ${input}`);
    process.exit(1);
  }

  let state = resume ? loadState() : { stage: 'init', results: {} };
  const startIdx = resume
    ? stages.findIndex(s => s.name === state.stage)
    : 0;

  console.log(`\n🚀 Pipeline: ${stages.map(s => s.name).join(' → ')}`);
  if (resume && startIdx > 0) console.log(`⏩ Resuming from: ${state.stage}`);

  const ctx = { input, results: state.results };
  const t0 = Date.now();

  for (let i = Math.max(0, startIdx); i < stages.length; i++) {
    const stage = stages[i];
    console.log(`\n── Stage ${i + 1}/${stages.length}: ${stage.name} ──`);
    console.log(`   ${stage.description}`);

    if (dryRun) {
      console.log(`   [DRY-RUN] Would execute: ${stage.name}`);
      continue;
    }

    try {
      const result = await stage.run(ctx);

      // Validate stage output if validator exists
      if (validators[stage.name]) {
        validators[stage.name](result);
        console.log(`   ✅ Validated`);
      }

      ctx.results[stage.name] = result;
      state = { stage: stage.name, results: ctx.results };
      saveState(state);
      console.log(`   ✅ Checkpoint saved`);
    } catch (err) {
      console.error(`   ❌ ${err.message}`);
      state.stage = stage.name;
      state.error = err.message;
      saveState(state);
      console.error(`\n💡 Fix issue, then: node pipeline.js ${input} --resume`);
      process.exit(1);
    }
  }

  const elapsed = ((Date.now() - t0) / 1000).toFixed(1);
  console.log(`\n🎉 Pipeline complete (${elapsed}s)\n`);
}

main().catch(err => {
  console.error(`💥 ${err.message}`);
  process.exit(1);
});
```

## Key Concepts

### 1. Stage Validation

Validate output giữa mỗi stage để catch data issues sớm:

```javascript
// TRƯỚC khi chạy stage N+1, validate output của stage N
const validators = {
  extract(result) {
    assert(result.records.length > 0, 'No records extracted');
    assert(result.records.every(r => r.id), 'Records missing ID field');
  },
  transform(result) {
    assert(result.transformed.length > 0, 'Transform produced empty output');
  },
};
```

### 2. Atomic Stage Output

Mỗi stage ghi output qua temp file → rename. Nếu crash giữa chừng, output không bị corrupt:

```bash
stage_transform() {
  # Write to temp
  process_data > "$WORK_DIR/transformed.tmp"
  # Atomic move only if successful
  mv "$WORK_DIR/transformed.tmp" "$WORK_DIR/transformed.json"
  set_state "transformed"
}
```

### 3. Pipeline Metrics

```javascript
// Track per-stage metrics
const metrics = {
  stages: [],
  record(name, { duration, inputCount, outputCount, errors }) {
    this.stages.push({ name, duration, inputCount, outputCount, errors });
  },
  summary() {
    console.log('\n━━━ Pipeline Metrics ━━━');
    for (const s of this.stages) {
      console.log(`  ${s.name}: ${s.duration}ms, in=${s.inputCount}, out=${s.outputCount}, err=${s.errors}`);
    }
  },
};
```

# Complex Script Patterns (300+ LOC)

Pipelines, checkpoint/resume, state machines, multi-stage workflows.

---

## Pipeline Pattern — Node.js

Cho data processing pipelines cần checkpoint, resume, và audit trail.

```javascript
#!/usr/bin/env node
// @ts-check
'use strict';

/**
 * <name> — Multi-stage data pipeline with checkpoint/resume
 *
 * Stages run sequentially. If a stage fails, the pipeline stops
 * and can be resumed from the last successful checkpoint.
 *
 * Usage: node <name>.js run <input> [--resume] [--stage <name>]
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// ─── Pipeline Engine ────────────────────────────────────────

class Pipeline {
  /**
   * @param {Object} config
   * @param {string} config.name - Pipeline name
   * @param {string} config.workDir - Working directory for state
   * @param {boolean} config.dryRun - Preview mode
   */
  constructor({ name, workDir, dryRun = false }) {
    this.name = name;
    this.workDir = workDir;
    this.dryRun = dryRun;
    this.stateFile = path.join(workDir, '.pipeline-state.json');
    this.stages = [];
    this.state = this._loadState();

    fs.mkdirSync(workDir, { recursive: true });
  }

  /** Register a pipeline stage */
  addStage(name, fn, { description = '', retries = 0 } = {}) {
    this.stages.push({ name, fn, description, retries });
    return this;
  }

  /** Execute all stages (or resume from checkpoint) */
  async run(input, { resumeFrom = null } = {}) {
    const runId = crypto.randomUUID().slice(0, 8);
    const startTime = Date.now();

    this.state.runId = runId;
    this.state.startedAt = new Date().toISOString();
    this.state.input = typeof input === 'string' ? input : '[object]';

    console.log(`\n🚀 Pipeline: ${this.name} (run ${runId})`);
    console.log(`   Stages: ${this.stages.map(s => s.name).join(' → ')}\n`);

    let context = { input, results: {}, meta: {} };
    let startIdx = 0;

    // Resume from checkpoint
    if (resumeFrom) {
      startIdx = this.stages.findIndex(s => s.name === resumeFrom);
      if (startIdx < 0) throw new Error(`Unknown stage: ${resumeFrom}`);
      context = { ...context, ...this.state.lastContext };
      console.log(`⏩ Resuming from stage: ${resumeFrom}\n`);
    }

    for (let i = startIdx; i < this.stages.length; i++) {
      const stage = this.stages[i];
      const stageStart = Date.now();

      console.log(`── Stage ${i + 1}/${this.stages.length}: ${stage.name} ──`);
      if (stage.description) console.log(`   ${stage.description}`);

      if (this.dryRun) {
        console.log(`   [DRY-RUN] Would execute: ${stage.name}\n`);
        continue;
      }

      try {
        const result = await this._runWithRetry(stage, context);
        context.results[stage.name] = result;

        const elapsed = ((Date.now() - stageStart) / 1000).toFixed(1);
        console.log(`   ✅ Done (${elapsed}s)\n`);

        // Checkpoint
        this.state.completedStages = this.stages.slice(0, i + 1).map(s => s.name);
        this.state.lastContext = context;
        this._saveState();

      } catch (err) {
        const elapsed = ((Date.now() - stageStart) / 1000).toFixed(1);
        console.error(`   ❌ Failed (${elapsed}s): ${err.message}\n`);

        this.state.failedStage = stage.name;
        this.state.error = err.message;
        this._saveState();

        console.error(`\n💡 Resume command:`);
        console.error(`   node ${path.basename(__filename)} run <input> --resume --stage ${stage.name}\n`);

        throw err;
      }
    }

    const totalElapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    console.log(`\n🎉 Pipeline complete (${totalElapsed}s)`);

    this.state.completedAt = new Date().toISOString();
    this.state.status = 'complete';
    this._saveState();

    return context.results;
  }

  /** @private */
  async _runWithRetry(stage, context) {
    let lastErr;
    for (let attempt = 0; attempt <= stage.retries; attempt++) {
      try {
        return await stage.fn(context);
      } catch (err) {
        lastErr = err;
        if (attempt < stage.retries) {
          const delay = 1000 * Math.pow(2, attempt);
          console.warn(`   ⚠️  Attempt ${attempt + 1} failed. Retry in ${delay}ms...`);
          await new Promise(r => setTimeout(r, delay));
        }
      }
    }
    throw lastErr;
  }

  /** @private */
  _loadState() {
    try {
      return JSON.parse(fs.readFileSync(this.stateFile, 'utf-8'));
    } catch {
      return { status: 'new', completedStages: [] };
    }
  }

  /** @private */
  _saveState() {
    fs.writeFileSync(this.stateFile, JSON.stringify(this.state, null, 2));
  }
}

// ─── Usage Example ──────────────────────────────────────────

async function main() {
  const pipeline = new Pipeline({
    name: 'data-transform',
    workDir: './pipeline-workspace',
    dryRun: process.argv.includes('--dry-run'),
  });

  pipeline
    .addStage('validate', async (ctx) => {
      // Validate input exists and is well-formed
      const stats = fs.statSync(ctx.input);
      return { bytes: stats.size, valid: true };
    }, { description: 'Validate input data' })

    .addStage('parse', async (ctx) => {
      // Parse raw data into structured format
      const raw = fs.readFileSync(ctx.input, 'utf-8');
      const data = JSON.parse(raw);
      return { recordCount: Array.isArray(data) ? data.length : 1 };
    }, { description: 'Parse and structure data', retries: 1 })

    .addStage('transform', async (ctx) => {
      // Apply business logic transformations
      return { transformed: true };
    }, { description: 'Apply transformations' })

    .addStage('output', async (ctx) => {
      // Write final output
      const outputPath = path.join('./pipeline-workspace', 'output.json');
      fs.writeFileSync(outputPath, JSON.stringify(ctx.results, null, 2));
      return { outputPath };
    }, { description: 'Write output files' });

  const resumeStage = process.argv.includes('--stage')
    ? process.argv[process.argv.indexOf('--stage') + 1]
    : null;

  await pipeline.run(process.argv[process.argv.length - 1], {
    resumeFrom: resumeStage,
  });
}

main().catch(err => {
  console.error(`\n💥 Pipeline failed: ${err.message}`);
  process.exit(1);
});
```

---

## State Machine Pattern — Python

Cho workflows phức tạp với branching logic.

```python
#!/usr/bin/env python3
"""State machine workflow engine with audit trail."""
from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from typing import Any, Callable

log = logging.getLogger(__name__)


class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    SUCCESS = auto()
    FAILED = auto()
    SKIPPED = auto()


@dataclass
class StepResult:
    name: str
    status: Status
    duration_ms: int = 0
    output: Any = None
    error: str | None = None


@dataclass
class WorkflowState:
    workflow_name: str
    run_id: str
    started_at: str = ""
    completed_at: str = ""
    current_step: str = ""
    steps: list[StepResult] = field(default_factory=list)
    context: dict = field(default_factory=dict)

    def save(self, path: Path):
        data = asdict(self)
        # Convert Status enums to strings
        for step in data["steps"]:
            step["status"] = step["status"].name
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    @classmethod
    def load(cls, path: Path) -> "WorkflowState":
        data = json.loads(path.read_text())
        for step in data["steps"]:
            step["status"] = Status[step["status"]]
        return cls(**data)


class Workflow:
    def __init__(self, name: str, work_dir: str = ".workflow"):
        self.name = name
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.steps: list[tuple[str, Callable, dict]] = []

    def step(self, name: str, *, description: str = "", retries: int = 0):
        """Decorator to register a workflow step."""
        def decorator(fn: Callable):
            self.steps.append((name, fn, {
                "description": description,
                "retries": retries,
            }))
            return fn
        return decorator

    def run(self, context: dict | None = None, resume_from: str | None = None) -> WorkflowState:
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        state = WorkflowState(
            workflow_name=self.name,
            run_id=run_id,
            started_at=datetime.now().isoformat(),
            context=context or {},
        )

        start_idx = 0
        if resume_from:
            names = [s[0] for s in self.steps]
            if resume_from not in names:
                raise ValueError(f"Unknown step: {resume_from}")
            start_idx = names.index(resume_from)
            log.info("Resuming from step: %s", resume_from)

        log.info("🚀 Workflow: %s (run %s)", self.name, run_id)
        log.info("   Steps: %s", " → ".join(s[0] for s in self.steps))

        for i in range(start_idx, len(self.steps)):
            name, fn, opts = self.steps[i]
            state.current_step = name
            log.info("── Step %d/%d: %s ──", i + 1, len(self.steps), name)

            t0 = time.monotonic()
            try:
                output = fn(state.context)
                elapsed = int((time.monotonic() - t0) * 1000)
                state.steps.append(StepResult(
                    name=name, status=Status.SUCCESS,
                    duration_ms=elapsed, output=output,
                ))
                log.info("   ✅ Done (%dms)", elapsed)
            except Exception as exc:
                elapsed = int((time.monotonic() - t0) * 1000)
                state.steps.append(StepResult(
                    name=name, status=Status.FAILED,
                    duration_ms=elapsed, error=str(exc),
                ))
                log.error("   ❌ Failed (%dms): %s", elapsed, exc)
                state.save(self.work_dir / f"state-{run_id}.json")
                raise

        state.completed_at = datetime.now().isoformat()
        state.save(self.work_dir / f"state-{run_id}.json")
        log.info("🎉 Workflow complete")
        return state
```

---

## Batch Processor Pattern — Bash

Xử lý hàng ngàn files với progress, parallel, và recovery.

```bash
#!/usr/bin/env bash
set -euo pipefail

# ─── Batch Processor with Checkpoint ────────────────────────
readonly WORK_DIR=".batch-work"
readonly DONE_FILE="$WORK_DIR/done.txt"
readonly FAIL_FILE="$WORK_DIR/failed.txt"
readonly PROGRESS_FILE="$WORK_DIR/progress.json"

init_batch() {
  mkdir -p "$WORK_DIR"
  touch "$DONE_FILE" "$FAIL_FILE"
}

is_done() {
  grep -qFx "$1" "$DONE_FILE" 2>/dev/null
}

mark_done() {
  echo "$1" >> "$DONE_FILE"
}

mark_failed() {
  echo "$1" >> "$FAIL_FILE"
}

save_progress() {
  local processed="$1" total="$2" failed="$3"
  cat > "$PROGRESS_FILE" <<EOF
{
  "processed": $processed,
  "total": $total,
  "failed": $failed,
  "last_update": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "pct": $(( processed * 100 / total ))
}
EOF
}

run_batch() {
  local input_dir="$1"
  local output_dir="$2"

  init_batch
  mkdir -p "$output_dir"

  # Collect items
  local items=()
  while IFS= read -r -d '' file; do
    items+=("$file")
  done < <(find "$input_dir" -type f -name '*.json' -print0 | sort -z)

  local total=${#items[@]}
  local processed=0 failed=0 skipped=0

  log "Processing $total items ($(wc -l < "$DONE_FILE" | tr -d ' ') already done)"

  for item in "${items[@]}"; do
    local key="$(basename "$item")"

    # Skip already processed (idempotent resume)
    if is_done "$key"; then
      ((skipped++))
      ((processed++))
      continue
    fi

    ((processed++))
    progress "$processed" "$total" "Batch"

    if process_one "$item" "$output_dir"; then
      mark_done "$key"
    else
      mark_failed "$key"
      ((failed++))
    fi

    # Save progress every 100 items
    if (( processed % 100 == 0 )); then
      save_progress "$processed" "$total" "$failed"
    fi
  done

  save_progress "$processed" "$total" "$failed"

  log "━━━ Batch Complete ━━━"
  log "  Total:    $total"
  log "  New:      $((processed - skipped))"
  log "  Skipped:  $skipped (already done)"
  log "  Failed:   $failed"

  [[ $failed -gt 0 ]] && warn "Failed items in: $FAIL_FILE"
}
```

---

## Key Patterns — Complex

### 1. Graceful Shutdown (Node.js)
```javascript
let shuttingDown = false;

function setupGracefulShutdown(cleanup) {
  const handler = async (signal) => {
    if (shuttingDown) return;
    shuttingDown = true;
    console.error(`\n⚠️  Received ${signal}. Finishing current task...`);
    try {
      await cleanup();
    } finally {
      process.exit(0);
    }
  };
  process.on('SIGINT', handler);
  process.on('SIGTERM', handler);
}

// Usage
setupGracefulShutdown(async () => {
  await saveState();
  await closeConnections();
});
```

### 2. Rate Limiter
```javascript
class RateLimiter {
  constructor(maxPerSecond) {
    this.interval = 1000 / maxPerSecond;
    this.lastCall = 0;
  }

  async wait() {
    const now = Date.now();
    const elapsed = now - this.lastCall;
    if (elapsed < this.interval) {
      await new Promise(r => setTimeout(r, this.interval - elapsed));
    }
    this.lastCall = Date.now();
  }
}

// Usage: const limiter = new RateLimiter(10); // 10 req/sec
// await limiter.wait(); await fetch(url);
```

### 3. Structured Audit Log
```javascript
function auditLog(workDir) {
  const logPath = path.join(workDir, 'audit.jsonl');
  return {
    write(entry) {
      const line = JSON.stringify({
        _ts: new Date().toISOString(),
        ...entry,
      });
      fs.appendFileSync(logPath, line + '\n');
    },
    read() {
      return fs.readFileSync(logPath, 'utf-8')
        .trim().split('\n')
        .filter(Boolean)
        .map(JSON.parse);
    },
  };
}
```

### 4. Rollback Support (bash)
```bash
declare -a ROLLBACK_STACK=()

# Push a rollback action
push_rollback() {
  ROLLBACK_STACK+=("$*")
}

# Execute all rollback actions in reverse order
rollback() {
  warn "Rolling back ${#ROLLBACK_STACK[@]} action(s)..."
  for ((i=${#ROLLBACK_STACK[@]}-1; i>=0; i--)); do
    log "  Undo: ${ROLLBACK_STACK[$i]}"
    eval "${ROLLBACK_STACK[$i]}" || warn "  Rollback step failed (continuing)"
  done
}

# Usage:
# cp original backup && push_rollback "cp backup original"
# trap rollback ERR
```

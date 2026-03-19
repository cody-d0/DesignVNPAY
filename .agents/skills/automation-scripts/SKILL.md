---
name: automation-scripts
description: >
  Tạo các script automation chuyên nghiệp theo chuẩn ngành (Shell/Node/Python).
  Áp dụng khi cần: viết bash script, tạo CLI tool, build automation pipeline,
  data processing script, file transformation, cron job, CI/CD script,
  deployment script, migration script, hoặc bất kỳ script nào cần chạy
  đáng tin cậy trong production.
  Bao gồm: error handling chuẩn, logging, idempotency, input validation,
  dry-run mode, progress reporting, self-test, test plan, và failure mode prediction.
  Triggers: "viết script", "automation", "tạo CLI", "bash script",
  "build script", "deploy script", "migration script", "cron job",
  "data pipeline script", "batch processing", "file processing script",
  "tạo tool", "viết tool tự động", "script chuyên nghiệp".
---

# Automation Scripts — Professional Standard

Tạo script automation **production-grade** với đầy đủ safety nets.

> **Triết lý:** Script phải **tự bảo vệ mình** — validate trước khi chạy,
> log mọi thứ quan trọng, fail loud khi cần, recover gracefully khi có thể.
> **"A script that fails silently is worse than a script that fails loudly."**

## Khi nào dùng Skill này

| Tình huống | Dùng? | Lý do |
|------------|-------|-------|
| Viết script chạy 1 lần | ✅ | Ngay cả throwaway script cũng cần error handling |
| Tạo CLI tool bền vững | ✅ | Full pattern: args parsing, help, validation |
| Pipeline data processing | ✅ | Idempotent + checkpoint + resume |
| Deploy/migration script | ✅ | Dry-run + rollback + audit trail |
| Quick snippet < 20 dòng | ❌ | Overkill — viết inline, không cần skill |

---

## Quy trình 5 bước

### Step 1 — Phân tích yêu cầu (TRƯỚC khi viết code)

**Bắt buộc trả lời 6 câu hỏi:**

| # | Câu hỏi | Ảnh hưởng |
|---|---------|-----------|
| 1 | Script chạy **ở đâu**? (local / CI / server / cron) | Quyết định logging style, dependency |
| 2 | Input **đến từ đâu**? (file / stdin / API / args) | Quyết định validation layer |
| 3 | Output **đi đâu**? (file / stdout / API / DB) | Quyết định output contract |
| 4 | **Ai** chạy script? (developer / ops / non-tech) | Quyết định UX level (help text, prompts) |
| 5 | Có cần **idempotent** không? (chạy lại = kết quả giống) | Quyết định state management |
| 6 | **Failure mode** nào nguy hiểm nhất? | Quyết định safety pattern |

Schema phân tích — lưu nội bộ (không cần file):
```
ANALYSIS:
  runtime: local|ci|server|cron
  input_source: [file, stdin, api, args]
  output_target: [file, stdout, api, db]
  operator: developer|ops|non-tech
  idempotent: true|false
  critical_failure: "mô tả failure mode nguy hiểm nhất"
  language: bash|node|python
  estimated_complexity: simple|moderate|complex
```

> **Chọn ngôn ngữ** dựa trên:
> - **Bash**: File ops, CLI wrappers, glue scripts, cron jobs (< 200 LOC)
> - **Node.js**: JSON processing, API calls, async workflows, ecosystem tools
> - **Python**: Data processing, ML pipeline, text parsing, complex logic

---

### Step 2 — Test Plan & Failure Prediction (TRƯỚC khi viết code)

**Đọc `references/testing.md` TRƯỚC**, rồi tạo:

#### 2a. Failure Mode Matrix

Dự đoán cách script có thể FAIL. Chọn từ 5 categories (A-E) trong framework.

**Minimum failure modes:**
- Simple script: ≥ 5
- Moderate script: ≥ 8
- Complex script: ≥ 12

```
FAILURE MODE MATRIX: <script-name>
| # | Failure Mode     | Sev  | Likely | Mitigation              | Test   |
|---|-----------------|------|--------|-------------------------|--------|
| F1| Input not found  | HIGH | HIGH   | validate + die() early  | T-F1   |
| F2| Disk full        | HIGH | LOW    | atomic write (tmp→mv)   | T-F2   |
| F3| Concurrent run   | HIGH | MED    | lockfile                | T-F3   |
| F4| JSON parse error | HIGH | MED    | try/catch + clear msg   | T-F4   |
| F5| Network timeout  | MED  | MED    | retry 3x, backoff       | T-F5   |
```

#### 2b. 4-Layer Test Plan

```
TEST PLAN: <script-name>
├── Layer 1: Happy Path
│   ├── T-H1: Standard input → correct output, exit 0
│   ├── T-H2: --dry-run → no side effects
│   └── T-H3: --help → usage text, exit 0
├── Layer 2: Edge Cases (Boundary Trinity: before/at/after)
│   ├── T-E1: Empty input → clear error
│   ├── T-E2: Path with spaces/unicode → works
│   └── T-E3: Single item (not only batch) → works
├── Layer 3: Failure Modes (1 test per F# above)
│   └── T-F1..T-FN: verify error msg + exit code + cleanup
└── Layer 4: Idempotency (nếu required)
    ├── T-I1: Run 2x → same output
    └── T-I2: Kill + rerun → clean state
```

> **Nguyên lý Tam Giới:** Test ở 3 điểm: **ngay trước** boundary, **tại** boundary, 
> **ngay sau** boundary. Systematic hơn random edge case testing.

---

### Step 3 — Viết Script theo Pattern Library

Đọc file pattern phù hợp từ `references/` **TRƯỚC khi viết code**:

| Complexity | Pattern File | Khi nào |
|------------|-------------|---------|
| Simple | `references/patterns-simple.md` | Script < 100 LOC, 1 task đơn |
| Moderate | `references/patterns-moderate.md` | CLI tool, multi-step, cần args |
| Complex | `references/patterns-complex.md` | Pipeline, state, checkpoint, resume |

> **Đọc pattern file trước, tuyệt đối KHÔNG viết script "từ đầu".**
>
> Pattern files chứa boilerplate đã được battle-tested, bao gồm:
> - Error handling skeleton
> - Logging setup
> - Args parsing template
> - Input validation
> - Output contract
> - Cleanup/trap handlers

#### Mandatory Elements (MỌI script phải có)

Dù simple hay complex, **mọi script** phải có đủ 10 elements:

```
┌───────────────────────────────────────────────────────────┐
│ 1. HEADER          — Shebang + description               │
│ 2. STRICT MODE     — set -euo pipefail / equivalent      │
│ 3. CONFIGURATION   — Constants, defaults, paths          │
│ 4. VALIDATION      — Check inputs trước khi chạy         │
│ 5. LOGGING         — Structured output + timestamps      │
│ 6. CORE LOGIC      — Business logic, separated           │
│ 7. CLEANUP         — trap EXIT, temp files, locks        │
│ 8. SELF-TEST       — --test flag chạy smoke test         │
│ 9. HELP            — --help hiển thị usage + examples    │
│ 10. TRACE          — Start/end time, duration, counts    │
└───────────────────────────────────────────────────────────┘
```

#### Language-Specific Standards

**Bash:**
```bash
#!/usr/bin/env bash
set -euo pipefail
# ↑ Strict mode: exit on error (-e), undefined var (-u), pipe fail (-o pipefail)
```

**Node.js:**
```javascript
#!/usr/bin/env node
// @ts-check — Enable type checking in VS Code
'use strict';
process.on('unhandledRejection', (err) => { console.error('💥 Unhandled:', err); process.exit(1); });
```

**Python:**
```python
#!/usr/bin/env python3
"""Module docstring — one-line summary."""
from __future__ import annotations
import sys, logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
```

#### Self-Test (--test flag)

Mọi script PHẢI có `--test` flag (xem patterns trong `references/testing.md`):
- Verify dependencies tồn tại
- Verify config/paths accessible
- Chạy minimal dry-run
- Exit 0 nếu pass, exit 1 nếu fail

#### Execution Tracing

Mọi script PHẢI log đủ để reconstruct execution:
- Start time, end time, duration
- Input params (masked nếu chứa secrets)
- Items processed / skipped / failed
- Exit code + reason

Xem pattern cụ thể trong `references/testing.md` section "Execution Tracing Template".

---

### Step 4 — Validation & Quality Gates

Chạy checklist **TRƯỚC khi deliver** cho user:

```
QUALITY GATE CHECKLIST (13 items):
□ [HEADER]      Có shebang + description comment?
□ [STRICT]      Strict mode / error policy?
□ [VALIDATE]    Input validation ở đầu script?
□ [LOGGING]     Có timestamps + level (INFO/WARN/ERROR)?
□ [IDEMPOTENT]  Idempotency patterns (nếu applicable)?
□ [DRY-RUN]     Có --dry-run flag? (nếu script có side effects)
□ [CLEANUP]     trap hoặc finally xử lý temp files?
□ [SELF-TEST]   Có --test hoặc --check flag?
□ [HELP]        --help hiển thị usage + examples?
□ [EXIT-CODE]   Exit codes có semantic meaning? (0=ok, 1=error, 2=usage)
□ [TRACE]       Execution tracing (start/end/duration/counts)?
□ [SECURITY]    Không hardcode credentials, tokens, passwords
□ [SHELLCHECK]  (bash) Chạy shellcheck nếu có sẵn
```

**Grade system:**
- **A** (12+/13, ≤1 warn): Exemplary — production-ready
- **B** (10-11/13): Good — ready to deliver
- **C** (8-9/13): Acceptable — minimum viable
- **FAIL** (any ❌ hoặc <8 pass): Must fix before delivering

**Auto-grade script** (chạy tuỳ chọn):
```bash
bash <skill>/scripts/quality-gate.sh <script-path>
```

---

### Step 5 — Document & Deliver

Mỗi script phải có:

1. **Header block** trong file:
   ```bash
   # ============================================================
   # Script: <name>
   # Purpose: <one-line>
   # Author: AI-assisted (automation-scripts skill)
   # Created: <date>
   # Usage: <command> [options] <args>
   # Dependencies: <list or "none">
   # Quality-grade: <A|B|C>
   # ============================================================
   ```

2. **README section** (nếu script phức tạp):
   - What it does
   - Prerequisites
   - Usage examples
   - Environment variables
   - Exit codes

---

## Anti-Patterns — TRÁNH tuyệt đối

| ❌ Tránh | ✅ Thay thế | Lý do |
|----------|-------------|-------|
| `cd dir && command` | `command -C dir` hoặc subshell `(cd dir && ...)` | Nếu cd fail, command chạy ở thư mục sai |
| Variables không quote | `"$var"` luôn có quotes | Word splitting + glob expansion |
| `cat file \| grep` | `grep pattern file` | UUOC (Useless Use of Cat) |
| Echoing secrets | Mask hoặc skip | Security |
| `rm -rf $var/` | Guard: `[[ -n "$var" ]] && rm -rf "$var/"` | Empty var = xoá root |
| Silent failure | `set -e` + explicit checks | "Tại sao script chạy xong mà data sai?" |
| Magic numbers | Named constants | Readability, maintainability |
| Inline SQL/queries | Parameterized queries | SQL injection |
| `sleep 5` polling | Exponential backoff | Resource waste |
| Global state mutation | Pure functions where possible | Testability |
| Script không có test plan | Tạo test plan TRƯỚC khi code | Script chưa sẵn sàng = disaster waiting |
| Retry vô hạn | MAX 2 retries → escalate (Anti-Stuck) | Infinite loop prevention |
| Test phụ thuộc lẫn nhau | Mỗi test standalone, chạy bất kỳ order | Debug dễ hơn, parallel OK |

---

## Template Reference

Khi user yêu cầu **loại script cụ thể**, đọc template tương ứng:

| Loại script | Template | Path |
|-------------|----------|------|
| File processor | Batch + progress | `references/templates/file-processor.md` |
| API caller | Retry + rate limit | `references/templates/api-caller.md` |
| Data pipeline | Checkpoint + resume | `references/templates/data-pipeline.md` |
| Deploy script | Dry-run + rollback | `references/templates/deploy-script.md` |
| Cron job | Lock + heartbeat | `references/templates/cron-job.md` |
| CLI tool | Args + help + validation | `references/templates/cli-tool.md` |
| Migration | Versioned + reversible | `references/templates/migration.md` |

**Test Plan & Failure framework:**

| Reference | Content | Path |
|-----------|---------|------|
| Testing Framework | Failure categories, 4-layer plan, self-test, circuit breaker, tracing | `references/testing.md` |

---

## Advanced Patterns

### Retry with Anti-Stuck Protocol

MAX 2 retries per operation: Retry 1 (auto-fix) → Retry 2 (manual-grade) → ⛔ Escalate.

Xem implementation: `references/testing.md` section "Retry & Circuit Breaker".

> **Khi nào dùng pattern nào?**
> - **Standard retry** (patterns-moderate.md): Đơn giản, 3 lần, exponential backoff. Dùng cho hầu hết scripts.
> - **Anti-Stuck retry** (testing.md): 3 lần nhưng Retry 2 có auto-fix step. Dùng khi script có thể self-recover.

### Circuit Breaker

Cho scripts gọi external services nhiều lần. Track failures → stop after threshold → auto-recover after cooldown.

Xem implementation: `references/testing.md` section "Circuit Breaker".

### Boundary Value Testing (Tam Giới)

Test ở 3 điểm cho mỗi boundary: **ngay trước** (n-1), **tại** (n), **ngay sau** (n+1).
Systematic hơn random edge case testing.

Xem guide: `references/testing.md` section "Layer 2".

### Token-Based Idempotency

Generate unique token per operation → store → reject duplicates.
Cho script context: dùng lockfiles/pidfiles with unique run IDs.

---

## Ràng buộc

- **KHÔNG** viết script thiếu error handling — luôn có ít nhất `set -euo pipefail` (bash) hoặc try/catch (node/python)
- **KHÔNG** hardcode paths tuyệt đối khi có thể dùng relative hoặc config
- **KHÔNG** skip validation "vì nhanh" — validate TRƯỚC, chạy SAU
- **KHÔNG** để script fail silently — fail loud, fail early
- **KHÔNG** bỏ qua cleanup — temp files, lock files, connections phải được xử lý
- **KHÔNG** skip test plan — LUÔN tạo failure matrix + 4-layer plan TRƯỚC khi code
- **KHÔNG** retry vô hạn — MAX 2 retries rồi escalate (Anti-Stuck Protocol)

---

## Liên kết với các BP

Script automation chất lượng cao áp dụng trực tiếp nhiều nguyên tắc:

- **BP-017** (2-Pipe): Validate cheap (test plan + validation) → execute expensive (core logic)
- **BP-022** (Self-Validation Gates): Script tự kiểm tra trước khi chạy (--test flag)
- **BP-023** (Index Before Reason): Count/check/predict failure modes trước, xử lý sau
- **BP-025** (Regex Quality Gates): Format đảm bảo bởi máy (quality-gate.sh)
- **BP-026** (Freedom Mismatch): Enforcement qua grading, không chỉ text instruction
- **BP-034** (Anti-Stuck Protocol): MAX 2 retries → escalate

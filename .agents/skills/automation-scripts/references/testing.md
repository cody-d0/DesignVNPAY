# Test Plan Framework for Automation Scripts

Script không có test plan = script chưa sẵn sàng deliver.

> **Nguyên tắc:** TRƯỚC khi viết code, phải biết code sẽ FAIL như thế nào.

---

## Quy trình tạo Test Plan

### Bước 1 — Liệt kê Failure Modes

**Mục đích:** Dự đoán mọi cách script có thể FAIL.

Sử dụng checklist theo category:

#### Category A — Input Failures
| # | Failure Mode | Ví dụ | Severity |
|---|-------------|-------|----------|
| A1 | Input không tồn tại | File path sai, API endpoint down | HIGH |
| A2 | Input rỗng | File 0 bytes, array rỗng, stdin empty | HIGH |
| A3 | Input quá lớn | File > RAM, array > 100K items | MEDIUM |
| A4 | Input sai format | JSON syntax error, CSV thiếu header | HIGH |
| A5 | Input encoding sai | UTF-16 thay vì UTF-8, BOM characters | MEDIUM |
| A6 | Input chứa ký tự đặc biệt | Spaces trong path, unicode names, newlines | MEDIUM |
| A7 | Input permissions sai | Không có quyền đọc, directory thay vì file | HIGH |

#### Category B — Output Failures  
| # | Failure Mode | Ví dụ | Severity |
|---|-------------|-------|----------|
| B1 | Disk full | Không đủ space để ghi output | HIGH |
| B2 | Permission denied (write) | Không có quyền ghi, directory read-only | HIGH |
| B3 | Partial write | Script crash giữa chừng → file corrupt | HIGH |
| B4 | Output overwrite conflict | Output file đã tồn tại, running instance khác | MEDIUM |

#### Category C — External Dependency Failures
| # | Failure Mode | Ví dụ | Severity |
|---|-------------|-------|----------|
| C1 | Missing tool/binary | `jq` chưa cài, `node` version sai | HIGH |
| C2 | Network timeout | API không phản hồi, DNS failure | MEDIUM |
| C3 | Rate limit / throttle | API trả 429, bị ban | MEDIUM |
| C4 | Auth failure | Token hết hạn, credentials sai | HIGH |
| C5 | Service unavailable | 500/502/503 response | MEDIUM |

#### Category D — Runtime Failures
| # | Failure Mode | Ví dụ | Severity |
|---|-------------|-------|----------|
| D1 | Out of memory | Processing file lớn hơn RAM | HIGH |
| D2 | Process timeout | Script chạy quá lâu, watchdog kill | MEDIUM |
| D3 | Concurrent conflict | 2 instance chạy cùng lúc, race condition | HIGH |
| D4 | Signal interrupt | User Ctrl+C, SIGTERM từ system | MEDIUM |
| D5 | Temp file leak | Crash → temp files không được cleanup | LOW |

#### Category E — Logic Failures
| # | Failure Mode | Ví dụ | Severity |
|---|-------------|-------|----------|
| E1 | Infinite loop | Retry không có max attempts | HIGH |
| E2 | Silent wrong result | Script exit 0 nhưng output sai | CRITICAL |
| E3 | Partial processing | 50/100 items OK, 50 bị skip không báo | HIGH |
| E4 | Idempotency violation | Chạy 2 lần → duplicate data | HIGH |

### Bước 2 — Chọn Failure Modes Relevant

Không phải mọi failure mode đều relevant cho mọi script.

**Quy tắc chọn:**
- Script Simple (< 100 LOC): Chọn ít nhất **5** failure modes
- Script Moderate (100-300 LOC): Chọn ít nhất **8** failure modes
- Script Complex (300+ LOC): Chọn ít nhất **12** failure modes

**Ưu tiên chọn theo:** HIGH severity + HIGH likelihood trước.

### Bước 3 — Tạo Failure Mode Matrix

```
FAILURE MODE MATRIX: <script-name>

| # | Failure Mode | Sev | Likely | Mitigation | Test |
|---|-------------|-----|--------|------------|------|
| F1 | Input not found | HIGH | HIGH | validate + die() early | T-E1 |
| F2 | Disk full during write | HIGH | LOW | atomic write (tmp→rename) | T-E2 |
| F3 | Concurrent runs | HIGH | MED | lockfile/mkdir lock | T-E3 |
| F4 | Network timeout | MED | MED | retry 3x, backoff | T-E4 |
| F5 | JSON parse error | HIGH | MED | try/catch + clear msg | T-E5 |
```

---

## 4-Layer Test Plan Template

### Layer 1 — Happy Path ✅

Script chạy đúng, input chuẩn, output đúng.

```
HAPPY PATH TESTS:
├── T-H1: Standard input → correct output, exit 0
├── T-H2: Multiple inputs → all processed correctly
├── T-H3: --dry-run → no side effects, correct preview
├── T-H4: --help → usage text displayed, exit 0
└── T-H5: --version → version number displayed, exit 0
```

### Layer 2 — Boundary & Edge Cases 🔲

Test ở ranh giới: trước / tại / sau boundary.

> **Nguyên lý Tam Giới (từ JA community):**
> Test 3 điểm: **境界直前** (just before), **境界そのもの** (at boundary), **境界直後** (just after)

```
EDGE CASE TESTS:
├── Input boundaries
│   ├── T-E1: Empty file (0 bytes) → clear error message
│   ├── T-E2: Single item → works correctly (not only batch)
│   ├── T-E3: Maximum reasonable size → doesn't OOM
│   └── T-E4: Just above max → graceful rejection
├── Path edge cases
│   ├── T-E5: Path with spaces ("my file.json") → works
│   ├── T-E6: Path with unicode ("日本語/ファイル.json") → works
│   ├── T-E7: Relative vs absolute path → both work
│   └── T-E8: Symlink as input → handled correctly
├── Data edge cases
│   ├── T-E9: Duplicate entries in input → handled
│   ├── T-E10: Null/undefined values in JSON → don't crash
│   └── T-E11: Deeply nested structure → handled
└── Permission edge cases
    ├── T-E12: Read-only output directory → clear error
    └── T-E13: File locked by another process → clear error
```

### Layer 3 — Failure Modes 💥

Mỗi failure mode từ Matrix PHẢI có ≥ 1 test.

```
FAILURE MODE TESTS:
├── T-F1: <Failure mode> → verify:
│   ├── Correct error message (human-readable)
│   ├── Correct exit code (non-zero)
│   ├── Cleanup runs (no temp file leaks)
│   └── Log entry written
├── T-F2: ...
└── T-FN: ...
```

**Verify cho mỗi failure test:**
1. ✅ Error message rõ ràng, chỉ ra vấn đề + cách fix
2. ✅ Exit code đúng (1=error, 2=usage, 3=partial)
3. ✅ Cleanup chạy (temp files xoá, locks giải phóng)
4. ✅ Log entry ghi nhận failure

### Layer 4 — Idempotency & Recovery 🔄

```
IDEMPOTENCY TESTS:
├── T-I1: Run 2x consecutively → same output, no duplicates
├── T-I2: Run after output exists → skip/update correctly
├── T-I3: Kill mid-run (Ctrl+C) → clean state
├── T-I4: Kill mid-run + re-run → resume correctly
└── T-I5: Run with stale lockfile → handle gracefully
```

---

## Self-Test Implementation Guide

Mỗi script nên có `--test` flag chạy smoke test nội bộ.

### Bash Self-Test Pattern
```bash
self_test() {
  local passed=0 failed=0

  # Test 1: Dependencies
  _test "Dependencies" "command -v jq >/dev/null 2>&1"

  # Test 2: Config accessible
  _test "Config exists" "[[ -f \"$CONFIG_FILE\" ]]"

  # Test 3: Output dir writable
  _test "Output writable" "touch \"$OUTPUT_DIR/.test\" && rm \"$OUTPUT_DIR/.test\""

  # Test 4: Dry run works
  _test "Dry-run" "$0 --dry-run < /dev/null"

  # Summary
  echo ""
  log "Self-test: $passed passed, $failed failed"
  [[ $failed -eq 0 ]] && exit 0 || exit 1
}

_test() {
  local label="$1"; shift
  if eval "$@" >/dev/null 2>&1; then
    echo "  ✅ $label"
    ((passed++))
  else
    echo "  ❌ $label"
    ((failed++))
  fi
}

[[ "${1:-}" == "--test" ]] && self_test
```

### Node.js Self-Test Pattern
```javascript
async function selfTest() {
  const tests = [
    ['Dependencies', () => { require('fs'); require('path'); }],
    ['Config readable', () => { fs.accessSync(CONFIG_FILE, fs.constants.R_OK); }],
    ['Output writable', () => {
      const tmp = path.join(OUTPUT_DIR, '.test');
      fs.writeFileSync(tmp, 'test');
      fs.unlinkSync(tmp);
    }],
  ];

  let passed = 0, failed = 0;
  for (const [name, fn] of tests) {
    try { fn(); console.log(`  ✅ ${name}`); passed++; }
    catch { console.log(`  ❌ ${name}`); failed++; }
  }

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

if (process.argv.includes('--test')) selfTest();
```

### Python Self-Test Pattern
```python
def self_test():
    import shutil
    tests = [
        ("Dependencies", lambda: __import__("json")),
        ("Config readable", lambda: Path(CONFIG_FILE).read_text()),
        ("Output writable", lambda: (
            Path(OUTPUT_DIR, ".test").write_text("t"),
            Path(OUTPUT_DIR, ".test").unlink(),
        )),
    ]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn(); print(f"  ✅ {name}"); passed += 1
        except Exception:
            print(f"  ❌ {name}"); failed += 1
    print(f"\nSelf-test: {passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)

if "--test" in sys.argv:
    self_test()
```

---

## Retry & Circuit Breaker Patterns

> **Khi nào dùng pattern nào?**
> - **Standard retry** (`patterns-moderate.md`): Đơn giản, 3 lần, exponential backoff. Dùng cho hầu hết scripts.
> - **Anti-Stuck retry** (bên dưới): 3 lần nhưng Retry 2 có auto-fix step. Dùng khi script có thể self-recover.

### Retry with Anti-Stuck Protocol

MAX 2 retries per operation. Retry 1 = auto-fix, Retry 2 = manual-like, then escalate/fail.

```javascript
async function withRetryAntiStuck(fn, label = 'operation') {
  // Attempt 1: Normal
  try { return await fn(); } catch (err1) {
    console.warn(`  ⚠ ${label}: Attempt 1 failed (${err1.message})`);
  }

  // Attempt 2: Auto-fix (e.g., clear cache, reset state)
  try {
    await autoFix();  // Script-specific recovery
    return await fn();
  } catch (err2) {
    console.warn(`  ⚠ ${label}: Attempt 2 (auto-fix) failed (${err2.message})`);
  }

  // Attempt 3: Last chance with manual-grade care
  try {
    return await fn();
  } catch (err3) {
    console.error(`  ⛔ ${label}: 3 attempts exhausted. Escalating.`);
    throw err3;  // Let caller decide
  }
}
```

### Circuit Breaker (for external service calls)

Dùng khi script gọi external services nhiều lần.

```javascript
class CircuitBreaker {
  constructor({ failThreshold = 5, cooldownMs = 30000 } = {}) {
    this.failures = 0;
    this.failThreshold = failThreshold;
    this.cooldownMs = cooldownMs;
    this.lastFail = 0;
    this.state = 'CLOSED'; // CLOSED → OPEN → HALF_OPEN
  }

  async call(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() - this.lastFail > this.cooldownMs) {
        this.state = 'HALF_OPEN'; // Try one request
      } else {
        throw new Error('Circuit breaker OPEN — service unavailable');
      }
    }

    try {
      const result = await fn();
      this.failures = 0;
      this.state = 'CLOSED';
      return result;
    } catch (err) {
      this.failures++;
      this.lastFail = Date.now();
      if (this.failures >= this.failThreshold) {
        this.state = 'OPEN';
        console.error(`⚡ Circuit breaker OPEN after ${this.failures} failures`);
      }
      throw err;
    }
  }
}
```

---

## Execution Tracing Template

Mỗi script nên log đủ thông tin để reconstruct execution:

```bash
# ─── Execution Trace ─────────────────────────────────────────
trace_start() {
  TRACE_START=$(date +%s)
  TRACE_ITEMS_OK=0
  TRACE_ITEMS_SKIP=0  
  TRACE_ITEMS_FAIL=0
  log "━━━ START ━━━"
  log "  Script:  $SCRIPT_NAME v$VERSION"
  log "  Args:    $*"
  log "  CWD:     $(pwd)"
  log "  User:    $(whoami)"
  log "  Time:    $(date -u +%Y-%m-%dT%H:%M:%SZ)"
}

trace_end() {
  local exit_code=$?
  local duration=$(( $(date +%s) - TRACE_START ))
  log "━━━ END ━━━"
  log "  Duration: ${duration}s"
  log "  OK:       $TRACE_ITEMS_OK"
  log "  Skipped:  $TRACE_ITEMS_SKIP"
  log "  Failed:   $TRACE_ITEMS_FAIL"
  log "  Exit:     $exit_code"
}
trap trace_end EXIT
```

```javascript
// Node.js equivalent
const trace = {
  start: Date.now(),
  ok: 0, skip: 0, fail: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`━━━ Trace ━━━`);
    console.error(`  Duration: ${duration}s`);
    console.error(`  OK: ${this.ok}  Skip: ${this.skip}  Fail: ${this.fail}`);
  },
};
process.on('exit', () => trace.log());
```

```python
# Python equivalent
import time, atexit

class Trace:
    def __init__(self):
        self.start = time.monotonic()
        self.ok = self.skip = self.fail = 0
    def log(self):
        d = time.monotonic() - self.start
        print(f"━━━ Trace ━━━", file=sys.stderr)
        print(f"  Duration: {d:.1f}s", file=sys.stderr)
        print(f"  OK: {self.ok}  Skip: {self.skip}  Fail: {self.fail}", file=sys.stderr)

trace = Trace()
atexit.register(trace.log)
```

# Template: Cron Job

Script chạy theo lịch với lock, heartbeat, và alerting.

## Khi nào dùng

- Scheduled data sync
- Periodic cleanup/maintenance
- Report generation
- Health monitoring

## Bash Skeleton

```bash
#!/usr/bin/env bash
# ============================================================
# Cron Job: <name>
# Schedule: */15 * * * * (every 15 minutes)
# Lock: Prevents concurrent runs
# Heartbeat: Writes timestamp for monitoring
# ============================================================
set -euo pipefail

readonly SCRIPT_NAME="$(basename "$0" .sh)"
readonly LOCK_DIR="/tmp/${SCRIPT_NAME}.lock"
readonly HEARTBEAT_FILE="/tmp/${SCRIPT_NAME}.heartbeat"
readonly LOG_DIR="${LOG_DIR:-/var/log/cron}"
readonly LOG_FILE="$LOG_DIR/${SCRIPT_NAME}-$(date +%Y%m%d).log"
readonly MAX_RUNTIME_SECONDS=600  # Kill if running > 10 min

# ─── Logging ────────────────────────────────────────────────
mkdir -p "$LOG_DIR"
exec > >(tee -a "$LOG_FILE") 2>&1

log()  { echo "$(date '+%Y-%m-%d %H:%M:%S') [$$] INFO  $*"; }
warn() { echo "$(date '+%Y-%m-%d %H:%M:%S') [$$] WARN  $*"; }
err()  { echo "$(date '+%Y-%m-%d %H:%M:%S') [$$] ERROR $*"; }

# ─── Lock ────────────────────────────────────────────────────
acquire_lock() {
  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    local pid
    pid=$(cat "$LOCK_DIR/pid" 2>/dev/null || echo "unknown")

    # Check if process is still alive
    if [[ "$pid" != "unknown" ]] && kill -0 "$pid" 2>/dev/null; then
      # Check if it's been running too long
      local lock_age
      lock_age=$(( $(date +%s) - $(stat -f %m "$LOCK_DIR/pid" 2>/dev/null || echo 0) ))

      if [[ $lock_age -gt $MAX_RUNTIME_SECONDS ]]; then
        warn "Stale lock (${lock_age}s old, PID $pid). Killing and taking over."
        kill "$pid" 2>/dev/null || true
        sleep 2
        rm -rf "$LOCK_DIR"
        mkdir "$LOCK_DIR"
      else
        log "Already running (PID $pid, ${lock_age}s). Exiting."
        exit 0
      fi
    else
      warn "Stale lock (PID $pid not running). Removing."
      rm -rf "$LOCK_DIR"
      mkdir "$LOCK_DIR"
    fi
  fi
  echo $$ > "$LOCK_DIR/pid"
}

release_lock() {
  rm -rf "$LOCK_DIR"
}

# ─── Heartbeat ──────────────────────────────────────────────
heartbeat() {
  cat > "$HEARTBEAT_FILE" <<EOF
{
  "script": "$SCRIPT_NAME",
  "pid": $$,
  "last_beat": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "status": "${1:-running}"
}
EOF
}

# ─── Cleanup ────────────────────────────────────────────────
cleanup() {
  local exit_code=$?
  heartbeat "$([ $exit_code -eq 0 ] && echo 'success' || echo 'failed')"
  release_lock

  if [[ $exit_code -ne 0 ]]; then
    err "Job failed with exit code $exit_code"
    # Optional: send alert
    # alert "CRON FAIL: $SCRIPT_NAME exited $exit_code"
  fi
}
trap cleanup EXIT

# ─── Timeout watchdog ───────────────────────────────────────
(
  sleep $MAX_RUNTIME_SECONDS
  if kill -0 $$ 2>/dev/null; then
    err "TIMEOUT: Exceeded ${MAX_RUNTIME_SECONDS}s. Killing."
    kill -TERM $$ 2>/dev/null
    sleep 5
    kill -9 $$ 2>/dev/null
  fi
) &
WATCHDOG_PID=$!
disown $WATCHDOG_PID

# ─── Main ────────────────────────────────────────────────────
main() {
  acquire_lock
  heartbeat "running"
  log "Job started"

  # ── Your cron logic here ──

  heartbeat "success"
  log "Job completed"

  # Kill the watchdog
  kill $WATCHDOG_PID 2>/dev/null || true
}

main
```

## Key Patterns

### 1. Log Rotation (built-in)
```bash
# Keep only last 7 days of logs
cleanup_old_logs() {
  find "$LOG_DIR" -name "${SCRIPT_NAME}-*.log" -mtime +7 -delete 2>/dev/null
}
cleanup_old_logs  # Call at start
```

### 2. Alert Integration
```bash
alert() {
  local message="$1"
  local severity="${2:-warning}"

  # Slack webhook
  if [[ -n "${SLACK_WEBHOOK:-}" ]]; then
    curl -sf -X POST "$SLACK_WEBHOOK" \
      -H 'Content-Type: application/json' \
      -d "{\"text\":\"[$severity] $SCRIPT_NAME: $message\"}" \
      >/dev/null 2>&1 || true
  fi

  # Or just email
  # echo "$message" | mail -s "[$severity] $SCRIPT_NAME" ops@example.com
}
```

### 3. Monitoring-Friendly Output
```bash
# Write metrics for Prometheus/monitoring
write_metrics() {
  local duration="$1" items_processed="$2" errors="$3"
  cat > "/tmp/${SCRIPT_NAME}_metrics.prom" <<EOF
# HELP cron_job_duration_seconds Duration of last cron job run
# TYPE cron_job_duration_seconds gauge
cron_job_duration_seconds{job="$SCRIPT_NAME"} $duration
# HELP cron_job_items_total Items processed in last run
# TYPE cron_job_items_total gauge
cron_job_items_total{job="$SCRIPT_NAME"} $items_processed
# HELP cron_job_errors_total Errors in last run
# TYPE cron_job_errors_total gauge
cron_job_errors_total{job="$SCRIPT_NAME"} $errors
EOF
}
```

### 4. Crontab Installation Helper
```bash
# Self-install crontab entry
install_cron() {
  local schedule="${1:-*/15 * * * *}"
  local script_path="$(realpath "$0")"
  local cron_line="$schedule $script_path"

  if crontab -l 2>/dev/null | grep -qF "$script_path"; then
    log "Crontab entry already exists"
  else
    (crontab -l 2>/dev/null; echo "$cron_line") | crontab -
    log "Installed: $cron_line"
  fi
}
```

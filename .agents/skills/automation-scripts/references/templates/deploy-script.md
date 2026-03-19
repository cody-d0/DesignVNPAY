# Template: Deploy Script

Script deploy với dry-run, rollback, và health check.

## Khi nào dùng

- Deploy ứng dụng lên server/cloud
- Update configuration
- Database schema updates
- Service restart/reload

## Bash Skeleton

```bash
#!/usr/bin/env bash
# ============================================================
# Deploy Script — with dry-run, rollback, and health check
# Usage: ./deploy.sh [--dry-run] [--rollback] [--env prod|staging]
# ============================================================
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly DEPLOY_LOG="deploy-$(date +%Y%m%d_%H%M%S).log"

# ─── Config ──────────────────────────────────────────────────
ENV="${ENV:-staging}"
DRY_RUN=false
ROLLBACK=false
HEALTH_CHECK_RETRIES=5
HEALTH_CHECK_INTERVAL=10

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)    DRY_RUN=true; shift ;;
    --rollback)   ROLLBACK=true; shift ;;
    --env)        ENV="$2"; shift 2 ;;
    -h|--help)    echo "Usage: $0 [--dry-run] [--rollback] [--env prod|staging]"; exit 0 ;;
    *)            die "Unknown: $1" ;;
  esac
done

# ─── Safety Checks ──────────────────────────────────────────
pre_deploy_checks() {
  log "🔍 Pre-deploy checks for env: $ENV"

  # 1. Confirm production deploys
  if [[ "$ENV" == "prod" && "$DRY_RUN" != true ]]; then
    echo -n "⚠️  Deploy to PRODUCTION? Type 'yes' to confirm: "
    read -r confirm
    [[ "$confirm" != "yes" ]] && die "Aborted."
  fi

  # 2. Check branch
  local branch
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
  if [[ "$ENV" == "prod" && "$branch" != "main" ]]; then
    die "Production deploys must be from 'main' branch (current: $branch)"
  fi

  # 3. Check for uncommitted changes
  if [[ -n "$(git status --porcelain 2>/dev/null)" ]]; then
    warn "Uncommitted changes detected!"
    [[ "$ENV" == "prod" ]] && die "Cannot deploy with uncommitted changes"
  fi

  # 4. Check dependencies
  command -v node >/dev/null 2>&1 || die "node required"

  log "✅ Pre-deploy checks passed"
}

# ─── Backup ─────────────────────────────────────────────────
declare -a ROLLBACK_ACTIONS=()

create_backup() {
  local backup_dir="backups/$(date +%Y%m%d_%H%M%S)"
  mkdir -p "$backup_dir"

  if [[ "$DRY_RUN" == true ]]; then
    log "[DRY-RUN] Would backup to: $backup_dir"
    return 0
  fi

  log "📦 Creating backup: $backup_dir"

  # Backup current state
  # cp -r ./dist "$backup_dir/dist" 2>/dev/null || true
  # cp .env.$ENV "$backup_dir/.env" 2>/dev/null || true

  ROLLBACK_ACTIONS+=("cp -r $backup_dir/dist ./dist 2>/dev/null || true")
  echo "$backup_dir" > .last-backup
  log "  Backup saved: $backup_dir"
}

# ─── Deploy Steps ────────────────────────────────────────────
deploy() {
  log "🚀 Deploying to $ENV..."

  exec_step "Build" \
    "npm run build" \
    "rm -rf dist"  # rollback: remove build

  exec_step "Upload" \
    "echo 'Would upload dist/ to server'" \
    "echo 'Would remove uploaded files'"  # rollback

  exec_step "Restart" \
    "echo 'Would restart service'" \
    "echo 'Would restart with old version'"  # rollback
}

exec_step() {
  local name="$1" cmd="$2" undo="${3:-}"

  log "  Step: $name"

  if [[ "$DRY_RUN" == true ]]; then
    log "  [DRY-RUN] $cmd"
    return 0
  fi

  if eval "$cmd"; then
    log "  ✅ $name"
    [[ -n "$undo" ]] && ROLLBACK_ACTIONS+=("$undo")
  else
    err "  ❌ $name failed"
    do_rollback
    exit 1
  fi
}

# ─── Rollback ────────────────────────────────────────────────
do_rollback() {
  warn "🔄 Rolling back ${#ROLLBACK_ACTIONS[@]} action(s)..."

  for ((i=${#ROLLBACK_ACTIONS[@]}-1; i>=0; i--)); do
    local action="${ROLLBACK_ACTIONS[$i]}"
    log "  Undo: $action"
    eval "$action" 2>/dev/null || warn "  Rollback step failed"
  done

  warn "Rollback complete. Check logs: $DEPLOY_LOG"
}

# ─── Health Check ────────────────────────────────────────────
health_check() {
  if [[ "$DRY_RUN" == true ]]; then
    log "[DRY-RUN] Would run health check"
    return 0
  fi

  log "🏥 Running health check..."
  local url="https://${ENV}.example.com/health"

  for i in $(seq 1 $HEALTH_CHECK_RETRIES); do
    if curl -sf "$url" > /dev/null 2>&1; then
      log "  ✅ Health check passed (attempt $i)"
      return 0
    fi
    warn "  Attempt $i/$HEALTH_CHECK_RETRIES failed. Waiting ${HEALTH_CHECK_INTERVAL}s..."
    sleep "$HEALTH_CHECK_INTERVAL"
  done

  err "❌ Health check failed after $HEALTH_CHECK_RETRIES attempts"
  do_rollback
  return 1
}

# ─── Main ────────────────────────────────────────────────────
if [[ "$ROLLBACK" == true ]]; then
  if [[ -f .last-backup ]]; then
    backup_dir=$(cat .last-backup)
    log "Rolling back to: $backup_dir"
    # Restore from backup
  else
    die "No backup found"
  fi
else
  pre_deploy_checks
  create_backup
  deploy
  health_check
fi

log "🎉 Deploy complete!"
```

## Key Concepts

### 1. Blue-Green Deploy Pattern
```bash
# Symlink swap for zero-downtime
ln -snf "$NEW_RELEASE_DIR" /srv/app/current_new
mv -T /srv/app/current_new /srv/app/current  # Atomic swap
```

### 2. Canary Check
```bash
# Deploy to 1 instance, verify, then roll out
deploy_canary() {
  deploy_to_instance "$CANARY_HOST"
  health_check "$CANARY_HOST"
  log "Canary OK — deploying to all instances"
  for host in "${HOSTS[@]}"; do
    deploy_to_instance "$host"
  done
}
```

### 3. Idempotent Config Update
```bash
# Only update if changed
update_config() {
  local new_hash old_hash
  new_hash=$(md5sum "$NEW_CONFIG" | cut -d' ' -f1)
  old_hash=$(md5sum "$CURRENT_CONFIG" 2>/dev/null | cut -d' ' -f1 || echo "none")

  if [[ "$new_hash" == "$old_hash" ]]; then
    log "Config unchanged — skipping"
    return 0
  fi

  cp "$CURRENT_CONFIG" "${CURRENT_CONFIG}.bak"
  cp "$NEW_CONFIG" "$CURRENT_CONFIG"
  push_rollback "cp ${CURRENT_CONFIG}.bak $CURRENT_CONFIG"
}
```

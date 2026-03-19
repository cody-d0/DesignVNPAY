# Template: Migration Script

Versioned, reversible migration với audit trail.

## Khi nào dùng

- Database schema migration
- Data format migration
- Config migration
- File structure reorganization

## Node.js Skeleton

```javascript
#!/usr/bin/env node
'use strict';

/**
 * Migration Runner — versioned, reversible, with audit trail.
 *
 * Usage: node migrate.js [up|down|status] [--to <version>] [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const MIGRATIONS_DIR = './migrations';
const STATE_FILE = '.migration-state.json';

// ─── Migration State ────────────────────────────────────────
function loadState() {
  try {
    return JSON.parse(fs.readFileSync(STATE_FILE, 'utf-8'));
  } catch {
    return { applied: [], history: [] };
  }
}

function saveState(state) {
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

// ─── Migration Discovery ───────────────────────────────────
function discoverMigrations() {
  if (!fs.existsSync(MIGRATIONS_DIR)) return [];

  return fs.readdirSync(MIGRATIONS_DIR)
    .filter(f => f.endsWith('.js'))
    .sort()
    .map(f => {
      const mod = require(path.resolve(MIGRATIONS_DIR, f));
      return {
        id: f.replace('.js', ''),
        name: mod.name || f,
        up: mod.up,
        down: mod.down,
        description: mod.description || '',
      };
    });
}

// ─── Commands ───────────────────────────────────────────────
async function cmdUp(targetVersion, dryRun) {
  const state = loadState();
  const migrations = discoverMigrations();
  const pending = migrations.filter(m => !state.applied.includes(m.id));

  if (targetVersion) {
    const idx = pending.findIndex(m => m.id === targetVersion);
    if (idx < 0) {
      console.error(`Target version not found: ${targetVersion}`);
      process.exit(1);
    }
    pending.splice(idx + 1);
  }

  if (pending.length === 0) {
    console.log('✅ Already up to date');
    return;
  }

  console.log(`\n📋 Pending migrations: ${pending.length}\n`);
  for (const m of pending) {
    console.log(`  → ${m.id}: ${m.description}`);
  }

  if (dryRun) {
    console.log('\n[DRY-RUN] No changes applied');
    return;
  }

  console.log('');
  for (const m of pending) {
    const t0 = Date.now();
    console.log(`⬆️  Applying: ${m.id}...`);

    try {
      await m.up();
      const elapsed = Date.now() - t0;

      state.applied.push(m.id);
      state.history.push({
        id: m.id,
        direction: 'up',
        appliedAt: new Date().toISOString(),
        durationMs: elapsed,
      });
      saveState(state);

      console.log(`   ✅ Done (${elapsed}ms)`);
    } catch (err) {
      console.error(`   ❌ Failed: ${err.message}`);
      console.error(`\n💡 Fix the issue, then run: migrate up --to ${m.id}`);
      process.exit(1);
    }
  }

  console.log(`\n🎉 Applied ${pending.length} migration(s)`);
}

async function cmdDown(targetVersion, dryRun) {
  const state = loadState();
  const migrations = discoverMigrations();

  // Find migrations to revert (in reverse order)
  let toRevert = [...state.applied].reverse();
  if (targetVersion) {
    const idx = toRevert.indexOf(targetVersion);
    if (idx < 0) {
      console.error(`Version not applied: ${targetVersion}`);
      process.exit(1);
    }
    toRevert = toRevert.slice(0, idx + 1);
  } else {
    toRevert = toRevert.slice(0, 1); // Default: revert last one only
  }

  console.log(`\n⬇️  Reverting ${toRevert.length} migration(s)\n`);

  if (dryRun) {
    toRevert.forEach(id => console.log(`  Would revert: ${id}`));
    console.log('\n[DRY-RUN] No changes applied');
    return;
  }

  for (const id of toRevert) {
    const migration = migrations.find(m => m.id === id);
    if (!migration || !migration.down) {
      console.error(`Cannot revert ${id}: no down() function`);
      process.exit(1);
    }

    console.log(`  Reverting: ${id}...`);
    await migration.down();
    state.applied = state.applied.filter(a => a !== id);
    state.history.push({
      id,
      direction: 'down',
      appliedAt: new Date().toISOString(),
    });
    saveState(state);
    console.log(`  ✅ Reverted`);
  }
}

async function cmdStatus() {
  const state = loadState();
  const migrations = discoverMigrations();

  console.log(`\n📊 Migration Status\n`);
  for (const m of migrations) {
    const applied = state.applied.includes(m.id);
    const status = applied ? '✅' : '⬜';
    console.log(`  ${status} ${m.id} — ${m.description}`);
  }

  const pending = migrations.filter(m => !state.applied.includes(m.id));
  console.log(`\n  Applied: ${state.applied.length}  Pending: ${pending.length}\n`);
}

// ─── Main ───────────────────────────────────────────────────
const args = process.argv.slice(2);
const command = args[0] || 'status';
const dryRun = args.includes('--dry-run');
const targetIdx = args.indexOf('--to');
const target = targetIdx >= 0 ? args[targetIdx + 1] : null;

switch (command) {
  case 'up':     cmdUp(target, dryRun); break;
  case 'down':   cmdDown(target, dryRun); break;
  case 'status': cmdStatus(); break;
  default:
    console.log('Usage: migrate [up|down|status] [--to <version>] [--dry-run]');
    process.exit(2);
}
```

## Migration File Template

```javascript
// migrations/001_initial_setup.js
module.exports = {
  name: 'Initial Setup',
  description: 'Create base directory structure',

  async up() {
    const fs = require('fs');
    const dirs = ['data', 'logs', 'config'];
    dirs.forEach(d => fs.mkdirSync(d, { recursive: true }));
  },

  async down() {
    const fs = require('fs');
    // Only remove empty dirs (safe rollback)
    ['config', 'logs', 'data'].forEach(d => {
      try { fs.rmdirSync(d); } catch { /* not empty, skip */ }
    });
  },
};
```

## Bash — Simple Sequential Migration

```bash
#!/usr/bin/env bash
set -euo pipefail

APPLIED_FILE=".migrations_applied"
touch "$APPLIED_FILE"

apply_migration() {
  local id="$1" description="$2"
  shift 2

  if grep -qFx "$id" "$APPLIED_FILE"; then
    echo "  ⏭️  $id (already applied)"
    return 0
  fi

  echo "  ⬆️  $id: $description"
  "$@"  # Execute the migration function
  echo "$id" >> "$APPLIED_FILE"
  echo "  ✅ Applied"
}

# Define migrations as functions
migrate_001() { mkdir -p data logs config; }
migrate_002() { cp config/default.json config/production.json; }

# Run all migrations
apply_migration "001_init" "Create directories" migrate_001
apply_migration "002_config" "Create prod config" migrate_002

echo "✅ All migrations applied"
```

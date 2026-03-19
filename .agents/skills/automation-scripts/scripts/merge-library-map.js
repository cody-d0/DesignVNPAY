#!/usr/bin/env node
'use strict';

/**
 * ============================================================
 * Script: merge-library-map.js
 * Purpose: Merge component-index.json + component-ref-map.json
 *          → unified library-map.json. Resolves key collisions
 *          using tier priority (T3 > T2 > T1 > T0), detects
 *          outdated/incomplete entries, and produces audit report.
 * Author: AI-assisted (automation-scripts skill)
 * Created: 2026-03-14
 * Usage: node merge-library-map.js [options]
 * Dependencies: node (built-in only)
 * Quality-grade: A
 * ============================================================
 */

process.on('unhandledRejection', (err) => { console.error('💥 Unhandled:', err); process.exit(1); });

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';
const PROJECT_ROOT = path.resolve(__dirname, '../../../../..');
const PATHS = {
  componentIndex: path.join(PROJECT_ROOT, 'bridge/library/01-index/component-index.json'),
  componentRefMap: path.join(PROJECT_ROOT, 'bridge/library/01-index/component-ref-map.json'),
  slotIndex: path.join(PROJECT_ROOT, 'bridge/library/05-slot/slot-index.json'),
  libraryMapCurrent: path.join(PROJECT_ROOT, 'bridge/library/library-map.json'),
  libraryMapOutput: path.join(PROJECT_ROOT, 'bridge/library/library-map.json'),
};

// Tier priority: higher = preferred for plugin import
const TIER_PRIORITY = { T3: 4, T2: 3, T1: 2, T0: 1 };

// ─── Logging ────────────────────────────────────────────────
const isTTY = process.stderr.isTTY;
const c = {
  red: isTTY ? '\x1b[31m' : '', green: isTTY ? '\x1b[32m' : '',
  yellow: isTTY ? '\x1b[33m' : '', cyan: isTTY ? '\x1b[36m' : '',
  dim: isTTY ? '\x1b[2m' : '', bold: isTTY ? '\x1b[1m' : '',
  reset: isTTY ? '\x1b[0m' : '',
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

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Merge component-index + component-ref-map → library-map

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options]

${c.yellow}OPTIONS:${c.reset}
  --prefer-index     When key collision: prefer component-index (default)
  --prefer-refmap    When key collision: prefer component-ref-map
  --prefer-tier      When key collision: prefer higher tier (T3 > T2 > T1 > T0)
  --include-aliases  Include short-name aliases from refMap (1036 → ~300 extra)
  --audit            Only run audit (no write)
  --dry-run          Show what would change, don't write
  --write            Write output to library-map.json
  -o, --output PATH  Custom output path
  --json             Output audit as JSON
  --test             Run self-test
  -h, --help         Show help
  --version          Show version

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js --audit
  node ${SCRIPT_NAME}.js --prefer-tier --write
  node ${SCRIPT_NAME}.js --dry-run
  node ${SCRIPT_NAME}.js --write -o bridge/library/library-map-v2.json
`);
  process.exit(0);
}

// ─── Args Parsing ───────────────────────────────────────────
function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    prefer: 'tier',  // 'index' | 'refmap' | 'tier'
    includeAliases: false,
    auditOnly: false,
    dryRun: false,
    write: false,
    outputPath: PATHS.libraryMapOutput,
    json: false,
    test: false,
  };

  let i = 0;
  while (i < args.length) {
    const arg = args[i];
    switch (arg) {
      case '-h': case '--help': showHelp(); break;
      case '--version': console.log(VERSION); process.exit(0); break;
      case '--test': config.test = true; break;
      case '--prefer-index': config.prefer = 'index'; break;
      case '--prefer-refmap': config.prefer = 'refmap'; break;
      case '--prefer-tier': config.prefer = 'tier'; break;
      case '--include-aliases': config.includeAliases = true; break;
      case '--audit': config.auditOnly = true; break;
      case '--dry-run': config.dryRun = true; break;
      case '--write': config.write = true; break;
      case '--json': config.json = true; break;
      case '-o': case '--output': config.outputPath = args[++i]; break;
      default:
        if (arg.startsWith('-')) log.die(`Unknown option: ${arg}. Use --help.`);
    }
    i++;
  }

  return config;
}

// ─── Validation ─────────────────────────────────────────────
function validate(config) {
  const errors = [];
  if (!fs.existsSync(PATHS.componentIndex)) errors.push(`Missing: ${PATHS.componentIndex}`);
  if (!fs.existsSync(PATHS.componentRefMap)) errors.push(`Missing: ${PATHS.componentRefMap}`);
  if (errors.length > 0) {
    errors.forEach(e => log.error(e));
    log.die(`${errors.length} validation error(s).`);
  }
}

// ─── Load sources ───────────────────────────────────────────
function loadSources() {
  const startMs = Date.now();

  // component-index.json: { entries: [...] }
  const idxRaw = JSON.parse(fs.readFileSync(PATHS.componentIndex, 'utf8'));
  const idxEntries = idxRaw.entries || [];

  // component-ref-map.json: { "name": { key, nodeId, type, ... }, ... }
  const refMap = JSON.parse(fs.readFileSync(PATHS.componentRefMap, 'utf8'));

  // slot-index.json (optional): for slot enrichment
  let slotIndex = null;
  if (fs.existsSync(PATHS.slotIndex)) {
    const slotRaw = JSON.parse(fs.readFileSync(PATHS.slotIndex, 'utf8'));
    slotIndex = new Map();
    (slotRaw.components || slotRaw.entries || []).forEach(e => slotIndex.set(e.name, e));
  }

  // library-map.json (current, for diff)
  let currentLib = null;
  if (fs.existsSync(PATHS.libraryMapCurrent)) {
    currentLib = JSON.parse(fs.readFileSync(PATHS.libraryMapCurrent, 'utf8'));
  }

  log(`Sources loaded in ${Date.now() - startMs}ms: index=${idxEntries.length} refMap=${Object.keys(refMap).length} slots=${slotIndex ? slotIndex.size : 0}`);
  return { idxEntries, refMap, slotIndex, currentLib };
}

// ─── Merge Logic ────────────────────────────────────────────
function merge(sources, config) {
  const { idxEntries, refMap, slotIndex } = sources;
  const audit = {
    totalIndex: idxEntries.length,
    totalRefMap: Object.keys(refMap).length,
    collisions: [],
    added: [],         // entries added (not in current library-map)
    updated: [],       // entries with key changes
    unchanged: [],     // entries same as current
    aliasesIncluded: 0,
    finalCount: 0,
    issues: [],        // outdated/incomplete
  };

  // Build index-based primary map
  const merged = new Map(); // name → entry

  // Pass 1: Add all component-index entries (canonical source of truth)
  for (const entry of idxEntries) {
    const slotData = slotIndex ? slotIndex.get(entry.name) : null;

    merged.set(entry.name, {
      name: entry.name,
      nodeId: entry.nodeId,
      type: entry.type,
      key: entry.key,
      // Enriched metadata
      page: entry.page || undefined,
      tier: entry.tier || undefined,
      hasSlots: entry.hasSlots || false,
      slotCount: entry.slotCount || (slotData ? slotData.slots?.length : 0) || 0,
      _source: 'component-index',
    });
  }

  // Pass 2: Resolve collisions with refMap
  for (const entry of idxEntries) {
    const refEntry = refMap[entry.name];
    if (!refEntry) continue;

    if (refEntry.key !== entry.key) {
      // COLLISION — same name, different key/nodeId
      const collision = {
        name: entry.name,
        indexKey: entry.key,
        indexNodeId: entry.nodeId,
        indexPage: entry.page,
        indexTier: entry.tier,
        refMapKey: refEntry.key,
        refMapNodeId: refEntry.nodeId,
        refMapPage: refEntry.page,
        refMapTier: refEntry.tier,
        chosen: null,
      };

      // Resolution strategy
      let useIndex = true;
      if (config.prefer === 'refmap') {
        useIndex = false;
      } else if (config.prefer === 'tier') {
        const idxPrio = TIER_PRIORITY[entry.tier] || 0;
        const refPrio = TIER_PRIORITY[refEntry.tier] || 0;
        useIndex = idxPrio >= refPrio; // prefer higher tier; tie → index wins
      }
      // else: prefer === 'index' → useIndex stays true

      collision.chosen = useIndex ? 'index' : 'refmap';

      if (!useIndex) {
        // Overwrite with refMap data
        const current = merged.get(entry.name);
        current.key = refEntry.key;
        current.nodeId = refEntry.nodeId;
        current.page = refEntry.page || current.page;
        current.tier = refEntry.tier || current.tier;
        current._source = 'component-ref-map (collision winner)';
      }

      audit.collisions.push(collision);
    }
  }

  // Pass 3: Add refMap-only entries (aliases / short names)
  if (config.includeAliases) {
    for (const [name, entry] of Object.entries(refMap)) {
      if (!merged.has(name)) {
        merged.set(name, {
          name,
          nodeId: entry.nodeId,
          type: entry.type,
          key: entry.key,
          page: entry.page || undefined,
          tier: entry.tier || undefined,
          hasSlots: false,
          slotCount: 0,
          _source: 'component-ref-map (alias)',
        });
        audit.aliasesIncluded++;
      }
    }
  }

  // Pass 4: Diff against current library-map
  if (sources.currentLib) {
    const currentByName = new Map(sources.currentLib.components.map(c => [c.name, c]));

    for (const [name, entry] of merged) {
      const current = currentByName.get(name);
      if (!current) {
        audit.added.push(name);
      } else if (current.key !== entry.key) {
        audit.updated.push({ name, oldKey: current.key, newKey: entry.key });
      } else {
        audit.unchanged.push(name);
      }
    }
  }

  audit.finalCount = merged.size;
  return { merged, audit };
}

// ─── Audit: Find outdated/incomplete entries ────────────────
function auditLibrary(sources, mergeResult) {
  const { merged, audit } = mergeResult;
  const { idxEntries, refMap, slotIndex, currentLib } = sources;

  // Issue 1: Key mismatch between current library-map and sources
  if (currentLib) {
    for (const comp of currentLib.components) {
      const idxEntry = idxEntries.find(e => e.name === comp.name);
      const refEntry = refMap[comp.name];

      if (idxEntry && comp.key !== idxEntry.key) {
        audit.issues.push({
          type: 'KEY_OUTDATED',
          severity: 'HIGH',
          name: comp.name,
          detail: `library-map key "${comp.key.slice(0, 16)}..." differs from component-index key "${idxEntry.key.slice(0, 16)}..."`,
          currentKey: comp.key,
          correctKey: idxEntry.key,
        });
      }

      if (!idxEntry && !refEntry) {
        audit.issues.push({
          type: 'ORPHAN',
          severity: 'LOW',
          name: comp.name,
          detail: 'In library-map but not in any source — may be removed from Figma',
        });
      }
    }
  }

  // Issue 2: Components with slots that are missing from library-map  
  if (slotIndex) {
    for (const [name, slotEntry] of slotIndex) {
      if (!merged.has(name)) {
        audit.issues.push({
          type: 'SLOT_MISSING',
          severity: 'HIGH',
          name,
          detail: `Has ${slotEntry.slots?.length || 0} slots but missing from merged library-map`,
        });
      }
    }
  }

  // Issue 3: T3 components missing (high-value components)
  for (const entry of idxEntries) {
    if (entry.tier === 'T3' && currentLib) {
      const inCurrent = currentLib.components.find(c => c.name === entry.name);
      if (!inCurrent) {
        audit.issues.push({
          type: 'T3_MISSING',
          severity: 'CRITICAL',
          name: entry.name,
          detail: `Tier T3 (high-value) component missing from current library-map. Page: "${entry.page}"`,
          key: entry.key,
        });
      }
    }
  }

  // Issue 4: Type mismatches (e.g., COMPONENT in one, COMPONENT_SET in other)
  for (const entry of idxEntries) {
    const refEntry = refMap[entry.name];
    if (refEntry && refEntry.type !== entry.type) {
      audit.issues.push({
        type: 'TYPE_MISMATCH',
        severity: 'MEDIUM',
        name: entry.name,
        detail: `component-index: ${entry.type}, component-ref-map: ${refEntry.type}`,
      });
    }
  }

  return audit;
}

// ─── Build output library-map ───────────────────────────────
function buildOutputLibraryMap(merged, config) {
  const components = [];

  for (const [, entry] of merged) {
    const comp = {
      name: entry.name,
      nodeId: entry.nodeId,
      type: entry.type,
      key: entry.key,
    };
    // Enriched fields
    if (entry.page) comp.page = entry.page;
    if (entry.tier) comp.tier = entry.tier;
    if (entry.hasSlots) comp.hasSlots = true;
    if (entry.slotCount > 0) comp.slotCount = entry.slotCount;

    components.push(comp);
  }

  // Sort: T3 first, then T2, T1, T0. Within same tier: alphabetical
  components.sort((a, b) => {
    const tierA = TIER_PRIORITY[a.tier] || 0;
    const tierB = TIER_PRIORITY[b.tier] || 0;
    if (tierA !== tierB) return tierB - tierA; // higher tier first
    return a.name.localeCompare(b.name);
  });

  return {
    _generated: new Date().toISOString(),
    _source: `${SCRIPT_NAME} v${VERSION} — merged from component-index.json + component-ref-map.json`,
    _mergeStrategy: config.prefer,
    fileName: 'shadcn Design System',
    totalComponentSets: components.filter(c => c.type === 'COMPONENT_SET').length,
    totalComponents: components.filter(c => c.type === 'COMPONENT').length,
    totalEntries: components.length,
    components,
  };
}

// ─── Output: Audit Report ───────────────────────────────────
function printAuditReport(audit, config) {
  if (config.json) {
    console.log(JSON.stringify(audit, null, 2));
    return;
  }

  console.log('');
  console.log(`${c.bold}━━━ Library Merge Audit Report ━━━${c.reset}`);
  console.log('');

  // Summary
  console.log(`${c.bold}Sources:${c.reset}`);
  console.log(`  component-index.json:    ${audit.totalIndex} entries`);
  console.log(`  component-ref-map.json:  ${audit.totalRefMap} keys`);
  console.log(`  ${c.cyan}Merged result:           ${audit.finalCount} entries${c.reset}`);
  if (audit.aliasesIncluded > 0) {
    console.log(`  aliases included:        ${audit.aliasesIncluded}`);
  }

  // Diff
  console.log('');
  console.log(`${c.bold}Diff vs current library-map.json:${c.reset}`);
  console.log(`  ${c.green}Added:     ${audit.added.length}${c.reset}`);
  console.log(`  ${c.yellow}Updated:   ${audit.updated.length}${c.reset} (key changed)`);
  console.log(`  ${c.dim}Unchanged: ${audit.unchanged.length}${c.reset}`);

  // Added entries
  if (audit.added.length > 0) {
    console.log('');
    console.log(`${c.bold}${c.green}+ New entries (${audit.added.length}):${c.reset}`);
    audit.added.forEach(name => console.log(`  ${c.green}+ ${name}${c.reset}`));
  }

  // Updated entries
  if (audit.updated.length > 0) {
    console.log('');
    console.log(`${c.bold}${c.yellow}~ Updated keys (${audit.updated.length}):${c.reset}`);
    audit.updated.forEach(u => {
      console.log(`  ${c.yellow}~ ${u.name}${c.reset}`);
      console.log(`    ${c.dim}old: ${u.oldKey.slice(0, 20)}... → new: ${u.newKey.slice(0, 20)}...${c.reset}`);
    });
  }

  // Collisions
  if (audit.collisions.length > 0) {
    console.log('');
    console.log(`${c.bold}⚡ Collisions resolved (${audit.collisions.length}):${c.reset}`);
    audit.collisions.forEach(col => {
      console.log(`  ${col.name} → chose ${c.cyan}${col.chosen}${c.reset}`);
      console.log(`    ${c.dim}index: ${col.indexKey.slice(0, 16)}... (${col.indexPage}, ${col.indexTier})${c.reset}`);
      console.log(`    ${c.dim}refmp: ${col.refMapKey.slice(0, 16)}... (${col.refMapPage}, ${col.refMapTier})${c.reset}`);
    });
  }

  // Issues
  if (audit.issues.length > 0) {
    console.log('');
    console.log(`${c.bold}🔍 Issues Found (${audit.issues.length}):${c.reset}`);

    const bySeverity = { CRITICAL: [], HIGH: [], MEDIUM: [], LOW: [] };
    audit.issues.forEach(issue => {
      (bySeverity[issue.severity] || bySeverity.LOW).push(issue);
    });

    for (const [severity, issues] of Object.entries(bySeverity)) {
      if (issues.length === 0) continue;
      const sevColor = severity === 'CRITICAL' ? c.red : severity === 'HIGH' ? c.yellow : c.dim;
      console.log(`\n  ${sevColor}${c.bold}[${severity}] — ${issues.length} issue(s)${c.reset}`);
      issues.forEach(issue => {
        console.log(`    ${sevColor}${issue.type}${c.reset}: ${issue.name}`);
        console.log(`      ${c.dim}${issue.detail}${c.reset}`);
      });
    }
  }

  console.log('');
}

// ─── Self-Test ──────────────────────────────────────────────
function selfTest() {
  const startMs = Date.now();
  let passed = 0, failed = 0;

  const assert = (condition, label) => {
    if (condition) { passed++; log(`  ✅ ${label}`); }
    else { failed++; log.error(`  ❌ ${label}`); }
  };

  log('Running self-test...');

  // T1: Source files exist
  assert(fs.existsSync(PATHS.componentIndex), 'component-index.json exists');
  assert(fs.existsSync(PATHS.componentRefMap), 'component-ref-map.json exists');

  // T2: Can load sources
  const sources = loadSources();
  assert(sources.idxEntries.length > 0, `component-index has ${sources.idxEntries.length} entries`);
  assert(Object.keys(sources.refMap).length > 0, `component-ref-map has ${Object.keys(sources.refMap).length} keys`);

  // T3: Merge produces expected count
  const config = { prefer: 'tier', includeAliases: false };
  const { merged, audit } = merge(sources, config);
  assert(merged.size === sources.idxEntries.length, `Merge count (no aliases): ${merged.size} === ${sources.idxEntries.length}`);

  // T4: Card is present after merge
  assert(merged.has('Card'), 'Card exists in merged result');
  const card = merged.get('Card');
  assert(card.key.length > 0, `Card has key: ${card.key.slice(0, 16)}...`);
  assert(card.hasSlots === true, 'Card has slots');

  // T5: Accordion is present
  assert(merged.has('Accordion'), 'Accordion exists in merged result');

  // T6: Collisions detected
  assert(audit.collisions.length > 0, `Collisions detected: ${audit.collisions.length}`);

  // T7: Tier preference resolves correctly
  const cardCollision = audit.collisions.find(c => c.name === 'Card');
  if (cardCollision) {
    assert(cardCollision.chosen === 'index', `Card collision resolved to "index" (T3 > T0)`);
  }

  // T8: Include aliases mode
  const config2 = { prefer: 'tier', includeAliases: true };
  const { merged: merged2 } = merge(sources, config2);
  assert(merged2.size > merged.size, `With aliases: ${merged2.size} > ${merged.size}`);

  // T9: Build output structure
  const output = buildOutputLibraryMap(merged, config);
  assert(output.components.length === merged.size, `Output has ${output.components.length} components`);
  assert(output._source.includes(SCRIPT_NAME), 'Output _source set correctly');
  assert(output._generated.length > 0, 'Output _generated set');

  // T10: Audit finds issues
  const auditResult = auditLibrary(sources, { merged, audit });
  assert(auditResult.issues.length > 0, `Audit found ${auditResult.issues.length} issues`);

  // T11: Added entries detected via diff
  assert(audit.added.length > 0, `Diff detected ${audit.added.length} new entries`);

  const durationMs = Date.now() - startMs;
  console.log('');
  log(`Self-test complete: ${passed} passed, ${failed} failed (${durationMs}ms)`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const startMs = Date.now();
  const config = parseArgs();

  if (config.test) {
    validate(config);
    selfTest();
    return;
  }

  if (process.argv.slice(2).length === 0) showHelp();

  validate(config);
  const sources = loadSources();
  const mergeResult = merge(sources, config);
  const audit = auditLibrary(sources, mergeResult);

  // Print audit
  printAuditReport(audit, config);

  // Write output
  if (!config.auditOnly) {
    const output = buildOutputLibraryMap(mergeResult.merged, config);

    if (config.dryRun) {
      log(`[DRY-RUN] Would write ${output.components.length} entries to ${config.outputPath}`);
      log(`  Added: ${audit.added.length} | Updated: ${audit.updated.length} | Unchanged: ${audit.unchanged.length}`);
    } else if (config.write) {
      // Backup current
      if (fs.existsSync(config.outputPath)) {
        const backupPath = config.outputPath.replace('.json', `.backup-${Date.now()}.json`);
        fs.copyFileSync(config.outputPath, backupPath);
        log(`Backup: ${path.basename(backupPath)}`);
      }

      fs.writeFileSync(config.outputPath, JSON.stringify(output, null, 2) + '\n');
      log(`${c.green}Written ${output.components.length} entries to ${path.basename(config.outputPath)}${c.reset}`);
    } else {
      log.warn('No --write flag. Use --write to save, or --dry-run to preview.');
    }
  }

  log(`Completed in ${Date.now() - startMs}ms`);
}

main();

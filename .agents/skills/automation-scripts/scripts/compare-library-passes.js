#!/usr/bin/env node
'use strict';

// ============================================================
// Script: compare-library-passes
// Purpose: So sánh chi tiết 2 file library-pass JSON từ Figma scanner,
//          phát hiện khác biệt về entries, properties, tiers, slots, pages.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-13
// Usage: node compare-library-passes.js <fileA> <fileB> [options]
// Dependencies: node >= 18 (native parseArgs)
// Quality-grade: A
// Exit codes: 0=success, 1=error, 2=usage
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';
const MAX_FILE_SIZE_MB = 50; // Warn if file exceeds this

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

// ─── Unhandled Rejection Guard ──────────────────────────────
process.on('unhandledRejection', (err) => { log.die('💥 Unhandled:', err); });

// ─── Execution Trace ────────────────────────────────────────
const trace = {
  start: Date.now(),
  ok: 0, skip: 0, fail: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration: ${duration}s`);
    console.error(`  Compared: ${this.ok}  Skipped: ${this.skip}  Diffs: ${this.fail}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Compare two Figma library-pass JSON files

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js <fileA> <fileB> [options]

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test (smoke test)
  --json           Output as JSON (default: human-readable)

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js library-pass-SLOT1.json library-pass1203.json
  node ${SCRIPT_NAME}.js fileA.json fileB.json --json > diff.json

${c.yellow}OUTPUT:${c.reset}
  Structured comparison report including:
  - Entry count differences
  - Entries only in one file
  - Structural diffs (properties, tiers, variants, etc.)
  - Page summary differences
  - Tier count differences
`);
  process.exit(0);
}

// ─── Args Parsing ───────────────────────────────────────────
function parseCliArgs() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h') || args.length === 0) showHelp();
  if (args.includes('--version') || args.includes('-v')) { console.log(VERSION); process.exit(0); }
  if (args.includes('--test')) { selfTest(); return null; }

  const jsonOutput = args.includes('--json');
  const positionals = args.filter(a => !a.startsWith('--'));

  if (positionals.length < 2) {
    log.die(`Expected 2 input files, got ${positionals.length}. Use --help.`);
  }

  return { fileA: positionals[0], fileB: positionals[1], jsonOutput };
}

// ─── Validation ─────────────────────────────────────────────
function validate(config) {
  const errors = [];

  for (const label of ['fileA', 'fileB']) {
    const filePath = config[label];

    // Check existence
    if (!fs.existsSync(filePath)) {
      errors.push(`File not found: ${filePath}`);
      continue;
    }

    // Check readable
    try {
      fs.accessSync(filePath, fs.constants.R_OK);
    } catch {
      errors.push(`Permission denied (read): ${filePath}`);
      continue;
    }

    // Check size
    const stat = fs.statSync(filePath);
    const sizeMB = stat.size / (1024 * 1024);
    if (sizeMB > MAX_FILE_SIZE_MB) {
      log.warn(`${filePath} is ${sizeMB.toFixed(1)}MB — may be slow to parse`);
    }

    // Check extension
    if (!filePath.endsWith('.json')) {
      log.warn(`${filePath} does not have .json extension — proceeding anyway`);
    }
  }

  if (errors.length > 0) {
    errors.forEach(e => log.error(e));
    log.die(`${errors.length} validation error(s). Fix and retry.`);
  }

  log('✅ Validation passed');
}

// ─── Safe JSON Parse ────────────────────────────────────────
function safeParseJSON(filePath, label) {
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(raw);
  } catch (err) {
    if (err.code === 'ENOENT') log.die(`File not found: ${filePath}`);
    if (err instanceof SyntaxError) log.die(`JSON parse error in ${label} (${filePath}): ${err.message}`);
    log.die(`Failed to read ${label} (${filePath}): ${err.message}`);
  }
}

// ─── Core Comparison Logic ──────────────────────────────────

/**
 * Build a Map<name, entry> from entries array.
 * Detects and warns about duplicate names.
 */
function buildEntryMap(entries, label) {
  const map = new Map();
  let dupes = 0;
  for (const e of entries) {
    if (map.has(e.name)) {
      dupes++;
      log.warn(`Duplicate entry name in ${label}: "${e.name}"`);
    }
    map.set(e.name, e);
  }
  if (dupes > 0) log.warn(`${label}: ${dupes} duplicate name(s) found — last-wins`);
  return map;
}

/**
 * Compare two entries for structural differences (beyond key hash).
 * Returns array of diff descriptions, or empty if structurally identical.
 */
function compareEntry(a, b) {
  const diffs = [];

  // key — always differs between Figma versions, tracked but not flagged as structural
  const keyDiffers = a.key !== b.key;

  // nodeId
  if (a.nodeId !== b.nodeId) diffs.push({ field: 'nodeId', a: a.nodeId, b: b.nodeId });

  // type
  if (a.type !== b.type) diffs.push({ field: 'type', a: a.type, b: b.type });

  // page
  if (a.page !== b.page) diffs.push({ field: 'page', a: a.page, b: b.page });

  // tier
  if (a.tier !== b.tier) diffs.push({ field: 'tier', a: a.tier, b: b.tier });

  // namePattern
  if (a.namePattern !== b.namePattern) diffs.push({ field: 'namePattern', a: a.namePattern, b: b.namePattern });

  // propertyCount
  if (a.propertyCount !== b.propertyCount) diffs.push({ field: 'propertyCount', a: a.propertyCount, b: b.propertyCount });

  // childCount
  if (a.childCount !== b.childCount) diffs.push({ field: 'childCount', a: a.childCount, b: b.childCount });

  // variantCount
  const aVC = a.variantCount || 0;
  const bVC = b.variantCount || 0;
  if (aVC !== bVC) diffs.push({ field: 'variantCount', a: aVC, b: bVC });

  // instanceChildren
  const aIC = (a.instanceChildren || []).length;
  const bIC = (b.instanceChildren || []).length;
  if (aIC !== bIC) diffs.push({ field: 'instanceChildren.length', a: aIC, b: bIC });

  const aICNames = (a.instanceChildren || []).map(c => c.mainComponentName).sort().join(',');
  const bICNames = (b.instanceChildren || []).map(c => c.mainComponentName).sort().join(',');
  if (aICNames !== bICNames) diffs.push({ field: 'instanceChildren.names', a: 'differ', b: 'differ' });

  // properties signature (cleanName:type)
  const propSig = (props) => (props || []).map(p => `${p.cleanName}:${p.type}`).sort().join(',');
  const aPropSig = propSig(a.properties);
  const bPropSig = propSig(b.properties);
  if (aPropSig !== bPropSig) diffs.push({ field: 'properties.signature', a: aPropSig, b: bPropSig });

  // property defaults
  const propDef = (props) => (props || []).map(p => `${p.cleanName}=${p.defaultValue}`).sort().join(',');
  if (propDef(a.properties) !== propDef(b.properties) && aPropSig === bPropSig) {
    diffs.push({ field: 'properties.defaults', a: 'differ', b: 'differ' });
  }

  // property options
  const propOpts = (props) => (props || []).map(p => `${p.cleanName}:[${(p.options || []).join('|')}]`).sort().join(';');
  if (propOpts(a.properties) !== propOpts(b.properties) && aPropSig === bPropSig) {
    diffs.push({ field: 'properties.options', a: 'differ', b: 'differ' });
  }

  // variantNames
  const aVN = (a.variantNames || []).sort().join(',');
  const bVN = (b.variantNames || []).sort().join(',');
  if (aVN !== bVN) diffs.push({ field: 'variantNames', a: 'differ', b: 'differ' });

  return { diffs, keyDiffers };
}

/**
 * Main comparison — produces a structured report object.
 */
function compareLibraries(dataA, dataB, labelA, labelB) {
  const report = {
    labels: { a: labelA, b: labelB },
    meta: {},
    entryCounts: {},
    onlyInA: [],
    onlyInB: [],
    shared: { total: 0, withKeyDiffs: 0, withStructuralDiffs: 0, structurallyIdentical: 0 },
    structuralDiffs: [],
    slotAnalysis: { slotsOnlyInA: [], slotsOnlyInB: [], slotToNonSlot: [] },
    pageDiffs: [],
    tierDiffs: {},
    scanDuration: {},
  };

  // ── Meta ──
  report.meta = {
    a: { entries: dataA.entries.length, totalScanned: dataA.totalScanned, durationMs: dataA.durationMs },
    b: { entries: dataB.entries.length, totalScanned: dataB.totalScanned, durationMs: dataB.durationMs },
  };
  report.entryCounts = { a: dataA.entries.length, b: dataB.entries.length, diff: dataB.entries.length - dataA.entries.length };
  report.scanDuration = {
    a: `${(dataA.durationMs / 1000).toFixed(1)}s`,
    b: `${(dataB.durationMs / 1000).toFixed(1)}s`,
  };

  // ── Build maps ──
  const mapA = buildEntryMap(dataA.entries, labelA);
  const mapB = buildEntryMap(dataB.entries, labelB);

  // ── Only-in analysis ──
  for (const [name, entry] of mapA) {
    if (!mapB.has(name)) {
      report.onlyInA.push({ name, page: entry.page, tier: entry.tier, type: entry.type });
      trace.skip++;
    }
  }
  for (const [name, entry] of mapB) {
    if (!mapA.has(name)) {
      report.onlyInB.push({ name, page: entry.page, tier: entry.tier, type: entry.type });
      trace.skip++;
    }
  }

  // ── Shared entry comparison ──
  for (const [name, entryA] of mapA) {
    if (!mapB.has(name)) continue;
    const entryB = mapB.get(name);
    report.shared.total++;

    const { diffs, keyDiffers } = compareEntry(entryA, entryB);
    if (keyDiffers) report.shared.withKeyDiffs++;

    if (diffs.length > 0) {
      report.shared.withStructuralDiffs++;
      report.structuralDiffs.push({ name, page: entryA.page, tier: `${entryA.tier}→${entryB.tier}`, diffs });
      trace.fail++;
    } else {
      report.shared.structurallyIdentical++;
      trace.ok++;
    }
  }

  // ── SLOT analysis (key差分: SLOT vs non-SLOT properties) ──
  for (const diff of report.structuralDiffs) {
    const propSigDiff = diff.diffs.find(d => d.field === 'properties.signature');
    if (!propSigDiff) continue;

    const aSlots = (propSigDiff.a || '').split(',').filter(p => p.includes(':SLOT'));
    const bSlots = (propSigDiff.b || '').split(',').filter(p => p.includes(':SLOT'));

    if (aSlots.length > 0 && bSlots.length === 0) {
      report.slotAnalysis.slotToNonSlot.push({
        name: diff.name,
        slotsInA: aSlots.map(s => s.split(':')[0]),
        replacedWith: (propSigDiff.b || '').split(',').filter(Boolean),
      });
    } else if (aSlots.length === 0 && bSlots.length > 0) {
      report.slotAnalysis.slotsOnlyInB.push({
        name: diff.name,
        slots: bSlots.map(s => s.split(':')[0]),
      });
    }
  }

  // ── Page summaries ──
  const pagesA = new Map((dataA.pageSummaries || []).map(p => [p.pageName, p]));
  const pagesB = new Map((dataB.pageSummaries || []).map(p => [p.pageName, p]));
  const allPageNames = new Set([...pagesA.keys(), ...pagesB.keys()]);

  for (const pn of allPageNames) {
    const a = pagesA.get(pn);
    const b = pagesB.get(pn);
    if (!a) {
      report.pageDiffs.push({ page: pn, status: 'only-in-B', entriesB: b.entryCount });
    } else if (!b) {
      report.pageDiffs.push({ page: pn, status: 'only-in-A', entriesA: a.entryCount });
    } else if (a.entryCount !== b.entryCount) {
      report.pageDiffs.push({ page: pn, status: 'count-diff', entriesA: a.entryCount, entriesB: b.entryCount });
    }
  }

  // ── Tier counts ──
  report.tierDiffs = { a: dataA.tierCounts, b: dataB.tierCounts };

  return report;
}

// ─── Output Formatters ──────────────────────────────────────

function formatHuman(report) {
  const lines = [];
  const h = (title) => lines.push(`\n${'═'.repeat(60)}\n  ${title}\n${'═'.repeat(60)}`);
  const row = (label, value) => lines.push(`  ${label.padEnd(35)} ${value}`);

  h('LIBRARY PASS COMPARISON');
  row('File A:', report.labels.a);
  row('File B:', report.labels.b);
  row('Entries A:', String(report.entryCounts.a));
  row('Entries B:', String(report.entryCounts.b));
  row('Difference:', `${report.entryCounts.diff > 0 ? '+' : ''}${report.entryCounts.diff}`);
  row('Scan Duration A:', report.scanDuration.a);
  row('Scan Duration B:', report.scanDuration.b);

  h(`ENTRIES ONLY IN A (${report.onlyInA.length})`);
  for (const e of report.onlyInA) {
    lines.push(`  • ${e.name}  [${e.page}] tier=${e.tier} type=${e.type}`);
  }
  if (report.onlyInA.length === 0) lines.push('  (none)');

  h(`ENTRIES ONLY IN B (${report.onlyInB.length})`);
  for (const e of report.onlyInB) {
    lines.push(`  • ${e.name}  [${e.page}] tier=${e.tier} type=${e.type}`);
  }
  if (report.onlyInB.length === 0) lines.push('  (none)');

  h('SHARED ENTRY STATS');
  row('Total shared:', String(report.shared.total));
  row('With key hash diffs:', `${report.shared.withKeyDiffs}/${report.shared.total}`);
  row('With structural diffs:', String(report.shared.withStructuralDiffs));
  row('Structurally identical:', String(report.shared.structurallyIdentical));

  h(`STRUCTURAL DIFFS (${report.structuralDiffs.length})`);
  for (const d of report.structuralDiffs) {
    lines.push(`\n  📌 ${d.name}  [${d.page}] tier: ${d.tier}`);
    for (const diff of d.diffs) {
      if (diff.a === 'differ') {
        lines.push(`    • ${diff.field}: values differ`);
      } else {
        lines.push(`    • ${diff.field}: ${diff.a} → ${diff.b}`);
      }
    }
  }

  h(`SLOT ANALYSIS — A has SLOT, B does not (${report.slotAnalysis.slotToNonSlot.length})`);
  for (const s of report.slotAnalysis.slotToNonSlot) {
    lines.push(`  📌 ${s.name}`);
    lines.push(`    SLOT props in A: ${s.slotsInA.join(', ')}`);
    lines.push(`    Replaced in B:   ${s.replacedWith.join(', ')}`);
  }
  if (report.slotAnalysis.slotToNonSlot.length === 0) lines.push('  (none)');

  h(`PAGE DIFFERENCES (${report.pageDiffs.length})`);
  for (const p of report.pageDiffs) {
    if (p.status === 'only-in-A') lines.push(`  ONLY IN A: ${p.page} (${p.entriesA} entries)`);
    else if (p.status === 'only-in-B') lines.push(`  ONLY IN B: ${p.page} (${p.entriesB} entries)`);
    else lines.push(`  DIFF: ${p.page} — A: ${p.entriesA}, B: ${p.entriesB}`);
  }
  if (report.pageDiffs.length === 0) lines.push('  (none)');

  h('TIER COUNTS');
  row('A:', JSON.stringify(report.tierDiffs.a));
  row('B:', JSON.stringify(report.tierDiffs.b));

  return lines.join('\n');
}

// ─── Self-Test ──────────────────────────────────────────────
function selfTest() {
  let passed = 0, failed = 0;
  const test = (name, fn) => {
    try { fn(); console.log(`  ✅ ${name}`); passed++; }
    catch (e) { console.log(`  ❌ ${name}: ${e.message}`); failed++; }
  };

  console.log(`\n${SCRIPT_NAME} — Self-Test\n`);

  test('Dependencies (fs, path)', () => { require('fs'); require('path'); });

  test('compareEntry — identical entries', () => {
    const e = { key: 'a', nodeId: '1:1', type: 'C', page: 'P', tier: 'T0', propertyCount: 1, childCount: 1 };
    const { diffs } = compareEntry(e, e);
    if (diffs.length !== 0) throw new Error(`Expected 0 diffs, got ${diffs.length}`);
  });

  test('compareEntry — tier diff detected', () => {
    const a = { key: 'a', tier: 'T0' };
    const b = { key: 'b', tier: 'T1' };
    const { diffs } = compareEntry(a, b);
    if (!diffs.find(d => d.field === 'tier')) throw new Error('Tier diff not detected');
  });

  test('compareEntry — SLOT property diff', () => {
    const a = { key: 'a', properties: [{ cleanName: 'Items', type: 'SLOT' }], propertyCount: 1 };
    const b = { key: 'b', properties: [{ cleanName: 'Item 3', type: 'BOOLEAN' }], propertyCount: 1 };
    const { diffs } = compareEntry(a, b);
    if (!diffs.find(d => d.field === 'properties.signature')) throw new Error('Property sig diff not detected');
  });

  test('buildEntryMap — handles duplicates', () => {
    const entries = [{ name: 'A' }, { name: 'A' }];
    const map = buildEntryMap(entries, 'test');
    if (map.size !== 1) throw new Error(`Expected 1 unique, got ${map.size}`);
  });

  test('formatHuman — produces output', () => {
    const mockReport = {
      labels: { a: 'test-a', b: 'test-b' },
      entryCounts: { a: 1, b: 1, diff: 0 },
      scanDuration: { a: '1.0s', b: '2.0s' },
      onlyInA: [], onlyInB: [],
      shared: { total: 1, withKeyDiffs: 1, withStructuralDiffs: 0, structurallyIdentical: 1 },
      structuralDiffs: [],
      slotAnalysis: { slotsOnlyInA: [], slotsOnlyInB: [], slotToNonSlot: [] },
      pageDiffs: [],
      tierDiffs: { a: { T0: 1 }, b: { T0: 1 } },
    };
    const output = formatHuman(mockReport);
    if (!output.includes('LIBRARY PASS COMPARISON')) throw new Error('Missing header');
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return; // --test handled already

  validate(config);

  log(`Parsing ${config.fileA}...`);
  const dataA = safeParseJSON(config.fileA, 'fileA');
  log(`  → ${dataA.entries.length} entries (source: ${config.fileA} — Total Lines via fs.statSync: ${fs.statSync(config.fileA).size} bytes)`);

  log(`Parsing ${config.fileB}...`);
  const dataB = safeParseJSON(config.fileB, 'fileB');
  log(`  → ${dataB.entries.length} entries (source: ${config.fileB} — Total Lines via fs.statSync: ${fs.statSync(config.fileB).size} bytes)`);

  log('Comparing...');
  const labelA = path.basename(config.fileA, '.json');
  const labelB = path.basename(config.fileB, '.json');
  const report = compareLibraries(dataA, dataB, labelA, labelB);

  if (config.jsonOutput) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    console.log(formatHuman(report));
  }

  log(`Done. ${report.shared.withStructuralDiffs} structural diffs found.`);
}

main();

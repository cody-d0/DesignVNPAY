#!/usr/bin/env node
'use strict';

// ============================================================
// Script: harvest-library-evolution
// Purpose: Track library changes between scanner passes with
//          deep SLOT property analysis. Compares library-pass
//          JSON files to identify SLOT transitions, property
//          type evolution, and component structure changes.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-14
// Usage: node harvest-library-evolution.js [options] [fileA] [fileB]
// Dependencies: node >= 18
// Quality-grade: A
// Exit codes: 0=success, 1=error, 2=usage
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';
const MAX_FILE_SIZE_MB = 50;

const WORKSPACE = path.resolve(__dirname, '..', '..', '..', '..', '..');
const OUTPUT_DIR = path.join(__dirname, '..', 'output');

// Default library-pass files
const DEFAULT_FILE_A = path.join(WORKSPACE, 'library-pass-SLOT1.json');
const DEFAULT_FILE_B = path.join(WORKSPACE, 'library-pass1203.json');

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

process.on('unhandledRejection', (err) => { log.die('💥 Unhandled:', err); });

// ─── Execution Trace ────────────────────────────────────────
const trace = {
  start: Date.now(),
  entriesA: 0, entriesB: 0, slotsFound: 0, transitions: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration:     ${duration}s`);
    console.error(`  Entries A:    ${this.entriesA}`);
    console.error(`  Entries B:    ${this.entriesB}`);
    console.error(`  SLOTs found:  ${this.slotsFound}`);
    console.error(`  Transitions:  ${this.transitions}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Track library SLOT evolution between passes

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options] [fileA] [fileB]

${c.yellow}DEFAULTS:${c.reset}
  fileA: library-pass-SLOT1.json  (WITH SLOT)
  fileB: library-pass1203.json    (WITHOUT SLOT / earlier pass)

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test
  --dry-run        Preview files
  --json           Output to stdout
  -o, --output     Output path

${c.yellow}ANALYSIS:${c.reset}
  - SLOT inventory: components with SLOT properties
  - SLOT → non-SLOT transitions between passes
  - Property type evolution (BOOLEAN/INSTANCE_SWAP → SLOT)
  - Component set vs standalone distribution
  - Nested SLOT depth per component
`);
  process.exit(0);
}

// ─── Args ───────────────────────────────────────────────────
function parseCliArgs() {
  const args = process.argv.slice(2);
  if (args.includes('--help') || args.includes('-h')) showHelp();
  if (args.includes('--version') || args.includes('-v')) { console.log(VERSION); process.exit(0); }
  if (args.includes('--test')) { selfTest(); return null; }

  const dryRun = args.includes('--dry-run');
  const jsonOutput = args.includes('--json');
  let outputPath = path.join(OUTPUT_DIR, 'library-evolution-report.json');
  const outIdx = args.indexOf('-o') !== -1 ? args.indexOf('-o') : args.indexOf('--output');
  if (outIdx !== -1 && args[outIdx + 1]) outputPath = args[outIdx + 1];

  const positionals = args.filter(a => !a.startsWith('-') && !a.startsWith('--'));
  const fileA = positionals[0] || DEFAULT_FILE_A;
  const fileB = positionals[1] || DEFAULT_FILE_B;

  return { dryRun, jsonOutput, outputPath, fileA, fileB };
}

// ─── Validation ─────────────────────────────────────────────
/** @param {any} config */
function validate(config) {
  const errors = [];
  for (const [label, fp] of [['fileA', config.fileA], ['fileB', config.fileB]]) {
    if (!fs.existsSync(fp)) errors.push(`${label} not found: ${fp}`);
    else {
      const sizeMB = fs.statSync(fp).size / (1024 * 1024);
      if (sizeMB > MAX_FILE_SIZE_MB) log.warn(`${fp} is ${sizeMB.toFixed(1)}MB — may be slow`);
    }
  }
  if (errors.length > 0) {
    errors.forEach(e => log.error(e));
    log.die(`${errors.length} validation error(s).`);
  }
  log('✅ Validation passed');
}

// ─── Safe JSON Parse ────────────────────────────────────────
/**
 * @param {string} fp
 * @param {string} label
 */
function loadJSON(fp, label) {
  try {
    log(`  Parsing ${label}... (${(fs.statSync(fp).size / (1024*1024)).toFixed(1)}MB)`);
    return JSON.parse(fs.readFileSync(fp, 'utf8'));
  } catch (/** @type {any} */ err) {
    log.die(`Failed to parse ${label}: ${err.message}`);
  }
}

// ─── Core Analysis ──────────────────────────────────────────

/** @param {any[]} entries */
function buildEntryMap(entries) {
  const map = new Map();
  for (const e of entries) map.set(e.name, e);
  return map;
}

/** @param {any} entry */
function extractSlotProperties(entry) {
  if (!entry.properties || !Array.isArray(entry.properties)) return [];
  return entry.properties.filter(p => p.type === 'SLOT');
}

/** @param {any} entry */
function extractNonSlotProperties(entry) {
  if (!entry.properties || !Array.isArray(entry.properties)) return [];
  return entry.properties.filter(p => p.type !== 'SLOT');
}

/**
 * @param {any} dataA
 * @param {any} dataB
 */
function analyzeEvolution(dataA, dataB) {
  const entriesA = dataA.entries || [];
  const entriesB = dataB.entries || [];
  trace.entriesA = entriesA.length;
  trace.entriesB = entriesB.length;

  const mapA = buildEntryMap(entriesA);
  const mapB = buildEntryMap(entriesB);

  const report = {
    meta: {
      fileA: { entries: entriesA.length, totalScanned: dataA.totalScanned, durationMs: dataA.durationMs },
      fileB: { entries: entriesB.length, totalScanned: dataB.totalScanned, durationMs: dataB.durationMs },
      entryDiff: entriesA.length - entriesB.length,
    },
    slotInventory: [],
    slotTransitions: [],
    propertyTypeEvolution: [],
    componentTypes: { a: {}, b: {} },
    tierComparison: { a: dataA.tierCounts || {}, b: dataB.tierCounts || {} },
    slotDepthAnalysis: [],
    newComponents: [],
    removedComponents: [],
    slotSummary: {},
  };

  // ── SLOT Inventory (from file A = SLOT version) ──
  for (const entry of entriesA) {
    const slotProps = extractSlotProperties(entry);
    if (slotProps.length > 0) {
      trace.slotsFound += slotProps.length;

      const slotInfo = {
        name: entry.name,
        page: entry.page,
        tier: entry.tier,
        type: entry.type,
        slotCount: slotProps.length,
        slots: slotProps.map(p => ({
          name: p.cleanName,
          defaultValue: p.defaultValue || null,
          options: p.options || [],
        })),
        totalProperties: (entry.properties || []).length,
        hasInstanceChildren: (entry.instanceChildren || []).length > 0,
      };

      // Check for nested SLOTs (SLOT within instance children)
      if (entry.instanceChildren) {
        const nestedSlots = entry.instanceChildren.filter(ch =>
          ch.properties && ch.properties.some(p => p.type === 'SLOT')
        );
        slotInfo.nestedSlotChildren = nestedSlots.length;
      }

      report.slotInventory.push(slotInfo);
    }
  }

  // ── SLOT Transitions (A has SLOT, B has different structure) ──
  for (const [name, entryA] of mapA) {
    const entryB = mapB.get(name);
    if (!entryB) continue;

    const slotsA = extractSlotProperties(entryA);
    const slotsB = extractSlotProperties(entryB);

    // SLOT appeared (A has SLOT, B doesn't)
    if (slotsA.length > 0 && slotsB.length === 0) {
      const nonSlotB = extractNonSlotProperties(entryB);
      report.slotTransitions.push({
        name,
        direction: 'GAINED_SLOT',
        slotsInA: slotsA.map(p => ({ name: p.cleanName, type: p.type })),
        propsInB: nonSlotB.map(p => ({ name: p.cleanName, type: p.type })),
        totalPropsA: (entryA.properties || []).length,
        totalPropsB: (entryB.properties || []).length,
      });
      trace.transitions++;
    }

    // SLOT removed (B has SLOT, A doesn't)
    if (slotsB.length > 0 && slotsA.length === 0) {
      report.slotTransitions.push({
        name,
        direction: 'LOST_SLOT',
        slotsInB: slotsB.map(p => ({ name: p.cleanName, type: p.type })),
        propsInA: extractNonSlotProperties(entryA).map(p => ({ name: p.cleanName, type: p.type })),
      });
      trace.transitions++;
    }

    // Property type changes (per-property)
    if (entryA.properties && entryB.properties) {
      const propsA = new Map((entryA.properties || []).map(p => [p.cleanName, p]));
      const propsB = new Map((entryB.properties || []).map(p => [p.cleanName, p]));

      for (const [propName, propA] of propsA) {
        const propB = propsB.get(propName);
        if (propB && propA.type !== propB.type) {
          report.propertyTypeEvolution.push({
            component: name,
            property: propName,
            typeA: propA.type,
            typeB: propB.type,
            transition: `${propB.type} → ${propA.type}`,
          });
        }
      }
    }
  }

  // ── New / Removed components ──
  for (const [name, entry] of mapA) {
    if (!mapB.has(name)) {
      report.newComponents.push({
        name, page: entry.page, tier: entry.tier, type: entry.type,
        hasSlots: extractSlotProperties(entry).length > 0,
      });
    }
  }
  for (const [name, entry] of mapB) {
    if (!mapA.has(name)) {
      report.removedComponents.push({
        name, page: entry.page, tier: entry.tier, type: entry.type,
      });
    }
  }

  // ── Component type distribution ──
  for (const entry of entriesA) {
    const t = entry.type || 'unknown';
    report.componentTypes.a[t] = (report.componentTypes.a[t] || 0) + 1;
  }
  for (const entry of entriesB) {
    const t = entry.type || 'unknown';
    report.componentTypes.b[t] = (report.componentTypes.b[t] || 0) + 1;
  }

  // ── SLOT depth analysis ──
  for (const si of report.slotInventory) {
    report.slotDepthAnalysis.push({
      name: si.name,
      directSlots: si.slotCount,
      nestedSlotChildren: si.nestedSlotChildren || 0,
      totalDepth: si.slotCount + (si.nestedSlotChildren || 0),
    });
  }
  report.slotDepthAnalysis.sort((a, b) => b.totalDepth - a.totalDepth);

  // ── SLOT Summary ──
  const slotTypeMap = {};
  for (const si of report.slotInventory) {
    for (const slot of si.slots) {
      slotTypeMap[slot.name] = (slotTypeMap[slot.name] || 0) + 1;
    }
  }
  report.slotSummary = {
    totalComponentsWithSlots: report.slotInventory.length,
    totalSlotProperties: trace.slotsFound,
    totalTransitions: trace.transitions,
    gainedSlot: report.slotTransitions.filter(t => t.direction === 'GAINED_SLOT').length,
    lostSlot: report.slotTransitions.filter(t => t.direction === 'LOST_SLOT').length,
    newComponents: report.newComponents.length,
    removedComponents: report.removedComponents.length,
    slotNameFrequency: Object.fromEntries(
      Object.entries(slotTypeMap).sort((a, b) => b[1] - a[1])
    ),
    topSlotComponents: report.slotDepthAnalysis.slice(0, 10),
  };

  return report;
}

// ─── Self-Test ──────────────────────────────────────────────
function selfTest() {
  let passed = 0, failed = 0;
  const test = (name, fn) => {
    try { fn(); console.log(`  ✅ ${name}`); passed++; }
    catch (e) { console.log(`  ❌ ${name}: ${e.message}`); failed++; }
  };

  console.log(`\n${SCRIPT_NAME} — Self-Test\n`);

  test('Dependencies', () => { require('fs'); require('path'); });

  test('buildEntryMap', () => {
    const map = buildEntryMap([{ name: 'A' }, { name: 'B' }]);
    if (map.size !== 2) throw new Error('Expected 2');
  });

  test('extractSlotProperties — with SLOT', () => {
    const entry = { properties: [{ cleanName: 'Items', type: 'SLOT' }, { cleanName: 'Label', type: 'TEXT' }] };
    const slots = extractSlotProperties(entry);
    if (slots.length !== 1) throw new Error(`Expected 1, got ${slots.length}`);
  });

  test('extractSlotProperties — no properties', () => {
    const slots = extractSlotProperties({});
    if (slots.length !== 0) throw new Error('Expected 0');
  });

  test('Default files exist', () => {
    // Just check one exists to validate workspace
    if (!fs.existsSync(DEFAULT_FILE_A) && !fs.existsSync(DEFAULT_FILE_B)) {
      log.warn('Neither default library-pass file found — will need explicit paths');
    }
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return;

  if (config.dryRun) {
    log('🔍 DRY-RUN — Would compare:');
    log(`  File A (SLOT):     ${config.fileA} (${fs.existsSync(config.fileA) ? 'EXISTS' : 'NOT FOUND'})`);
    log(`  File B (non-SLOT): ${config.fileB} (${fs.existsSync(config.fileB) ? 'EXISTS' : 'NOT FOUND'})`);
    return;
  }

  validate(config);

  log('━━━ Harvesting Library Evolution ━━━\n');

  const dataA = loadJSON(config.fileA, 'fileA (SLOT)');
  const dataB = loadJSON(config.fileB, 'fileB (non-SLOT)');

  log('  Analyzing evolution...');
  const report = analyzeEvolution(dataA, dataB);

  // Add scan meta
  report.scanMeta = {
    timestamp: new Date().toISOString(),
    fileA: path.basename(config.fileA),
    fileB: path.basename(config.fileB),
    scriptVersion: VERSION,
  };

  if (config.jsonOutput) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    fs.mkdirSync(path.dirname(config.outputPath), { recursive: true });
    fs.writeFileSync(config.outputPath, JSON.stringify(report, null, 2));
    log(`\n📄 Report written: ${config.outputPath}`);
    log(`   Size: ${(fs.statSync(config.outputPath).size / 1024).toFixed(1)} KB`);
  }

  // Print key findings
  log('\n━━━ SLOT Evolution Summary ━━━');
  log(`  Components with SLOTs:  ${report.slotSummary.totalComponentsWithSlots}`);
  log(`  Total SLOT properties:  ${report.slotSummary.totalSlotProperties}`);
  log(`  SLOT transitions:       ${report.slotSummary.totalTransitions}`);
  log(`    Gained SLOT: ${report.slotSummary.gainedSlot}`);
  log(`    Lost SLOT:   ${report.slotSummary.lostSlot}`);
  log(`  New components:         ${report.slotSummary.newComponents}`);
  log(`  Removed components:     ${report.slotSummary.removedComponents}`);
  if (report.slotSummary.topSlotComponents.length > 0) {
    log(`  Top SLOT components:    ${report.slotSummary.topSlotComponents.slice(0, 5).map(s => `${s.name}(${s.totalDepth})`).join(', ')}`);
  }
}

main();

#!/usr/bin/env node
'use strict';

// ============================================================
// Script: harvest-spec-patterns
// Purpose: Phân tích 34 xPOS specs + test specs, extract reusable patterns:
//          componentRef frequency, role distribution, token usage,
//          layout patterns, fallback inventory, state/override patterns.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-14
// Usage: node harvest-spec-patterns.js [options]
// Dependencies: node >= 18
// Quality-grade: A
// Exit codes: 0=success, 1=error, 2=usage
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

const WORKSPACE = path.resolve(__dirname, '..', '..', '..', '..', '..');
const XPOS_DIR = path.join(WORKSPACE, 'bridge', 'specs', 'xpos');
const TESTS_DIR = path.join(WORKSPACE, 'bridge', 'specs', 'tests');
const SPECS_ROOT = path.join(WORKSPACE, 'bridge', 'specs');
const OUTPUT_DIR = path.join(__dirname, '..', 'output');

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
  specsProcessed: 0, totalNodes: 0, warnings: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration:   ${duration}s`);
    console.error(`  Specs:      ${this.specsProcessed}`);
    console.error(`  Nodes:      ${this.totalNodes}`);
    console.error(`  Warnings:   ${this.warnings}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Extract reusable patterns from Bridge specs

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options]

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test
  --dry-run        Preview sources
  --json           Output to stdout
  -o, --output     Output path (default: output/spec-patterns-report.json)

${c.yellow}SCAN DIRS:${c.reset}
  bridge/specs/xpos/   — 34 xPOS production specs
  bridge/specs/tests/  — test specs
  bridge/specs/*.json  — standalone specs
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
  let outputPath = path.join(OUTPUT_DIR, 'spec-patterns-report.json');
  const outIdx = args.indexOf('-o') !== -1 ? args.indexOf('-o') : args.indexOf('--output');
  if (outIdx !== -1 && args[outIdx + 1]) outputPath = args[outIdx + 1];

  return { dryRun, jsonOutput, outputPath };
}

// ─── Validation ─────────────────────────────────────────────
function validate() {
  if (!fs.existsSync(XPOS_DIR)) log.die(`xPOS dir not found: ${XPOS_DIR}`);
  log('✅ Validation passed');
}

// ─── Utilities ──────────────────────────────────────────────
function safeReadJSON(f) {
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); }
  catch { log.warn(`Failed to parse: ${f}`); trace.warnings++; return null; }
}

function globDir(dir, ext) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(f => f.endsWith(ext)).map(f => path.join(dir, f));
}

function inc(map, key) { map[key] = (map[key] || 0) + 1; }

// ─── Node Walker ────────────────────────────────────────────

/**
 * Recursively walk a spec node tree, calling visitor on each node.
 * @param {object} node
 * @param {function} visitor - (node, depth, parentNode)
 * @param {number} depth
 * @param {object|null} parent
 */
function walkNodes(node, visitor, depth = 0, parent = null) {
  if (!node) return;
  visitor(node, depth, parent);
  if (node.children) {
    for (const child of node.children) {
      walkNodes(child, visitor, depth + 1, node);
    }
  }
  // Handle state mutations with embedded nodes
  if (node.states) {
    for (const state of node.states) {
      if (state.mutations) {
        for (const m of state.mutations) {
          if (m.node) walkNodes(m.node, visitor, depth + 1, node);
        }
      }
    }
  }
}

// ─── Core Analysis ──────────────────────────────────────────

function analyzeSpecs(specFiles) {
  const report = {
    componentRefFrequency: {},
    roleDistribution: {},
    tokenUsage: { spacing: {}, color: {}, radius: {} },
    layoutPatterns: { maxDepth: 0, avgDepth: 0, depthDistribution: {}, gridPatterns: [] },
    fallbackInventory: [],
    statePatterns: [],
    overridePatterns: {},
    perSpec: [],
  };

  let totalDepthSum = 0;
  let totalNodeCount = 0;

  for (const f of specFiles) {
    const data = safeReadJSON(f);
    if (!data || !data.root) continue;
    trace.specsProcessed++;

    const basename = path.basename(f);
    const specReport = {
      file: basename,
      screen: data.screen || '(unnamed)',
      specVersion: data.specVersion || '(unknown)',
      nodeCount: 0,
      componentRefCount: 0,
      generativeCount: 0,
      maxDepth: 0,
      uniqueRoles: new Set(),
      uniqueTokens: new Set(),
    };

    // Walk all nodes
    walkNodes(data.root, (node, depth) => {
      specReport.nodeCount++;
      totalNodeCount++;
      trace.totalNodes++;

      // Depth tracking
      if (depth > specReport.maxDepth) specReport.maxDepth = depth;
      if (depth > report.layoutPatterns.maxDepth) report.layoutPatterns.maxDepth = depth;
      inc(report.layoutPatterns.depthDistribution, String(depth));
      totalDepthSum += depth;

      // Role distribution
      if (node.role) {
        inc(report.roleDistribution, node.role);
        specReport.uniqueRoles.add(node.role);
      }

      // componentRef frequency
      if (node.componentRef) {
        inc(report.componentRefFrequency, node.componentRef);
        specReport.componentRefCount++;
      } else if (node.role && node.role !== 'screen') {
        specReport.generativeCount++;
      }

      // Token usage — spacing
      if (node.gap && typeof node.gap === 'string') {
        inc(report.tokenUsage.spacing, node.gap);
        specReport.uniqueTokens.add(node.gap);
      }
      if (node.padding && Array.isArray(node.padding)) {
        for (const p of node.padding) {
          if (typeof p === 'string') {
            inc(report.tokenUsage.spacing, p);
            specReport.uniqueTokens.add(p);
          }
        }
      }

      // Token usage — color
      for (const colorProp of ['fill', 'textFill', 'stroke']) {
        if (node[colorProp] && typeof node[colorProp] === 'string' && !node[colorProp].startsWith('#')) {
          inc(report.tokenUsage.color, node[colorProp]);
          specReport.uniqueTokens.add(node[colorProp]);
        }
      }

      // Token usage — radius
      if (node.radius && typeof node.radius === 'string') {
        inc(report.tokenUsage.radius, node.radius);
        specReport.uniqueTokens.add(node.radius);
      }

      // Layout patterns — detect grid structures
      if (node.layout === 'horizontal' && node.children && node.children.length >= 2) {
        const allFill = node.children.every(ch => ch.width === 'fill');
        if (allFill) {
          report.layoutPatterns.gridPatterns.push({
            specFile: basename,
            key: node.key,
            columns: node.children.length,
            depth,
          });
        }
      }

      // Fallback inventory
      if (node._fallback || node._note) {
        const note = node._fallback || node._note || '';
        if (note.includes('fallback') || note.includes('COMPONENT type')
            || note.includes('key import fails') || note.includes('generative')
            || note.includes('no library match') || note.includes('wrong Pro Blocks')) {
          report.fallbackInventory.push({
            specFile: basename,
            nodeKey: node.key,
            reason: note.substring(0, 200),
            componentRef: node.componentRef || null,
          });
        }
      }

      // Override patterns
      if (node.componentRef && node.overrides) {
        const ref = node.componentRef;
        if (!report.overridePatterns[ref]) report.overridePatterns[ref] = {};
        for (const propName of Object.keys(node.overrides)) {
          inc(report.overridePatterns[ref], propName);
        }
      }
    });

    // State patterns
    if (data.states && data.states.length > 0) {
      for (const state of data.states) {
        const mutationTypes = {};
        if (state.mutations) {
          for (const m of state.mutations) {
            inc(mutationTypes, m.action || 'unknown');
          }
        }
        report.statePatterns.push({
          specFile: basename,
          stateName: state.name,
          trigger: state.trigger || '(none)',
          mutationCount: state.mutations ? state.mutations.length : 0,
          mutationTypes,
        });
      }
    }

    // Convert Sets to counts for serialization
    report.perSpec.push({
      ...specReport,
      uniqueRoles: specReport.uniqueRoles.size,
      uniqueTokens: specReport.uniqueTokens.size,
    });
  }

  // Compute average depth
  report.layoutPatterns.avgDepth = totalNodeCount > 0
    ? Math.round((totalDepthSum / totalNodeCount) * 10) / 10
    : 0;

  return report;
}

// ─── Sort helpers ───────────────────────────────────────────
function sortMapDesc(obj) {
  return Object.fromEntries(
    Object.entries(obj).sort((a, b) => b[1] - a[1])
  );
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

  test('xPOS directory exists', () => {
    if (!fs.existsSync(XPOS_DIR)) throw new Error('Not found');
  });

  test('walkNodes — counts correctly', () => {
    let count = 0;
    walkNodes({ key: 'a', children: [{ key: 'b' }, { key: 'c', children: [{ key: 'd' }] }] },
      () => count++);
    if (count !== 4) throw new Error(`Expected 4, got ${count}`);
  });

  test('walkNodes — depth tracking', () => {
    const depths = [];
    walkNodes({ key: 'a', children: [{ key: 'b', children: [{ key: 'c' }] }] },
      (_, depth) => depths.push(depth));
    if (JSON.stringify(depths) !== '[0,1,2]') throw new Error(`Expected [0,1,2], got ${JSON.stringify(depths)}`);
  });

  test('inc — counter', () => {
    const m = {};
    inc(m, 'a'); inc(m, 'a'); inc(m, 'b');
    if (m.a !== 2 || m.b !== 1) throw new Error('Counter mismatch');
  });

  test('sortMapDesc — ordering', () => {
    const sorted = sortMapDesc({ a: 1, b: 3, c: 2 });
    const keys = Object.keys(sorted);
    if (keys[0] !== 'b') throw new Error(`Expected 'b' first, got '${keys[0]}'`);
  });

  test('globDir — nonexistent returns empty', () => {
    const r = globDir('/nonexistent', '.json');
    if (r.length !== 0) throw new Error('Expected empty');
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return;

  validate();

  // Collect all spec files
  const specFiles = [
    ...globDir(XPOS_DIR, '.json'),
    ...globDir(TESTS_DIR, '.json'),
    ...globDir(SPECS_ROOT, '.json').filter(f => {
      const b = path.basename(f);
      // Exclude non-spec files
      return !['converter-manifest.json', 'full-ddl-tokens.json', 'full-tokens.json', 'validate-specs.js'].includes(b);
    }),
  ];

  if (config.dryRun) {
    log(`🔍 DRY-RUN — Would scan ${specFiles.length} spec files:`);
    log(`  xPOS:       ${globDir(XPOS_DIR, '.json').length}`);
    log(`  Tests:      ${globDir(TESTS_DIR, '.json').length}`);
    log(`  Standalone: ${globDir(SPECS_ROOT, '.json').length}`);
    return;
  }

  log('━━━ Harvesting Spec Patterns ━━━\n');
  log(`  Total spec files: ${specFiles.length}`);

  const report = analyzeSpecs(specFiles);

  // Sort frequency maps for readability
  report.componentRefFrequency = sortMapDesc(report.componentRefFrequency);
  report.roleDistribution = sortMapDesc(report.roleDistribution);
  report.tokenUsage.spacing = sortMapDesc(report.tokenUsage.spacing);
  report.tokenUsage.color = sortMapDesc(report.tokenUsage.color);
  report.tokenUsage.radius = sortMapDesc(report.tokenUsage.radius);

  // Add summary
  const summary = {
    timestamp: new Date().toISOString(),
    specsAnalyzed: trace.specsProcessed,
    totalNodes: trace.totalNodes,
    uniqueComponentRefs: Object.keys(report.componentRefFrequency).length,
    uniqueRoles: Object.keys(report.roleDistribution).length,
    uniqueSpacingTokens: Object.keys(report.tokenUsage.spacing).length,
    uniqueColorTokens: Object.keys(report.tokenUsage.color).length,
    uniqueRadiusTokens: Object.keys(report.tokenUsage.radius).length,
    totalFallbacks: report.fallbackInventory.length,
    totalStates: report.statePatterns.length,
    totalGridPatterns: report.layoutPatterns.gridPatterns.length,
    scriptVersion: VERSION,
  };

  const finalReport = { summary, ...report };

  if (config.jsonOutput) {
    console.log(JSON.stringify(finalReport, null, 2));
  } else {
    fs.mkdirSync(path.dirname(config.outputPath), { recursive: true });
    fs.writeFileSync(config.outputPath, JSON.stringify(finalReport, null, 2));
    log(`\n📄 Report written: ${config.outputPath}`);
    log(`   Size: ${(fs.statSync(config.outputPath).size / 1024).toFixed(1)} KB`);
  }

  // Print key findings
  log('\n━━━ Key Findings ━━━');
  log(`  Components used: ${Object.keys(report.componentRefFrequency).length} unique refs`);
  log(`  Top 5 componentRefs: ${Object.entries(report.componentRefFrequency).slice(0, 5).map(([k, v]) => `${k}(${v})`).join(', ')}`);
  log(`  Roles used: ${Object.keys(report.roleDistribution).length}/30`);
  log(`  Fallbacks: ${report.fallbackInventory.length} generative fallbacks with notes`);
  log(`  States: ${report.statePatterns.length} state definitions across specs`);
  log(`  Grid patterns: ${report.layoutPatterns.gridPatterns.length} detected`);
}

main();

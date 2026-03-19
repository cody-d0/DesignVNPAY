#!/usr/bin/env node
'use strict';

// ============================================================
// Script: harvest-bridge-context
// Purpose: Deep scan toàn bộ bridge development artifacts, tổng hợp
//          scripts, library indexes, resolver maps, rules, plugin source
//          thành structured JSON report cho SLOT-based plugin development.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-14
// Usage: node harvest-bridge-context.js [options]
// Dependencies: node >= 18
// Quality-grade: A
// Exit codes: 0=success, 1=error, 2=usage
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

// Workspace root — resolve relative to this script's location
const WORKSPACE = path.resolve(__dirname, '..', '..', '..', '..', '..');
const BRIDGE_DIR = path.join(WORKSPACE, 'bridge');
const DATA_DIR = path.join(WORKSPACE, 'data');
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

// ─── Unhandled Rejection Guard ──────────────────────────────
process.on('unhandledRejection', (err) => { log.die('💥 Unhandled:', err); });

// ─── Execution Trace ────────────────────────────────────────
const trace = {
  start: Date.now(),
  filesScanned: 0, insights: 0, warnings: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration:      ${duration}s`);
    console.error(`  Files scanned: ${this.filesScanned}`);
    console.error(`  Insights:      ${this.insights}`);
    console.error(`  Warnings:      ${this.warnings}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Deep scan bridge development artifacts

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options]

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test (smoke test)
  --dry-run        Preview what would be scanned
  --json           Output to stdout (default: write to file)
  -o, --output     Output path (default: output/bridge-context-report.json)

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js                          # Full scan, write report file
  node ${SCRIPT_NAME}.js --dry-run                # Preview sources
  node ${SCRIPT_NAME}.js --json | jq '.scripts'   # Pipe to jq
`);
  process.exit(0);
}

// ─── Args Parsing ───────────────────────────────────────────
function parseCliArgs() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) showHelp();
  if (args.includes('--version') || args.includes('-v')) { console.log(VERSION); process.exit(0); }
  if (args.includes('--test')) { selfTest(); return null; }

  const dryRun = args.includes('--dry-run');
  const jsonOutput = args.includes('--json');

  let outputPath = path.join(OUTPUT_DIR, 'bridge-context-report.json');
  const outIdx = args.indexOf('-o') !== -1 ? args.indexOf('-o') : args.indexOf('--output');
  if (outIdx !== -1 && args[outIdx + 1]) outputPath = args[outIdx + 1];

  return { dryRun, jsonOutput, outputPath };
}

// ─── Validation ─────────────────────────────────────────────
function validate() {
  const errors = [];

  if (!fs.existsSync(BRIDGE_DIR)) errors.push(`Bridge dir not found: ${BRIDGE_DIR}`);
  if (!fs.existsSync(DATA_DIR)) errors.push(`Data dir not found: ${DATA_DIR}`);

  if (errors.length > 0) {
    errors.forEach(e => log.error(e));
    log.die(`${errors.length} validation error(s). Is workspace correct? (${WORKSPACE})`);
  }

  log('✅ Validation passed');
  log(`  Workspace: ${WORKSPACE}`);
}

// ─── Utilities ──────────────────────────────────────────────
/** @param {string} filePath */
function safeReadJSON(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (_e) {
    log.warn(`Failed to parse JSON: ${filePath}`);
    trace.warnings++;
    return null;
  }
}

/** @param {string} filePath */
function safeReadText(filePath) {
  try {
    return fs.readFileSync(filePath, 'utf8');
  } catch (_e) {
    log.warn(`Failed to read: ${filePath}`);
    trace.warnings++;
    return null;
  }
}

/**
 * @param {string} dir
 * @param {string} ext
 */
function globDir(dir, ext) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith(ext))
    .map(f => path.join(dir, f));
}

/** @param {string | null} text */
function countLines(text) {
  return text ? text.split('\n').length : 0;
}

// ─── Core Harvesters ────────────────────────────────────────

/**
 * Scan bridge/scripts/*.js — extract metadata about each script.
 */
function harvestScripts() {
  const scriptsDir = path.join(BRIDGE_DIR, 'scripts');
  const files = [
    ...globDir(scriptsDir, '.js'),
    ...globDir(scriptsDir, '.ts'),
  ];

  log(`  📂 Scripts: ${files.length} files in ${scriptsDir}`);

  return files.map(f => {
    const text = safeReadText(f);
    if (!text) return null;
    trace.filesScanned++;

    const basename = path.basename(f);
    const lines = countLines(text);

    // Extract purpose from header comment
    const purposeMatch = text.match(/\/\/\s*Purpose:\s*(.+)/i)
      || text.match(/\*\s+(.+?)\s+\*/);
    const purpose = purposeMatch ? purposeMatch[1].trim() : '(no description)';

    // Extract dependencies (require/import)
    const requires = (text.match(/require\(['"`]([^'"]+)['"`]\)/g) || [])
      .map(m => { const r = m.match(/['"`]([^'"]+)['"`]/); return r ? r[1] : ''; });
    const imports = (text.match(/from\s+['"`]([^'"]+)['"`]/g) || [])
      .map(m => { const r = m.match(/['"`]([^'"]+)['"`]/); return r ? r[1] : ''; });
    const deps = [...new Set([...requires, ...imports])];

    // Extract exported functions
    const exportedFns = (text.match(/(?:module\.exports\s*=|export\s+(?:default\s+)?(?:function|const|class))\s*(\w+)?/g) || []);

    // Detect key patterns
    const patterns = [];
    if (text.includes('componentRef')) patterns.push('componentRef-handling');
    if (text.includes('variantIndex') || text.includes('variant-index')) patterns.push('variant-resolution');
    if (text.includes('setBoundVariable') || text.includes('binding')) patterns.push('variable-binding');
    if (text.includes('specVersion')) patterns.push('spec-versioning');
    if (text.includes('SLOT') || text.includes('slot')) patterns.push('slot-awareness');
    if (text.includes('Auto Layout') || text.includes('autoLayout') || text.includes('layoutMode')) patterns.push('auto-layout');

    return {
      name: basename,
      purpose,
      loc: lines,
      dependencies: deps,
      exports: exportedFns.length,
      patterns,
    };
  }).filter(Boolean);
}

/**
 * Scan bridge/library/01-index/*.json — library catalog stats.
 */
function harvestLibraryStats() {
  const indexDir = path.join(BRIDGE_DIR, 'library', '01-index');
  const files = globDir(indexDir, '.json');
  log(`  📂 Library index: ${files.length} files in ${indexDir}`);

  const stats = {
    totalComponents: 0,
    tierDistribution: {},
    indexFiles: [],
    slotsFound: 0,
    componentTypes: {},
    pagesScanned: 0,
  };

  for (const f of files) {
    const data = safeReadJSON(f);
    if (!data) continue;
    trace.filesScanned++;

    const basename = path.basename(f);
    const entryCount = Array.isArray(data) ? data.length
      : data.entries ? data.entries.length
      : typeof data === 'object' ? Object.keys(data).length
      : 0;

    stats.indexFiles.push({ name: basename, entries: entryCount });

    // component-index.json specific analysis
    if (basename === 'component-index.json') {
      const entries = data.entries || (Array.isArray(data) ? data : []);
      stats.totalComponents = entries.length;

      for (const entry of entries) {
        // Tier distribution
        const tier = entry.tier || 'unknown';
        stats.tierDistribution[tier] = (stats.tierDistribution[tier] || 0) + 1;

        // Component type
        const type = entry.type || 'unknown';
        stats.componentTypes[type] = (stats.componentTypes[type] || 0) + 1;

        // SLOT detection
        if (entry.properties) {
          const slotProps = (Array.isArray(entry.properties) ? entry.properties : [])
            .filter(p => p.type === 'SLOT' || (p.cleanName && p.cleanName.toUpperCase().includes('SLOT')));
          stats.slotsFound += slotProps.length;
        }
      }

      if (data.pageSummaries) {
        stats.pagesScanned = data.pageSummaries.length;
      }
    }
  }

  return stats;
}

/**
 * Scan bridge/library/04-resolver/*.json — resolver map stats.
 */
function harvestResolverMaps() {
  const resolverDir = path.join(BRIDGE_DIR, 'library', '04-resolver');
  const files = globDir(resolverDir, '.json');
  log(`  📂 Resolver maps: ${files.length} files in ${resolverDir}`);

  const maps = {};

  for (const f of files) {
    const data = safeReadJSON(f);
    if (!data) continue;
    trace.filesScanned++;

    const basename = path.basename(f, '.json');
    const count = Array.isArray(data) ? data.length
      : typeof data === 'object' ? Object.keys(data).length
      : 0;

    maps[basename] = { count, sampleKeys: Object.keys(data).slice(0, 5) };
  }

  return maps;
}

/**
 * Extract rules from AGENT_RULES.md as structured data.
 */
function harvestRules() {
  const rulesFile = path.join(BRIDGE_DIR, 'plugin', 'AGENT_RULES.md');
  const text = safeReadText(rulesFile);
  if (!text) return [];
  trace.filesScanned++;

  const rules = [];

  // Extract The 2 Immutable Rules
  const rule1Match = text.match(/### Rule 1[^\n]*\n\n```\n([\s\S]*?)```/);
  if (rule1Match) {
    rules.push({
      id: 'RULE-1', name: 'Instantiation-First',
      description: rule1Match[1].trim(),
      enforcement: 'IMMUTABLE',
    });
  }

  const rule2Match = text.match(/### Rule 2[^\n]*\n\n```\n([\s\S]*?)```/);
  if (rule2Match) {
    rules.push({
      id: 'RULE-2', name: 'Pre-binding',
      description: rule2Match[1].trim(),
      enforcement: 'IMMUTABLE',
    });
  }

  // Extract 30 valid roles
  const rolesMatch = text.match(/```\n(Base:[\s\S]*?Button:.*?)\n```/);
  if (rolesMatch) {
    const roleLines = rolesMatch[1].trim().split('\n');
    const allRoles = roleLines.flatMap(line => {
      const parts = line.split(':').slice(1).join(':').trim();
      return parts.split(',').map(r => r.trim()).filter(Boolean);
    });
    rules.push({
      id: 'ROLE-DEFS', name: 'Valid Roles (30)',
      description: `${allRoles.length} roles defined`,
      enforcement: 'SCHEMA',
      roles: allRoles,
    });
  }

  // Extract prohibitions (P1-P10)
  const prohibitions = [];
  const pMatches = text.matchAll(/\|\s*P(\d+)\s*\|\s*\*\*([^*]+)\*\*[^|]*\|\s*([^|]+)\|/g);
  for (const m of pMatches) {
    prohibitions.push({ id: `P${m[1]}`, rule: m[2].trim(), reason: m[3].trim() });
  }
  if (prohibitions.length > 0) {
    rules.push({
      id: 'PROHIBITIONS', name: 'Absolute Prohibitions',
      description: `${prohibitions.length} explicit prohibitions`,
      enforcement: 'ABSOLUTE',
      items: prohibitions,
    });
  }

  // Extract quality gates
  const gates = [];
  const gateBlocks = text.match(/### Gate \d+[\s\S]*?(?=###|---|\n##)/g) || [];
  for (const block of gateBlocks) {
    const nameMatch = block.match(/### (Gate \d+ — [^\n]+)/);
    if (nameMatch) gates.push({ name: nameMatch[1].trim() });
  }
  if (gates.length > 0) {
    rules.push({
      id: 'QUALITY-GATES', name: 'Quality Gates',
      description: `${gates.length} gates defined`,
      enforcement: 'GATE',
      items: gates,
    });
  }

  return rules;
}

/**
 * Scan non-xpos specs for test patterns and design system specs.
 */
function harvestSpecMeta() {
  const specsDir = path.join(BRIDGE_DIR, 'specs');
  const files = globDir(specsDir, '.json');
  const testDir = path.join(specsDir, 'tests');
  const testFiles = globDir(testDir, '.json');

  log(`  📂 Specs (root): ${files.length} files`);
  log(`  📂 Specs (tests): ${testFiles.length} files`);

  const specMeta = [];

  for (const f of [...files, ...testFiles]) {
    const data = safeReadJSON(f);
    if (!data) continue;
    trace.filesScanned++;

    const basename = path.basename(f);
    const isTest = f.includes('/tests/');

    specMeta.push({
      name: basename,
      type: isTest ? 'test' : 'standalone',
      specVersion: data.specVersion || '(unknown)',
      screen: data.screen || '(unnamed)',
      hasTokens: !!(data.tokens && data.tokens.collections && data.tokens.collections.length > 0),
      hasStates: !!(data.states && data.states.length > 0),
      nodeCount: countNodes(data.root),
    });
  }

  return specMeta;
}

/** @param {any} node */
function countNodes(node) {
  if (!node) return 0;
  let count = 1;
  if (node.children) {
    for (const child of node.children) {
      count += countNodes(child);
    }
  }
  return count;
}

/**
 * Generate actionable insights from all harvested data.
 */
/**
 * @param {any[]} scripts
 * @param {any} libraryStats
 * @param {any} resolverMaps
 * @param {any[]} rules
 * @param {any[]} specMeta
 */
function generateInsights(scripts, libraryStats, resolverMaps, rules, specMeta) {
  const insights = [];

  // Insight: SLOT coverage
  if (libraryStats.slotsFound > 0) {
    insights.push({
      category: 'SLOT',
      finding: `${libraryStats.slotsFound} SLOT properties found in library catalog`,
      source: 'component-index.json',
      value: 'SLOT-ready components available for new plugin ver',
    });
    trace.insights++;
  }

  // Insight: Script patterns for SLOT
  const slotAwareScripts = scripts.filter(s => s.patterns.includes('slot-awareness'));
  if (slotAwareScripts.length > 0) {
    insights.push({
      category: 'SLOT',
      finding: `${slotAwareScripts.length} scripts already handle SLOT: ${slotAwareScripts.map(s => s.name).join(', ')}`,
      source: 'bridge/scripts/',
      value: 'Existing SLOT handling patterns to build on',
    });
    trace.insights++;
  }

  // Insight: componentRef usage in scripts
  const compRefScripts = scripts.filter(s => s.patterns.includes('componentRef-handling'));
  insights.push({
    category: 'ARCHITECTURE',
    finding: `${compRefScripts.length}/${scripts.length} scripts handle componentRef resolution`,
    source: 'bridge/scripts/',
    value: 'Component resolution is a cross-cutting concern',
  });
  trace.insights++;

  // Insight: Library scale
  insights.push({
    category: 'SCALE',
    finding: `Library has ${libraryStats.totalComponents} components across ${libraryStats.pagesScanned} pages`,
    source: 'library/01-index/',
    value: `Tier distribution: ${JSON.stringify(libraryStats.tierDistribution)}`,
  });
  trace.insights++;

  // Insight: Spec version consistency
  const versionMap = {};
  for (const s of specMeta) {
    versionMap[s.specVersion] = (versionMap[s.specVersion] || 0) + 1;
  }
  insights.push({
    category: 'CONSISTENCY',
    finding: `Spec versions in use: ${JSON.stringify(versionMap)}`,
    source: 'bridge/specs/',
    value: 'Version alignment check for migration',
  });
  trace.insights++;

  // Insight: Token-free specs (Verify-Only compliance)
  const tokenFreeSpecs = specMeta.filter(s => !s.hasTokens);
  insights.push({
    category: 'RULE-COMPLIANCE',
    finding: `${tokenFreeSpecs.length}/${specMeta.length} specs are token-free (Verify-Only compliant)`,
    source: 'bridge/specs/',
    value: 'Verify-Only adoption rate for Rule 2',
  });
  trace.insights++;

  // Insight: Total LOC in bridge scripts
  const totalLOC = scripts.reduce((sum, s) => sum + s.loc, 0);
  insights.push({
    category: 'SCALE',
    finding: `Bridge scripts total: ${totalLOC} LOC across ${scripts.length} files`,
    source: 'bridge/scripts/',
    value: 'Codebase scale for plugin development context',
  });
  trace.insights++;

  return insights;
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

  test('Workspace resolution', () => {
    if (!fs.existsSync(WORKSPACE)) throw new Error(`Workspace not found: ${WORKSPACE}`);
  });

  test('Bridge directory exists', () => {
    if (!fs.existsSync(BRIDGE_DIR)) throw new Error(`Bridge dir not found: ${BRIDGE_DIR}`);
  });

  test('countNodes — empty', () => {
    if (countNodes(null) !== 0) throw new Error('Expected 0');
  });

  test('countNodes — nested', () => {
    const node = { children: [{ children: [{}, {}] }, {}] };
    if (countNodes(node) !== 5) throw new Error(`Expected 5, got ${countNodes(node)}`);
  });

  test('globDir — returns array', () => {
    const result = globDir('/nonexistent/path', '.json');
    if (!Array.isArray(result)) throw new Error('Expected array');
    if (result.length !== 0) throw new Error('Expected empty for nonexistent path');
  });

  test('safeReadJSON — invalid path returns null', () => {
    const result = safeReadJSON('/nonexistent/file.json');
    if (result !== null) throw new Error('Expected null');
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return; // --test handled

  validate();

  if (config.dryRun) {
    log('🔍 DRY-RUN — Sources that would be scanned:');
    log(`  bridge/scripts/     → ${globDir(path.join(BRIDGE_DIR, 'scripts'), '.js').length + globDir(path.join(BRIDGE_DIR, 'scripts'), '.ts').length} files`);
    log(`  library/01-index/   → ${globDir(path.join(BRIDGE_DIR, 'library', '01-index'), '.json').length} files`);
    log(`  library/04-resolver/→ ${globDir(path.join(BRIDGE_DIR, 'library', '04-resolver'), '.json').length} files`);
    log(`  AGENT_RULES.md      → ${fs.existsSync(path.join(BRIDGE_DIR, 'plugin', 'AGENT_RULES.md')) ? '1 file' : 'NOT FOUND'}`);
    log(`  specs/ (root)       → ${globDir(path.join(BRIDGE_DIR, 'specs'), '.json').length} files`);
    log(`  specs/tests/        → ${globDir(path.join(BRIDGE_DIR, 'specs', 'tests'), '.json').length} files`);
    log('No output written.');
    return;
  }

  log('━━━ Harvesting Bridge Context ━━━\n');

  log('📂 Stage 1: Scripts');
  const scripts = harvestScripts();

  log('📂 Stage 2: Library Stats');
  const libraryStats = harvestLibraryStats();

  log('📂 Stage 3: Resolver Maps');
  const resolverMaps = harvestResolverMaps();

  log('📂 Stage 4: Agent Rules');
  const rules = harvestRules();

  log('📂 Stage 5: Spec Metadata');
  const specMeta = harvestSpecMeta();

  log('💡 Stage 6: Generate Insights');
  const insights = generateInsights(scripts, libraryStats, resolverMaps, rules, specMeta);

  // ── Assemble report ──
  const report = {
    scanMeta: {
      timestamp: new Date().toISOString(),
      workspace: WORKSPACE,
      filesScanned: trace.filesScanned,
      duration: `${((Date.now() - trace.start) / 1000).toFixed(1)}s`,
      scriptVersion: VERSION,
    },
    scripts,
    libraryStats,
    resolverMaps,
    rulesExtracted: rules,
    specMeta,
    insights,
  };

  // ── Output ──
  if (config.jsonOutput) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    fs.mkdirSync(path.dirname(config.outputPath), { recursive: true });
    fs.writeFileSync(config.outputPath, JSON.stringify(report, null, 2));
    log(`\n📄 Report written: ${config.outputPath}`);
    log(`   Size: ${(fs.statSync(config.outputPath).size / 1024).toFixed(1)} KB`);
  }

  log(`\n✅ Done. ${scripts.length} scripts, ${libraryStats.totalComponents} components, ${insights.length} insights.`);
}

main();

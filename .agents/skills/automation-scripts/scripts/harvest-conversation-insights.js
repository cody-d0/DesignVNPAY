#!/usr/bin/env node
'use strict';

// ============================================================
// Script: harvest-conversation-insights
// Purpose: Mine Knowledge Item (KI) artifacts for Bridge development
//          lessons learned — bug patterns, architecture decisions,
//          case studies, test results, cross-KI connections.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-14
// Usage: node harvest-conversation-insights.js [options]
// Dependencies: node >= 18
// Quality-grade: A
// Exit codes: 0=success, 1=error, 2=usage
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

const HOME = process.env.HOME || process.env.USERPROFILE || '/Users/dataism';
const KI_BASE = path.join(HOME, '.gemini', 'antigravity', 'knowledge');
const WORKSPACE = path.resolve(__dirname, '..', '..', '..', '..', '..');
const OUTPUT_DIR = path.join(__dirname, '..', 'output');

// KIs relevant to Bridge development
const TARGET_KIS = [
  'figma_bridge_system',
  'ba_design_pipeline_architecture',
  'shadcn_identity_distillery',
  'vnpay_design_ecosystem',
  'design_data_layer_system',
  'bigger_picture_bp_system',
  'vnpay_agentic_context_management',
];

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
  kisScanned: 0, artifactsRead: 0, insightsExtracted: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration:   ${duration}s`);
    console.error(`  KIs:        ${this.kisScanned}`);
    console.error(`  Artifacts:  ${this.artifactsRead}`);
    console.error(`  Insights:   ${this.insightsExtracted}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Mine KI artifacts for Bridge development insights

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options]

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test
  --dry-run        Preview KIs to scan
  --json           Output to stdout
  --all            Scan ALL KIs, not just Bridge-relevant ones
  -o, --output     Output path

${c.yellow}TARGET KIs:${c.reset}
  ${TARGET_KIS.join('\n  ')}
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
  const scanAll = args.includes('--all');
  let outputPath = path.join(OUTPUT_DIR, 'conversation-insights-report.json');
  const outIdx = args.indexOf('-o') !== -1 ? args.indexOf('-o') : args.indexOf('--output');
  if (outIdx !== -1 && args[outIdx + 1]) outputPath = args[outIdx + 1];

  return { dryRun, jsonOutput, outputPath, scanAll };
}

// ─── Validation ─────────────────────────────────────────────
function validate() {
  if (!fs.existsSync(KI_BASE)) log.die(`KI base not found: ${KI_BASE}`);
  log('✅ Validation passed');
  log(`  KI base: ${KI_BASE}`);
}

// ─── Utilities ──────────────────────────────────────────────
/** @param {string} f */
function safeReadJSON(f) {
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); }
  catch (_e) { return null; }
}

/** @param {string} f */
function safeReadText(f) {
  try { return fs.readFileSync(f, 'utf8'); }
  catch (_e) { return null; }
}

/**
 * @param {string} dir
 * @param {string} ext
 * @param {number} [maxDepth]
 */
function findFiles(dir, ext, maxDepth = 5) {
  /** @type {string[]} */
  const results = [];
  /**
   * @param {string} d
   * @param {number} depth
   */
  function walk(d, depth) {
    if (depth > maxDepth || !fs.existsSync(d)) return;
    const entries = fs.readdirSync(d, { withFileTypes: true });
    for (const e of entries) {
      const fp = path.join(d, e.name);
      if (e.isDirectory()) walk(fp, depth + 1);
      else if (e.name.endsWith(ext)) results.push(fp);
    }
  }
  walk(dir, 0);
  return results;
}

// ─── Core Extractors ────────────────────────────────────────

/**
 * Extract structured data from a KI's metadata.json
 */
/** @param {string} kiDir */
function extractKIMetadata(kiDir) {
  const metaFile = path.join(kiDir, 'metadata.json');
  const meta = safeReadJSON(metaFile);
  if (!meta) return null;

  return {
    title: meta.title || path.basename(kiDir),
    summary: meta.summary || '(no summary)',
    createdAt: meta.createdAt || null,
    lastModified: meta.lastModified || null,
    references: meta.references || [],
    artifactPaths: meta.artifactPaths || [],
  };
}

/**
 * Extract insights from a markdown artifact.
 */
/**
 * @param {string} artifactPath
 * @param {string} kiName
 */
function extractArtifactInsights(artifactPath, kiName) {
  const text = safeReadText(artifactPath);
  if (!text) return [];
  trace.artifactsRead++;

  const basename = path.basename(artifactPath, '.md');
  const insights = [];

  // Extract headings structure
  const headings = (text.match(/^#{1,3}\s+.+$/gm) || []).map(h => h.trim());

  // Detect bug/troubleshooting patterns
  if (text.match(/bug|troubleshoot|fix|issue|error|crash|fail/i)) {
    const bugSections = text.match(/(?:^#{1,3}\s+.*(?:bug|fix|issue|error|crash|troubleshoot).*$[\s\S]*?)(?=^#{1,3}\s|$)/gmi) || [];
    for (const section of bugSections.slice(0, 5)) {
      const titleMatch = section.match(/^#{1,3}\s+(.+)$/m);
      insights.push({
        category: 'BUG_PATTERN',
        ki: kiName,
        artifact: basename,
        title: titleMatch ? titleMatch[1].trim() : '(untitled)',
        snippet: section.substring(0, 300).trim(),
      });
      trace.insightsExtracted++;
    }
  }

  // Detect architecture decisions
  if (text.match(/architecture|design|decision|pattern|strategy/i)) {
    const patterns = text.match(/(?:^#{1,3}\s+.*(?:architecture|design|pattern|strategy|approach).*$[\s\S]*?)(?=^#{1,3}\s|$)/gmi) || [];
    for (const section of patterns.slice(0, 5)) {
      const titleMatch = section.match(/^#{1,3}\s+(.+)$/m);
      insights.push({
        category: 'ARCHITECTURE',
        ki: kiName,
        artifact: basename,
        title: titleMatch ? titleMatch[1].trim() : '(untitled)',
        snippet: section.substring(0, 300).trim(),
      });
      trace.insightsExtracted++;
    }
  }

  // Detect performance insights
  if (text.match(/performance|optimization|speed|latency|cache|batch/i)) {
    insights.push({
      category: 'PERFORMANCE',
      ki: kiName,
      artifact: basename,
      title: `Performance patterns in ${basename}`,
      snippet: '',
    });
    trace.insightsExtracted++;
  }

  // Detect SLOT-related content
  if (text.match(/\bSLOT\b|slot\s+prop|slot-based/i)) {
    insights.push({
      category: 'SLOT',
      ki: kiName,
      artifact: basename,
      title: `SLOT references in ${basename}`,
      snippet: (text.match(/.*\bSLOT\b.*/gi) || []).slice(0, 3).join('\n'),
    });
    trace.insightsExtracted++;
  }

  // Detect test results
  if (text.match(/test\s*result|validation|pass|fail|gate\s*\d/i)) {
    insights.push({
      category: 'TEST_RESULT',
      ki: kiName,
      artifact: basename,
      title: `Test results in ${basename}`,
      snippet: '',
    });
    trace.insightsExtracted++;
  }

  // Cross-KI references
  const kiRefs = text.match(/(?:see|ref|from|in)\s+(?:KI|knowledge\s+item)[:.]?\s*["'`]([^"'`]+)["'`]/gi) || [];
  for (const ref of kiRefs) {
    insights.push({
      category: 'CROSS_REFERENCE',
      ki: kiName,
      artifact: basename,
      title: `Cross-ref: ${ref.substring(0, 100)}`,
      snippet: '',
    });
    trace.insightsExtracted++;
  }

  // BP references
  const bpRefs = text.match(/BP-\d{3}/g) || [];
  if (bpRefs.length > 0) {
    insights.push({
      category: 'BP_REFERENCE',
      ki: kiName,
      artifact: basename,
      title: `BPs referenced: ${[...new Set(bpRefs)].join(', ')}`,
      snippet: '',
    });
    trace.insightsExtracted++;
  }

  return insights;
}

/**
 * Harvest a single KI directory.
 */
/** @param {string} kiDir */
function harvestKI(kiDir) {
  const kiName = path.basename(kiDir);
  trace.kisScanned++;

  const meta = extractKIMetadata(kiDir);
  const artifactDir = path.join(kiDir, 'artifacts');
  const artifacts = findFiles(artifactDir, '.md');

  log(`  📂 ${kiName}: ${artifacts.length} artifacts`);

  const insights = [];
  for (const a of artifacts) {
    const extracted = extractArtifactInsights(a, kiName);
    insights.push(...extracted);
  }

  return {
    name: kiName,
    metadata: meta,
    artifactCount: artifacts.length,
    artifactNames: artifacts.map(a => path.relative(artifactDir, a)),
    insights,
    headingMap: artifacts.reduce((/** @type {Record<string, string[]>} */ acc, a) => {
      const text = safeReadText(a);
      if (text) {
        const headings = (text.match(/^#{1,2}\s+.+$/gm) || []).map(h => h.replace(/^#+\s+/, ''));
        acc[path.basename(a, '.md')] = headings;
      }
      return acc;
    }, {}),
  };
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

  test('KI base directory exists', () => {
    if (!fs.existsSync(KI_BASE)) throw new Error(`Not found: ${KI_BASE}`);
  });

  test('Target KIs accessible', () => {
    let found = 0;
    for (const ki of TARGET_KIS) {
      if (fs.existsSync(path.join(KI_BASE, ki))) found++;
    }
    if (found === 0) throw new Error('No target KIs found');
    console.log(`    (${found}/${TARGET_KIS.length} KIs found)`);
  });

  test('extractArtifactInsights — empty string', () => {
    // Should not crash on empty
    const result = extractArtifactInsights('/nonexistent/file.md', 'test');
    if (!Array.isArray(result)) throw new Error('Expected array');
  });

  test('findFiles — nonexistent dir', () => {
    const result = findFiles('/nonexistent', '.md');
    if (result.length !== 0) throw new Error('Expected empty');
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return;

  validate();

  // Determine which KIs to scan
  let kiDirs;
  if (config.scanAll) {
    kiDirs = fs.readdirSync(KI_BASE, { withFileTypes: true })
      .filter(e => e.isDirectory())
      .map(e => path.join(KI_BASE, e.name));
  } else {
    kiDirs = TARGET_KIS
      .map(ki => path.join(KI_BASE, ki))
      .filter(d => fs.existsSync(d));
  }

  if (config.dryRun) {
    log(`🔍 DRY-RUN — Would scan ${kiDirs.length} KIs:`);
    for (const d of kiDirs) {
      const artDir = path.join(d, 'artifacts');
      const count = fs.existsSync(artDir)
        ? findFiles(artDir, '.md').length
        : 0;
      log(`  ${path.basename(d)}: ${count} artifacts`);
    }
    return;
  }

  log('━━━ Harvesting Conversation Insights ━━━\n');
  log(`  Scanning ${kiDirs.length} Knowledge Items\n`);

  const kiReports = kiDirs.map(d => harvestKI(d));

  // Aggregate insights by category
  const allInsights = kiReports.flatMap(ki => ki.insights);
  const byCategory = {};
  for (const insight of allInsights) {
    if (!byCategory[insight.category]) byCategory[insight.category] = [];
    byCategory[insight.category].push(insight);
  }

  const report = {
    scanMeta: {
      timestamp: new Date().toISOString(),
      kiBase: KI_BASE,
      kisScanned: trace.kisScanned,
      artifactsRead: trace.artifactsRead,
      totalInsights: trace.insightsExtracted,
      scriptVersion: VERSION,
    },
    kiSummaries: kiReports.map(ki => ({
      name: ki.name,
      title: ki.metadata ? ki.metadata.title : ki.name,
      summary: ki.metadata ? ki.metadata.summary.substring(0, 200) : '',
      artifactCount: ki.artifactCount,
      insightCount: ki.insights.length,
    })),
    insightsByCategory: byCategory,
    categoryCounts: Object.fromEntries(
      Object.entries(byCategory)
        .map(([k, v]) => [k, v.length])
        .sort((a, b) => b[1] - a[1])
    ),
    kiDetails: kiReports,
  };

  if (config.jsonOutput) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    fs.mkdirSync(path.dirname(config.outputPath), { recursive: true });
    fs.writeFileSync(config.outputPath, JSON.stringify(report, null, 2));
    log(`\n📄 Report written: ${config.outputPath}`);
    log(`   Size: ${(fs.statSync(config.outputPath).size / 1024).toFixed(1)} KB`);
  }

  log('\n━━━ Insight Summary ━━━');
  for (const [cat, items] of Object.entries(report.categoryCounts)) {
    log(`  ${cat}: ${items}`);
  }
}

main();

#!/usr/bin/env node
'use strict';

/**
 * ============================================================
 * Script: find-component-in-library.js
 * Purpose: Search for components in library-map.json by name
 *          with exact, fuzzy, prefix, and contains matching.
 * Author: AI-assisted (automation-scripts skill)
 * Created: 2026-03-14
 * Usage: node find-component-in-library.js <query> [options]
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
const DEFAULT_LIBRARY_MAP = path.join(PROJECT_ROOT, 'bridge/library/library-map.json');

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
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Search components in library-map.json

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js <query> [options]

${c.yellow}SEARCH MODES:${c.reset}
  (default)         Contains match (case-insensitive)
  --exact            Exact name match only
  --prefix           Starts with query
  --fuzzy            Fuzzy token matching (splits on "/" and spaces)

${c.yellow}FILTER OPTIONS:${c.reset}
  --type <type>      Filter by type: COMPONENT_SET | COMPONENT
  --exclude-pro      Exclude "Pro Blocks /..." entries
  --exclude-blocks   Exclude "Blocks /..." entries
  --base-only        Only show base components (no Pro Blocks, no Blocks)

${c.yellow}OUTPUT OPTIONS:${c.reset}
  --json             Output as JSON (for piping)
  --keys             Show only component keys (for spec patching)
  --limit <n>        Max results (default: 50)

${c.yellow}OTHER:${c.reset}
  -l, --library <path>  Custom library-map.json path
  -h, --help             Show help
  --test                 Run self-test
  --version              Show version

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js Card
  node ${SCRIPT_NAME}.js "Accordion" --base-only
  node ${SCRIPT_NAME}.js "Form / 1." --exact --keys
  node ${SCRIPT_NAME}.js Tabs --json
  node ${SCRIPT_NAME}.js Card --type COMPONENT_SET
`);
  process.exit(0);
}

// ─── Args Parsing ───────────────────────────────────────────
function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    query: '',
    mode: 'contains',       // exact | prefix | contains | fuzzy
    type: null,              // COMPONENT_SET | COMPONENT | null
    excludePro: false,
    excludeBlocks: false,
    baseOnly: false,
    json: false,
    keys: false,
    limit: 50,
    libraryPath: DEFAULT_LIBRARY_MAP,
    test: false,
  };

  if (args.length === 0) showHelp();

  let i = 0;
  while (i < args.length) {
    const arg = args[i];
    switch (arg) {
      case '-h': case '--help': showHelp(); break;
      case '--version': console.log(VERSION); process.exit(0); break;
      case '--test': config.test = true; break;
      case '--exact': config.mode = 'exact'; break;
      case '--prefix': config.mode = 'prefix'; break;
      case '--fuzzy': config.mode = 'fuzzy'; break;
      case '--type': config.type = args[++i]; break;
      case '--exclude-pro': config.excludePro = true; break;
      case '--exclude-blocks': config.excludeBlocks = true; break;
      case '--base-only': config.excludePro = true; config.excludeBlocks = true; break;
      case '--json': config.json = true; break;
      case '--keys': config.keys = true; break;
      case '--limit': config.limit = parseInt(args[++i], 10) || 50; break;
      case '-l': case '--library': config.libraryPath = args[++i]; break;
      default:
        if (arg.startsWith('-')) log.die(`Unknown option: ${arg}. Use --help.`);
        config.query = arg;
    }
    i++;
  }

  return config;
}

// ─── Validation ─────────────────────────────────────────────
/**
 * @param {any} config
 */
function validate(config) {
  if (!config.test && !config.query) {
    log.die('No search query provided. Use: node find-component-in-library.js <query>');
  }
  if (!fs.existsSync(config.libraryPath)) {
    log.die(`Library map not found: ${config.libraryPath}`);
  }
  if (config.type && !['COMPONENT_SET', 'COMPONENT'].includes(config.type)) {
    log.die(`Invalid type filter: ${config.type}. Must be COMPONENT_SET or COMPONENT.`);
  }
}

// ─── Load library-map ───────────────────────────────────────
/** @param {string} filePath */
function loadLibraryMap(filePath) {
  const startMs = Date.now();
  const raw = fs.readFileSync(filePath, 'utf8');
  const data = JSON.parse(raw);
  const components = data.components || [];
  log(`Loaded ${components.length} components from library-map (${Date.now() - startMs}ms)`);
  return { components, meta: { fileName: data.fileName, totalComponentSets: data.totalComponentSets, totalComponents: data.totalComponents } };
}

// ─── Matching Engine ────────────────────────────────────────
/**
 * @param {string} name
 * @param {string} query
 * @param {string} mode
 */
function matchComponent(name, query, mode) {
  const nameLower = name.toLowerCase();
  const queryLower = query.toLowerCase();

  switch (mode) {
    case 'exact':
      return name === query;
    case 'prefix':
      return nameLower.startsWith(queryLower);
    case 'contains':
      return nameLower.includes(queryLower);
    case 'fuzzy': {
      // Split query into tokens and check if all present in name
      const queryTokens = queryLower.split(/[\s\/]+/).filter(Boolean);
      return queryTokens.every(token => nameLower.includes(token));
    }
    default:
      return nameLower.includes(queryLower);
  }
}

/**
 * @param {string} name
 * @param {string} query
 */
function scoreMatch(name, query) {
  const nameLower = name.toLowerCase();
  const queryLower = query.toLowerCase();
  
  if (name === query) return 100;                        // exact
  if (nameLower === queryLower) return 95;               // case-insensitive exact
  if (nameLower.startsWith(queryLower + ' /')) return 90; // "Card / ..." for query "Card"
  if (nameLower.startsWith(queryLower)) return 85;       // prefix
  if (nameLower.includes(' / ' + queryLower)) return 80; // "Blocks / Card"
  
  // Length penalty — shorter names more relevant
  const lengthRatio = queryLower.length / nameLower.length;
  return Math.round(50 + lengthRatio * 30);
}

// ─── Search ─────────────────────────────────────────────────
/**
 * @param {any[]} components
 * @param {any} config
 */
function search(components, config) {
  let results = components.filter(comp => {
    // Apply filters
    if (config.excludePro && comp.name.startsWith('Pro Blocks /')) return false;
    if (config.excludeBlocks && comp.name.startsWith('Blocks /')) return false;
    if (config.type && comp.type !== config.type) return false;
    
    return matchComponent(comp.name, config.query, config.mode);
  });

  // Score and sort
  results = results.map(comp => ({
    ...comp,
    _score: scoreMatch(comp.name, config.query),
  }));
  results.sort((a, b) => b._score - a._score);

  return results.slice(0, config.limit);
}

// ─── Output ─────────────────────────────────────────────────
/**
 * @param {any[]} results
 * @param {any} config
 */
function outputResults(results, config) {
  if (config.json) {
    const output = results.map(r => ({
      name: r.name,
      nodeId: r.nodeId,
      type: r.type,
      key: r.key,
      score: r._score,
    }));
    console.log(JSON.stringify(output, null, 2));
    return;
  }

  if (config.keys) {
    results.forEach(r => console.log(`${r.name}\t${r.key}\t${r.type}`));
    return;
  }

  // Table output
  console.log('');
  console.log(`${c.bold}Search: "${config.query}" (mode: ${config.mode})${c.reset}`);
  console.log(`${'─'.repeat(90)}`);
  console.log(`${c.dim}Score${c.reset}  ${c.dim}Type${c.reset}            ${c.dim}Name${c.reset}                               ${c.dim}Key (first 16)${c.reset}       ${c.dim}NodeId${c.reset}`);
  console.log(`${'─'.repeat(90)}`);

  for (const r of results) {
    const scoreColor = r._score >= 90 ? c.green : r._score >= 70 ? c.yellow : c.dim;
    const typeLabel = r.type === 'COMPONENT_SET' ? 'SET      ' : 'COMPONENT';
    console.log(
      `${scoreColor}${String(r._score).padStart(5)}${c.reset}  ${typeLabel}  ${r.name.padEnd(40).slice(0, 40)}  ${r.key.slice(0, 16)}...  ${r.nodeId}`
    );
  }

  console.log(`${'─'.repeat(90)}`);
  console.log(`${c.cyan}Found: ${results.length} result(s)${c.reset} (limit: ${config.limit})`);
  console.log('');
}

// ─── Self-Test ──────────────────────────────────────────────
/** @param {any} config */
function selfTest(config) {
  const startMs = Date.now();
  let passed = 0;
  let failed = 0;

  const assert = (condition, label) => {
    if (condition) { passed++; log(`  ✅ ${label}`); }
    else { failed++; log.error(`  ❌ ${label}`); }
  };

  log('Running self-test...');

  // T1: Library map exists
  assert(fs.existsSync(config.libraryPath), 'Library map file exists');

  // T2: Can parse library map
  let components = [];
  try {
    const data = JSON.parse(fs.readFileSync(config.libraryPath, 'utf8'));
    components = data.components || [];
    assert(components.length > 0, `Library map has ${components.length} components`);
  } catch (e) {
    assert(false, `Library map parseable: ${e.message}`);
  }

  // T3: Exact match works
  const exactResults = components.filter(c => matchComponent(c.name, 'Tabs', 'exact'));
  assert(exactResults.length >= 1, `Exact search "Tabs" finds >= 1 (got ${exactResults.length})`);

  // T4: Contains match works  
  const containsResults = components.filter(c => matchComponent(c.name, 'card', 'contains'));
  assert(containsResults.length >= 1, `Contains search "card" finds >= 1 (got ${containsResults.length})`);

  // T5: Fuzzy match works
  const fuzzyResults = components.filter(c => matchComponent(c.name, 'form 1', 'fuzzy'));
  assert(fuzzyResults.length >= 1, `Fuzzy search "form 1" finds >= 1 (got ${fuzzyResults.length})`);

  // T6: Type filter works
  const setOnly = components.filter(c => c.type === 'COMPONENT_SET');
  assert(setOnly.length > 0 && setOnly.length < components.length, `Type filter separates SETs (${setOnly.length}) from total (${components.length})`);

  // T7: Score ordering
  const scored = [
    { name: 'Card', _score: scoreMatch('Card', 'Card') },
    { name: 'Card / Example Footer', _score: scoreMatch('Card / Example Footer', 'Card') },
    { name: 'Pro Blocks / Card / 1.', _score: scoreMatch('Pro Blocks / Card / 1.', 'Card') },
  ];
  assert(scored[0]._score > scored[1]._score, `Exact name "Card" scores higher than "Card / Example Footer"`);

  const durationMs = Date.now() - startMs;
  console.log('');
  log(`Self-test complete: ${passed} passed, ${failed} failed (${durationMs}ms)`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const startMs = Date.now();
  const config = parseArgs();
  validate(config);

  if (config.test) {
    selfTest(config);
    return;
  }

  const { components } = loadLibraryMap(config.libraryPath);
  const results = search(components, config);
  outputResults(results, config);

  log(`Search completed in ${Date.now() - startMs}ms`);
}

main();

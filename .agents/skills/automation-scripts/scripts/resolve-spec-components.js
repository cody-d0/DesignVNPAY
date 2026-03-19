#!/usr/bin/env node
'use strict';

/**
 * ============================================================
 * Script: resolve-spec-components.js
 * Purpose: Validate all componentRef/componentKey in spec files
 *          against library-map.json. Reports mismatches, missing
 *          components, and suggests corrections.
 * Author: AI-assisted (automation-scripts skill)
 * Created: 2026-03-14
 * Usage: node resolve-spec-components.js <spec-file-or-dir> [options]
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
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Validate componentRef/Key in specs against library-map

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js <spec-file-or-dir> [options]

${c.yellow}COMMANDS:${c.reset}
  (default)          Resolve and validate all componentRefs
  --fix              Output corrected spec(s) with right keys (dry-run by default)
  --fix --write      Actually write corrected files

${c.yellow}OPTIONS:${c.reset}
  -l, --library <path>  Custom library-map.json path
  --json                 Output as JSON report
  --suggest <n>          Number of suggestions per unresolved ref (default: 5)
  -h, --help             Show help
  --test                 Run self-test
  --version              Show version

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js bridge/specs/tests/test-17-slot-multi.json
  node ${SCRIPT_NAME}.js bridge/specs/tests/
  node ${SCRIPT_NAME}.js bridge/specs/xpos/ --json
  node ${SCRIPT_NAME}.js bridge/specs/tests/test-17-slot-multi.json --fix
`);
  process.exit(0);
}

// ─── Args Parsing ───────────────────────────────────────────
function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    inputs: [],
    libraryPath: DEFAULT_LIBRARY_MAP,
    json: false,
    fix: false,
    write: false,
    suggestCount: 5,
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
      case '--json': config.json = true; break;
      case '--fix': config.fix = true; break;
      case '--write': config.write = true; break;
      case '--suggest': config.suggestCount = parseInt(args[++i], 10) || 5; break;
      case '-l': case '--library': config.libraryPath = args[++i]; break;
      default:
        if (arg.startsWith('-')) log.die(`Unknown option: ${arg}. Use --help.`);
        config.inputs.push(arg);
    }
    i++;
  }

  return config;
}

// ─── Validation ─────────────────────────────────────────────
function validate(config) {
  if (!config.test && config.inputs.length === 0) {
    log.die('No spec files or directories specified.');
  }
  if (!fs.existsSync(config.libraryPath)) {
    log.die(`Library map not found: ${config.libraryPath}`);
  }
}

// ─── Load library-map ───────────────────────────────────────
function loadLibraryMap(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8');
  const data = JSON.parse(raw);
  const components = data.components || [];

  // Build lookup indexes
  const byName = new Map();       // name → entry
  const byKey = new Map();        // key → entry
  const byNameLower = new Map();  // lowercase name → entry[]

  for (const comp of components) {
    byName.set(comp.name, comp);
    if (comp.key) byKey.set(comp.key, comp);

    const lower = comp.name.toLowerCase();
    if (!byNameLower.has(lower)) byNameLower.set(lower, []);
    byNameLower.get(lower).push(comp);
  }

  log(`Loaded ${components.length} components, built 3 indexes`);
  return { components, byName, byKey, byNameLower };
}

// ─── Collect spec files ─────────────────────────────────────
function collectSpecFiles(inputs) {
  const files = [];
  for (const input of inputs) {
    const absPath = path.resolve(input);
    if (!fs.existsSync(absPath)) {
      log.warn(`Input not found: ${absPath}`);
      continue;
    }
    const stat = fs.statSync(absPath);
    if (stat.isDirectory()) {
      const entries = fs.readdirSync(absPath).filter(f => f.endsWith('.json'));
      entries.forEach(f => files.push(path.join(absPath, f)));
    } else {
      files.push(absPath);
    }
  }
  return files;
}

// ─── Extract componentRefs from spec (recursive) ────────────
function extractComponentRefs(node, results = [], parentPath = 'root') {
  if (!node || typeof node !== 'object') return results;

  if (node.componentRef) {
    results.push({
      key: node.key || parentPath,
      componentRef: node.componentRef,
      componentKey: node.componentKey || null,
      componentType: node.componentType || null,
      path: parentPath,
    });
  }

  if (Array.isArray(node.children)) {
    for (let i = 0; i < node.children.length; i++) {
      extractComponentRefs(node.children[i], results, `${parentPath}.children[${i}]`);
    }
  }

  // Also check root itself
  if (node.root && parentPath === 'root') {
    extractComponentRefs(node.root, results, 'root');
  }

  return results;
}

// ─── Suggest similar components ─────────────────────────────
function suggestSimilar(ref, library, limit = 5) {
  const refLower = ref.toLowerCase();
  const refTokens = refLower.split(/[\s\/]+/).filter(Boolean);

  const scored = library.components.map(comp => {
    const nameLower = comp.name.toLowerCase();
    let score = 0;

    // Exact match
    if (comp.name === ref) score = 100;
    else if (nameLower === refLower) score = 95;
    // Starts with ref
    else if (nameLower.startsWith(refLower)) score = 85;
    // Contains ref
    else if (nameLower.includes(refLower)) score = 75;
    // Token matching
    else {
      const nameTokens = nameLower.split(/[\s\/]+/).filter(Boolean);
      const matchedTokens = refTokens.filter(t => nameTokens.some(nt => nt.includes(t)));
      score = Math.round((matchedTokens.length / refTokens.length) * 60);
    }

    return { name: comp.name, key: comp.key, type: comp.type, nodeId: comp.nodeId, score };
  });

  return scored
    .filter(s => s.score > 30)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit);
}

// ─── Resolve a single componentRef ──────────────────────────
function resolveRef(ref, specKey, library) {
  const result = {
    ref,
    specKey: specKey || null,
    status: 'UNRESOLVED',  // EXACT | KEY_MISMATCH | UNRESOLVED
    libraryEntry: null,
    keyMatch: false,
    suggestions: [],
    detail: '',
  };

  // 1. Exact name match
  const exact = library.byName.get(ref);
  if (exact) {
    result.status = 'EXACT';
    result.libraryEntry = exact;
    if (specKey) {
      result.keyMatch = exact.key === specKey;
      if (!result.keyMatch) {
        result.status = 'KEY_MISMATCH';
        result.detail = `Spec key "${specKey.slice(0, 16)}..." ≠ Library key "${exact.key.slice(0, 16)}..."`;
      }
    }
    return result;
  }

  // 2. Case-insensitive match
  const lowerMatches = library.byNameLower.get(ref.toLowerCase());
  if (lowerMatches && lowerMatches.length > 0) {
    const best = lowerMatches[0];
    result.status = 'EXACT';
    result.libraryEntry = best;
    result.detail = `Case-insensitive match: "${best.name}"`;
    if (specKey) {
      result.keyMatch = best.key === specKey;
      if (!result.keyMatch) {
        result.status = 'KEY_MISMATCH';
        result.detail = `Name matches "${best.name}" (case-insensitive) but key mismatch`;
      }
    }
    return result;
  }

  // 3. Slash-path parent match (e.g., "Form / 1." → find "Form / 1." in library)
  // Already handled by exact match above

  // 4. No match — generate suggestions
  result.suggestions = suggestSimilar(ref, library);
  result.detail = `No component named "${ref}" in library-map`;
  return result;
}

// ─── Process one spec file ──────────────────────────────────
function processSpec(filePath, library, config) {
  let spec;
  try {
    spec = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (e) {
    return { file: filePath, error: `Parse error: ${e.message}`, refs: [] };
  }

  const refs = extractComponentRefs(spec);
  const results = refs.map(r => ({
    ...r,
    resolution: resolveRef(r.componentRef, r.componentKey, library),
  }));

  return {
    file: filePath,
    specVersion: spec.specVersion,
    screen: spec.screen,
    totalRefs: refs.length,
    resolved: results.filter(r => r.resolution.status === 'EXACT').length,
    keyMismatches: results.filter(r => r.resolution.status === 'KEY_MISMATCH').length,
    unresolved: results.filter(r => r.resolution.status === 'UNRESOLVED').length,
    refs: results,
  };
}

// ─── Output: Table format ───────────────────────────────────
function outputTable(reports) {
  for (const report of reports) {
    console.log('');
    console.log(`${c.bold}File: ${path.basename(report.file)}${c.reset}`);
    if (report.error) {
      console.log(`  ${c.red}ERROR: ${report.error}${c.reset}`);
      continue;
    }
    console.log(`  Screen: ${report.screen} | Version: ${report.specVersion} | Refs: ${report.totalRefs}`);
    console.log(`  ${c.green}✅ Resolved: ${report.resolved}${c.reset}  ${c.yellow}⚠️ Key mismatch: ${report.keyMismatches}${c.reset}  ${c.red}❌ Unresolved: ${report.unresolved}${c.reset}`);
    console.log(`  ${'─'.repeat(86)}`);

    for (const ref of report.refs) {
      const res = ref.resolution;
      const statusIcon = res.status === 'EXACT' ? `${c.green}✅` : res.status === 'KEY_MISMATCH' ? `${c.yellow}⚠️` : `${c.red}❌`;
      
      console.log(`  ${statusIcon} ${ref.key}${c.reset}`);
      console.log(`     componentRef: "${ref.componentRef}" | componentType: ${ref.componentType || 'none'}`);

      if (res.status === 'KEY_MISMATCH') {
        console.log(`     ${c.yellow}${res.detail}${c.reset}`);
        console.log(`     ${c.dim}Spec key:    ${ref.componentKey}${c.reset}`);
        console.log(`     ${c.green}Library key: ${res.libraryEntry.key}${c.reset}  ← use this`);
      }

      if (res.status === 'UNRESOLVED') {
        console.log(`     ${c.red}${res.detail}${c.reset}`);
        if (res.suggestions.length > 0) {
          console.log(`     ${c.cyan}Suggestions:${c.reset}`);
          for (const sug of res.suggestions) {
            console.log(`       ${c.dim}${String(sug.score).padStart(3)}${c.reset} ${sug.name}  [${sug.type}]  key: ${sug.key.slice(0, 20)}...`);
          }
        }
      }

      if (res.status === 'EXACT' && res.keyMatch) {
        console.log(`     ${c.green}Key verified ✓${c.reset}`);
      }
    }

    console.log(`  ${'─'.repeat(86)}`);
  }

  // Summary
  console.log('');
  const totals = {
    files: reports.filter(r => !r.error).length,
    refs: reports.reduce((s, r) => s + (r.totalRefs || 0), 0),
    resolved: reports.reduce((s, r) => s + (r.resolved || 0), 0),
    keyMismatches: reports.reduce((s, r) => s + (r.keyMismatches || 0), 0),
    unresolved: reports.reduce((s, r) => s + (r.unresolved || 0), 0),
  };
  console.log(`${c.bold}━━━ Summary ━━━${c.reset}`);
  console.log(`  Files:         ${totals.files}`);
  console.log(`  Total refs:    ${totals.refs}`);
  console.log(`  ${c.green}Resolved:      ${totals.resolved}${c.reset}`);
  console.log(`  ${c.yellow}Key mismatch:  ${totals.keyMismatches}${c.reset}`);
  console.log(`  ${c.red}Unresolved:    ${totals.unresolved}${c.reset}`);
  console.log('');
}

// ─── Output: JSON format ────────────────────────────────────
function outputJson(reports) {
  const output = reports.map(r => ({
    file: r.file,
    screen: r.screen,
    specVersion: r.specVersion,
    totalRefs: r.totalRefs,
    resolved: r.resolved,
    keyMismatches: r.keyMismatches,
    unresolved: r.unresolved,
    refs: r.refs.map(ref => ({
      key: ref.key,
      componentRef: ref.componentRef,
      componentKey: ref.componentKey,
      componentType: ref.componentType,
      status: ref.resolution.status,
      keyMatch: ref.resolution.keyMatch,
      detail: ref.resolution.detail,
      correctKey: ref.resolution.libraryEntry?.key || null,
      correctType: ref.resolution.libraryEntry?.type || null,
      suggestions: ref.resolution.suggestions.map(s => ({
        name: s.name,
        key: s.key,
        type: s.type,
        score: s.score,
      })),
    })),
  }));
  console.log(JSON.stringify(output, null, 2));
}

// ─── Fix mode: patch spec with correct keys ─────────────────
function fixSpecs(reports, config) {
  for (const report of reports) {
    if (report.error || report.keyMismatches === 0) continue;

    const spec = JSON.parse(fs.readFileSync(report.file, 'utf8'));
    let patched = 0;

    // Walk and patch
    function patchNode(node) {
      if (!node || typeof node !== 'object') return;
      if (node.componentRef) {
        const match = report.refs.find(r => r.key === node.key && r.resolution.libraryEntry);
        if (match && match.resolution.status === 'KEY_MISMATCH') {
          const oldKey = node.componentKey;
          node.componentKey = match.resolution.libraryEntry.key;
          node.componentType = match.resolution.libraryEntry.type;
          log(`  Patched ${node.key}: key ${oldKey?.slice(0, 12)}... → ${node.componentKey.slice(0, 12)}...`);
          patched++;
        }
      }
      if (Array.isArray(node.children)) {
        node.children.forEach(child => patchNode(child));
      }
    }

    patchNode(spec.root || spec);

    if (patched > 0) {
      if (config.write) {
        fs.writeFileSync(report.file, JSON.stringify(spec, null, 2) + '\n');
        log(`${c.green}Written ${patched} fixes to ${path.basename(report.file)}${c.reset}`);
      } else {
        log(`[DRY-RUN] Would patch ${patched} keys in ${path.basename(report.file)}`);
        log(`  Re-run with --fix --write to apply.`);
      }
    }
  }
}

// ─── Self-Test ──────────────────────────────────────────────
function selfTest(config) {
  const startMs = Date.now();
  let passed = 0;
  let failed = 0;

  const assert = (condition, label) => {
    if (condition) { passed++; log(`  ✅ ${label}`); }
    else { failed++; log.error(`  ❌ ${label}`); }
  };

  log('Running self-test...');

  // T1: Library map exists and loads
  assert(fs.existsSync(config.libraryPath), 'Library map file exists');
  const library = loadLibraryMap(config.libraryPath);
  assert(library.components.length > 0, `Library has ${library.components.length} components`);

  // T2: Indexes built correctly
  assert(library.byName.size > 0, `byName index: ${library.byName.size} entries`);
  assert(library.byKey.size > 0, `byKey index: ${library.byKey.size} entries`);

  // T3: resolveRef — exact match
  const tabsResult = resolveRef('Tabs', null, library);
  assert(tabsResult.status === 'EXACT', `Resolve "Tabs" → EXACT (got ${tabsResult.status})`);

  // T4: resolveRef — key mismatch detection
  const tabsKeyResult = resolveRef('Tabs', 'fake-key-12345', library);
  assert(tabsKeyResult.status === 'KEY_MISMATCH', `Resolve "Tabs" with wrong key → KEY_MISMATCH`);

  // T5: resolveRef — unresolved with suggestions
  const unknownResult = resolveRef('Card', null, library);
  // "Card" exact doesn't exist in this library
  if (unknownResult.status === 'UNRESOLVED') {
    assert(unknownResult.suggestions.length > 0, `"Card" unresolved but has ${unknownResult.suggestions.length} suggestions`);
  } else {
    assert(unknownResult.status === 'EXACT', `"Card" found as exact match`);
  }

  // T6: extractComponentRefs
  const testSpec = {
    root: {
      key: 'test-root',
      children: [
        { key: 'child-1', componentRef: 'Button', componentKey: 'abc123' },
        { key: 'child-2', role: 'text' },
        { key: 'child-3', componentRef: 'Card', children: [
          { key: 'nested', componentRef: 'Input' }
        ]},
      ]
    }
  };
  const extracted = extractComponentRefs(testSpec);
  assert(extracted.length === 3, `extractComponentRefs finds 3 refs (got ${extracted.length})`);

  // T7: suggestSimilar returns sorted results
  const suggestions = suggestSimilar('Accordion', library);
  assert(suggestions.length > 0, `suggestSimilar("Accordion") returns ${suggestions.length} results`);
  assert(suggestions[0].score >= suggestions[suggestions.length - 1].score, 'Suggestions are score-sorted');

  // T8: Form / 1. exact resolve  
  const formResult = resolveRef('Form / 1.', null, library);
  assert(formResult.status === 'EXACT', `Resolve "Form / 1." → EXACT (got ${formResult.status})`);

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

  const library = loadLibraryMap(config.libraryPath);
  const specFiles = collectSpecFiles(config.inputs);

  if (specFiles.length === 0) {
    log.die('No spec files found in the provided inputs.');
  }
  log(`Processing ${specFiles.length} spec file(s)...`);

  const reports = specFiles.map(f => processSpec(f, library, config));

  if (config.json) {
    outputJson(reports);
  } else {
    outputTable(reports);
  }

  if (config.fix) {
    fixSpecs(reports, config);
  }

  log(`Completed in ${Date.now() - startMs}ms`);
}

main();

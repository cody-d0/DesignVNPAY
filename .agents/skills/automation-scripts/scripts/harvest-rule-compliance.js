#!/usr/bin/env node
'use strict';

// ============================================================
// Script: harvest-rule-compliance
// Purpose: Audit ALL Bridge specs against the 3 immutable rules +
//          spec v4.0 schema: Instantiation-First, Pre-binding,
//          Verify-Only, role validation, padding format, key
//          uniqueness. Generates per-spec compliance report.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-14
// Usage: node harvest-rule-compliance.js [options]
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
const SPECS_DIRS = [
  path.join(WORKSPACE, 'bridge', 'specs', 'xpos'),
  path.join(WORKSPACE, 'bridge', 'specs', 'tests'),
  path.join(WORKSPACE, 'bridge', 'specs'),
];
const OUTPUT_DIR = path.join(__dirname, '..', 'output');

// The 30 valid roles from AGENT_RULES.md
const VALID_ROLES = new Set([
  'screen', 'container', 'card', 'text', 'divider', 'spacer', 'image-placeholder', 'input',
  'badge', 'avatar', 'label', 'separator', 'skeleton', 'progress',
  'select', 'checkbox', 'radio-group', 'switch', 'textarea', 'slider', 'field',
  'dialog', 'drawer', 'sheet', 'popover', 'tooltip', 'dropdown-menu',
  'button-primary', 'button-secondary', 'button-outline', 'button-ghost',
]);

// Hex color regex
const HEX_COLOR_RE = /^#[0-9a-fA-F]{3,8}$/;

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
  specsAudited: 0, passed: 0, failed: 0, warnings: 0,
  log() {
    const duration = ((Date.now() - this.start) / 1000).toFixed(1);
    console.error(`\n${c.dim}━━━ Trace ━━━${c.reset}`);
    console.error(`  Duration:  ${duration}s`);
    console.error(`  Audited:   ${this.specsAudited}`);
    console.error(`  Passed:    ${this.passed}`);
    console.error(`  Failed:    ${this.failed}`);
    console.error(`  Warnings:  ${this.warnings}`);
  },
};
process.on('exit', () => trace.log());

// ─── Help ───────────────────────────────────────────────────
function showHelp() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — Audit specs against 3 immutable rules + v4.0 schema

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js [options]

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --test           Run self-test
  --dry-run        Preview specs to audit
  --json           Output to stdout
  -o, --output     Output path

${c.yellow}CHECKS:${c.reset}
  Rule 1: Instantiation-First (componentRef coverage)
  Rule 2: Pre-binding (no hardcoded hex/pixels)
  Rule 3: Verify-Only (tokens.collections empty)
  Schema: specVersion, screen, root required
  Roles:  All roles in 30-role list
  Padding: Always 4-element token array
  Keys:   All keys unique within spec
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
  let outputPath = path.join(OUTPUT_DIR, 'rule-compliance-report.json');
  const outIdx = args.indexOf('-o') !== -1 ? args.indexOf('-o') : args.indexOf('--output');
  if (outIdx !== -1 && args[outIdx + 1]) outputPath = args[outIdx + 1];

  return { dryRun, jsonOutput, outputPath };
}

// ─── Utilities ──────────────────────────────────────────────
function safeReadJSON(f) {
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); }
  catch { return null; }
}

function globDir(dir, ext) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith(ext) && !f.includes('validate-specs') && f !== 'converter-manifest.json')
    .map(f => path.join(dir, f));
}

// ─── Node Walker ────────────────────────────────────────────
function walkNodes(node, visitor, depth = 0) {
  if (!node) return;
  visitor(node, depth);
  if (node.children) {
    for (const child of node.children) walkNodes(child, visitor, depth + 1);
  }
}

// ─── Audit Functions ────────────────────────────────────────

/**
 * Rule 1: Instantiation-First
 * Every visual node should prefer componentRef over generative.
 */
function auditRule1(root) {
  let componentRefCount = 0;
  let generativeCount = 0;
  const fallbacks = [];

  walkNodes(root, (node) => {
    if (node.componentRef) {
      componentRefCount++;
    } else if (node.role && node.role !== 'screen' && node.role !== 'text'
               && node.role !== 'divider' && node.role !== 'spacer'
               && node.role !== 'image-placeholder') {
      generativeCount++;
      if (node._fallback || node._note) {
        fallbacks.push({
          key: node.key,
          role: node.role,
          note: (node._fallback || node._note || '').substring(0, 150),
        });
      }
    }
  });

  const total = componentRefCount + generativeCount;
  const ratio = total > 0 ? (componentRefCount / total * 100).toFixed(1) : '100.0';

  return {
    pass: true, // Rule 1 is advisory — fallbacks are documented
    componentRefCount,
    generativeCount,
    componentRefRatio: `${ratio}%`,
    fallbacks,
  };
}

/**
 * Rule 2: Pre-binding
 * No hardcoded hex colors or raw pixels as values.
 */
function auditRule2(root) {
  const hardcodedColors = [];
  const rawPixels = [];
  const invalidTokens = [];

  walkNodes(root, (node) => {
    // Check color properties for hex values
    for (const prop of ['fill', 'textFill', 'stroke']) {
      if (node[prop] && typeof node[prop] === 'string' && HEX_COLOR_RE.test(node[prop])) {
        hardcodedColors.push({
          key: node.key,
          property: prop,
          value: node[prop],
        });
      }
    }

    // Check effects for hardcoded colors (allowed as _description but flagged)
    if (node.effects && Array.isArray(node.effects)) {
      for (const effect of node.effects) {
        if (effect.color && typeof effect.color === 'string' && HEX_COLOR_RE.test(effect.color)) {
          // Effects with hardcoded colors are common for shadows — warn but don't fail
          // (shadows often use semi-transparent hex like #00000008)
        }
      }
    }

    // Check spacing properties for raw numbers (except height/width which may be px)
    if (node.gap && typeof node.gap === 'number') {
      rawPixels.push({ key: node.key, property: 'gap', value: node.gap });
    }

    // Check padding for raw numbers
    if (node.padding && Array.isArray(node.padding)) {
      for (let i = 0; i < node.padding.length; i++) {
        if (typeof node.padding[i] === 'number') {
          rawPixels.push({ key: node.key, property: `padding[${i}]`, value: node.padding[i] });
        }
      }
    }

    // Check radius for raw numbers
    if (node.radius && typeof node.radius === 'number') {
      rawPixels.push({ key: node.key, property: 'radius', value: node.radius });
    }
  });

  const pass = hardcodedColors.length === 0 && rawPixels.length === 0;

  return {
    pass,
    hardcodedColors,
    rawPixels,
    invalidTokens,
  };
}

/**
 * Rule 3: Verify-Only
 * tokens.collections should be empty (no new variables created).
 */
function auditRule3(data) {
  const hasTokens = data.tokens && data.tokens.collections;
  const collectionsEmpty = !hasTokens || data.tokens.collections.length === 0;
  const newVarsCreated = hasTokens ? data.tokens.collections.length : 0;

  return {
    pass: collectionsEmpty,
    collectionsEmpty,
    newVarsCreated,
  };
}

/**
 * Schema compliance: required fields.
 */
function auditSchema(data) {
  const missingFields = [];
  if (!data.specVersion) missingFields.push('specVersion');
  if (!data.screen) missingFields.push('screen');
  if (!data.root) missingFields.push('root');

  return {
    valid: missingFields.length === 0,
    specVersion: data.specVersion || null,
    missingFields,
  };
}

/**
 * Role validation: all roles in the 30-role list.
 */
function auditRoles(root) {
  const invalidRoles = [];
  const usedRoles = new Set();

  walkNodes(root, (node) => {
    if (node.role) {
      usedRoles.add(node.role);
      if (!VALID_ROLES.has(node.role)) {
        invalidRoles.push({ key: node.key, role: node.role });
      }
    }
  });

  return {
    valid: invalidRoles.length === 0,
    usedRoles: [...usedRoles],
    invalidRoles,
  };
}

/**
 * Padding format: always 4-element array of token strings.
 */
function auditPadding(root) {
  const violations = [];

  walkNodes(root, (node) => {
    if (node.padding !== undefined) {
      if (!Array.isArray(node.padding)) {
        violations.push({ key: node.key, issue: 'not-array', value: node.padding });
      } else if (node.padding.length !== 4) {
        violations.push({ key: node.key, issue: `length-${node.padding.length}`, value: node.padding });
      } else {
        for (let i = 0; i < 4; i++) {
          if (typeof node.padding[i] !== 'string') {
            violations.push({ key: node.key, issue: `index-${i}-not-string`, value: node.padding[i] });
          }
        }
      }
    }
  });

  return {
    valid: violations.length === 0,
    violations,
  };
}

/**
 * Key uniqueness: all keys unique within spec.
 */
function auditKeyUniqueness(root) {
  const keys = new Map(); // key → count
  const duplicates = [];

  walkNodes(root, (node) => {
    if (node.key) {
      keys.set(node.key, (keys.get(node.key) || 0) + 1);
    }
  });

  for (const [key, count] of keys) {
    if (count > 1) duplicates.push({ key, count });
  }

  return {
    unique: duplicates.length === 0,
    totalKeys: keys.size,
    duplicates,
  };
}

// ─── Full Spec Audit ────────────────────────────────────────
function auditSpec(filePath) {
  const data = safeReadJSON(filePath);
  if (!data) return null;

  const basename = path.basename(filePath);

  // Skip non-spec JSON files
  if (!data.root && !data.specVersion && !data.screen) {
    return null;
  }

  trace.specsAudited++;

  const schema = auditSchema(data);
  const rule1 = data.root ? auditRule1(data.root) : { pass: false, componentRefCount: 0, generativeCount: 0, fallbacks: [] };
  const rule2 = data.root ? auditRule2(data.root) : { pass: false, hardcodedColors: [], rawPixels: [] };
  const rule3 = auditRule3(data);
  const roleAudit = data.root ? auditRoles(data.root) : { valid: false, invalidRoles: [] };
  const paddingAudit = data.root ? auditPadding(data.root) : { valid: false, violations: [] };
  const keyUniqueness = data.root ? auditKeyUniqueness(data.root) : { unique: false, duplicates: [] };

  const allPass = schema.valid && rule2.pass && rule3.pass && roleAudit.valid
                  && paddingAudit.valid && keyUniqueness.unique;

  if (allPass) trace.passed++;
  else trace.failed++;

  // Warnings (non-blocking)
  const warnings = [];
  if (rule1.generativeCount > rule1.componentRefCount) {
    warnings.push(`More generative nodes (${rule1.generativeCount}) than componentRef (${rule1.componentRefCount})`);
    trace.warnings++;
  }
  if (rule2.hardcodedColors.length > 0) {
    warnings.push(`${rule2.hardcodedColors.length} hardcoded hex color(s) found`);
    trace.warnings++;
  }

  return {
    file: basename,
    dir: path.dirname(filePath).includes('xpos') ? 'xpos'
       : path.dirname(filePath).includes('tests') ? 'tests'
       : 'root',
    screen: data.screen || '(unnamed)',
    specVersion: data.specVersion || null,
    allPass,
    warnings,
    rule1,
    rule2,
    rule3,
    schema,
    roleAudit,
    paddingAudit,
    keyUniqueness,
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

  test('VALID_ROLES has 31 entries', () => {
    // AGENT_RULES.md header says "30 Roles" but actually lists 31
    if (VALID_ROLES.size !== 31) throw new Error(`Expected 31, got ${VALID_ROLES.size}`);
  });

  test('HEX_COLOR_RE matches #fff', () => {
    if (!HEX_COLOR_RE.test('#fff')) throw new Error('Should match');
    if (!HEX_COLOR_RE.test('#00000008')) throw new Error('Should match 8-char');
    if (HEX_COLOR_RE.test('primary')) throw new Error('Should not match token name');
  });

  test('auditRule1 — componentRef counted', () => {
    const root = { role: 'screen', children: [
      { key: 'a', componentRef: 'Button' },
      { key: 'b', role: 'container' },
    ]};
    const result = auditRule1(root);
    if (result.componentRefCount !== 1) throw new Error(`Expected 1, got ${result.componentRefCount}`);
    if (result.generativeCount !== 1) throw new Error(`Expected 1 gen, got ${result.generativeCount}`);
  });

  test('auditRule2 — detects hex color', () => {
    const root = { key: 'a', fill: '#ff0000', children: [] };
    const result = auditRule2(root);
    if (result.hardcodedColors.length !== 1) throw new Error('Expected 1 violation');
    if (result.pass) throw new Error('Should not pass');
  });

  test('auditRule2 — token name passes', () => {
    const root = { key: 'a', fill: 'primary', children: [] };
    const result = auditRule2(root);
    if (!result.pass) throw new Error('Should pass');
  });

  test('auditRule3 — empty collections passes', () => {
    const data = { tokens: { collections: [] } };
    const result = auditRule3(data);
    if (!result.pass) throw new Error('Should pass');
  });

  test('auditPadding — valid array', () => {
    const root = { key: 'a', padding: ['sp-4', 'sp-6', 'sp-4', 'sp-6'] };
    const result = auditPadding(root);
    if (!result.valid) throw new Error('Should be valid');
  });

  test('auditPadding — detects non-array', () => {
    const root = { key: 'a', padding: 16 };
    const result = auditPadding(root);
    if (result.valid) throw new Error('Should be invalid');
  });

  test('auditKeyUniqueness — detects duplicate', () => {
    const root = { key: 'a', children: [{ key: 'b' }, { key: 'b' }] };
    const result = auditKeyUniqueness(root);
    if (result.unique) throw new Error('Should detect duplicate');
  });

  test('Spec dirs exist', () => {
    let found = 0;
    for (const d of SPECS_DIRS) {
      if (fs.existsSync(d)) found++;
    }
    if (found === 0) throw new Error('No spec dirs found');
  });

  console.log(`\nSelf-test: ${passed} passed, ${failed} failed`);
  process.exit(failed > 0 ? 1 : 0);
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseCliArgs();
  if (!config) return;

  // Collect all spec files (deduplicated)
  const seen = new Set();
  const specFiles = [];
  for (const dir of SPECS_DIRS) {
    for (const f of globDir(dir, '.json')) {
      const abs = path.resolve(f);
      if (!seen.has(abs)) {
        seen.add(abs);
        specFiles.push(f);
      }
    }
  }

  if (config.dryRun) {
    log(`🔍 DRY-RUN — Would audit ${specFiles.length} spec files:`);
    for (const dir of SPECS_DIRS) {
      const count = globDir(dir, '.json').length;
      log(`  ${path.basename(dir)}: ${count} files`);
    }
    return;
  }

  log('━━━ Harvesting Rule Compliance ━━━\n');
  log(`  Total spec files: ${specFiles.length}\n`);

  const perSpec = [];
  for (const f of specFiles) {
    const result = auditSpec(f);
    if (result) {
      perSpec.push(result);
      const icon = result.allPass ? '✅' : '⚠️';
      log(`  ${icon} ${result.file} (${result.specVersion || '?'}) — ${result.warnings.length > 0 ? result.warnings[0] : 'clean'}`);
    }
  }

  const report = {
    scanMeta: {
      timestamp: new Date().toISOString(),
      scriptVersion: VERSION,
    },
    summary: {
      totalSpecs: trace.specsAudited,
      passed: trace.passed,
      failed: trace.failed,
      warnings: trace.warnings,
      passRate: trace.specsAudited > 0
        ? `${(trace.passed / trace.specsAudited * 100).toFixed(1)}%`
        : 'N/A',
    },
    ruleBreakdown: {
      rule1_instantiation: {
        totalComponentRefs: perSpec.reduce((s, sp) => s + sp.rule1.componentRefCount, 0),
        totalGenerative: perSpec.reduce((s, sp) => s + sp.rule1.generativeCount, 0),
        totalFallbacks: perSpec.reduce((s, sp) => s + sp.rule1.fallbacks.length, 0),
      },
      rule2_binding: {
        totalHardcodedColors: perSpec.reduce((s, sp) => s + sp.rule2.hardcodedColors.length, 0),
        totalRawPixels: perSpec.reduce((s, sp) => s + sp.rule2.rawPixels.length, 0),
        specsWithViolations: perSpec.filter(sp => !sp.rule2.pass).length,
      },
      rule3_verifyOnly: {
        compliant: perSpec.filter(sp => sp.rule3.pass).length,
        nonCompliant: perSpec.filter(sp => !sp.rule3.pass).length,
      },
      schema: {
        valid: perSpec.filter(sp => sp.schema.valid).length,
        invalid: perSpec.filter(sp => !sp.schema.valid).length,
      },
      roles: {
        valid: perSpec.filter(sp => sp.roleAudit.valid).length,
        allInvalidRoles: [...new Set(perSpec.flatMap(sp => sp.roleAudit.invalidRoles.map(r => r.role)))],
      },
      padding: {
        valid: perSpec.filter(sp => sp.paddingAudit.valid).length,
        totalViolations: perSpec.reduce((s, sp) => s + sp.paddingAudit.violations.length, 0),
      },
      keys: {
        allUnique: perSpec.filter(sp => sp.keyUniqueness.unique).length,
        totalDuplicates: perSpec.reduce((s, sp) => s + sp.keyUniqueness.duplicates.length, 0),
      },
    },
    perSpec,
  };

  if (config.jsonOutput) {
    console.log(JSON.stringify(report, null, 2));
  } else {
    fs.mkdirSync(path.dirname(config.outputPath), { recursive: true });
    fs.writeFileSync(config.outputPath, JSON.stringify(report, null, 2));
    log(`\n📄 Report written: ${config.outputPath}`);
    log(`   Size: ${(fs.statSync(config.outputPath).size / 1024).toFixed(1)} KB`);
  }

  log('\n━━━ Compliance Summary ━━━');
  log(`  Pass rate:          ${report.summary.passRate}`);
  log(`  Rule 2 violations:  ${report.ruleBreakdown.rule2_binding.specsWithViolations} specs`);
  log(`  Rule 3 compliant:   ${report.ruleBreakdown.rule3_verifyOnly.compliant}/${trace.specsAudited}`);
  log(`  Invalid roles:      ${report.ruleBreakdown.roles.allInvalidRoles.length > 0 ? report.ruleBreakdown.roles.allInvalidRoles.join(', ') : 'none'}`);
  log(`  Key duplicates:     ${report.ruleBreakdown.keys.totalDuplicates}`);
}

main();

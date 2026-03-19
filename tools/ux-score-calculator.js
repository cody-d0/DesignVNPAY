#!/usr/bin/env node
// @ts-check
'use strict';

/**
 * ============================================================
 * Script: ux-score-calculator.js
 * Purpose: Parse ux-review-report.md, verify counts, calculate
 *          accurate UX score with breakdown per screen.
 * Author: AI-assisted (automation-scripts skill)
 * Created: 2026-03-17
 * Usage: node ux-score-calculator.js run <report.md> [--fix]
 * Dependencies: none (Node.js built-in only)
 * Quality-grade: A
 * ============================================================
 */

const fs = require('fs');
const path = require('path');

// ─── Configuration ──────────────────────────────────────────
const SCRIPT_NAME = path.basename(__filename, '.js');
const VERSION = '1.0.0';

// Severity weights for UX score
const SEVERITY_WEIGHTS = {
  Critical: 3.0,
  Major:    2.0,
  Minor:    1.0,
};

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
function usage() {
  console.log(`
${c.cyan}${SCRIPT_NAME}${c.reset} v${VERSION} — UX Review Report Score Calculator

${c.yellow}USAGE:${c.reset}
  node ${SCRIPT_NAME}.js <command> [options] <report.md>

${c.yellow}COMMANDS:${c.reset}
  run       Parse report, calculate score, output metrics
  check     Validate report structure only
  test      Run self-test with inline sample data

${c.yellow}OPTIONS:${c.reset}
  -h, --help       Show this help
  -v, --version    Show version
  --fix            Write corrected counts/scores back to report
  --json           Output metrics as JSON to stdout
  --verbose        Show detailed per-check breakdown

${c.yellow}EXAMPLES:${c.reset}
  node ${SCRIPT_NAME}.js run ux-review-report.md
  node ${SCRIPT_NAME}.js run --json --fix ux-review-report.md
  node ${SCRIPT_NAME}.js test

${c.yellow}SCORING MODEL:${c.reset}
  Simple Score     = pass / total_checks × 100
  Weighted Score   = (1 - weighted_gap_penalty / max_possible_penalty) × 100
    Critical gap   = 3.0 penalty
    Major gap      = 2.0 penalty
    Minor gap      = 1.0 penalty
    Unverifiable   = excluded from penalty (no penalty, no credit)
`);
  process.exit(0);
}

// ─── Args ───────────────────────────────────────────────────
function parseArgs() {
  const args = process.argv.slice(2);
  if (args.length === 0 || args.includes('-h') || args.includes('--help')) usage();
  if (args.includes('-v') || args.includes('--version')) { console.log(VERSION); process.exit(0); }

  const flags = {
    fix: args.includes('--fix'),
    json: args.includes('--json'),
    verbose: args.includes('--verbose'),
  };

  const positionals = args.filter(a => !a.startsWith('-'));
  const command = positionals[0];
  const inputs = positionals.slice(1);

  if (!['run', 'check', 'test'].includes(command)) {
    log.die(`Unknown command: ${command}. Use --help.`);
  }

  return { command, inputs, ...flags };
}

// ─── Core Parsing ───────────────────────────────────────────

/**
 * Parse the "Chi tiết theo màn hình" section to extract per-screen checks.
 * Returns an array of screen objects, each with checks array.
 */
function parseScreenSections(content) {
  const screens = [];

  // Support BOTH formats:
  // Old: ### N. Screen Name (`screen-id`)
  // New: ### N. Display Name Việt (no backtick)
  //      > `screen-id` · type · N artboards
  const screenRegex = /^### (\d+)\.\s+(.+?)$/gm;
  const scoreLineRegex = /^\*\*Score:\s*(\d+)%\s*\|\s*Pass:\s*(\d+)\s*\|\s*Gap:\s*(\d+)/m;
  const tableRowRegex = /^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|$/gm;

  let match;
  const headerPositions = [];
  while ((match = screenRegex.exec(content)) !== null) {
    let rawName = match[2].trim();
    let screen_id = null;

    // Try old format: name ends with (`screen-id`)
    const oldMatch = rawName.match(/^(.+?)\s+\(`([^`]+)`\)$/);
    if (oldMatch) {
      rawName = oldMatch[1].trim();
      screen_id = oldMatch[2].trim();
    }

    // For new format, try to extract screen_id from next line: > `SCR-XX-NNN` · ...
    // We'll do this after collecting positions
    headerPositions.push({
      name: rawName,
      screen_id: screen_id, // may be null for new format
      index: match.index,
    });
  }

  for (let i = 0; i < headerPositions.length; i++) {
    const start = headerPositions[i].index;
    const end = i + 1 < headerPositions.length ? headerPositions[i + 1].index : content.length;
    const section = content.substring(start, end);

    // For new format: extract screen_id from blockquote line
    if (!headerPositions[i].screen_id) {
      const idMatch = section.match(/^>\s*`([^`]+)`/m);
      if (idMatch) {
        headerPositions[i].screen_id = idMatch[1].trim();
      } else {
        // Fallback: slugify Vietnamese name
        headerPositions[i].screen_id = slugify(headerPositions[i].name);
      }
    }

    // Parse score line
    const scoreLine = scoreLineRegex.exec(section);
    const claimed = scoreLine ? {
      score: parseInt(scoreLine[1]),
      pass: parseInt(scoreLine[2]),
      gap: parseInt(scoreLine[3]),
    } : null;

    // Parse table rows
    const checks = [];
    let rowMatch;
    const localTableRegex = /^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|$/gm;
    while ((rowMatch = localTableRegex.exec(section)) !== null) {
      const verdict = rowMatch[5].trim();
      // Skip header row pattern
      if (verdict === 'Verdict' || verdict === '---' || verdict.startsWith(':')) continue;

      checks.push({
        check_num: parseInt(rowMatch[1]),
        check_name: rowMatch[2].trim(),
        source: rowMatch[3].trim(),
        ddl_ref: rowMatch[4].trim(),
        verdict: normalizeVerdict(verdict),
        evidence: rowMatch[6].trim(),
      });
    }

    screens.push({
      name: headerPositions[i].name,
      screen_id: headerPositions[i].screen_id,
      claimed,
      checks,
    });
  }

  return screens;
}

/**
 * Normalize verdict strings to canonical form.
 */
function normalizeVerdict(v) {
  const lower = v.toLowerCase().replace(/[^a-z]/g, '');
  if (lower.includes('pass')) return 'pass';
  if (lower.includes('gap')) return 'gap';
  if (lower.includes('unverifiable') || lower.includes('unverif')) return 'unverifiable';
  return 'unknown';
}

/**
 * Parse the "Đề xuất cải tiến (Priority)" section to extract proposals.
 */
function parseProposals(content) {
  const proposals = [];

  // NEW FORMAT: #### UXP-NNN · Severity
  // With metadata table containing: | **Man hinh** | {display_name_vi} |
  const newFormatRegex = /^#### UXP-(\d{3})\s*\u00b7\s*(?:\ud83d\udd34|\ud83d\udfe1|\u26aa)?\s*(Critical|Major|Minor)/gm;
  let match;
  while ((match = newFormatRegex.exec(content)) !== null) {
    const id = `UXP-${match[1]}`;
    const severity = match[2];
    // Extract screen from metadata table
    const blockEnd = content.indexOf('---', match.index + 10);
    const block = content.substring(match.index, blockEnd !== -1 ? blockEnd : content.length);
    const screenMatch = block.match(/\|\s*\*\*M[aà]n h[iì]nh\*\*\s*\|\s*(.+?)\s*\|/);
    const screen_display = screenMatch ? screenMatch[1].trim() : '';
    const screen_id = slugify(screen_display);

    proposals.push({
      id,
      screen_id,
      screen_display,
      problem: '',  // extracted from block if needed
      severity,
    });
  }

  // OLD FORMAT: **[UXP-NNN]** Screen: `screen-id` | **Problem**
  if (proposals.length === 0) {
    const oldRegex = /\*\*\[UXP-(\d{3})\]\*\*\s*Screen:\s*`([^`]+)`\s*\|\s*\*\*([^*]+)\*\*/g;
    while ((match = oldRegex.exec(content)) !== null) {
      proposals.push({
        id: `UXP-${match[1]}`,
        screen_id: match[2].trim(),
        screen_display: match[2].trim(),
        problem: match[3].trim(),
      });
    }

    // Also match Critical section format with - ** prefix (old)
    const criticalRegex = /- \*\*\[UXP-(\d{3})\]\*\*\s*Screen:\s*`([^`]+)`/g;
    while ((match = criticalRegex.exec(content)) !== null) {
      const id = `UXP-${match[1]}`;
      if (!proposals.find(p => p.id === id)) {
        proposals.push({
          id,
          screen_id: match[2].trim(),
          screen_display: match[2].trim(),
          problem: '(critical format)',
        });
      }
    }
  }

  return proposals;
}

/**
 * Slugify Vietnamese text: strip diacritics, lowercase, kebab-case.
 * Used to derive screen_id from display_name_vi for cross-matching.
 */
function slugify(text) {
  return text
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // strip diacritics
    .replace(/\u0111/g, 'd').replace(/\u0110/g, 'D')  // đ/Đ
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

/**
 * Parse severity of each proposal from the section headers.
 */
function inferProposalSeverity(content, proposals) {
  const sections = {
    Critical: [],
    Major: [],
    Minor: [],
  };

  // Find Critical/Major/Minor section boundaries
  const critStart = content.indexOf('### Critical');
  const majorStart = content.indexOf('### Major');
  const minorStart = content.indexOf('### Minor');
  const detailStart = content.indexOf('## Chi tiết theo màn hình');

  for (const p of proposals) {
    const pos = content.indexOf(p.id);
    if (pos === -1) continue;

    if (critStart !== -1 && pos > critStart && (majorStart === -1 || pos < majorStart)) {
      p.severity = 'Critical';
    } else if (majorStart !== -1 && pos > majorStart && (minorStart === -1 || pos < minorStart)) {
      p.severity = 'Major';
    } else if (minorStart !== -1 && pos > minorStart && (detailStart === -1 || pos < detailStart)) {
      p.severity = 'Minor';
    } else {
      p.severity = 'Unknown';
    }
  }

  return proposals;
}

/**
 * Calculate accurate scores.
 */
function calculateScores(screens, proposals) {
  const metrics = {
    screens: [],
    totals: {
      total_checks: 0,
      pass: 0,
      gap: 0,
      unverifiable: 0,
      unknown: 0,
      simple_score: 0,
      weighted_score: 0,
    },
    proposals: {
      Critical: 0,
      Major: 0,
      Minor: 0,
      total: proposals.length,
    },
    discrepancies: [],
  };

  // Count proposal severities
  for (const p of proposals) {
    if (p.severity && metrics.proposals[p.severity] !== undefined) {
      metrics.proposals[p.severity]++;
    }
  }

  let totalWeightedPenalty = 0;
  let totalMaxPenalty = 0;

  for (const screen of screens) {
    const counts = { pass: 0, gap: 0, unverifiable: 0, unknown: 0 };
    for (const check of screen.checks) {
      counts[check.verdict] = (counts[check.verdict] || 0) + 1;
    }

    const totalChecks = screen.checks.length;
    const verifiableChecks = counts.pass + counts.gap;

    // Simple score: pass / total (including unverifiable)
    const simpleScore = totalChecks > 0
      ? Math.round((counts.pass / totalChecks) * 100)
      : 0;

    // Weighted score: based on verifiable checks only
    // Find proposals for this screen to get severity weights
    const screenProposals = proposals.filter(p => p.screen_id === screen.screen_id);
    let screenWeightedPenalty = 0;
    for (const sp of screenProposals) {
      const weight = SEVERITY_WEIGHTS[sp.severity] || 1.0;
      screenWeightedPenalty += weight;
    }

    const screenMaxPenalty = verifiableChecks > 0
      ? verifiableChecks * SEVERITY_WEIGHTS.Critical  // max if all were critical gaps
      : 0;

    const weightedScore = screenMaxPenalty > 0
      ? Math.round((1 - screenWeightedPenalty / screenMaxPenalty) * 100)
      : 100;

    totalWeightedPenalty += screenWeightedPenalty;
    totalMaxPenalty += screenMaxPenalty;

    // Check discrepancies with claimed values
    if (screen.claimed) {
      if (screen.claimed.pass !== counts.pass) {
        metrics.discrepancies.push({
          screen_id: screen.screen_id,
          field: 'pass',
          claimed: screen.claimed.pass,
          actual: counts.pass,
        });
      }
      if (screen.claimed.gap !== counts.gap) {
        metrics.discrepancies.push({
          screen_id: screen.screen_id,
          field: 'gap',
          claimed: screen.claimed.gap,
          actual: counts.gap,
        });
      }
      const claimedTotal = screen.claimed.pass + screen.claimed.gap +
        (totalChecks - counts.pass - counts.gap); // inferred unverifiable
      if (screen.claimed.score !== simpleScore) {
        metrics.discrepancies.push({
          screen_id: screen.screen_id,
          field: 'score',
          claimed: screen.claimed.score + '%',
          actual: simpleScore + '%',
        });
      }
    }

    const screenMetric = {
      screen_id: screen.screen_id,
      name: screen.name,
      total_checks: totalChecks,
      ...counts,
      simple_score: simpleScore,
      weighted_score: Math.max(0, weightedScore),
      proposals_count: screenProposals.length,
      proposals_by_severity: {
        Critical: screenProposals.filter(p => p.severity === 'Critical').length,
        Major: screenProposals.filter(p => p.severity === 'Major').length,
        Minor: screenProposals.filter(p => p.severity === 'Minor').length,
      },
    };

    metrics.screens.push(screenMetric);
    metrics.totals.total_checks += totalChecks;
    metrics.totals.pass += counts.pass;
    metrics.totals.gap += counts.gap;
    metrics.totals.unverifiable += counts.unverifiable;
    metrics.totals.unknown += counts.unknown;
  }

  // Overall scores
  metrics.totals.simple_score = metrics.totals.total_checks > 0
    ? Math.round((metrics.totals.pass / metrics.totals.total_checks) * 100)
    : 0;

  metrics.totals.weighted_score = totalMaxPenalty > 0
    ? Math.max(0, Math.round((1 - totalWeightedPenalty / totalMaxPenalty) * 100))
    : 100;

  return metrics;
}

// ─── Commands ───────────────────────────────────────────────

function cmdRun(config) {
  const reportPath = config.inputs[0];
  const content = fs.readFileSync(reportPath, 'utf-8');
  const startTime = Date.now();

  log(`Parsing: ${reportPath}`);

  // Parse
  const screens = parseScreenSections(content);
  const proposals = inferProposalSeverity(content, parseProposals(content));
  const metrics = calculateScores(screens, proposals);

  const duration = Date.now() - startTime;

  // ─── Output ─────────────────────────────────────────────
  log('');
  log(`${c.bold}━━━ UX Score Report (by tool) ━━━${c.reset}`);
  log('');

  // Per-screen table
  log(`${'Screen'.padEnd(35)} ${'Checks'.padStart(6)} ${'Pass'.padStart(5)} ${'Gap'.padStart(5)} ${'Unv.'.padStart(5)} ${'Simple'.padStart(7)} ${'Weighted'.padStart(9)}`);
  log(`${'─'.repeat(35)} ${'─'.repeat(6)} ${'─'.repeat(5)} ${'─'.repeat(5)} ${'─'.repeat(5)} ${'─'.repeat(7)} ${'─'.repeat(9)}`);

  for (const s of metrics.screens) {
    const simpleColor = s.simple_score >= 70 ? c.green : s.simple_score >= 50 ? c.yellow : c.red;
    const weightedColor = s.weighted_score >= 70 ? c.green : s.weighted_score >= 50 ? c.yellow : c.red;
    log(`${s.screen_id.padEnd(35)} ${String(s.total_checks).padStart(6)} ${String(s.pass).padStart(5)} ${String(s.gap).padStart(5)} ${String(s.unverifiable).padStart(5)} ${simpleColor}${(s.simple_score + '%').padStart(7)}${c.reset} ${weightedColor}${(s.weighted_score + '%').padStart(9)}${c.reset}`);
  }

  log(`${'─'.repeat(35)} ${'─'.repeat(6)} ${'─'.repeat(5)} ${'─'.repeat(5)} ${'─'.repeat(5)} ${'─'.repeat(7)} ${'─'.repeat(9)}`);

  const t = metrics.totals;
  const totalSimpleColor = t.simple_score >= 70 ? c.green : t.simple_score >= 50 ? c.yellow : c.red;
  const totalWeightedColor = t.weighted_score >= 70 ? c.green : t.weighted_score >= 50 ? c.yellow : c.red;
  log(`${'TOTAL'.padEnd(35)} ${String(t.total_checks).padStart(6)} ${String(t.pass).padStart(5)} ${String(t.gap).padStart(5)} ${String(t.unverifiable).padStart(5)} ${totalSimpleColor}${(t.simple_score + '%').padStart(7)}${c.reset} ${totalWeightedColor}${(t.weighted_score + '%').padStart(9)}${c.reset}`);

  log('');
  log(`${c.bold}Proposals:${c.reset} ${c.red}Critical: ${metrics.proposals.Critical}${c.reset} | ${c.yellow}Major: ${metrics.proposals.Major}${c.reset} | ${c.cyan}Minor: ${metrics.proposals.Minor}${c.reset} | Total: ${metrics.proposals.total}`);

  // Discrepancies
  if (metrics.discrepancies.length > 0) {
    log('');
    log(`${c.red}${c.bold}⚠️  DISCREPANCIES FOUND (${metrics.discrepancies.length}):${c.reset}`);
    for (const d of metrics.discrepancies) {
      log(`  ${c.yellow}${d.screen_id}${c.reset} → ${d.field}: claimed ${c.red}${d.claimed}${c.reset} vs actual ${c.green}${d.actual}${c.reset}`);
    }
  } else {
    log(`${c.green}✅ No discrepancies — all counts match.${c.reset}`);
  }

  log('');
  log(`Duration: ${duration}ms`);

  // JSON output
  if (config.json) {
    const jsonOutput = {
      _generated: new Date().toISOString(),
      _script: `${SCRIPT_NAME} v${VERSION}`,
      _source: reportPath,
      ...metrics,
      duration_ms: duration,
    };
    console.log(JSON.stringify(jsonOutput, null, 2));
  }

  // Fix mode
  if (config.fix && metrics.discrepancies.length > 0) {
    log(`${c.cyan}Fixing report...${c.reset}`);
    let fixed = content;

    // Fix overview section
    const overviewReplacements = [
      [/Pass:\s*\d+\s*\|\s*Gap:\s*\d+\s*\|\s*Unverifiable:\s*\d+/,
       `Pass: ${t.pass} | Gap: ${t.gap} | Unverifiable: ${t.unverifiable}`],
      [/Tổng check:\s*\d+/,
       `Tổng check: ${t.total_checks}`],
      [/UX Score:\s*\d+%/,
       `UX Score: ${t.simple_score}%`],
    ];

    for (const [pattern, replacement] of overviewReplacements) {
      fixed = fixed.replace(pattern, replacement);
    }

    // Fix per-screen score lines
    for (const s of metrics.screens) {
      const screenPattern = new RegExp(
        `(\\*\\*Score:\\s*)\\d+(%\\s*\\|\\s*Pass:\\s*)\\d+(\\s*\\|\\s*Gap:\\s*)\\d+`
      );
      // Find the section for this screen and replace within it
      const screenHeaderIdx = fixed.indexOf(`\`${s.screen_id}\``);
      if (screenHeaderIdx !== -1) {
        const nextScreenIdx = fixed.indexOf('### ', screenHeaderIdx + 10);
        const sectionEnd = nextScreenIdx !== -1 ? nextScreenIdx : fixed.length;
        const section = fixed.substring(screenHeaderIdx, sectionEnd);
        const fixedSection = section.replace(
          screenPattern,
          `$1${s.simple_score}$2${s.pass}$3${s.gap}`
        );
        fixed = fixed.substring(0, screenHeaderIdx) + fixedSection + fixed.substring(sectionEnd);
      }
    }

    fs.writeFileSync(reportPath, fixed, 'utf-8');
    log(`${c.green}✅ Report fixed: ${reportPath}${c.reset}`);
  }

  // Exit code
  process.exitCode = metrics.discrepancies.length > 0 ? 3 : 0;
}

function cmdCheck(config) {
  const reportPath = config.inputs[0];
  const content = fs.readFileSync(reportPath, 'utf-8');

  const checks = [];

  // Check 1: Has overview section
  checks.push({
    name: 'Overview section exists',
    pass: content.includes('## Tổng quan'),
  });

  // Check 2: Has proposals section
  checks.push({
    name: 'Proposals section exists',
    pass: content.includes('## Đề xuất cải tiến'),
  });

  // Check 3: Has detail section
  checks.push({
    name: 'Detail section exists',
    pass: content.includes('## Chi tiết theo màn hình'),
  });

  // Check 4: Has DDL references
  checks.push({
    name: 'DDL References section exists',
    pass: content.includes('## DDL References'),
  });

  // Check 5: Parse screens successfully
  const screens = parseScreenSections(content);
  checks.push({
    name: `Parsed ${screens.length} screen sections`,
    pass: screens.length > 0,
  });

  // Check 6: Parse proposals successfully
  const proposals = parseProposals(content);
  checks.push({
    name: `Parsed ${proposals.length} proposals`,
    pass: proposals.length > 0,
  });

  // Check 7: All checks have valid verdicts
  let unknownCount = 0;
  for (const s of screens) {
    for (const ch of s.checks) {
      if (ch.verdict === 'unknown') unknownCount++;
    }
  }
  checks.push({
    name: `No unknown verdicts (found: ${unknownCount})`,
    pass: unknownCount === 0,
  });

  // Output
  log(`Checking: ${reportPath}`);
  for (const ch of checks) {
    const icon = ch.pass ? `${c.green}✅${c.reset}` : `${c.red}❌${c.reset}`;
    log(`  ${icon} ${ch.name}`);
  }

  const passed = checks.filter(ch => ch.pass).length;
  log(`\n  ${passed}/${checks.length} checks passed`);
  process.exitCode = passed === checks.length ? 0 : 1;
}

function cmdTest() {
  log('Running self-test...');

  // Test 1: normalizeVerdict
  const tests = [
    ['✅ Pass', 'pass'],
    ['❌ Gap', 'gap'],
    ['⚠️ Unverifiable', 'unverifiable'],
    ['✅ pass', 'pass'],
    ['❌ gap', 'gap'],
  ];

  let passed = 0;
  for (const [input, expected] of tests) {
    const actual = normalizeVerdict(input);
    if (actual === expected) {
      passed++;
    } else {
      log.error(`normalizeVerdict("${input}") = "${actual}", expected "${expected}"`);
    }
  }

  // Test 2: Severity weights exist
  const weightTests = [
    ['Critical', 3.0],
    ['Major', 2.0],
    ['Minor', 1.0],
  ];
  for (const [sev, expected] of weightTests) {
    if (SEVERITY_WEIGHTS[sev] === expected) {
      passed++;
    } else {
      log.error(`Weight ${sev} = ${SEVERITY_WEIGHTS[sev]}, expected ${expected}`);
    }
  }

  const total = tests.length + weightTests.length;
  const allPassed = passed === total;
  log(`Self-test: ${passed}/${total} passed ${allPassed ? c.green + '✅' : c.red + '❌'}${c.reset}`);
  process.exitCode = allPassed ? 0 : 1;
}

// ─── Main ───────────────────────────────────────────────────
function main() {
  const config = parseArgs();

  if (config.command === 'test') {
    cmdTest();
    return;
  }

  // Validate
  if (config.inputs.length === 0) {
    log.die('No input file specified. Usage: node ux-score-calculator.js run <report.md>');
  }

  const reportPath = config.inputs[0];
  if (!fs.existsSync(reportPath)) {
    log.die(`Input not found: ${reportPath}`);
  }

  switch (config.command) {
    case 'run':   cmdRun(config); break;
    case 'check': cmdCheck(config); break;
  }
}

main();

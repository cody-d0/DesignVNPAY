#!/usr/bin/env node
// @ts-check
'use strict';
process.on('unhandledRejection', (err) => { console.error('💥 Unhandled:', err); process.exit(1); });

// ============================================================
// Script: extract-icon-inventory.js
// Purpose: Phase 2c-bis — Extract icon inventory from Figma
//          metadata XML. Pipe 1 (deterministic, cheap).
//          Outputs icon_inventory[] per screen for Phase 2d
//          agent reasoning.
// Author: AI-assisted (automation-scripts skill)
// Created: 2026-03-17
// Usage:
//   node tools/scripts/extract-icon-inventory.js <metadata_xml> <boundaries_json> [--dry-run] [--test] [--help]
//   node tools/scripts/extract-icon-inventory.js --sim <metadata_xml>
// Dependencies: Node.js >= 18 (no external packages)
// Quality-grade: A
// ============================================================

const fs = require('fs');
const path = require('path');

// ─── CONFIGURATION ───────────────────────────────────────────

/**
 * Icon name patterns — multi-convention support.
 * 
 * 3 naming conventions observed across VNPAY projects:
 * 1. ic_* prefix (Co-op Bank): ic_contact, ic_acc_red, ic_backhome
 * 2. kebab-case (SDK Thanh Toán): caret-arrow-down, close-x, checkmark-circle
 * 3. snake_case descriptive (CTNBKC): back_arrow, calendar_picker, toggle_off
 * 
 * Pattern categories:
 * - TRIGGER: icons that likely open another screen/overlay
 * - NAVIGATION: icons for screen-level navigation (back, home)
 * - TOGGLE: state toggles
 * - DECORATION: visual-only icons (section headers, logos)
 * - ACTION: icons for actions (share, save, delete)
 * - INFO: informational icons (help, tooltip)
 * - UNKNOWN: matched by size heuristic, not by name
 */
const ICON_PATTERNS = {
  // ── Prefix-based patterns (Convention 1: ic_*, drop_*, btn_*, etc.) ──
  prefix: [
    { regex: /^ic_/i,         category: 'varies',     note: 'Co-op Bank convention' },
    { regex: /^drop_/i,       category: 'trigger',    note: 'Dropdown/picker trigger' },
    { regex: /^btn_/i,        category: 'action',     note: 'Button' },
    { regex: /^back_/i,       category: 'navigation', note: 'Back button' },
    { regex: /^clear_/i,      category: 'action',     note: 'Close/dismiss' },
    { regex: /^close/i,       category: 'action',     note: 'Close button' },
    { regex: /^arrow_/i,      category: 'navigation', note: 'Arrow navigation' },
    { regex: /^check_/i,      category: 'decoration', note: 'Checkmark' },
    { regex: /^logo_/i,       category: 'decoration', note: 'Logo' },
    { regex: /^form_/i,       category: 'layout',     note: 'Form container' },
  ],

  // ── Exact-match patterns (Convention 1 + 3) ──
  exact: [
    { name: 'switch',              category: 'toggle',     note: 'Toggle switch' },
    { name: 'home',                category: 'navigation', note: 'Home button' },
    { name: 'share',               category: 'action',     note: 'Share action' },
    { name: 'delete',              category: 'action',     note: 'Delete action' },
  ],

  // ── Substring patterns (Convention 2: kebab-case, Convention 3: snake_case) ──
  substring: [
    // Navigation
    { regex: /back[-_]?(arrow|white|button|nav)?$/i,   category: 'navigation' },
    { regex: /home[-_]?(indicator|button|icon)?$/i,    category: 'navigation' },
    { regex: /caret[-_]?arrow[-_]?(left|up)/i,         category: 'navigation' },
    
    // Triggers (likely open new screen)
    { regex: /caret[-_]?arrow[-_]?(down|right)/i,      category: 'trigger' },
    { regex: /contact[-_]?(person|picker|icon)?$/i,    category: 'trigger' },
    { regex: /calendar[-_]?(picker)?$/i,               category: 'trigger' },
    { regex: /(drop|chevron)[-_]?(down|blue|right)?$/i,category: 'trigger' },
    { regex: /search[-_]?(grey|icon|bar)?$/i,          category: 'trigger' },
    { regex: /person[-_]?add/i,                        category: 'trigger' },
    { regex: /plus[-_]?(circle|add)?$/i,               category: 'trigger' },
    { regex: /qr[-_]?(scan|code)?$/i,                  category: 'trigger' },
    { regex: /scan[-_]?(icon|qr|code)?$/i,             category: 'trigger' },
    { regex: /camera/i,                                category: 'trigger' },
    { regex: /filter/i,                                category: 'trigger' },
    
    // Toggles
    { regex: /toggle[-_]?(on|off)?$/i,                 category: 'toggle' },
    { regex: /switch[-_]?(on|off)?$/i,                 category: 'toggle' },
    
    // Dismiss/Close
    { regex: /close[-_]?(x|button|icon|login)?$/i,     category: 'action' },
    { regex: /clear[-_]?(login|x|button)?$/i,          category: 'action' },
    { regex: /dismiss/i,                               category: 'action' },
    
    // Decoration
    { regex: /checkmark[-_]?(circle|done)?$/i,         category: 'decoration' },
    { regex: /success[-_]?(check|icon)?$/i,            category: 'decoration' },
    { regex: /logo[-_]?/i,                             category: 'decoration' },
    { regex: /bank[-_]?logo/i,                         category: 'decoration' },
    { regex: /coop[-_]?bank/i,                         category: 'decoration' },
    { regex: /circle[-_]?(blue|red|green)?$/i,         category: 'decoration' },
    
    // Actions
    { regex: /save[-_]?(image|photo)?$/i,              category: 'action' },
    { regex: /share[-_]?(icon)?$/i,                    category: 'action' },
    { regex: /copy[-_]?(icon)?$/i,                     category: 'action' },
    { regex: /download/i,                              category: 'action' },
    { regex: /edit[-_]?(icon|pen)?$/i,                 category: 'action' },
    { regex: /delete[-_]?(icon|button)?$/i,            category: 'action' },
    
    // Info
    { regex: /quest[-_]?\d*/i,                         category: 'info' },
    { regex: /help[-_]?(icon)?$/i,                     category: 'info' },
    { regex: /info[-_]?(icon|circle)?$/i,              category: 'info' },
    { regex: /tooltip/i,                               category: 'info' },
    { regex: /warning[-_]?(icon)?$/i,                  category: 'info' },
    { regex: /error[-_]?(icon)?$/i,                    category: 'info' },
    
    // OTP / Auth
    { regex: /otp[-_]?(cell|input|box)?/i,             category: 'decoration' },
    { regex: /fingerprint|faceid|biometric/i,          category: 'action' },
  ],
};

/**
 * Size heuristic: frames ≤ MAX_ICON_SIZE in both dimensions
 * are candidate icons even without matching name patterns.
 */
const MAX_ICON_SIZE = 48;

/**
 * Exclusion patterns: frames that should NEVER be classified as icons
 * even if they match size heuristic.
 */
const EXCLUSION_PATTERNS = [
  /^Vector$/i,
  /^Rectangle/i,
  /^Line \d+/i,
  /^Ellipse/i,
  /^Path \d+/i,
  /^Subtraction/i,
  /^Group \d+$/,           // Generic groups (Group 12345)
  /^Mask Group/i,
  /^Clip path/i,
  /^clip-/i,
  /^Background/i,
  /^Symbol$/i,
  /^Label$/i,
  /^Key Light/i,
  /^Space$/i,
  /^Return$/i,
  /^Shift$/i,
  /^Delete$/i,
  /^Home Indicator$/i,
  /^Bars\//i,              // Status bar components
  /^battery$/i,
  /^bluetooth$/i,
  /^Time$/i,
  /^Keys$/i,
  /^Keyboard/i,
  /^[A-Z]$/,               // Single letters (keyboard keys)
  /^\d+$/,                 // Pure numbers
  /^Repeat Grid/i,
  /^Left Detail$/i,
  /^Right Detail$/i,
];

// ─── LOGGING ─────────────────────────────────────────────────

const LOG_LEVELS = { debug: 0, info: 1, warn: 2, error: 3 };
let currentLogLevel = LOG_LEVELS.info;

function log(level, msg, data) {
  if (LOG_LEVELS[level] < currentLogLevel) return;
  const prefix = { debug: '🔍', info: 'ℹ️ ', warn: '⚠️ ', error: '❌' }[level];
  const ts = new Date().toISOString().slice(11, 19);
  console.error(`${ts} ${prefix} ${msg}${data ? ' ' + JSON.stringify(data) : ''}`);
}

// ─── CORE: XML PARSING (lightweight, no deps) ────────────────

/**
 * Parse Figma metadata XML into frame objects.
 * Uses regex — intentionally simple, no DOM parser needed.
 */
function parseFramesFromXML(xml) {
  const frames = [];
  // Match <frame> and <section> tags with attributes
  const frameRegex = /<(?:frame|section)\s+id="([^"]+)"\s+name="([^"]+)"\s+x="([^"]+)"\s+y="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"/g;
  let m;
  while ((m = frameRegex.exec(xml)) !== null) {
    frames.push({
      id: m[1],
      name: m[2],
      x: parseFloat(m[3]),
      y: parseFloat(m[4]),
      width: parseFloat(m[5]),
      height: parseFloat(m[6]),
    });
  }
  // Also match self-closing <text> and <vector> with id/name (for adjacent text lookup)
  const textRegex = /<text\s+id="([^"]+)"\s+name="([^"]+)"\s+x="([^"]+)"\s+y="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"/g;
  const textNodes = [];
  while ((m = textRegex.exec(xml)) !== null) {
    textNodes.push({
      id: m[1],
      name: m[2],
      x: parseFloat(m[3]),
      y: parseFloat(m[4]),
      width: parseFloat(m[5]),
      height: parseFloat(m[6]),
    });
  }
  return { frames, textNodes };
}

// ─── CORE: ICON MATCHING ─────────────────────────────────────

/**
 * Check if a frame name matches any icon pattern.
 * Returns { matched: true, category, matchedBy, note } or { matched: false }
 */
function matchIconPattern(name) {
  // 1. Check exclusions first
  for (const excl of EXCLUSION_PATTERNS) {
    if (excl.test(name)) return { matched: false, reason: 'excluded' };
  }

  // 2. Exact match
  for (const pat of ICON_PATTERNS.exact) {
    if (name.toLowerCase() === pat.name.toLowerCase()) {
      return { matched: true, category: pat.category, matchedBy: 'exact', note: pat.note };
    }
  }

  // 3. Prefix match
  for (const pat of ICON_PATTERNS.prefix) {
    if (pat.regex.test(name)) {
      // Refine category for ic_* based on sub-patterns
      let category = pat.category;
      if (category === 'varies') {
        category = refineIcCategory(name);
      }
      return { matched: true, category, matchedBy: 'prefix', note: pat.note };
    }
  }

  // 4. Substring match
  for (const pat of ICON_PATTERNS.substring) {
    if (pat.regex.test(name)) {
      return { matched: true, category: pat.category, matchedBy: 'substring', note: '' };
    }
  }

  return { matched: false, reason: 'no_pattern_match' };
}

/**
 * Refine category for ic_* icons based on suffix
 */
function refineIcCategory(name) {
  const lower = name.toLowerCase();
  if (/ic_contact|ic_person|ic_user|ic_add/i.test(lower)) return 'trigger';
  if (/ic_search/i.test(lower)) return 'trigger';
  if (/ic_back|ic_home|ic_nav/i.test(lower)) return 'navigation';
  if (/ic_acc|ic_money|ic_human|ic_tit|ic_quest/i.test(lower)) return 'decoration';
  if (/ic_share|ic_save|ic_copy|ic_edit/i.test(lower)) return 'action';
  if (/ic_qr|ic_scan|ic_camera/i.test(lower)) return 'trigger';
  if (/ic_calendar|ic_date|ic_picker/i.test(lower)) return 'trigger';
  return 'decoration'; // default for unrecognized ic_*
}

/**
 * Check size heuristic: small frames that might be icons
 */
function matchSizeHeuristic(frame) {
  return frame.width <= MAX_ICON_SIZE && frame.height <= MAX_ICON_SIZE
    && frame.width > 0 && frame.height > 0;
}

// ─── CORE: SCREEN ASSIGNMENT ─────────────────────────────────

/**
 * Assign each icon to its parent screen based on boundaries.
 * Uses artboard_node_ids from screen_boundaries to determine container.
 */
function assignToScreen(iconFrame, boundaries, allFrames) {
  // Strategy: find the closest ancestor frame that is an artboard in boundaries
  // Since we don't have tree structure from flat XML, use position-based matching
  for (const boundary of boundaries) {
    for (const nodeId of boundary.artboard_node_ids) {
      const artboard = allFrames.find(f => f.id === nodeId);
      if (!artboard) continue;
      // Check if icon position is within artboard bounds (rough check)
      // Note: x/y in Figma metadata can be relative to parent, so this is approximate
      // The key signal is that icons appear in the XML between their parent artboard tags
    }
  }
  // Fallback: return null, let the XML nesting determine parent
  return null;
}

/**
 * Parse XML nesting to determine parent screen for each icon.
 * Walks XML structure to find which top-level artboard contains each icon.
 */
function buildParentMap(xml, screenNodeIds) {
  const parentMap = new Map(); // icon_id → screen_id
  
  // Build section artboard containers from XML nesting
  // Find each artboard's XML range
  const artboardRanges = [];
  for (const nodeId of screenNodeIds) {
    const openTag = new RegExp(`<(?:frame|section)\\s+id="${nodeId.replace(':', '\\:')}"[^>]*>`, 'g');
    const match = openTag.exec(xml);
    if (!match) continue;
    
    const startPos = match.index;
    // Find matching close tag (simplified — count nesting)
    let depth = 1;
    let pos = startPos + match[0].length;
    while (depth > 0 && pos < xml.length) {
      const nextOpen = xml.indexOf('<frame ', pos);
      const nextSection = xml.indexOf('<section ', pos);
      const nextClose = xml.indexOf('</frame>', pos);
      const nextSectionClose = xml.indexOf('</section>', pos);
      
      const opens = [nextOpen, nextSection].filter(x => x >= 0);
      const closes = [nextClose, nextSectionClose].filter(x => x >= 0);
      
      const nearestOpen = opens.length ? Math.min(...opens) : Infinity;
      const nearestClose = closes.length ? Math.min(...closes) : Infinity;
      
      if (nearestClose < nearestOpen) {
        depth--;
        pos = nearestClose + 8; // </frame> length
      } else if (nearestOpen < nearestClose) {
        depth++;
        pos = nearestOpen + 7;
      } else {
        break;
      }
    }
    const endPos = pos;
    artboardRanges.push({ nodeId, startPos, endPos });
  }
  
  return artboardRanges;
}

// ─── CORE: ADJACENT TEXT LOOKUP ──────────────────────────────

/**
 * Find text nodes adjacent to an icon (within proximity radius).
 * Used by Phase 2d agent reasoning as context.
 */
function findAdjacentText(icon, textNodes, radius = 100) {
  return textNodes
    .filter(t => {
      const dx = Math.abs(t.x - icon.x);
      const dy = Math.abs(t.y - icon.y);
      return dx <= radius && dy <= radius;
    })
    .sort((a, b) => {
      const da = Math.abs(a.x - icon.x) + Math.abs(a.y - icon.y);
      const db = Math.abs(b.x - icon.x) + Math.abs(b.y - icon.y);
      return da - db;
    })
    .slice(0, 5) // max 5 adjacent texts
    .map(t => t.name);
}

// ─── MAIN: EXTRACT ICON INVENTORY ────────────────────────────

function extractIconInventory(xmlPath, boundariesPath, options = {}) {
  const startTime = Date.now();
  
  // ── Validate inputs ──
  if (!fs.existsSync(xmlPath)) {
    log('error', `Metadata XML not found: ${xmlPath}`);
    process.exit(1);
  }
  
  const xml = fs.readFileSync(xmlPath, 'utf-8');
  const { frames, textNodes } = parseFramesFromXML(xml);
  log('info', `Parsed ${frames.length} frames, ${textNodes.length} text nodes from metadata`);

  // ── Load boundaries (optional) ──
  let boundaries = [];
  let screenNodeIds = new Set();
  if (boundariesPath && fs.existsSync(boundariesPath)) {
    const boundariesData = JSON.parse(fs.readFileSync(boundariesPath, 'utf-8'));
    boundaries = boundariesData.screen_boundaries || boundariesData || [];
    for (const b of boundaries) {
      for (const nid of (b.artboard_node_ids || [])) {
        screenNodeIds.add(nid);
      }
    }
    log('info', `Loaded ${boundaries.length} screen boundaries`);
  }

  // ── Build parent map for screen assignment ──
  const artboardRanges = screenNodeIds.size > 0 
    ? buildParentMap(xml, [...screenNodeIds])
    : [];

  // ── Extract icons ──
  const iconInventory = [];
  const stats = { 
    total_frames: frames.length, 
    matched_by_name: 0, 
    matched_by_size: 0, 
    excluded: 0,
    by_category: {}
  };

  for (const frame of frames) {
    // Skip artboard-level frames (they are screens, not icons)
    if (screenNodeIds.has(frame.id)) continue;

    const nameMatch = matchIconPattern(frame.name);
    const sizeMatch = matchSizeHeuristic(frame);

    let isIcon = false;
    let source = 'metadata';
    let category = 'unknown';
    let matchedBy = 'none';

    if (nameMatch.matched) {
      isIcon = true;
      category = nameMatch.category;
      matchedBy = nameMatch.matchedBy;
      stats.matched_by_name++;
    } else if (nameMatch.reason === 'excluded') {
      stats.excluded++;
      continue;
    } else if (sizeMatch && !nameMatch.reason) {
      // Size heuristic — only if not excluded
      // Re-check exclusions for size-matched
      let excluded = false;
      for (const excl of EXCLUSION_PATTERNS) {
        if (excl.test(frame.name)) { excluded = true; break; }
      }
      if (!excluded) {
        isIcon = true;
        category = 'unknown';
        matchedBy = 'size_heuristic';
        stats.matched_by_size++;
      }
    }

    if (!isIcon) continue;

    // ── Determine parent screen ──
    let parentScreenId = null;
    // Find which artboard range contains this frame's XML position
    const frameTag = `id="${frame.id}"`;
    const framePos = xml.indexOf(frameTag);
    if (framePos >= 0) {
      for (const range of artboardRanges) {
        if (framePos >= range.startPos && framePos <= range.endPos) {
          // Find boundary with this nodeId
          const parent = boundaries.find(b => 
            (b.artboard_node_ids || []).includes(range.nodeId)
          );
          if (parent) {
            parentScreenId = parent.screen_id;
          }
          break;
        }
      }
    }

    // ── Find adjacent text ──
    const adjacentText = findAdjacentText(frame, textNodes);

    // ── Build icon entry ──
    const icon = {
      icon_name: frame.name,
      figma_node_id: frame.id,
      x: frame.x,
      y: frame.y,
      width: frame.width,
      height: frame.height,
      category,
      matched_by: matchedBy,
      parent_screen_id: parentScreenId,
      adjacent_text: adjacentText,
      source,
    };

    iconInventory.push(icon);

    // Update category stats
    stats.by_category[category] = (stats.by_category[category] || 0) + 1;
  }

  const duration = Date.now() - startTime;
  stats.total_icons = iconInventory.length;
  stats.duration_ms = duration;

  log('info', `Extracted ${iconInventory.length} icons in ${duration}ms`, {
    by_name: stats.matched_by_name,
    by_size: stats.matched_by_size,
    excluded: stats.excluded,
    categories: stats.by_category,
  });

  return { icon_inventory: iconInventory, stats };
}

// ─── SIM CHECK: Verify coverage ──────────────────────────────

function runSimCheck(xmlPath) {
  log('info', '🧪 Running simulation check...');

  const xml = fs.readFileSync(xmlPath, 'utf-8');
  const { frames, textNodes } = parseFramesFromXML(xml);

  // ── Test 1: All known icon names should be matched ──
  const knownIcons = [
    // Convention 1: ic_* prefix
    'ic_contact', 'ic_acc_red', 'ic_backhome', 'ic_human_tit', 
    'ic_money_tit', 'ic_quest20', 'ic_search_grey',
    // Convention 1: other prefixes
    'back_white', 'drop_blue', 'btn_main', 'clear_login', 'switch',
    'form_drop', 'form_fill', 'form_success',
    // Convention 2: kebab-case
    'caret-arrow-down', 'caret-arrow-left', 'checkmark-circle',
    'close-x', 'home', 'save-image', 'share',
    // Convention 3: snake_case descriptive
    'back_arrow', 'bank_logo', 'calendar_picker', 'calendar',
    'chevron_down', 'close_x', 'contact_person', 'coop_bank_logo',
    'person_add', 'plus_circle', 's_circle_blue', 'save_image',
    'success_checkmark', 'toggle_off', 'toggle_on',
    // Future patterns (anticipated)
    'ic_qr_scan', 'ic_camera', 'ic_fingerprint', 'ic_notification',
    'qr-code', 'scan-icon', 'biometric', 'filter-icon',
    'edit-pen', 'copy-icon', 'download', 'delete-button',
    'warning-icon', 'error-icon', 'info-circle', 'tooltip',
  ];

  let passCount = 0;
  let failCount = 0;
  const failures = [];

  for (const name of knownIcons) {
    const result = matchIconPattern(name);
    if (result.matched) {
      passCount++;
    } else {
      failCount++;
      failures.push({ name, reason: result.reason || 'no_match' });
    }
  }

  // ── Test 2: Known NON-icons should NOT be matched ──
  const knownNonIcons = [
    'Vector', 'Rectangle 5126', 'Line 20', 'Ellipse 379',
    'Group 16916', 'Mask Group 29', 'Clip path group',
    'clip-CTNTK_1', 'Background', 'Symbol', 'Label',
    'Key Light', 'Space', 'Return', 'Shift', 'Time',
    'Keys', 'Keyboard Alphabetic', 'A', 'B', 'C', '123',
    'Repeat Grid 15', 'Left Detail', 'Right Detail',
    'battery', 'bluetooth', 'Path 10472', 'Subtraction 6',
    'Home Indicator', 'Bars/Status Bar/Status Bar - On Light',
  ];

  let tnPassCount = 0;
  let tnFailCount = 0;
  const tnFailures = [];

  for (const name of knownNonIcons) {
    const result = matchIconPattern(name);
    if (!result.matched) {
      tnPassCount++;
    } else {
      tnFailCount++;
      tnFailures.push({ name, matched_as: result.category, by: result.matchedBy });
    }
  }

  // ── Test 3: Category assignment accuracy ──
  const categoryTests = [
    { name: 'ic_contact',      expected: 'trigger' },
    { name: 'drop_blue',       expected: 'trigger' },
    { name: 'ic_search_grey',  expected: 'trigger' },
    { name: 'calendar_picker', expected: 'trigger' },
    { name: 'chevron_down',    expected: 'trigger' },
    { name: 'contact_person',  expected: 'trigger' },
    { name: 'back_white',      expected: 'navigation' },
    { name: 'ic_backhome',     expected: 'navigation' },
    { name: 'caret-arrow-left',expected: 'navigation' },
    { name: 'switch',          expected: 'toggle' },
    { name: 'toggle_off',      expected: 'toggle' },
    { name: 'clear_login',     expected: 'action' },
    { name: 'close-x',         expected: 'action' },
    { name: 'save_image',      expected: 'action' },
    { name: 'share',           expected: 'action' },
    { name: 'checkmark-circle',expected: 'decoration' },
    { name: 'bank_logo',       expected: 'decoration' },
    { name: 'ic_human_tit',    expected: 'decoration' },
  ];

  let catPassCount = 0;
  let catFailCount = 0;
  const catFailures = [];

  for (const test of categoryTests) {
    const result = matchIconPattern(test.name);
    if (result.matched && result.category === test.expected) {
      catPassCount++;
    } else {
      catFailCount++;
      catFailures.push({ 
        name: test.name, 
        expected: test.expected, 
        got: result.matched ? result.category : 'NOT_MATCHED'
      });
    }
  }

  // ── Test 4: Run on actual metadata if provided ──
  let actualResult = null;
  if (xmlPath && fs.existsSync(xmlPath)) {
    const result = extractIconInventory(xmlPath, null, { quiet: true });
    actualResult = {
      total_icons: result.icon_inventory.length,
      categories: result.stats.by_category,
      sample: result.icon_inventory.slice(0, 5).map(i => 
        `${i.icon_name} (${i.category}, ${i.matched_by})`
      ),
    };
  }

  // ── Report ──
  console.log('\n╔══════════════════════════════════════════════╗');
  console.log('║   🧪 ICON EXTRACTION SIM CHECK REPORT       ║');
  console.log('╠══════════════════════════════════════════════╣');
  console.log(`║ Test 1: Known icons detected                ║`);
  console.log(`║   ✅ Pass: ${String(passCount).padStart(3)}/${knownIcons.length}                            ║`);
  if (failures.length) {
    console.log(`║   ❌ Fail: ${String(failCount).padStart(3)}                               ║`);
    for (const f of failures) {
      console.log(`║     → ${f.name.padEnd(30)} (${f.reason})  ║`);
    }
  }
  console.log('╠──────────────────────────────────────────────╣');
  console.log(`║ Test 2: Non-icons correctly excluded         ║`);
  console.log(`║   ✅ Pass: ${String(tnPassCount).padStart(3)}/${knownNonIcons.length}                            ║`);
  if (tnFailures.length) {
    console.log(`║   ❌ False positives: ${String(tnFailCount).padStart(3)}                     ║`);
    for (const f of tnFailures) {
      console.log(`║     → ${f.name.padEnd(25)} matched as ${f.matched_as} ║`);
    }
  }
  console.log('╠──────────────────────────────────────────────╣');
  console.log(`║ Test 3: Category accuracy                    ║`);
  console.log(`║   ✅ Pass: ${String(catPassCount).padStart(3)}/${categoryTests.length}                            ║`);
  if (catFailures.length) {
    console.log(`║   ❌ Misclassified: ${String(catFailCount).padStart(3)}                      ║`);
    for (const f of catFailures) {
      console.log(`║     → ${f.name.padEnd(20)} expected=${f.expected.padEnd(12)} got=${f.got} ║`);
    }
  }
  if (actualResult) {
    console.log('╠──────────────────────────────────────────────╣');
    console.log(`║ Test 4: Actual metadata extraction            ║`);
    console.log(`║   Icons found: ${actualResult.total_icons}                            `);
    console.log(`║   Categories: ${JSON.stringify(actualResult.categories)}  `);
    for (const s of actualResult.sample) {
      console.log(`║     → ${s}`);
    }
  }
  console.log('╠══════════════════════════════════════════════╣');

  const totalPass = passCount + tnPassCount + catPassCount;
  const totalTests = knownIcons.length + knownNonIcons.length + categoryTests.length;
  const pct = Math.round(totalPass / totalTests * 100);
  const grade = pct >= 95 ? 'A' : pct >= 85 ? 'B' : pct >= 70 ? 'C' : 'FAIL';

  console.log(`║ TOTAL: ${totalPass}/${totalTests} (${pct}%) — Grade: ${grade}              `);
  console.log('╚══════════════════════════════════════════════╝\n');

  return { pass: totalPass, total: totalTests, pct, grade, failures, tnFailures, catFailures };
}

// ─── SELF-TEST ───────────────────────────────────────────────

function runSelfTest() {
  log('info', '🔧 Running self-test...');
  
  const tests = [
    // Name matches
    () => { const r = matchIconPattern('ic_contact'); return r.matched && r.category === 'trigger' ? null : 'ic_contact should be trigger'; },
    () => { const r = matchIconPattern('drop_blue'); return r.matched && r.category === 'trigger' ? null : 'drop_blue should be trigger'; },
    () => { const r = matchIconPattern('back_white'); return r.matched && r.category === 'navigation' ? null : 'back_white should be navigation'; },
    () => { const r = matchIconPattern('switch'); return r.matched && r.category === 'toggle' ? null : 'switch should be toggle'; },
    () => { const r = matchIconPattern('clear_login'); return r.matched ? null : 'clear_login should match'; },
    // Exclusions
    () => { const r = matchIconPattern('Vector'); return !r.matched ? null : 'Vector should be excluded'; },
    () => { const r = matchIconPattern('Group 12345'); return !r.matched ? null : 'Group 12345 should be excluded'; },
    () => { const r = matchIconPattern('Rectangle 5126'); return !r.matched ? null : 'Rectangle should be excluded'; },
    // Size heuristic
    () => { const r = matchSizeHeuristic({ width: 24, height: 24 }); return r ? null : '24x24 should match size'; },
    () => { const r = matchSizeHeuristic({ width: 375, height: 667 }); return !r ? null : '375x667 should not match size'; },
    // Convention 2
    () => { const r = matchIconPattern('caret-arrow-down'); return r.matched ? null : 'caret-arrow-down should match'; },
    () => { const r = matchIconPattern('close-x'); return r.matched ? null : 'close-x should match'; },
    // Convention 3
    () => { const r = matchIconPattern('calendar_picker'); return r.matched && r.category === 'trigger' ? null : 'calendar_picker should be trigger'; },
    () => { const r = matchIconPattern('toggle_off'); return r.matched && r.category === 'toggle' ? null : 'toggle_off should be toggle'; },
  ];

  let pass = 0;
  let fail = 0;
  for (let i = 0; i < tests.length; i++) {
    const err = tests[i]();
    if (err) {
      log('error', `Self-test ${i + 1}: FAIL — ${err}`);
      fail++;
    } else {
      pass++;
    }
  }
  
  log('info', `Self-test: ${pass}/${tests.length} passed`);
  return fail === 0;
}

// ─── CLI ─────────────────────────────────────────────────────

function showHelp() {
  console.log(`
Usage:
  extract-icon-inventory.js <metadata_xml> [boundaries_json] [options]
  extract-icon-inventory.js --sim <metadata_xml>
  extract-icon-inventory.js --test
  extract-icon-inventory.js --help

Arguments:
  metadata_xml       Path to Figma metadata XML file (from get_metadata)
  boundaries_json    Path to screen_boundaries.json (optional, for parent assignment)

Options:
  --sim              Run simulation check with known test vectors
  --test             Run self-test (smoke test)
  --dry-run          Show what would be extracted without writing output
  --output <path>    Write icon_inventory.json to specified path
  --verbose          Enable debug logging
  --help             Show this help message

Output (stdout as JSON):
  {
    "icon_inventory": [...],   // Array of icon objects per screen
    "stats": { ... }           // Extraction statistics
  }

Examples:
  # Extract from metadata, output to stdout
  node tools/scripts/extract-icon-inventory.js metadata.xml

  # Extract with boundaries for parent screen assignment
  node tools/scripts/extract-icon-inventory.js metadata.xml .handoff/screen_boundaries.json

  # Run simulation check
  node tools/scripts/extract-icon-inventory.js --sim metadata.xml

  # Self-test
  node tools/scripts/extract-icon-inventory.js --test
`);
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.includes('--help') || args.length === 0) {
    showHelp();
    process.exit(0);
  }

  if (args.includes('--verbose')) {
    currentLogLevel = LOG_LEVELS.debug;
  }

  if (args.includes('--test')) {
    const ok = runSelfTest();
    process.exit(ok ? 0 : 1);
  }

  if (args.includes('--sim')) {
    const xmlIdx = args.indexOf('--sim') + 1;
    const xmlPath = args[xmlIdx] || null;
    const result = runSimCheck(xmlPath);
    process.exit(result.grade === 'FAIL' ? 1 : 0);
  }

  // Main extraction
  const positional = args.filter(a => !a.startsWith('--'));
  const xmlPath = positional[0];
  const boundariesPath = positional[1] || null;
  const dryRun = args.includes('--dry-run');

  if (!xmlPath) {
    log('error', 'Missing required argument: metadata_xml');
    showHelp();
    process.exit(2);
  }

  const result = extractIconInventory(xmlPath, boundariesPath);

  if (dryRun) {
    log('info', `[DRY-RUN] Would extract ${result.icon_inventory.length} icons`);
    log('info', `Categories: ${JSON.stringify(result.stats.by_category)}`);
    for (const icon of result.icon_inventory.slice(0, 10)) {
      log('info', `  ${icon.icon_name} (${icon.category}) → screen: ${icon.parent_screen_id || 'unknown'}`);
    }
    process.exit(0);
  }

  // Output
  const outputIdx = args.indexOf('--output');
  if (outputIdx >= 0 && args[outputIdx + 1]) {
    const outPath = args[outputIdx + 1];
    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    fs.writeFileSync(outPath, JSON.stringify(result, null, 2));
    log('info', `Written to ${outPath}`);
  } else {
    console.log(JSON.stringify(result, null, 2));
  }

  process.exit(0);
}

main();

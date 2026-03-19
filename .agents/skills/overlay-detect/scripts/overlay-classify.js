#!/usr/bin/env node
/**
 * overlay-classify.js — Metadata pre-classifier for overlay detection
 *
 * Extracts structural signals from Figma metadata JSON to identify
 * potential overlay artboards. Agent uses this output + vision for
 * final 7-signal scoring.
 *
 * Usage:
 *   node overlay-classify.js <metadata_json> <section_node_id>
 *   node overlay-classify.js --test    # self-test with inline data
 *
 * Output: JSON to stdout with pre_classification[] per artboard
 */

'use strict';

const fs = require('fs');
const path = require('path');

// ─── Known overlay indicator patterns ───
const CLOSE_ICON_PATTERNS = [
  /^ic_close/i, /^close/i, /^icon.?close/i, /^x$/i, /^btn.?close/i,
  /^ic_cancel/i, /cancel.?icon/i, /^dismiss/i
];

const KEYBOARD_PATTERNS = [
  /^keyboard/i, /^key$/i, /^space$/i, /^return$/i, /^backspace$/i,
  /^shift$/i, /^delete$/i, /^123$/i, /^go$/i
];

const OVERLAY_TITLE_PATTERNS = [
  /danh bạ/i, /ngân hàng thụ hưởng/i, /chọn/i, /tìm kiếm/i,
  /xác thực/i, /otp/i, /mã pin/i, /bộ lọc/i, /filter/i,
  /sort/i, /sắp xếp/i, /chia sẻ/i, /share/i,
  /select/i, /picker/i, /choose/i, /search/i,
  /contacts/i, /beneficiary/i, /recipients/i
];

const NAV_BACK_PATTERNS = [
  /^back_white$/i, /^back$/i, /^ic_back/i, /^arrow.?left/i, /^nav_back/i
];

// ─── Node traversal helpers ───

function findNode(root, targetId) {
  if (root.id === targetId) return root;
  for (const c of (root.children || [])) {
    const found = findNode(c, targetId);
    if (found) return found;
  }
  return null;
}

function getArtboards(sectionNode) {
  const results = [];
  function walk(node, depth) {
    if (node.type === 'FRAME' && depth === 2) {
      const bb = node.absoluteBoundingBox || {};
      results.push({
        id: node.id,
        name: node.name,
        width: bb.width || 0,
        height: bb.height || 0,
        children: node.children || [],
        _node: node
      });
    }
    for (const c of (node.children || [])) {
      walk(c, depth + 1);
    }
  }
  walk(sectionNode, 0);
  return results;
}

function getSectionName(sectionNode) {
  return sectionNode.name || '';
}

function getSubSections(sectionNode) {
  const subs = [];
  for (const c of (sectionNode.children || [])) {
    if (c.type === 'SECTION' || c.type === 'FRAME' || c.type === 'GROUP') {
      subs.push({ id: c.id, name: c.name, type: c.type });
    }
  }
  return subs;
}

// ─── Signal extractors ───

function matchesAny(name, patterns) {
  return patterns.some(p => p.test(name));
}

function extractS1(artboard, sectionName, subSections) {
  // S1: artboard name == section name OR sub-section name
  const abName = artboard.name.trim();
  if (abName === sectionName.trim()) return true;
  return subSections.some(s => abName === s.name.trim());
}

function extractCloseIcon(node, depth = 0) {
  if (depth > 6) return false;
  const name = (node.name || '').trim();
  if (matchesAny(name, CLOSE_ICON_PATTERNS)) {
    const bb = node.absoluteBoundingBox || {};
    const w = bb.width || 999;
    const h = bb.height || 999;
    if (w <= 48 && h <= 48) return true;
  }
  for (const c of (node.children || [])) {
    if (extractCloseIcon(c, depth + 1)) return true;
  }
  return false;
}

function extractKeyboardNodes(node, depth = 0) {
  let count = 0;
  if (depth > 4) return 0;
  const name = (node.name || '').trim();
  if (name.length === 1 && /^[A-Z]$/.test(name)) count++;
  if (matchesAny(name, KEYBOARD_PATTERNS)) count++;
  for (const c of (node.children || [])) {
    count += extractKeyboardNodes(c, depth + 1);
  }
  return count;
}

function extractTextNodes(node, depth = 0) {
  const texts = [];
  if (depth > 8) return texts;
  if (node.type === 'TEXT') {
    const chars = (node.characters || '').trim();
    if (chars.length > 1) texts.push(chars);
  }
  for (const c of (node.children || [])) {
    texts.push(...extractTextNodes(c, depth + 1));
  }
  return texts;
}

function extractOverlayTitleSignal(texts) {
  // Check if first meaningful text (likely title) matches overlay patterns
  const title = texts.find(t => t.length > 2 && t.length < 60);
  if (!title) return { match: false, title: null };
  const match = OVERLAY_TITLE_PATTERNS.some(p => p.test(title));
  return { match, title };
}

function extractNavBack(node, depth = 0) {
  if (depth > 4) return false;
  const name = (node.name || '').trim();
  if (matchesAny(name, NAV_BACK_PATTERNS)) {
    const bb = node.absoluteBoundingBox || {};
    const w = bb.width || 999;
    const h = bb.height || 999;
    if (w <= 48 && h <= 48) return true;
  }
  for (const c of (node.children || [])) {
    if (extractNavBack(c, depth + 1)) return true;
  }
  return false;
}

function countDirectChildren(artboard) {
  return (artboard.children || []).length;
}

function hasClipGroup(artboard) {
  for (const c of (artboard.children || [])) {
    if (c.type === 'GROUP' && /clip/i.test(c.name || '')) return true;
  }
  return false;
}

// ─── Main classify ───

function classify(metadataPath, sectionNodeId) {
  const raw = JSON.parse(fs.readFileSync(metadataPath, 'utf8'));
  const nodeKey = Object.keys(raw.nodes || {})[0] || sectionNodeId;
  const rootDoc = (raw.nodes[nodeKey] || {}).document;
  if (!rootDoc) {
    console.error(`❌ Cannot find document node for ${sectionNodeId}`);
    process.exit(1);
  }

  const sectionNode = findNode(rootDoc, sectionNodeId) || rootDoc;
  const sectionName = getSectionName(sectionNode);
  const subSections = getSubSections(sectionNode);
  const artboards = getArtboards(sectionNode);

  if (artboards.length === 0) {
    console.error(`❌ No artboards found under section ${sectionNodeId}`);
    process.exit(1);
  }

  // Find "primary" artboard per sub-section (largest by area, or first)
  const primaryPerSub = {};
  for (const sub of subSections) {
    const subArtboards = artboards.filter(a => {
      const parentSub = subSections.find(s => {
        const subNode = findNode(sectionNode, s.id);
        return subNode && findNode(subNode, a.id);
      });
      return parentSub && parentSub.id === sub.id;
    });
    if (subArtboards.length > 0) {
      const primary = subArtboards.reduce((best, a) =>
        (a.width * a.height > best.width * best.height) ? a : best
      , subArtboards[0]);
      primaryPerSub[sub.id] = primary.id;
    }
  }

  const classifications = artboards.map(ab => {
    const s1 = extractS1(ab, sectionName, subSections);
    const hasClose = extractCloseIcon(ab._node);
    const keyboardCount = extractKeyboardNodes(ab._node);
    const hasKeyboard = keyboardCount >= 10;
    const texts = extractTextNodes(ab._node);
    const titleSignal = extractOverlayTitleSignal(texts);
    const hasBack = extractNavBack(ab._node);
    const childCount = countDirectChildren(ab);
    const hasClip = hasClipGroup(ab);

    // Heuristic: needs vision if any metadata hint suggests overlay
    const metadataHints = [s1, hasClose, titleSignal.match, hasKeyboard].filter(Boolean).length;
    const needsVision = metadataHints >= 1;

    // Find which sub-section this artboard belongs to
    let parentSubId = null;
    for (const sub of subSections) {
      const subNode = findNode(sectionNode, sub.id);
      if (subNode && findNode(subNode, ab.id)) {
        parentSubId = sub.id;
        break;
      }
    }
    const isPrimary = primaryPerSub[parentSubId] === ab.id;

    return {
      artboard_id: ab.id,
      artboard_name: ab.name,
      size: `${ab.width}x${ab.height}`,
      parent_sub_section: parentSubId,
      is_primary_artboard: isPrimary,
      signals: {
        s1_same_name: s1,
        has_close_icon_name: hasClose,
        has_keyboard_nodes: hasKeyboard,
        keyboard_node_count: keyboardCount,
        has_clip_group: hasClip,
        has_nav_back: hasBack,
        overlay_title_match: titleSignal.match,
        overlay_title_text: titleSignal.title,
        direct_child_count: childCount
      },
      needs_vision: needsVision,
      metadata_hint_count: metadataHints,
      // Pre-verdict based on metadata alone (agent must confirm with vision)
      metadata_verdict: isPrimary ? 'LIKELY_STANDALONE' :
        (hasClose && !hasBack) ? 'LIKELY_OVERLAY' :
        (titleSignal.match) ? 'LIKELY_OVERLAY' :
        (hasKeyboard) ? 'LIKELY_VARIANT' :
        'NEEDS_VISION'
    };
  });

  return {
    section_node_id: sectionNodeId,
    section_name: sectionName,
    sub_sections: subSections.map(s => ({ id: s.id, name: s.name, primary_artboard: primaryPerSub[s.id] || null })),
    total_artboards: artboards.length,
    pre_classification: classifications,
    summary: {
      likely_overlay: classifications.filter(c => c.metadata_verdict === 'LIKELY_OVERLAY').length,
      likely_standalone: classifications.filter(c => c.metadata_verdict === 'LIKELY_STANDALONE').length,
      likely_variant: classifications.filter(c => c.metadata_verdict === 'LIKELY_VARIANT').length,
      needs_vision: classifications.filter(c => c.metadata_verdict === 'NEEDS_VISION').length
    }
  };
}

// ─── Self-test ───

function selfTest() {
  console.log('🔧 overlay-classify.js self-test...');
  const checks = [];

  // Test pattern matching
  checks.push({ name: 'CLOSE_ICON ic_close', pass: matchesAny('ic_close', CLOSE_ICON_PATTERNS) });
  checks.push({ name: 'CLOSE_ICON X', pass: matchesAny('X', CLOSE_ICON_PATTERNS) });
  checks.push({ name: 'CLOSE_ICON btn_close', pass: matchesAny('btn_close', CLOSE_ICON_PATTERNS) });
  checks.push({ name: 'NOT_CLOSE back_white', pass: !matchesAny('back_white', CLOSE_ICON_PATTERNS) });
  checks.push({ name: 'KB space', pass: matchesAny('space', KEYBOARD_PATTERNS) });
  checks.push({ name: 'KB go', pass: matchesAny('go', KEYBOARD_PATTERNS) });
  checks.push({ name: 'OVERLAY_TITLE danh bạ', pass: OVERLAY_TITLE_PATTERNS.some(p => p.test('Danh bạ thụ hưởng')) });
  checks.push({ name: 'OVERLAY_TITLE xác thực', pass: OVERLAY_TITLE_PATTERNS.some(p => p.test('Xác thực giao dịch')) });
  checks.push({ name: 'OVERLAY_TITLE ngân hàng', pass: OVERLAY_TITLE_PATTERNS.some(p => p.test('Ngân hàng thụ hưởng')) });
  checks.push({ name: 'NOT_OVERLAY standard title', pass: !OVERLAY_TITLE_PATTERNS.some(p => p.test('Chuyển tiền nhanh 24/7')) });
  checks.push({ name: 'NAV_BACK back_white', pass: matchesAny('back_white', NAV_BACK_PATTERNS) });
  checks.push({ name: 'NOT_NAV ic_contact', pass: !matchesAny('ic_contact', NAV_BACK_PATTERNS) });

  const passed = checks.filter(c => c.pass).length;
  const total = checks.length;
  checks.forEach(c => console.log(`  ${c.pass ? '✅' : '❌'} ${c.name}`));
  console.log(`\nSelf-test: ${passed}/${total} passed`);
  process.exit(passed === total ? 0 : 1);
}

// ─── CLI ───

const args = process.argv.slice(2);

if (args[0] === '--test') {
  selfTest();
} else if (args[0] === '--help' || args.length < 2) {
  console.log(`
overlay-classify.js — Metadata pre-classifier for overlay detection

Usage:
  node overlay-classify.js <metadata_json> <section_node_id>
  node overlay-classify.js --test

Arguments:
  metadata_json    Path to Figma metadata JSON (depth≥3)
  section_node_id  Figma node ID of the section to classify (e.g., "22:5454")

Output: JSON to stdout with pre_classification[] per artboard
`);
  process.exit(args[0] === '--help' ? 0 : 1);
} else {
  const metaPath = path.resolve(args[0]);
  const sectionId = args[1];
  if (!fs.existsSync(metaPath)) {
    console.error(`❌ File not found: ${metaPath}`);
    process.exit(1);
  }
  const result = classify(metaPath, sectionId);
  console.log(JSON.stringify(result, null, 2));
}

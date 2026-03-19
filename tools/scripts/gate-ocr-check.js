#!/usr/bin/env node
// ============================================================
// Gate B: OCR Data Validation
// Purpose: Verify screen_inventory.json has OCR data for all
//          screens that have wireframe_images
// Usage:   node tools/scripts/gate-ocr-check.js <handoff_dir>
// Exit:    0 = all pass, 1 = missing OCR data
// ============================================================

'use strict';
const fs = require('fs');
const path = require('path');

const handoffDir = process.argv[2];
if (!handoffDir) {
  console.error('Usage: node gate-ocr-check.js <handoff_dir>');
  console.error('  handoff_dir: path to .handoff/ folder (or parent containing .handoff/)');
  process.exit(1);
}

// Resolve .handoff path
let resolvedDir = handoffDir;
if (!handoffDir.endsWith('.handoff')) {
  const sub = path.join(handoffDir, '.handoff');
  if (fs.existsSync(sub)) resolvedDir = sub;
}

const invPath = path.join(resolvedDir, 'screen_inventory.json');
const manifestPath = path.join(resolvedDir, 'handoff-manifest.json');

// Check files exist
if (!fs.existsSync(invPath)) {
  console.error(`❌ GATE-B FAIL: screen_inventory.json not found: ${invPath}`);
  console.log(JSON.stringify({ gate: 'B', status: 'FAIL', reason: 'screen_inventory.json not found' }));
  process.exit(1);
}

const inv = JSON.parse(fs.readFileSync(invPath, 'utf-8'));
const screens = inv.screens || [];

if (screens.length === 0) {
  console.error('❌ GATE-B FAIL: screens array is empty');
  console.log(JSON.stringify({ gate: 'B', status: 'FAIL', reason: 'screens array empty' }));
  process.exit(1);
}

const results = { pass: [], fail: [], warn: [] };

for (const screen of screens) {
  const id = screen.id || screen.screen_id || '(unknown)';
  const checks = [];

  // Check 1: wireframe_images exists and non-empty
  const hasWireframes = Array.isArray(screen.wireframe_images) && screen.wireframe_images.length > 0;
  checks.push({ field: 'wireframe_images', ok: hasWireframes });

  // Check 2: consumer_payload exists
  const hasPayload = screen.consumer_payload != null;
  checks.push({ field: 'consumer_payload', ok: hasPayload });

  // Check 3: ocr_full_table exists and non-empty (only if wireframes exist)
  const hasOcr = Array.isArray(screen.ocr_full_table) && screen.ocr_full_table.length > 0;
  checks.push({ field: 'ocr_full_table', ok: hasOcr, required: hasWireframes });

  // Check 4: ocr_round1_text exists (only if wireframes exist)
  const hasRound1 = Array.isArray(screen.ocr_round1_text) && screen.ocr_round1_text.length > 0;
  checks.push({ field: 'ocr_round1_text', ok: hasRound1, required: hasWireframes });

  // Check 5: ocr_screen_context exists
  const hasContext = typeof screen.ocr_screen_context === 'string' && screen.ocr_screen_context.length > 0;
  checks.push({ field: 'ocr_screen_context', ok: hasContext, required: hasWireframes });

  // Check 6: ocr_full_table coverage — must have ≥50% of ocr_round1_text items
  // Prevents "selective" OCR table where agent only writes representative entries
  const round1Len = hasRound1 ? screen.ocr_round1_text.length : 0;
  const ocrTableLen = hasOcr ? screen.ocr_full_table.length : 0;
  const coverageOk = round1Len === 0 || ocrTableLen >= Math.ceil(round1Len * 0.5);
  if (hasWireframes && hasRound1 && hasOcr && !coverageOk) {
    results.warn.push({ id, msg: `ocr_full_table coverage low: ${ocrTableLen}/${round1Len} (${Math.round(ocrTableLen/round1Len*100)}%, need ≥50%)` });
    console.error(`⚠️  WARN: ${id} — ocr_full_table coverage: ${ocrTableLen}/${round1Len} entries (${Math.round(ocrTableLen/round1Len*100)}%)`);
  }

  // Check 7: ocr_round2_icons exists (Phase 2g Round 2 — icon verification via vision)
  const hasRound2 = Array.isArray(screen.ocr_round2_icons) && screen.ocr_round2_icons.length > 0;
  if (hasWireframes && !hasRound2) {
    results.warn.push({ id, msg: 'missing ocr_round2_icons — OCR Round 2 (icon vision) not completed' });
    console.error(`⚠️  WARN: ${id} — missing ocr_round2_icons (Round 2 not run?)`);
  }

  // Evaluate
  const failures = checks.filter(c => !c.ok && c.required !== false);
  const missing = checks.filter(c => !c.ok).map(c => c.field);

  if (!hasWireframes) {
    // No wireframes → warn (not fatal, but images should exist)
    results.warn.push({ id, missing: ['wireframe_images'], msg: 'No wireframe_images — images not saved' });
    console.error(`⚠️  WARN: ${id} — missing wireframe_images (images not downloaded?)`);
  } else if (failures.length > 0) {
    results.fail.push({ id, missing });
    console.error(`❌ FAIL: ${id} — missing: ${missing.join(', ')}`);
  } else {
    results.pass.push({ id });
    console.error(`✅ OK: ${id}`);
  }
}

// Check manifest ocr_done consistency
if (fs.existsSync(manifestPath)) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  if (manifest.ocr_done === true && (results.fail.length > 0 || results.warn.length > 0)) {
    console.error('');
    console.error(`⚠️  INCONSISTENCY: manifest says ocr_done=true but ${results.fail.length} fails + ${results.warn.length} warns`);
    results.inconsistency = 'ocr_done:true but data missing';
  }
}

console.error('');
console.error('━━━ Gate B: OCR Data Validation ━━━');
console.error(`Pass: ${results.pass.length} | Fail: ${results.fail.length} | Warn: ${results.warn.length} | Total: ${screens.length}`);

const output = {
  gate: 'B',
  status: results.fail.length > 0 ? 'FAIL' : (results.warn.length > 0 ? 'WARN' : 'PASS'),
  pass: results.pass.length,
  fail: results.fail.length,
  warn: results.warn.length,
  total: screens.length,
  details: results,
};

console.log(JSON.stringify(output, null, 2));

if (results.fail.length > 0) {
  console.error(`❌ GATE-B FAILED: ${results.fail.length} screens lack required OCR data`);
  process.exit(1);
}

if (results.warn.length > 0) {
  console.error(`⚠️  GATE-B PASSED with ${results.warn.length} warnings (quality degradation — consider fixing)`);
  process.exit(0);
}

console.error('✅ GATE-B PASSED');
process.exit(0);

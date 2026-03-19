#!/usr/bin/env node
/**
 * DDL Prefetch — Query toàn bộ DDL capabilities cho UX Review
 * 
 * Chạy SAU Gate DDL PASS, TRƯỚC Skills A/B/C
 * Output: .handoff/ddl-context.json (structured DDL data cho agent)
 * 
 * Usage: node tools/scripts/ddl-prefetch.js <prd_folder> [--product <type>]
 * Example: node tools/scripts/ddl-prefetch.js coopbank/4 --product banking
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const PROJECT_ROOT = path.resolve(__dirname, '../..');
const DDL_API = path.join(PROJECT_ROOT, 'DDL/scripts/ddl-api.js');

// ─── Args ───
const args = process.argv.slice(2);
if (args.length < 1) {
  console.error('Usage: node tools/scripts/ddl-prefetch.js <prd_folder> [--product <type>]');
  process.exit(1);
}

const prdFolder = path.resolve(PROJECT_ROOT, args[0]);
const productIdx = args.indexOf('--product');
const productType = productIdx >= 0 ? args[productIdx + 1] : 'banking';
const modeFlag = args.includes('--dark') ? 'Dark' : 'Light';
const platformFlag = args.includes('--desktop') ? 'Desktop' : 'Mobile';

// ─── Helpers ───
function ddl(cmd) {
  try {
    const result = execSync(`node "${DDL_API}" ${cmd}`, { 
      encoding: 'utf-8', 
      cwd: PROJECT_ROOT,
      timeout: 15000
    });
    return JSON.parse(result.trim());
  } catch (e) {
    console.warn(`  ⚠️  DDL query failed: ${cmd}`);
    return null;
  }
}

function log(msg) {
  const ts = new Date().toLocaleTimeString('en-US', { hour12: false });
  console.log(`${ts} ${msg}`);
}

// ─── Phase 1: Component Detection ───────────────────────
log('━━━ DDL Prefetch ━━━');
log('');
log('Phase 1: Component Detection');

// Get all component schemas
const allComponents = ddl('--component all');
log(`  Found ${allComponents ? allComponents.length : 0} DDL component schemas`);

// Auto-detect from screen_inventory or prd folder
let screenComponents = {};
const inventoryPath = path.join(prdFolder, '.handoff', 'screen_inventory.json');
const handoffPath = path.join(prdFolder, '.handoff');

if (fs.existsSync(inventoryPath)) {
  const inventory = JSON.parse(fs.readFileSync(inventoryPath, 'utf-8'));
  const screens = inventory.screens || inventory;
  
  // Simple keyword-based component detection from screen data
  const componentKeywords = {
    'otp-input-1': ['otp', 'xác nhận', 'mã xác thực', 'sms otp', 'verify'],
    'text-input-1': ['nhập', 'input', 'form', 'tài khoản', 'số tiền', 'số thẻ'],
    'loading-spinner-1': ['loading', 'đang tải', 'xử lý', 'processing'],
    'empty-state-1': ['danh bạ', 'danh sách', 'lịch sử', 'contacts', 'empty'],
    'receipt-preview-1': ['kết quả', 'result', 'thành công', 'biên lai', 'receipt'],
    'app-header-1': ['header', 'nav', 'back', 'chuyển tiền', 'navigation'],
    'step-indicator-1': ['bước', 'step', 'wizard', 'progress'],
    'countdown-timer-1': ['countdown', 'timer', 'đếm ngược', 'hết hạn'],
    'numpad-1': ['numpad', 'bàn phím số', 'amount', 'keypad'],
    'password-strength-1': ['password', 'mật khẩu'],
    'network-banner-1': ['network', 'offline', 'kết nối'],
    'bottom-tab-bar-1': ['tab bar', 'bottom nav', 'trang chủ'],
  };
  
  (Array.isArray(screens) ? screens : []).forEach(screen => {
    const screenText = JSON.stringify(screen).toLowerCase();
    const matched = [];
    
    for (const [compId, keywords] of Object.entries(componentKeywords)) {
      if (keywords.some(kw => screenText.includes(kw))) {
        matched.push(compId);
      }
    }
    
    if (matched.length > 0) {
      screenComponents[screen.id || screen.screen_id] = matched;
    }
  });
  
  log(`  Screens with component matches: ${Object.keys(screenComponents).length}`);
}

// ─── Phase 2: Component Specs ───────────────────────────
log('');
log('Phase 2: Fetching Component Specs');

const matchedComponentIds = [...new Set(Object.values(screenComponents).flat())];
const componentSpecs = {};
const componentTokens = {};

matchedComponentIds.forEach(compId => {
  const spec = ddl(`--component ${compId}`);
  if (spec) {
    componentSpecs[compId] = spec;
    log(`  ✅ ${compId}: ${spec.schema?.description || 'loaded'}`);
    
    // Also resolve tokens
    const tokens = ddl(`--component-tokens ${compId} --mode ${modeFlag} --platform ${platformFlag}`);
    if (tokens) {
      componentTokens[compId] = tokens;
      log(`     Tokens: ${tokens.resolvedCount}/${tokens.totalRefs} resolved`);
    }
  }
});

// ─── Phase 3: UX Guidelines (full DB, not just CSV) ─────
log('');
log('Phase 3: UX Guidelines & Laws (from DDL DB)');

const guidelinesHigh = ddl('--guidelines --severity High');
const guidelinesCritical = ddl('--guidelines --source web-interface');
const allLaws = ddl('--ux-laws');

log(`  High-severity guidelines: ${guidelinesHigh?.length || 0}`);
log(`  Web-interface rules: ${guidelinesCritical?.length || 0} (incl. Critical)`);
log(`  UX Laws: ${allLaws?.length || 0}`);

// Extract laws with trigger_conditions
const lawsWithTriggers = (allLaws || []).filter(l => l.trigger_conditions);
log(`  Laws with auto-trigger: ${lawsWithTriggers.length}`);

// ─── Phase 4: WCAG Accessibility ────────────────────────
log('');
log('Phase 4: WCAG Accessibility Audit');

const wcag = ddl('--accessibility');
let wcagSummary = null;
if (wcag) {
  // Parse the text output if it's not JSON
  if (typeof wcag === 'string') {
    wcagSummary = { raw: wcag };
  } else {
    wcagSummary = wcag;
  }
  log(`  WCAG report loaded`);
}

// ─── Phase 5: Product Type Context ──────────────────────
log('');
log('Phase 5: Product Type Context');

const productContext = ddl(`--product-type ${productType}`);
if (productContext) {
  log(`  Product: ${productContext.product_name}`);
  log(`  Style: ${productContext.primary_style}`);
  log(`  Key: ${productContext.key_considerations?.substring(0, 80)}...`);
}

const colorPalette = ddl(`--color-palette ${productType}`);
if (colorPalette) {
  const palette = Array.isArray(colorPalette) ? colorPalette[0] : colorPalette;
  log(`  Palette: ${palette?.primary_color} / ${palette?.secondary_color} / bg ${palette?.bg_color}`);
}

// ─── Phase 6: Token Resolution (key tokens) ─────────────
log('');
log('Phase 6: Key Token Resolutions');

const keyTokenPaths = [
  'base.primary', 'base.destructive', 'base.ring', 'base.border',
  'base.background', 'base.foreground', 'base.muted-foreground',
  'base.card', 'base.secondary', 'spacing.2', 'spacing.4', 'spacing.6'
];

const resolvedTokens = {};
keyTokenPaths.forEach(tp => {
  const resolved = ddl(`--resolve ${tp} --mode ${modeFlag}`);
  if (resolved) {
    resolvedTokens[tp] = resolved;
  }
});
log(`  Resolved: ${Object.keys(resolvedTokens).length}/${keyTokenPaths.length} key tokens`);

// ─── Phase 7: Law Auto-Trigger Analysis ─────────────────
log('');
log('Phase 7: Law Auto-Trigger per Screen');

const lawMatches = {};
for (const [screenId, compIds] of Object.entries(screenComponents)) {
  const matches = [];
  const signals = compIds.join(' ');
  
  lawsWithTriggers.forEach(law => {
    try {
      const triggers = typeof law.trigger_conditions === 'string' 
        ? JSON.parse(law.trigger_conditions) 
        : law.trigger_conditions;
      
      let matched = false;
      
      // Check state_signal
      if (triggers.state_signal) {
        matched = triggers.state_signal.some(sig => signals.includes(sig));
      }
      
      // Check component_signal
      if (triggers.component_signal) {
        matched = matched || triggers.component_signal.some(sig => 
          compIds.some(c => c.includes(sig))
        );
      }
      
      // Check min_interactive (heuristic: form screens have 3+ interactive)
      if (triggers.min_interactive && compIds.includes('text-input-1')) {
        matched = true;
      }
      
      if (matched) {
        matches.push({
          law: law.name,
          category: law.category,
          statement: law.statement,
          trigger: triggers
        });
      }
    } catch (e) {
      // skip malformed trigger
    }
  });
  
  if (matches.length > 0) {
    lawMatches[screenId] = matches;
    log(`  ${screenId}: ${matches.map(m => m.law).join(', ')}`);
  }
}

// ─── Assemble Output ────────────────────────────────────
const output = {
  _generated: new Date().toISOString(),
  _script: 'ddl-prefetch v1.0.0',
  _product_type: productType,
  _mode: modeFlag,
  _platform: platformFlag,
  
  product_context: productContext,
  color_palette: colorPalette,
  
  screen_components: screenComponents,
  component_specs: componentSpecs,
  component_tokens: componentTokens,
  
  guidelines: {
    high_severity: guidelinesHigh,
    web_interface: guidelinesCritical,
    total_count: (guidelinesHigh?.length || 0) + (guidelinesCritical?.length || 0)
  },
  
  ux_laws: {
    all: allLaws,
    with_triggers: lawsWithTriggers,
    auto_matches_per_screen: lawMatches
  },
  
  wcag: wcagSummary,
  
  resolved_tokens: resolvedTokens,
  
  summary: {
    components_detected: matchedComponentIds.length,
    components_with_specs: Object.keys(componentSpecs).length,
    guidelines_total: (guidelinesHigh?.length || 0) + (guidelinesCritical?.length || 0),
    laws_total: allLaws?.length || 0,
    laws_auto_triggered: Object.values(lawMatches).reduce((sum, m) => sum + m.length, 0),
    tokens_resolved: Object.keys(resolvedTokens).length
  }
};

// ─── Write Output ───────────────────────────────────────
if (!fs.existsSync(handoffPath)) {
  fs.mkdirSync(handoffPath, { recursive: true });
}

const outputPath = path.join(handoffPath, 'ddl-context.json');
fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));

log('');
log('━━━ DDL Prefetch Complete ━━━');
log('');
log(`Output: ${outputPath}`);
log(`Components: ${output.summary.components_detected} detected → ${output.summary.components_with_specs} specs loaded`);
log(`Guidelines: ${output.summary.guidelines_total} (incl. web-interface Critical)`);
log(`Laws: ${output.summary.laws_total} total, ${output.summary.laws_auto_triggered} auto-triggered`);
log(`Tokens: ${output.summary.tokens_resolved} key tokens resolved`);
log('');

// Exit code 0 = success
process.exit(0);

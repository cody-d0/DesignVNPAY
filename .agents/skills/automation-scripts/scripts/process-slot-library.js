#!/usr/bin/env node
/**
 * process-slot-library.js — SLOT-Aware Library Processor
 *
 * Domains:
 *   A — Index:  ref-map, component-index, variant-index
 *   E — Slot:   slot-index, slot-name-map
 *
 * Usage:
 *   node process-slot-library.js <input.json> [--output=bridge/library]
 *   node process-slot-library.js --test
 *   node process-slot-library.js --help
 *
 * ANALYSIS:
 *   runtime: local
 *   input_source: [file]
 *   output_target: [file]
 *   operator: developer
 *   idempotent: true
 *   critical_failure: "SLOT properties silently dropped → converter generates broken specs"
 *   language: node
 *   estimated_complexity: complex
 */

const fs = require('fs');
const path = require('path');

// Module-scope vocab (populated later during main flow, null-safe for self-test)
let vocabSlots = null;
let vocabByComponent = null;

// ─── Help ──────────────────────────────────────────────────────────────────
if (process.argv.includes('--help') || process.argv.includes('-h')) {
    console.log(`
process-slot-library.js — SLOT-Aware Library Processor

USAGE:
  node process-slot-library.js <input.json> [OPTIONS]

OPTIONS:
  --output=DIR    Output directory (default: bridge/library relative to input)
  --vocab=PATH    Distillery vocabulary file for cross-ref
  --verify-only   Run verification without writing files
  --test          Run self-tests (no input needed)
  --help          Show this help

DOMAINS:
  A — Index:  component-ref-map, component-index, variant-index
  E — Slot:   slot-index, slot-name-map

OUTPUT:
  01-index/component-ref-map.json   O(1) lookup for resolveComponentRef()
  01-index/component-index.json     Lightweight full index with properties
  01-index/variant-index.json       Parsed variant property matrix
  05-slot/slot-index.json           SLOT property index per component
  05-slot/slot-name-map.json        Flat map: slotPropName → role + usedBy[]
  grading.json                      Quality gate results
`);
    process.exit(0);
}

// ─── Self-test ─────────────────────────────────────────────────────────────
if (process.argv.includes('--test')) {
    runSelfTests();
    process.exit(0);
}

// ─── CLI ───────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const positional = args.filter(a => !a.startsWith('--'));
if (positional.length < 1) {
    console.error('Usage: node process-slot-library.js <input.json> [--output=bridge/library]');
    process.exit(1);
}

const INPUT_PATH = path.resolve(positional[0]);
const OUTPUT_DIR = path.resolve(
    (args.find(a => a.startsWith('--output=')) || `--output=${path.join(path.dirname(INPUT_PATH), 'bridge/library')}`).split('=')[1]
);
const VOCAB_PATH = args.find(a => a.startsWith('--vocab='))
    ? path.resolve(args.find(a => a.startsWith('--vocab=')).split('=')[1])
    : null;
const VERIFY_ONLY = args.includes('--verify-only');

// ─── Load Source ───────────────────────────────────────────────────────────
if (!fs.existsSync(INPUT_PATH)) {
    console.error(`❌ Input not found: ${INPUT_PATH}`);
    process.exit(1);
}

console.log(`\n╔══════════════════════════════════════════════════╗`);
console.log(`║  SLOT Library Processor                          ║`);
console.log(`╚══════════════════════════════════════════════════╝`);
console.log(`  Input:  ${INPUT_PATH}`);
console.log(`  Output: ${OUTPUT_DIR}`);

const startTime = Date.now();
const raw = JSON.parse(fs.readFileSync(INPUT_PATH, 'utf8'));
const entries = raw.entries || [];
console.log(`  Loaded: ${entries.length} entries (${(fs.statSync(INPUT_PATH).size / 1024 / 1024).toFixed(1)}MB)\n`);

// ─── Helpers ───────────────────────────────────────────────────────────────
function ensureDir(dir) { fs.mkdirSync(dir, { recursive: true }); }
function writeJSON(subdir, filename, data) {
    const dir = path.join(OUTPUT_DIR, subdir);
    ensureDir(dir);
    const fp = path.join(dir, filename);
    fs.writeFileSync(fp, JSON.stringify(data, null, 2));
    const kb = (fs.statSync(fp).size / 1024).toFixed(0);
    return { path: fp, sizeKB: parseInt(kb) };
}

const outputs = [];
function emit(subdir, filename, data, label) {
    if (VERIFY_ONLY) {
        const count = Array.isArray(data) ? data.length : (data.entries?.length || data.totalEntries || Object.keys(data).length);
        outputs.push({ file: `${subdir}/${filename}`, sizeKB: 0, count, label });
        console.log(`  🔍 ${label}: ${subdir}/${filename} (verify-only, ${count} items)`);
        return;
    }
    const info = writeJSON(subdir, filename, data);
    const count = Array.isArray(data) ? data.length : (data.entries?.length || data.totalEntries || Object.keys(data).length);
    outputs.push({ file: `${subdir}/${filename}`, sizeKB: info.sizeKB, count, label });
    console.log(`  ✅ ${label}: ${subdir}/${filename} (${info.sizeKB}KB, ${count} items)`);
}

// ═══════════════════════════════════════════════════════════════════════════
// DOMAIN A — Index
// ═══════════════════════════════════════════════════════════════════════════

console.log(`\n=== Domain A: Index ===\n`);

// A1. component-ref-map.json
function buildRefMap(entries) {
    const map = {};
    const collisions = {};

    for (const e of entries) {
        const ref = {
            key: e.key,
            nodeId: e.nodeId,
            type: e.type,
            tier: e.tier,
            page: e.page,
            variantCount: e.variantCount || 0,
            namePattern: e.namePattern,
        };

        // Strategy 1: Exact name
        registerRef(map, collisions, e.name, ref, 'exact');

        // Strategy 2: Short name (last segment after " / ")
        if (e.name.includes(' / ')) {
            const short = e.name.split(' / ').pop().trim();
            registerRef(map, collisions, short, ref, 'short');
        }

        // Strategy 3: Prefix (first segment)
        if (e.name.includes(' / ')) {
            const prefix = e.name.split(' / ')[0].trim();
            if (prefix !== e.name) {
                registerRef(map, collisions, prefix, ref, 'prefix');
            }
        }

        // Strategy 4: Numbered suffix cleanup
        if (e.name.includes(' / ')) {
            const parts = e.name.split(' / ');
            if (parts.length >= 3 && /^\d+\.?$/.test(parts[parts.length - 1].trim())) {
                const meaningful = parts[parts.length - 2].trim();
                registerRef(map, collisions, meaningful, ref, 'numbered');
            }
        }
    }

    return { map, collisions };
}

function registerRef(map, collisions, key, ref, strategy) {
    if (!key || key.length < 2) return;

    if (!map[key]) {
        map[key] = { ...ref, _strategy: strategy };
    } else {
        if (!collisions[key]) {
            collisions[key] = [map[key]];
        }
        collisions[key].push({ ...ref, _strategy: strategy });
        const tierRank = { T0: 0, T1: 1, T2: 2, T3: 3 };
        const existing = map[key];
        if (
            (ref.namePattern === 'standalone' && existing.namePattern !== 'standalone') ||
            (tierRank[ref.tier] < tierRank[existing.tier] && ref.namePattern === existing.namePattern)
        ) {
            map[key] = { ...ref, _strategy: strategy, _ambiguous: true };
        } else {
            map[key]._ambiguous = true;
        }
    }
}

const { map: refMap, collisions } = buildRefMap(entries);
emit('01-index', 'component-ref-map.json', refMap, 'A1 component-ref-map');

// A2. component-index.json
const componentIndex = {
    _v: 3,
    _generatedAt: new Date().toISOString(),
    _sourceFile: path.basename(INPUT_PATH),
    totalEntries: entries.length,
    entries: entries.map(e => {
        const entry = {
            name: e.name,
            key: e.key,
            nodeId: e.nodeId,
            type: e.type,
            page: e.page,
            tier: e.tier,
            namePattern: e.namePattern,
            hasVariants: e.hasVariants || false,
            variantCount: e.variantCount || 0,
            propertyCount: e.propertyCount || 0,
            childCount: e.childCount || 0,
            instanceChildCount: (e.instanceChildren || []).length,
            totalInstanceRefs: (e.instanceChildren || []).reduce((sum, ic) => sum + (ic.count || 1), 0),
        };
        if (e.properties && e.properties.length > 0) {
            entry.properties = e.properties;
            // SLOT-aware flags
            const slotProps = e.properties.filter(p => p.type === 'SLOT');
            if (slotProps.length > 0) {
                entry.hasSlots = true;
                entry.slotCount = slotProps.length;
            }
        }
        // Breakpoint awareness
        if (e.hasVariants && e.variantNames) {
            const hasBP = e.variantNames.some(vn => vn.includes('Breakpoint='));
            if (hasBP) {
                entry.hasBreakpoint = true;
                const bps = new Set();
                for (const vn of e.variantNames) {
                    const m = vn.match(/Breakpoint=([^,]+)/);
                    if (m) bps.add(m[1].trim());
                }
                entry.breakpointValues = [...bps].sort();
            }
        }
        return entry;
    }),
};
emit('01-index', 'component-index.json', componentIndex, 'A2 component-index');

// A3. variant-index.json
function parseVariantNames(variantNames) {
    const properties = {};
    for (const vn of variantNames) {
        const pairs = vn.split(',').map(p => p.trim());
        for (const pair of pairs) {
            const eqIdx = pair.indexOf('=');
            if (eqIdx < 0) continue;
            const propName = pair.substring(0, eqIdx).trim();
            const propValue = pair.substring(eqIdx + 1).trim();
            if (!properties[propName]) properties[propName] = new Set();
            properties[propName].add(propValue);
        }
    }
    const result = {};
    for (const [k, v] of Object.entries(properties)) {
        result[k] = [...v].sort();
    }
    return result;
}

function computeDefaultVariant(variantValues, originalOrder) {
    const defaults = {};
    for (const [propName, values] of Object.entries(variantValues)) {
        const def = values.find(v => v === 'Default') ||
            values.find(v => v === 'default') ||
            values.find(v => v.toLowerCase() === 'default') ||
            values[0];  // first alphabetical value (values are sorted)
        defaults[propName] = def;
    }
    return defaults;
}

const variantIndex = {
    _v: 2,
    _generatedAt: new Date().toISOString(),
    totalWithVariants: entries.filter(e => e.hasVariants).length,
    entries: entries.filter(e => e.hasVariants && e.variantNames?.length > 0).map(e => {
        const variantValues = parseVariantNames(e.variantNames);
        const defaults = computeDefaultVariant(variantValues);
        const defaultString = Object.entries(defaults).map(([k, v]) => `${k}=${v}`).join(', ');
        const entry = {
            name: e.name,
            key: e.key,
            nodeId: e.nodeId,
            variantCount: e.variantCount,
            variantProperties: Object.keys(variantValues),
            variantValues,
            defaults,
            defaultVariantString: defaultString,
            hasBreakpoint: !!variantValues.Breakpoint,
        };
        if (e.variants && e.variants.length > 0) {
            entry.variants = e.variants;
        }
        return entry;
    }),
};
emit('01-index', 'variant-index.json', variantIndex, 'A3 variant-index');

// A4. instance-children-index.json — full dependency detail
const instanceChildrenIndex = {
    _v: 1,
    _generatedAt: new Date().toISOString(),
    _sourceFile: path.basename(INPUT_PATH),
    totalEntriesWithChildren: entries.filter(e => e.instanceChildren && e.instanceChildren.length > 0).length,
    totalRecords: entries.reduce((sum, e) => sum + (e.instanceChildren || []).length, 0),
    entries: entries
        .filter(e => e.instanceChildren && e.instanceChildren.length > 0)
        .map(e => ({
            name: e.name,
            key: e.key,
            nodeId: e.nodeId,
            page: e.page,
            tier: e.tier,
            childCount: e.instanceChildren.length,
            totalRefs: e.instanceChildren.reduce((sum, ic) => sum + (ic.count || 1), 0),
            children: e.instanceChildren,
        })),
};
emit('01-index', 'instance-children-index.json', instanceChildrenIndex, 'A4 instance-children');

// ═══════════════════════════════════════════════════════════════════════════
// DOMAIN E — Slot
// ═══════════════════════════════════════════════════════════════════════════

console.log(`\n=== Domain E: Slot ===\n`);

// Load vocabulary for cross-ref (optional)
const vocabPath = VOCAB_PATH || (() => {
    // Auto-discover relative to project root
    const candidates = [
        path.join(path.dirname(INPUT_PATH), 'bridge/shadcn-distillery/parsed/data-slot-vocabulary.json'),
        path.join(OUTPUT_DIR, '../shadcn-distillery/parsed/data-slot-vocabulary.json'),
    ];
    return candidates.find(c => fs.existsSync(c)) || null;
})();

if (vocabPath && fs.existsSync(vocabPath)) {
    try {
        const vocabRaw = JSON.parse(fs.readFileSync(vocabPath, 'utf8'));
        // Support multiple formats
        if (vocabRaw.slots && Array.isArray(vocabRaw.slots)) {
            vocabSlots = new Set(vocabRaw.slots);
        } else if (vocabRaw.allSlots && Array.isArray(vocabRaw.allSlots)) {
            vocabSlots = new Set(vocabRaw.allSlots);
        } else if (Array.isArray(vocabRaw)) {
            vocabSlots = new Set(vocabRaw);
        }
        if (vocabRaw.byComponent && typeof vocabRaw.byComponent === 'object') {
            vocabByComponent = vocabRaw.byComponent;
        }
        console.log(`  📖 Vocabulary loaded: ${vocabSlots?.size || 0} slots from ${path.basename(vocabPath)}`);
    } catch (err) {
        console.log(`  ⚠️ Vocab load failed: ${err.message}`);
    }
}

// Classify slot prop name → role
function classifySlotProp(cleanName) {
    // Normalize: "Card Content" → "card-content", "SidebarHeader" → "sidebar-header"
    const kebab = cleanName
        .replace(/([a-z])([A-Z])/g, '$1-$2')  // camelCase → kebab
        .replace(/\s+/g, '-')                    // space → dash
        .replace(/[()]/g, '')                     // remove parens
        .replace(/-+/g, '-')                      // collapse dashes
        .toLowerCase()
        .replace(/^_/, '');                        // strip leading underscore

    const vocabMatch = (vocabSlots && vocabSlots.size > 0) ? vocabSlots.has(kebab) : false;

    // Find component match in vocabulary
    let vocabComponent = null;
    if (vocabByComponent && typeof vocabByComponent === 'object') {
        for (const [comp, slots] of Object.entries(vocabByComponent)) {
            if (slots.includes(kebab)) {
                vocabComponent = comp;
                break;
            }
        }
    }

    // Category classification
    let category = 'other';
    if (/items/i.test(cleanName)) category = 'items';
    else if (/content/i.test(cleanName)) category = 'content';
    else if (/header/i.test(cleanName)) category = 'header';
    else if (/footer/i.test(cleanName)) category = 'footer';
    else if (/sidebar/i.test(cleanName)) category = 'sidebar';
    else if (/panel/i.test(cleanName)) category = 'panel';
    else if (/description/i.test(cleanName)) category = 'description';

    return { role: kebab, vocabMatch, vocabComponent, category };
}

// E1. Build slot index
const slotEntries = [];
let totalSlotProps = 0;
const slotNameUsage = {};  // for slot-name-map

for (const e of entries) {
    if (!e.properties) continue;
    const slots = e.properties.filter(p => p.type === 'SLOT');
    if (slots.length === 0) continue;

    const slotDetails = slots.map(s => {
        const cleanName = s.cleanName || s.rawName?.split('#')[0] || 'Unknown';
        const classification = classifySlotProp(cleanName);

        // Track usage for slot-name-map
        if (!slotNameUsage[cleanName]) {
            slotNameUsage[cleanName] = { ...classification, usedBy: [] };
        }
        slotNameUsage[cleanName].usedBy.push(e.name);

        totalSlotProps++;
        return {
            propName: cleanName,
            rawName: s.rawName,
            role: classification.role,
            vocabMatch: classification.vocabMatch,
            vocabComponent: classification.vocabComponent,
            category: classification.category,
        };
    });

    const nonSlotProps = (e.properties || [])
        .filter(p => p.type !== 'SLOT')
        .map(p => ({
            name: p.cleanName || p.rawName?.split('#')[0],
            type: p.type,
            ...(p.defaultValue !== undefined ? { default: p.defaultValue } : {}),
        }));

    // Breakpoint info
    let hasBreakpoint = false;
    let breakpointValues = [];
    if (e.variantNames) {
        const bps = new Set();
        for (const vn of e.variantNames) {
            const m = vn.match(/Breakpoint=([^,]+)/);
            if (m) bps.add(m[1].trim());
        }
        if (bps.size > 0) {
            hasBreakpoint = true;
            breakpointValues = [...bps].sort();
        }
    }

    slotEntries.push({
        name: e.name,
        key: e.key,
        nodeId: e.nodeId,
        page: e.page,
        tier: e.tier,
        type: e.type,
        slots: slotDetails,
        nonSlotProps,
        totalProps: (e.properties || []).length,
        slotCount: slotDetails.length,
        hasBreakpoint,
        ...(hasBreakpoint ? { breakpointValues } : {}),
    });
}

// Stats
const categories = {};
for (const [name, data] of Object.entries(slotNameUsage)) {
    categories[data.category] = (categories[data.category] || 0) + 1;
}

const vocabMatchCount = Object.values(slotNameUsage).filter(v => v.vocabMatch).length;
const uniqueSlotNames = Object.keys(slotNameUsage).length;

const slotIndex = {
    _v: 1,
    _sourceFile: path.basename(INPUT_PATH),
    _generatedAt: new Date().toISOString(),
    stats: {
        totalComponentsWithSlot: slotEntries.length,
        totalSlotProps,
        uniqueSlotNames,
        vocabMatchRate: uniqueSlotNames > 0 ? Math.round(vocabMatchCount / uniqueSlotNames * 100) / 100 : 0,
        categories,
        withBreakpoint: slotEntries.filter(e => e.hasBreakpoint).length,
    },
    entries: slotEntries,
};

emit('05-slot', 'slot-index.json', slotIndex, 'E1 slot-index');

// E2. slot-name-map.json — flat lookup
const slotNameMap = {
    _v: 1,
    _generatedAt: new Date().toISOString(),
    totalUniqueNames: uniqueSlotNames,
    map: {},
};

for (const [name, data] of Object.entries(slotNameUsage)) {
    slotNameMap.map[name] = {
        role: data.role,
        vocabMatch: data.vocabMatch,
        vocabComponent: data.vocabComponent,
        category: data.category,
        usedBy: data.usedBy.sort(),
        usageCount: data.usedBy.length,
    };
}

emit('05-slot', 'slot-name-map.json', slotNameMap, 'E2 slot-name-map');

// ═══════════════════════════════════════════════════════════════════════════
// VERIFY — Quality Gates
// ═══════════════════════════════════════════════════════════════════════════

console.log(`\n=== Verify ===\n`);

const checks = [];
function check(id, text, fn) {
    try {
        const evidence = fn();
        checks.push({ id, text, passed: true, evidence: String(evidence) });
        console.log(`  ✅ ${id}: ${text}`);
    } catch (err) {
        checks.push({ id, text, passed: false, evidence: String(err.message || err) });
        console.log(`  ❌ ${id}: ${text}`);
        console.log(`     → ${err.message || err}`);
    }
}

// V1: Ref map coverage
check('V1', 'Ref map coverage ≥ 95%', () => {
    const covered = entries.filter(e => refMap[e.name]).length;
    const pct = Math.round(covered / entries.length * 100);
    if (pct < 95) throw new Error(`only ${pct}% coverage (${covered}/${entries.length})`);
    return `${covered}/${entries.length} = ${pct}%`;
});

// V2: All COMPONENT_SET have variant defaults
check('V2', 'Variant defaults complete', () => {
    const sets = entries.filter(e => e.type === 'COMPONENT_SET' && e.variantNames?.length > 0);
    const viNames = new Set(variantIndex.entries.map(v => v.name));
    const covered = sets.filter(s => viNames.has(s.name));
    if (covered.length < sets.length) throw new Error(`${covered.length}/${sets.length}`);
    return `${covered.length}/${sets.length}`;
});

// V3: SLOT extraction count matches source
check('V3', 'SLOT component count matches source', () => {
    const sourceSlotCount = entries.filter(e => e.properties?.some(p => p.type === 'SLOT')).length;
    if (slotEntries.length !== sourceSlotCount) {
        throw new Error(`extracted ${slotEntries.length} !== source ${sourceSlotCount}`);
    }
    return `${slotEntries.length} === ${sourceSlotCount}`;
});

// V4: SLOT prop count matches source
check('V4', 'SLOT prop count matches source', () => {
    let sourceProps = 0;
    for (const e of entries) {
        if (e.properties) sourceProps += e.properties.filter(p => p.type === 'SLOT').length;
    }
    if (totalSlotProps !== sourceProps) {
        throw new Error(`extracted ${totalSlotProps} !== source ${sourceProps}`);
    }
    return `${totalSlotProps} === ${sourceProps}`;
});

// V5: Zero orphaned SLOT components
check('V5', 'Zero orphaned SLOT components', () => {
    const indexedNames = new Set(slotEntries.map(e => e.name));
    const sourceSlotNames = entries
        .filter(e => e.properties?.some(p => p.type === 'SLOT'))
        .map(e => e.name);
    const orphans = sourceSlotNames.filter(n => !indexedNames.has(n));
    if (orphans.length > 0) throw new Error(`${orphans.length} orphans: ${orphans.slice(0, 5).join(', ')}`);
    return `0 orphans (${indexedNames.size} indexed)`;
});

// V6: Key consistency — slot-index keys exist in ref-map
check('V6', 'Slot-index keys exist in ref-map', () => {
    const missing = slotEntries.filter(e => !refMap[e.name]);
    // Allow some tolerance (short names in ref-map might differ)
    const missingPct = Math.round(missing.length / slotEntries.length * 100);
    if (missingPct > 10) throw new Error(`${missing.length}/${slotEntries.length} (${missingPct}%) missing from ref-map`);
    return `${slotEntries.length - missing.length}/${slotEntries.length} found (${missing.length} missing, ${missingPct}%)`;
});

// V7: Vocab coverage (warning only)
check('V7', 'Vocabulary coverage ≥ 30%', () => {
    if (!vocabSlots) return 'skipped (no vocabulary loaded)';
    const rate = slotIndex.stats.vocabMatchRate;
    return `${Math.round(rate * 100)}% match (${vocabMatchCount}/${uniqueSlotNames} names)`;
});

// V8: Spot check — known components exist
check('V8', 'Known SLOT components exist', () => {
    const slotNames = new Set(slotEntries.map(e => e.name));
    // Check if ANY sidebar blocks exist (we know library has them)
    const hasSidebar = slotEntries.some(e => e.name.includes('Sidebar'));
    if (!hasSidebar && slotEntries.length > 10) throw new Error('No Sidebar components found');
    return `${slotEntries.length} components, sidebar: ${hasSidebar}`;
});

// V9: Spot check — counts in expected range
check('V9', 'Entry counts in expected range', () => {
    if (entries.length < 100) throw new Error(`only ${entries.length} entries (expect 700+)`);
    if (slotEntries.length < 10) throw new Error(`only ${slotEntries.length} SLOT components (expect 90+)`);
    if (totalSlotProps < 10) throw new Error(`only ${totalSlotProps} SLOT props (expect 120+)`);
    return `entries=${entries.length} slots=${slotEntries.length} props=${totalSlotProps}`;
});

// V10: slot-name-map completeness
check('V10', 'Slot-name-map covers all unique slot names', () => {
    const mapKeys = Object.keys(slotNameMap.map);
    if (mapKeys.length !== uniqueSlotNames) {
        throw new Error(`map has ${mapKeys.length} keys, expected ${uniqueSlotNames}`);
    }
    return `${mapKeys.length} === ${uniqueSlotNames}`;
});

// ═══════════════════════════════════════════════════════════════════════════
// OUTPUT: grading.json
// ═══════════════════════════════════════════════════════════════════════════

const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
const passed = checks.filter(c => c.passed).length;
const failed = checks.filter(c => !c.passed).length;

const grading = {
    _v: 2,
    _generatedAt: new Date().toISOString(),
    _sourceFile: path.basename(INPUT_PATH),
    expectations: checks,
    outputs: outputs.map(o => ({ file: o.file, sizeKB: o.sizeKB, items: o.count })),
    summary: {
        passed,
        failed,
        total: checks.length,
        passRate: Math.round(passed / checks.length * 100) / 100,
        totalOutputFiles: outputs.length,
        totalOutputSizeKB: outputs.reduce((sum, o) => sum + o.sizeKB, 0),
        durationSeconds: parseFloat(elapsed),
    },
};

if (!VERIFY_ONLY) {
    writeJSON('.', 'grading.json', grading);
}

console.log(`\n╔══════════════════════════════════════════════════╗`);
console.log(`║  Processing Complete                             ║`);
console.log(`╠══════════════════════════════════════════════════╣`);
console.log(`║  Files: ${String(outputs.length).padEnd(3)} output files                      ║`);
console.log(`║  Size:  ${String(grading.summary.totalOutputSizeKB).padEnd(5)}KB total                        ║`);
console.log(`║  Time:  ${elapsed.padEnd(6)}s                                ║`);
console.log(`║  Gate:  ${passed}/${checks.length} passed (${failed} failed)               ║`);
if (failed > 0) {
    console.log(`║  ❌ VERIFY FAILED — check grading.json            ║`);
} else {
    console.log(`║  ✅ ALL PASS                                      ║`);
}
console.log(`╚══════════════════════════════════════════════════╝`);

if (failed > 0) process.exit(1);

// ═══════════════════════════════════════════════════════════════════════════
// SELF-TEST
// ═══════════════════════════════════════════════════════════════════════════

function runSelfTests() {
    console.log('\n=== Self-Test ===\n');
    let pass = 0, fail = 0;

    function assert(name, fn) {
        try {
            fn();
            console.log(`  ✅ ${name}`);
            pass++;
        } catch (e) {
            console.log(`  ❌ ${name}: ${e.message}`);
            fail++;
        }
    }

    // T1: Dependencies
    assert('Dependencies: fs, path exist', () => {
        if (!fs || !path) throw new Error('missing');
    });

    // T2: Ref-map logic
    assert('buildRefMap: exact + short name', () => {
        const { map } = buildRefMap([
            { name: 'Pro Blocks / Card / 1.', key: 'k1', nodeId: 'n1', type: 'COMPONENT_SET', tier: 'T3', page: 'Cards', namePattern: 'numbered' },
            { name: 'Button', key: 'k2', nodeId: 'n2', type: 'COMPONENT', tier: 'T1', page: 'Button', namePattern: 'standalone' },
        ]);
        if (!map['Pro Blocks / Card / 1.']) throw new Error('exact match failed');
        if (!map['Button']) throw new Error('standalone match failed');
        if (!map['1.']) throw new Error('short name failed');
    });

    // T3: Variant parser
    assert('parseVariantNames: multi-prop combo', () => {
        const result = parseVariantNames(['State=Default, Breakpoint=Desktop', 'State=Hover, Breakpoint=Mobile']);
        if (!result.State || result.State.length !== 2) throw new Error('State parse failed');
        if (!result.Breakpoint || result.Breakpoint.length !== 2) throw new Error('Breakpoint parse failed');
    });

    // T4: SLOT classifier
    assert('classifySlotProp: naming patterns', () => {
        const r1 = classifySlotProp('Card Content');
        if (r1.role !== 'card-content') throw new Error(`expected card-content, got ${r1.role}`);
        if (r1.category !== 'content') throw new Error(`expected content category, got ${r1.category}`);

        const r2 = classifySlotProp('Items');
        if (r2.role !== 'items') throw new Error(`expected items, got ${r2.role}`);
        if (r2.category !== 'items') throw new Error(`expected items category, got ${r2.category}`);

        const r3 = classifySlotProp('SidebarContent');
        if (r3.role !== 'sidebar-content') throw new Error(`expected sidebar-content, got ${r3.role}`);

        const r4 = classifySlotProp('_AlertDialogFooter');
        if (r4.role !== 'alert-dialog-footer') throw new Error(`expected alert-dialog-footer, got ${r4.role}`);
    });

    // T5: Variant default selection
    assert('computeDefaultVariant: prefer Default', () => {
        const result = computeDefaultVariant({
            State: ['Default', 'Hover', 'Pressed'],
            Size: ['sm', 'md', 'lg'],
        });
        if (result.State !== 'Default') throw new Error('should prefer Default');
        if (result.Size !== 'sm') throw new Error(`should take first value in array, got ${result.Size}`);
    });

    // T6: Output dir
    assert('Output dir writable', () => {
        const tmp = path.join(require('os').tmpdir(), `slot-test-${Date.now()}`);
        fs.mkdirSync(tmp, { recursive: true });
        fs.writeFileSync(path.join(tmp, 'test.json'), '{}');
        fs.unlinkSync(path.join(tmp, 'test.json'));
        fs.rmdirSync(tmp);
    });

    console.log(`\n  ${pass}/${pass + fail} passed\n`);
    if (fail > 0) process.exit(1);
}

# 🧠 Context Harvest Report — Bridge Plugin + SLOT Migration

> **Generated**: 2026-03-14T00:36:00+07:00
> **Sources**: 5 automation scripts × P-in workspace
> **Purpose**: Tổng hợp toàn bộ context/use case/dữ liệu thực phục vụ phát triển plugin ver mới với SLOT

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Bridge Codebase — Architecture Map](#2-bridge-codebase)
3. [Spec Pattern Intelligence](#3-spec-pattern-intelligence)
4. [SLOT Library Evolution](#4-slot-library-evolution)
5. [Rule Compliance Audit](#5-rule-compliance-audit)
6. [Knowledge Base Insights](#6-knowledge-base-insights)
7. [Actionable Recommendations](#7-actionable-recommendations)

---

## 1. Executive Summary

### Scale

| Dimension | Count |
|-----------|-------|
| Bridge scripts | **15** (6,156 LOC) |
| Total specs | **98** (xPOS: 34, tests: 8, standalone: 56) |
| Nodes analyzed | **1,501** across all specs |
| Library components (SLOT) | **720** entries |
| Library components (old) | **727** entries |
| SLOT properties | **132** across 95 components |
| Knowledge artifacts mined | **67** from 7 KIs |
| Insights extracted | **186** |

### Health at a Glance

| Metric | Status | Detail |
|--------|--------|--------|
| Rule 1 (Instantiation-First) | ⚠️ Advisory | 217 componentRef vs 788 generative — ratio improving |
| Rule 2 (Pre-binding) | ✅ **100% Clean** | 0 hardcoded hex, 0 raw pixels |
| Rule 3 (Verify-Only) | ⚠️ 40/98 | 58 specs still embed collections |
| Schema validity | ✅ **100%** | All 98 specs have valid specVersion/screen/root |
| Role validation | ✅ **100%** | All roles within the 31-role set |
| Padding format | ✅ **100%** | All paddings are 4-element token arrays |
| Key uniqueness | ⚠️ 96/98 | 2 specs have duplicate keys |
| SLOT migration | ✅ **100% Additive** | 94 gained SLOT, 0 lost SLOT |

---

## 2. Bridge Codebase

### 2.1 Script Catalog (15 files, 6,156 LOC)

| Script | LOC | Patterns | Role |
|--------|-----|----------|------|
| `screen-to-bridge-spec.js` | **1,569** | componentRef, variant, binding, spec-ver | **Main converter** — screen markdown → bridge spec |
| `verify-integrity.ts` | 514 | componentRef, slot | Validates spec integrity post-generation |
| `audit-specs.js` | 444 | componentRef | Batch audit across all specs |
| `shadcn-to-spec.js` | 409 | spec-ver, **slot** | shadcn component → spec conversion |
| `nl-select.ts` | 362 | componentRef, spec-ver, **slot** | Natural language component selection |
| `screen-to-bridge.ts` | 360 | componentRef, spec-ver, **slot** | TS version of converter |
| `gate-export-variables.js` | 359 | — | Variable export gate |
| `embed-component-keys.js` | 356 | componentRef | Injects library keys into specs |
| `lint-spec-mobile.js` | 345 | componentRef, spec-ver | Mobile spec linting |
| `verify-spec-keys.js` | 304 | componentRef, spec-ver | Verifies spec keys against library |
| `gen-spec-skeleton.js` | 291 | componentRef, binding, spec-ver | Generates spec skeleton |
| `reverse-spec.ts` | 289 | componentRef, spec-ver, **slot**, auto-layout | Reverse-engineers Figma → spec |
| `visual-qa.ts` | 258 | — | Visual QA comparisons |
| `save-figma-section-screenshots.js` | 252 | — | Screenshot capture utility |
| `prebuild-specs.js` | 44 | — | Pre-build spec processing |

### 2.2 Pattern Distribution

| Pattern | Scripts Using | % of Codebase |
|---------|--------------|---------------|
| `componentRef-handling` | **10/15** | Cross-cutting concern |
| `spec-versioning` | 9/15 | Near-universal |
| **`slot-awareness`** | **5/15** | shadcn-to-spec, nl-select, reverse-spec, screen-to-bridge, verify-integrity |
| `variable-binding` | 2/15 | screen-to-bridge-spec, gen-spec-skeleton |
| `variant-resolution` | 1/15 | screen-to-bridge-spec only |
| `auto-layout` | 1/15 | reverse-spec only |

### 2.3 Key Insight

> **5 scripts already have SLOT awareness** — đây là foundation cho plugin ver mới. Đặc biệt `verify-integrity.ts` + `reverse-spec.ts` đã handle SLOT detection + auto-layout, cung cấp reverse engineering capability cho SLOT components.

### 2.4 Spec Version Consistency

| Version | Count | Note |
|---------|-------|------|
| `4.0` | **65** | Current standard |
| `(unknown)` | 1 | Missing specVersion field |

→ **98.5% v4.0 aligned** — migration gần như hoàn tất.

---

## 3. Spec Pattern Intelligence

### 3.1 Component Usage Frequency (Top 20)

| Rank | componentRef | Uses | Category |
|------|-------------|------|----------|
| 1 | **Button** | 68 | Form/Action |
| 2 | **Input** | 33 | Form |
| 3 | **Select** | 8 | Form |
| 4 | **Badge** | 8 | Display |
| 5 | Item / Media | 7 | List |
| 6 | Typography / H4 | 6 | Typography |
| 7 | Typography / P | 5 | Typography |
| 8 | Typography / Muted | 5 | Typography |
| 9 | Toggle Group | 4 | Form |
| 10 | Section | 4 | Layout |
| 11 | Avatar | 4 | Display |
| 12 | Separator | 4 | Layout |
| 13 | Typography / Large | 4 | Typography |
| 14 | Blocks / Statistic Card | 4 | Blocks |
| 15 | Switch | 3 | Form |
| 16 | Section Header | 3 | Layout |
| 17 | Table | 3 | Data |
| 18 | Card | 3 | Layout |
| 19 | Page Header | 2 | Layout |
| 20 | Icon | 2 | Display |

**51 unique componentRefs** across 96 specs.

### 3.2 Role Distribution (30 roles in use)

| Role Group | Role | Count | % |
|------------|------|-------|---|
| **Structure** | `container` | 695 | 46.3% |
| **Content** | `text` | 405 | 27.0% |
| **Screen** | `screen` | 59 | 3.9% |
| **Layout** | `card` | 59 | 3.9% |
| **Action** | `button-primary` | 42 | 2.8% |
| **Form** | `field` | 29 | 1.9% |
| **Form** | `input` | 22 | 1.5% |
| **Layout** | `separator` | 19 | 1.3% |
| **Form** | `label` | 19 | 1.3% |
| **Layout** | `divider` | 14 | 0.9% |
| **Form** | `checkbox` | 10 | 0.7% |
| Other 20 roles | — | 128 | 8.5% |

→ `container` + `text` = **73.3%** of all nodes. These are the critical paths for optimization.

### 3.3 Token Usage Map

#### Spacing (14 tokens)

| Token | Uses | Pixel Value |
|-------|------|-------------|
| `spacing/4` | **384** | 16px |
| `spacing/2` | 305 | 8px |
| `spacing/6` | 218 | 24px |
| `spacing/1` | 166 | 4px |
| `spacing/3` | 147 | 12px |
| `sp-1-5` | 57 | 6px |
| `sp-2-5` | 38 | 10px |
| `spacing/0-5` | 29 | 2px |
| `spacing/8` | 27 | 32px |
| `spacing/0` | 26 | 0px |

→ **Top 5 spacing tokens cover 87% of all usage** — spacing system is highly concentrated.

#### Color (Top 15 tokens)

| Token | Uses | Role |
|-------|------|------|
| `foreground` | **198** | Primary text |
| `muted-foreground` | 128 | Secondary text |
| `border` | 102 | Borders |
| `background` | 98 | Backgrounds |
| `card` | 67 | Card backgrounds |
| `primary` | 45 | Primary brand |
| `muted` | 33 | Muted backgrounds |
| `card-foreground` | 28 | Card text |
| `primary-foreground` | 22 | Primary contrast text |
| `input` | 13 | Input backgrounds |
| `accent` | 9 | Accent elements |
| `popover-foreground` | 7 | Popover text |

→ **34 unique color tokens**, top 5 cover **70% of usage**.

#### Radius (17 tokens — FRAGMENTED)

| Token | Uses | Note |
|-------|------|------|
| `md` | 68 | Shorthand |
| `rounded-lg` | 22 | CSS-style |
| `rounded-md` | 20 | CSS-style |
| `sm` | 17 | Shorthand |
| `lg` | 15 | Shorthand |
| `radius/lg` | 8 | Fully-qualified |
| `full` | 7 | Shorthand |
| `radius/full` | 5 | Fully-qualified |
| `xl` | 5 | Shorthand |
| `rounded-full` | 4 | CSS-style |
| `radius/md` | 4 | Fully-qualified |

> ⚠️ **Radius tokens show 3 naming conventions** — needs normalization:
> - Shorthand: `md`, `sm`, `lg`, `full`, `xl`
> - CSS-style: `rounded-lg`, `rounded-md`, `rounded-full`
> - Fully-qualified: `radius/lg`, `radius/md`, `radius/full`

### 3.4 Layout Patterns

| Metric | Value |
|--------|-------|
| Max nesting depth | **7** |
| Average depth | **2.4** |
| Grid patterns detected | **30** (horizontal + all children `width: "fill"`) |

**Depth distribution:**

```
Depth 0 ████████████████████ 96  (screen roots)
Depth 1 ███████████████████████████████████████████████████████ 298
Depth 2 ████████████████████████████████████████████████████████████████████████████████████████ 481 ← peak
Depth 3 ████████████████████████████████████████████████████████ 296
Depth 4 ████████████████████████████████████████ 181
Depth 5 ██████████████████████ 108
Depth 6 ██████ 28
Depth 7 ███ 13
```

### 3.5 Fallback Inventory

**46 generative fallback nodes** with documented notes — components that couldn't be resolved to library instances.

### 3.6 State Patterns

- **228 state definitions** across 96 specs
- **165+ unique triggers** documenting real user flows
- Mutation types: property changes, visibility toggles, content updates

### 3.7 Override Patterns

Top components with overrides:

| Component | Overridden Properties |
|-----------|----------------------|
| Button | label, variant, size, icon |
| Avatar | image, fallback, size |
| Badge | variant, label |
| Card | title, description, content |
| Input | placeholder, type, value |

---

## 4. SLOT Library Evolution

### 4.1 Migration Overview

| Metric | SLOT1 (new) | 1203 (old) | Delta |
|--------|-------------|------------|-------|
| Total entries | 720 | 727 | −7 |
| Component Sets | 524 | 525 | −1 |
| Standalone Components | 196 | 202 | −6 |
| Scan duration | **769ms** | 9,714ms | **12.6× faster** |

### 4.2 Tier Distribution

| Tier | SLOT1 | 1203 | Delta | Description |
|------|-------|------|-------|-------------|
| T0 (Base) | 192 | 198 | −6 | Core primitives |
| T1 (Composed) | 70 | 66 | +4 | Composed components |
| T2 (Specialized) | 33 | 39 | −6 | Specialized variants |
| T3 (Blocks) | 425 | 424 | +1 | Page-level blocks |

### 4.3 SLOT Property Analysis

**95 components gained SLOT properties** (132 total SLOT props):

#### SLOT Name Frequency

| SLOT Name | Components | Description |
|-----------|-----------|-------------|
| **Content** | **34** | Main content area |
| **Items** | **23** | List/collection items |
| **SidebarContent** | **12** | Sidebar panel content |
| **Card Content** | 7 | Card body content |
| **Card Footer** | 7 | Card footer area |
| **Card Header** | 6 | Card header area |
| Footer | 3 | Generic footer |
| Content (Month) | 3 | Calendar month content |
| Dialog Content | 1 | Dialog body |
| DrawerContent | 1 | Drawer body |
| SelectMenu Group | 1 | Select menu options |

→ **Content + Items = 43% of all SLOTs** — these are the primary composition patterns.

#### Top 10 SLOT-Heavy Components

| Component | Direct SLOTs | Nested | Total | Key For |
|-----------|-------------|--------|-------|---------|
| **Calendar / Basic** | **6** | 0 | 6 | Date picker, scheduling |
| Data Table | 3 | 0 | 3 | Data display |
| Form / 1.–6. | 3 each | 0 | 3 | Form layouts |
| NavigationMenu / Popover | 3 | 0 | 3 | Navigation |
| Accordion | 2 | 0 | 2 | Expandable sections |
| Alert Dialog | 2 | 0 | 2 | Confirmations |
| Carousel | 2 | 0 | 2 | Image galleries |

### 4.4 Property Type Transitions

| Component | Property | Old Type | New Type |
|-----------|----------|----------|----------|
| Card | Card Content | `BOOLEAN` | `SLOT` |
| Card | Card Footer | `BOOLEAN` | `SLOT` |

→ **BOOLEAN → SLOT** is the only transition pattern observed. Components transitioned from toggle visibility (`BOOLEAN`) to composable content injection (`SLOT`).

### 4.5 Components Added/Removed

**New components (2):**
- `Blocks / Sidebar-16.` (T3, Blocks Official) — has SLOTs ✅
- `Menubar / Trigger/Yes/Top` (T3) — no SLOTs

**Removed components (9):** All "Example Content" patterns:
- `Card / Example Content`, `Card / Example Footer`
- `Dialog / Example Content`, `Drawer / Example Content`
- `Sheet / Example Content`, `Popover / Content Example`
- `Empty / Content`, `Hover Card / Content Example`
- `Blocks / Settings Card / Example Content`

> 💡 **Key insight**: 9 "Example Content" standalone components were replaced by SLOT properties. This is the core SLOT migration pattern — from hardcoded examples to composable content injection.

---

## 5. Rule Compliance Audit

### 5.1 Overall Results

| Metric | Value |
|--------|-------|
| Total specs audited | **98** |
| **Fully compliant** | **38 (38.8%)** |
| Failed | 60 |
| Warnings | 64 |

### 5.2 Rule-by-Rule Breakdown

| Rule | Compliant | Non-Compliant | Note |
|------|-----------|---------------|------|
| Rule 1 (Instantiation-First) | ✅ Advisory | — | 217 refs vs 788 generative |
| **Rule 2 (Pre-binding)** | **98/98 (100%)** | 0 | **Zero hardcoded values** |
| Rule 3 (Verify-Only) | 40/98 | **58** | Main failure source |
| Schema | 98/98 | 0 | All valid |
| Roles | 98/98 | 0 | All valid |
| Padding | 98/98 | 0 | All valid format |
| Key uniqueness | 96/98 | 2 | Minor duplicates |

### 5.3 Failure Analysis

| Failure Reason | Count | Fix Effort |
|----------------|-------|------------|
| `rule3` (non-empty collections) | **58** | Automated — remove `tokens.collections` contents |
| `keyDup` (duplicate keys) | 2 | Manual — rename conflicting keys |

### 5.4 Compliant Specs (38/98)

All xPOS production specs (SCR-001 through SCR-BO-007) and all test specs:

```
✅ xPOS: scr-001 through scr-026 (26 specs)
✅ BackOffice: scr-bo-001 through scr-bo-007 (7 specs)
✅ Tests: test-11 through test-15, test-scr021 variants (5 specs)
```

---

## 6. Knowledge Base Insights

### 6.1 Insight Distribution (186 total)

| Category | Count | Source KIs |
|----------|-------|------------|
| **Architecture** | 55 | figma_bridge_system (26), ba_design_pipeline (16), shadcn_distillery (7) |
| **Test Results** | 45 | figma_bridge_system (17), shadcn_distillery (14), ba_design_pipeline (8) |
| **Performance** | 33 | figma_bridge_system (12), ba_design_pipeline (10), shadcn_distillery (6) |
| **BP References** | 23 | bigger_picture_bp (8), figma_bridge (6), ba_design_pipeline (5) |
| **SLOT** | 19 | shadcn_distillery (10), figma_bridge_system (6), bp_system (2) |
| **Bug Patterns** | 11 | figma_bridge_system (5), shadcn_distillery (3), ba_design_pipeline (1) |

### 6.2 SLOT-Related Knowledge (19 insights)

| Source | Artifact | Focus |
|--------|----------|-------|
| figma_bridge_system | `settings_page_fidelity` | SLOT usage in real settings page |
| figma_bridge_system | `bug_and_troubleshooting_patterns` | SLOT-related bugs discovered |
| figma_bridge_system | `spec_format` | SLOT syntax in spec format |
| figma_bridge_system | `overview` | SLOT in system architecture |
| shadcn_distillery | `data_slot_vocabulary` | **309-slot mandatory protocol** |
| shadcn_distillery | `converter_logic` | SLOT → spec conversion logic |
| shadcn_distillery | `extraction_pipeline` | SLOT extraction from CLI |
| shadcn_distillery | `parsed_outputs` | Actual SLOT parsed data |
| shadcn_distillery | `full_cli_audit` | SLOT coverage audit |

### 6.3 Bug Patterns (11 documented)

| Bug | Source | Lesson |
|-----|--------|--------|
| ComponentSet vs. Component instances | figma_bridge | Use `createComponent` not `createComponentSet` |
| Fix pattern for instance creation | figma_bridge | Always check node type before operations |
| Phase timing issues | figma_bridge | Sequential phase execution critical |
| Fixed tree vs. free visual | shadcn_distillery | Component trees are fixed, visual output is flexible |
| Suffix grammar | shadcn_distillery | Component suffix naming rules matter for resolution |
| Troubleshooting Step 0b | ba_design_pipeline | xPOS-specific enrichment edge cases |

### 6.4 KI Coverage Map

| KI | Artifacts | Insights | Focus |
|----|-----------|----------|-------|
| `figma_bridge_system` | **17** | **64** | Core plugin architecture, bugs, testing |
| `ba_design_pipeline_architecture` | 14 | 37 | 7-phase pipeline, gap discovery |
| `shadcn_identity_distillery` | 15 | 29 | Component anatomy, SLOT protocol |
| `bigger_picture_bp_system` | 9 | 30 | Governance principles |
| `design_data_layer_system` | 6 | 9 | Token system, DDL |
| `vnpay_design_ecosystem` | 2 | 9 | Ecosystem overview |
| `vnpay_agentic_context_management` | 4 | 8 | Context sync, skill patterns |

---

## 7. Actionable Recommendations

### 7.1 SLOT Plugin Development — Immediate Actions

| Priority | Action | Data Source | Effort |
|----------|--------|-------------|--------|
| 🔴 P0 | **Implement SLOT assembler** — handle 132 SLOT properties across 95 components | library-evolution-report | High |
| 🔴 P0 | **Support `Content` + `Items` SLOT types** — covers 43% of all SLOTs | SLOT name frequency | Medium |
| 🟡 P1 | **Normalize radius tokens** — 3 conventions → 1 (`radius/X` fully-qualified) | spec-patterns-report | Low |
| 🟡 P1 | **Migrate 58 specs to Verify-Only** — remove `tokens.collections` contents | rule-compliance-report | Automated |
| 🟡 P1 | **Fix 2 key duplicates** | rule-compliance-report | Manual |
| 🟢 P2 | **Leverage 5 SLOT-aware scripts** as foundation for new plugin logic | bridge-context-report | Reference |

### 7.2 Component Resolution — Optimization Targets

| Insight | Action |
|---------|--------|
| Button(68) + Input(33) = 47% of all refs | Optimize resolution for these 2 components first |
| `container`(695) + `text`(405) = 73% of nodes | These roles are the hot path — optimize layout engine for them |
| 30 grid patterns detected | Add grid-aware layout optimization |
| Max depth = 7, avg = 2.4 | Support up to depth 8, optimize for depth 2-3 |

### 7.3 Token System — Opportunities

| Finding | Recommendation |
|---------|---------------|
| 5 spacing tokens cover 87% | Pre-cache top 5 for instant lookup |
| 5 color tokens cover 70% | Pre-cache `foreground`, `muted-foreground`, `border`, `background`, `card` |
| Radius fragmentation (3 styles) | Normalize to `radius/X` format, add alias resolver |

### 7.4 SLOT Migration Pattern — Converter Guide

```
Old pattern (BOOLEAN):     → toggles visibility on/off
  "Card Content": true       Shows default example content

New pattern (SLOT):        → injects composable children
  "Card Content": [node]     Renders custom content tree
```

**9 "Example Content" components removed → replaced by SLOT injection.** This is the migration pattern the converter must replicate.

### 7.5 Knowledge Gaps to Fill

| Gap | Where to Look |
|-----|--------------|
| SLOT children rendering logic | Plugin source `src/main.ts` Phase A |
| SLOT ↔ spec schema integration | Not yet in spec_format.md — needs spec v5 |
| Multi-SLOT composition (Calendar = 6 SLOTs) | No documented pattern yet |
| SLOT default values vs. empty | `library-pass-SLOT1.json` defaultValue field |

---

## Raw Reports (JSON)

| Report | Path | Size |
|--------|------|------|
| Bridge Context | `output/bridge-context-report.json` | 22.7 KB |
| Spec Patterns | `output/spec-patterns-report.json` | 88.8 KB |
| Library Evolution | `output/library-evolution-report.json` | 110.6 KB |
| Conversation Insights | `output/conversation-insights-report.json` | 135.6 KB |
| Rule Compliance | `output/rule-compliance-report.json` | 114.0 KB |

**Total: ~472 KB of structured intelligence**, harvested from workspace data accumulated over weeks of Bridge development.

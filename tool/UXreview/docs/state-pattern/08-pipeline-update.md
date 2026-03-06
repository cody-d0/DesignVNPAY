# Pipeline Update: Phase 6.5 + Phase 7 Extended

This document specifies how to integrate state-pattern cross-referencing into the existing comp-extract pipeline.

---

## 1. Updated Pipeline Overview

```
Phase 1 — Extract (screen_registry, component_registry)
Phase 2 — Extract Props (component_props_from_prd)
Phase 3 — Normalize (component_key, component_group)
Phase 4 — Map States (state_matrix, COMPbase only)
Phase 5 — Map Tokens (token_mapping via temp1.json)
Phase 6 — Coverage Diff (missing_components, missing_component_states, missing_tokens)
                │
                ▼
  ┌─────────────────────────────────┐
  │  Phase 6.5 — State-Pattern     │  ← NEW
  │  Cross-Reference               │
  │                                 │
  │  Input:                         │
  │    component_registry           │
  │    component_props_from_prd     │
  │    state_matrix                 │
  │    token_mapping                │
  │    06-component-scenario-       │
  │      mapping.json               │
  │    07-crossref-spec.md (rules)  │
  │                                 │
  │  Output:                        │
  │    state_pattern_gaps[]         │
  └───────────────┬─────────────────┘
                  │
                  ▼
  ┌─────────────────────────────────┐
  │  Phase 7 — UX Gap Augmentation  │  ← EXTENDED
  │  (ui-ux-pro-max)               │
  │                                 │
  │  Input (existing):              │
  │    COMPbase component_registry  │
  │    COMPbase state_matrix        │
  │    missing_components           │
  │    missing_component_states     │
  │    Wireframe > Mô tả màn hình  │
  │                                 │
  │  Input (new):                   │
  │    state_pattern_gaps[]    ← NEW│
  │                                 │
  │  Output (existing):             │
  │    comp_extend_components       │
  │    comp_extend_state_extensions │
  │    ux_writing_proposals         │
  │    ui_enrichment_proposals      │
  │                                 │
  │  Output (new):                  │
  │    state_pattern_extensions[]   │  ← NEW
  └───────────────┬─────────────────┘
                  │
                  ▼
Phase 8 — Output (Markdown + JSON)
```

---

## 2. Phase 6.5 Specification

### Purpose

Run the cross-reference algorithm from `07-crossref-spec.md` to identify which components are missing interaction-state capabilities defined in the state-pattern scenarios.

### Input

| Source | Description |
|---|---|
| `component_registry[]` | From Phase 3 output |
| `component_props_from_prd[]` | From Phase 2 output |
| `state_matrix[]` | From Phase 4 output |
| `token_mapping[]` | From Phase 5 output |
| `06-component-scenario-mapping.json` | Static mapping file |
| `07-crossref-spec.md` | Cross-reference rules |

### Algorithm

```
for each component in component_registry:
  1. Look up applicable scenario IDs:
     - First try: component_key_mapping[component.component_key]
     - Fallback: group_mapping[component.component_group].applicable_scenarios

  2. For each applicable scenario:
     a. Run gate check (prerequisite). If fails → skip scenario.
     b. Run field checks against component_props, state_matrix, token_mapping.
     c. If any non-gate check fails → emit gap entry.

  3. Assign priority per rules in crossref-spec Section 4.
```

### Output: `state_pattern_gaps[]`

Each entry:

```json
{
  "scenario_id": "S1",
  "scenario_name": "NEW Badge — Hide After Viewed",
  "component_key": "ProductCard",
  "component_group": "Cards/Lists",
  "gap_type": "missing_interaction_state",
  "gap_detail": "No novelty indicator lifecycle (show → view → hide)",
  "failed_checks": [
    { "check_id": 1, "field": "component_props_from_prd", "expected": "badge/new/indicator prop", "found": "none" },
    { "check_id": 2, "field": "state_matrix", "expected": "viewed/seen trigger", "found": "none" }
  ],
  "required_interaction_state": "viewed",
  "required_events": ["ITEM_VIEWED"],
  "required_selector": "selectIsNew(item)",
  "persistence_tier": "localStorage",
  "priority": "High",
  "source": "state-pattern/06-component-scenario-mapping.json"
}
```

### Constraints

- Phase 6.5 produces **only gap data**. It does NOT propose solutions (that is Phase 7's job).
- Every gap entry must reference the mapping source.
- Do not emit gaps for scenarios marked `not_applicable` in the mapping.
- Do not emit gaps if the gate check fails (e.g., component is not navigable → skip S3).

---

## 3. Phase 7 Extended Input

### What Changes

Phase 7 already receives:
- COMPbase `component_registry`
- COMPbase `component_props_from_prd`
- COMPbase `state_matrix`
- `missing_components[]`
- `missing_component_states[]`
- COMPbase/missing `token_mapping`
- Current `Wireframe > Mô tả màn hình`

**New input**: `state_pattern_gaps[]` from Phase 6.5.

### How Phase 7 Uses the New Input

Phase 7 processes `state_pattern_gaps[]` as an additional gap source alongside existing COMPbase diff gaps. For each gap entry:

1. **Match to ui-ux-pro-max rules** using `ux_guideline_cross_refs` from the mapping JSON:
   - Look up `ux_guidelines_csv` and `web_interface_csv` row numbers for the scenario.
   - Extract relevant `Do` / `Don't` / `Code Example Good` values.

2. **Generate `state_pattern_extensions[]`** entries (see Deliverable 4 for schema).

3. **Priority merge**: If a component already has a COMPextend proposal from regular Phase 7 processing AND also has a `state_pattern_gap`, merge into a single enriched proposal with both `ui_ux_rule_ref` AND `state_pattern_ref`.

### Processing Order Within Phase 7

```
Phase 7 execution:
  1. Process existing COMPbase diff gaps (unchanged)
     → comp_extend_components
     → comp_extend_state_extensions
     → ux_writing_proposals
     → ui_enrichment_proposals

  2. Process state_pattern_gaps[] (new)
     → state_pattern_extensions[]

  3. Merge/dedup where both sources flag the same component
     → unified proposals with dual references
```

### Priority Rules for State-Pattern Extensions

Follow the existing Phase 7 priority order with state-pattern gaps slotted in:

1. Accessibility + Touch + Interaction (Critical) — includes S5 (onboarding), S6 (search history touch targets)
2. Layout + Performance (High) — includes S8 (expand/collapse animation)
3. State + Persistence (High) — **new tier** — includes S1 (badge), S3 (recently viewed), S4 (pinned), S7 (filter pref)
4. Typography/Color + Animation + Content Writing (Medium) — includes S2 (dismissible animation)

---

## 4. What Does NOT Change

| Component | Change? | Reason |
|---|---|---|
| Phase 1-5 | No | Extraction, normalization, state/token mapping unchanged |
| Phase 6 (Coverage Diff) | No | Existing diff logic stays; Phase 6.5 runs after it |
| Phase 7 existing logic | No | Existing COMPbase→COMPextend flow preserved |
| Phase 8 output structure | Minimal | Add new section in Markdown + new key in JSON |
| `comp-extraction/SKILL.md` | Update | Add Phase 6.5 documentation + Phase 7 extended input |
| `pdr-analyze/SKILL.md` | No | Upstream skill not affected |
| `pdr-extract/SKILL.md` | No | Upstream skill not affected |
| `ui-ux-pro-max` data files | No | CSV data unchanged; just consumed differently |

---

## 5. Integration Into comp-extraction SKILL.md

When updating the skill, add the following between Phase 6 and Phase 7:

### New Section: Phase 6.5 — State-Pattern Cross-Reference

```markdown
### Phase 6.5 — State-Pattern Cross-Reference

After Coverage Diff (Phase 6), cross-reference components against state-pattern scenarios.

**Input**:
- Phase 3-5 outputs (component_registry, component_props, state_matrix, token_mapping)
- `XPOS/state-pattern/06-component-scenario-mapping.json` (mapping table)
- `XPOS/state-pattern/07-crossref-spec.md` (check rules)

**Process**:
1. For each component, look up applicable scenarios from mapping.
2. Run gate checks, then field checks per crossref-spec.
3. Emit `state_pattern_gaps[]` for components with failed checks.

**Output**: `state_pattern_gaps[]` (gap entries only, no proposals).
```

### Updated Section: Phase 7 Input List

Add to existing Phase 7 input documentation:

```markdown
**Additional input (from Phase 6.5)**:
- `state_pattern_gaps[]`: interaction-state gaps identified by cross-referencing
  state-pattern scenarios against component fields.

Generate `state_pattern_extensions[]` for each gap using ui-ux-pro-max rules
referenced in `ux_guideline_cross_refs` from the mapping JSON.
```

---

## 6. Validation Checklist

Before shipping the pipeline update:

- [ ] Phase 6.5 runs after Phase 6 and before Phase 7 (sequential, not parallel)
- [ ] `state_pattern_gaps[]` is a flat array, not nested
- [ ] Gate checks prevent false positives (non-navigable items don't get S3 gaps)
- [ ] Priority assignment follows the crossref-spec rules
- [ ] Phase 7 processes regular gaps first, then state-pattern gaps
- [ ] Merged proposals have both `ui_ux_rule_ref` and `state_pattern_ref`
- [ ] Phase 8 output includes `state_pattern_extensions[]` in both Markdown and JSON
- [ ] No changes to Phase 1-5 behavior

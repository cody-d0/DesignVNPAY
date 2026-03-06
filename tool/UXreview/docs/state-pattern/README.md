# Reusable State Pattern for UX — Documentation Index

A framework-agnostic state management pattern designed for document-explorer web applications. Born from a single observation — "the NEW badge doesn't disappear after viewing" — and formalized into an extensible architecture that covers any stateful UX feature.

---

## Documents

| # | File | Purpose |
|---|---|---|
| 00 | [State Map: Current Implementation](./00-state-map-current.md) | Audit of existing state, events, and gaps in `index.html` |
| 01 | [State Contract Specification](./01-state-contract.md) | Core architecture: slices, events, reducers, selectors, effects |
| 02 | [Scenario Catalog](./02-scenario-catalog.md) | 8 concrete use cases with transitions and expected outcomes |
| 03 | [Persistence Policy](./03-persistence-policy.md) | Storage tiers, TTL, migration, serialization rules |
| 04 | [Extensibility Template](./04-extensibility-template.md) | Step-by-step guide to add new features without modifying core |
| 05 | [UX Quality Checklist](./05-ux-quality-checklist.md) | KPIs, per-feature checklists, scenario tests, scorecard |
| 06 | [Component-Scenario Mapping](./06-component-scenario-mapping.json) | JSON mapping: component_group/key to scenario IDs + UX rule cross-refs |
| 07 | [Cross-Reference Spec](./07-crossref-spec.md) | Per-scenario field checks against comp-extract output |
| 08 | [Pipeline Update](./08-pipeline-update.md) | Phase 6.5 spec + Phase 7 extended input for comp-extract |
| 09 | [Output Schema](./09-output-schema.md) | `state_pattern_extensions[]` formal definition + examples |

---

## Quick Summary

### Architecture

```
UserEvent → EventBus → Reducers → StateStore → Selectors → UI
                                       ↓
                                  Effects → Persistence (localStorage / sessionStorage / URL)
```

### State Layers

- **sourceState**: Data from `files.json` (fetched fresh, never persisted)
- **uiState**: Current view, filter, search (transient + URL hash)
- **interactionState**: Viewed, pinned, dismissed, history (persisted in localStorage)
- **syncState**: Dirty flags, version (memory only)

### Key Principle

> Add new features by adding events + reducer rules + selectors + persistence declaration.
> Never modify the store, event bus, or persistence engine.

### Use Cases Covered

1. NEW badge (hide after viewed)
2. Dismissible announcements
3. Recently viewed files
4. Pinned files
5. Onboarding checklist
6. Search history
7. Filter preference memory
8. Folder expand/collapse state

### Metrics

- State Consistency: 100%
- Task Completion Rate: >= 95%
- Confusion Rate: <= 5%
- Recoverability: >= 80%
- Persistence Accuracy: 100%
- Load Time Impact: <= 50ms

---

## How to Use

### Core Pattern (docs 00-05)

1. **Start with the State Map** (00) to understand what exists today.
2. **Read the State Contract** (01) for the full architecture specification.
3. **Browse the Scenario Catalog** (02) for concrete examples.
4. **Consult the Persistence Policy** (03) when choosing storage tiers.
5. **Use the Extensibility Template** (04) when adding a new feature.
6. **Run the UX Quality Checklist** (05) before shipping any stateful feature.

### Pipeline Integration (docs 06-09)

7. **Use the Component-Scenario Mapping** (06) to find which scenarios apply to your components.
8. **Follow the Cross-Reference Spec** (07) to check gaps in comp-extract output.
9. **Integrate via the Pipeline Update** (08) to add Phase 6.5 to comp-extract.
10. **Use the Output Schema** (09) to generate `state_pattern_extensions[]` entries.

---

## Integration with comp-extract Pipeline

Documents 06-09 bridge the state-pattern with the comp-extract pipeline:

```
comp-extract Phase 6 (Coverage Diff)
        |
        v
Phase 6.5: Cross-reference components against 8 scenarios (06 mapping + 07 rules)
        |
        v
Phase 7: UX Gap Augmentation (existing + state_pattern_gaps[] input)
        |
        v
Phase 8: Output includes state_pattern_extensions[] (09 schema)
```

---

## Source Plans

- State pattern research: `.cursor/plans/state-pattern-research_9a1b00fc.plan.md`
- Pipeline integration: `.cursor/plans/đánh_giá_bổ_sung_workflow_392fc67e.plan.md`

# Cross-Reference Spec: Use Case → Field Checklist

For each state-pattern scenario, this spec defines exactly which fields in the comp-extract output must be checked to identify gaps. The cross-reference runs **after** Phase 6 (Coverage Diff) and produces a structured gap list as input for Phase 7.

---

## 1. Field Sources (from comp-extract output)

| Field Set | Key Columns | Purpose |
|---|---|---|
| `component_registry[]` | `component_key`, `component_group`, `prd_type`, `description` | Component identity and classification |
| `component_props_from_prd[]` | `component_key`, `prop_key`, `prop_value_excerpt` | Explicit props from PRD |
| `state_matrix[]` | `component_key`, `state`, `trigger_from_prd`, `status` | UI states with evidence |
| `token_mapping[]` | `component_key`, `state`, `token_ref`, `status` | Token coverage per state |
| `missing_components[]` | `component_key`, `gap_type` | Components with insufficient coverage |
| `missing_component_states[]` | `component_key`, `state`, `gap_type` | States absent in COMPbase |

---

## 2. Cross-Reference Rules Per Scenario

### S1: NEW Badge (Novelty Indicator)

**Applies to**: component_group IN (`Cards/Lists`, `Info/Feedback`, `Special`) OR component_key has list/card/item semantics.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Has novelty prop? | `component_props_from_prd[]` | No prop matching `badge`, `new`, `indicator`, `novelty`, `status_tag` for this component_key |
| 2 | Has viewed state? | `state_matrix[]` | No row with `state = 'active'` or trigger referencing "viewed", "read", "seen" |
| 3 | Has badge token? | `token_mapping[]` | No token for badge/indicator variant of this component |

**Gap output if any check fails**:

```json
{
  "scenario_id": "S1",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "No novelty indicator lifecycle (show → view → hide)",
  "required_interaction_state": "viewed",
  "required_events": ["ITEM_VIEWED"],
  "required_selector": "selectIsNew(item)",
  "persistence_tier": "localStorage"
}
```

---

### S2: Dismissible Announcements

**Applies to**: component_group IN (`Layout`, `Info/Feedback`, `Special`) OR component_key matches banner/popup/dialog/tooltip semantics.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Has dismiss action? | `component_props_from_prd[]` | No prop matching `dismiss`, `close`, `hide`, `remove` |
| 2 | Has dismiss/hidden state? | `state_matrix[]` | No row with `state = 'empty'` or trigger referencing "dismissed", "hidden", "closed" |
| 3 | Has close button token? | `token_mapping[]` | No token for close/dismiss action variant |

**Gap output**:

```json
{
  "scenario_id": "S2",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "No dismiss lifecycle (show → dismiss → persist hidden)",
  "required_interaction_state": "dismissed",
  "required_events": ["ITEM_DISMISSED", "UNDO"],
  "required_selector": "selectIsDismissed(id)",
  "persistence_tier": "localStorage"
}
```

---

### S3: Recently Viewed

**Applies to**: component_group IN (`Cards/Lists`) OR component_key matches navigable content (detail views, cards with links).

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Is a navigable item? | `component_props_from_prd[]` | Has prop referencing `link`, `navigate`, `detail`, `view`, `open` |
| 2 | Has history tracking? | `state_matrix[]` | No row with trigger referencing "recent", "history", "last viewed" |
| 3 | Has visual recency indicator? | `token_mapping[]` | No token differentiation for recent vs non-recent items |

**Gap output** (only if check 1 passes — item IS navigable):

```json
{
  "scenario_id": "S3",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "Navigable item has no recently-viewed tracking",
  "required_interaction_state": "recentlyViewed",
  "required_events": ["ITEM_OPENED"],
  "required_selector": "selectRecentlyViewed()",
  "persistence_tier": "localStorage"
}
```

---

### S4: Pinned Items

**Applies to**: component_group IN (`Cards/Lists`) AND item represents user-browsable content.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Has pin/favorite action? | `component_props_from_prd[]` | No prop matching `pin`, `favorite`, `bookmark`, `star` |
| 2 | Has pinned state? | `state_matrix[]` | No row with `state = 'active'` and trigger referencing "pin", "favorite" |
| 3 | Has pin icon token? | `token_mapping[]` | No token for pin/star icon variant |

**Gap output**:

```json
{
  "scenario_id": "S4",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "Browsable item has no pin/favorite capability",
  "required_interaction_state": "pinned",
  "required_events": ["ITEM_PINNED", "ITEM_UNPINNED"],
  "required_selector": "selectIsPinned(path)",
  "persistence_tier": "localStorage"
}
```

---

### S5: Onboarding Checklist

**Applies to**: component_group IN (`Input/Form`, `Navigation/Action`, `Special`) where the component is part of a multi-step flow.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Part of a flow? | `component_registry[]` | Multiple components share same `screen_id` in a sequential flow |
| 2 | Has progress indicator? | `component_props_from_prd[]` | No prop matching `step`, `progress`, `checklist`, `guide` |
| 3 | Has completed state? | `state_matrix[]` | No row with `state = 'success'` or trigger referencing "complete", "done" |

**Gap output** (only if check 1 passes — IS part of a flow):

```json
{
  "scenario_id": "S5",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "Multi-step flow has no onboarding/progress tracking",
  "required_interaction_state": "onboarding",
  "required_events": ["ONBOARDING_STEP_COMPLETED"],
  "required_selector": "selectOnboardingProgress()",
  "persistence_tier": "localStorage"
}
```

---

### S6: Search History

**Applies to**: component_group = `Search/Filter` AND component_key matches search semantics.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Is a search component? | `component_registry[]` | `component_key` contains `search` or `prd_type` contains "Search" |
| 2 | Has history prop? | `component_props_from_prd[]` | No prop matching `history`, `recent`, `suggestion`, `autocomplete` |
| 3 | Has autocomplete token? | `token_mapping[]` | No token for dropdown/suggestion variant |

**Gap output** (only if check 1 passes):

```json
{
  "scenario_id": "S6",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "Search component has no query history or suggestions",
  "required_interaction_state": "searchHistory",
  "required_events": ["SEARCH_QUERY_CHANGED", "SEARCH_HISTORY_CLEARED"],
  "required_selector": "selectSearchSuggestions(query)",
  "persistence_tier": "localStorage"
}
```

---

### S7: Filter Preference Memory

**Applies to**: component_group = `Search/Filter` AND component_key matches filter/tab semantics. Also `Switch` components.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Is a filter/tab component? | `component_registry[]` | `component_key` contains `filter`, `tab`, `dropdown-filter`, `switch` |
| 2 | Has preference persistence? | `component_props_from_prd[]` | No prop referencing `default`, `remember`, `persist`, `preference` |
| 3 | Has active state token? | `token_mapping[]` | Token exists for active state (this is usually covered) |

**Gap output** (only if check 1 passes):

```json
{
  "scenario_id": "S7",
  "component_key": "<key>",
  "gap_type": "missing_persistence",
  "gap_detail": "Filter/tab selection resets on reload",
  "required_interaction_state": "filterPreference",
  "required_events": ["FILTER_CHANGED"],
  "required_selector": "selectFilterPreference()",
  "persistence_tier": "localStorage"
}
```

---

### S8: Folder Expand/Collapse

**Applies to**: component_group IN (`Cards/Lists`, `Special`) AND component_key matches section/group/accordion semantics.

**Check fields**:

| # | Check | Field | Condition for GAP |
|---|---|---|---|
| 1 | Is a grouping component? | `component_registry[]` | `component_key` contains `section`, `group`, `form-section`, `accordion` |
| 2 | Has expand/collapse prop? | `component_props_from_prd[]` | No prop matching `expand`, `collapse`, `toggle`, `accordion` |
| 3 | Has collapse animation token? | `token_mapping[]` | No token for collapsed/expanded variant |

**Gap output** (only if check 1 passes):

```json
{
  "scenario_id": "S8",
  "component_key": "<key>",
  "gap_type": "missing_interaction_state",
  "gap_detail": "Grouped section has no expand/collapse memory",
  "required_interaction_state": "folderExpanded",
  "required_events": ["SECTION_TOGGLED"],
  "required_selector": "selectIsExpanded(sectionId)",
  "persistence_tier": "sessionStorage"
}
```

---

## 3. Execution Algorithm

```
function crossReferenceScenarios(compExtractOutput, scenarioMapping):

  gaps = []

  for each component in compExtractOutput.component_registry:
    group = component.component_group
    key = component.component_key

    // Get applicable scenarios from mapping
    scenarioIds = scenarioMapping.component_key_mapping[key]
                  ?? scenarioMapping.group_mapping[group].applicable_scenarios

    for each scenarioId in scenarioIds:
      checks = getChecksForScenario(scenarioId)

      allChecksPassed = true
      gateCheckPassed = true  // prerequisite check (e.g., "is navigable?")

      for each check in checks:
        if check.isGateCheck:
          gateCheckPassed = evaluateCheck(check, component, compExtractOutput)
          if not gateCheckPassed:
            break  // skip this scenario for this component
        else:
          if not evaluateCheck(check, component, compExtractOutput):
            allChecksPassed = false

      if gateCheckPassed and not allChecksPassed:
        gaps.push(buildGapEntry(scenarioId, component, checks))

  return gaps
```

---

## 4. Gap Priority Assignment

| Scenario | Base Priority | Upgrade Condition |
|---|---|---|
| S1 (NEW badge) | Medium | High if component is primary list item (CardItem, ProductCard) |
| S2 (Dismissible) | Low | Medium if component is system feedback (InfoBox, Dialog) |
| S3 (Recently viewed) | Medium | High if screen has > 10 navigable items |
| S4 (Pinned) | Medium | High if component is user's primary working item |
| S5 (Onboarding) | Low | High if flow has >= 3 steps AND is first-time user path |
| S6 (Search history) | Medium | High if search is the primary navigation method |
| S7 (Filter preference) | Medium | High if filter has > 3 options |
| S8 (Expand/collapse) | Low | Medium if screen has > 3 collapsible sections |

---

## 5. Summary

This cross-reference spec transforms abstract state-pattern scenarios into concrete, field-level checks against comp-extract output. The result is a `state_pattern_gaps[]` array that feeds into Phase 7 (UX Gap Augmentation) as an additional input alongside the existing COMPbase diff.

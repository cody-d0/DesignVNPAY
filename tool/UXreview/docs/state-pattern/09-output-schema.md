# Output Schema: `state_pattern_extensions[]`

Formal schema definition for the new output produced by Phase 7 when processing state-pattern gaps.

---

## 1. JSON Schema

```json
{
  "state_pattern_extensions": [
    {
      "scenario_id": "string",
      "scenario_name": "string",
      "component_key": "string",
      "component_group": "string",
      "gap_type": "string",
      "gap_detail": "string",
      "proposal_type": "string",
      "proposal_detail": "string",
      "required_interaction_state": "string",
      "required_events": ["string"],
      "required_selector": "string",
      "persistence_tier": "string",
      "ui_ux_rule_ref": "string",
      "state_pattern_ref": "string",
      "priority": "string",
      "impact": "string",
      "proposal_basis": "string",
      "status": "COMPextend"
    }
  ]
}
```

---

## 2. Field Definitions

| Field | Type | Required | Description |
|---|---|---|---|
| `scenario_id` | string | Yes | Scenario identifier from mapping (S1-S8) |
| `scenario_name` | string | Yes | Human-readable scenario name |
| `component_key` | string | Yes | Normalized component key from comp-extract |
| `component_group` | string | Yes | Component group (Input/Form, Cards/Lists, etc.) |
| `gap_type` | enum | Yes | One of: `missing_interaction_state`, `missing_persistence`, `missing_event`, `missing_selector` |
| `gap_detail` | string | Yes | Description of what is missing |
| `proposal_type` | enum | Yes | One of: `interaction_state`, `persistence`, `ui_enrichment`, `ux_writing` |
| `proposal_detail` | string | Yes | Concrete proposal for how to address the gap |
| `required_interaction_state` | string | Yes | State key to add (e.g., `viewed`, `pinned`, `dismissed`) |
| `required_events` | string[] | Yes | Event types needed for this feature |
| `required_selector` | string | Yes | Selector function signature |
| `persistence_tier` | enum | Yes | One of: `memory`, `sessionStorage`, `localStorage`, `url` |
| `ui_ux_rule_ref` | string | Yes | Reference to ui-ux-pro-max rule (e.g., `ux-guidelines#3: Active State`) |
| `state_pattern_ref` | string | Yes | Reference to scenario catalog (e.g., `scenario-catalog#S1: NEW Badge`) |
| `priority` | enum | Yes | One of: `Critical`, `High`, `Medium`, `Low` |
| `impact` | string | Yes | Expected UX impact description |
| `proposal_basis` | string | Yes | Evidence source: `state_pattern_scenario + ui_ux_guideline` |
| `status` | const | Yes | Always `COMPextend` |

---

## 3. Enum Values

### `gap_type`

| Value | When Used |
|---|---|
| `missing_interaction_state` | Component lacks a tracked user-intent state (viewed, pinned, dismissed) |
| `missing_persistence` | Interaction state exists but has no persistence declaration |
| `missing_event` | State exists but no event triggers transitions |
| `missing_selector` | State and events exist but no derived selector for UI |

### `proposal_type`

| Value | When Used |
|---|---|
| `interaction_state` | Proposal adds a new interaction state + events + reducer |
| `persistence` | Proposal adds persistence tier for existing state |
| `ui_enrichment` | Proposal adds visual elements (badge, icon, section) |
| `ux_writing` | Proposal adds text content (empty state message, tooltip) |

### `priority`

| Value | Criteria |
|---|---|
| `Critical` | Accessibility or core usability blocked |
| `High` | Primary user flow affected; high-frequency component |
| `Medium` | Enhancement for common but non-critical interaction |
| `Low` | Nice-to-have; infrequent use case |

### `persistence_tier`

| Value | Storage | Lifetime |
|---|---|---|
| `memory` | JS variable | Page unload |
| `sessionStorage` | Tab storage | Tab close |
| `localStorage` | Browser storage | Explicit clear |
| `url` | Hash/query params | Shareable |

---

## 4. Example Entries

### Example 1: ProductCard missing NEW badge lifecycle

```json
{
  "scenario_id": "S1",
  "scenario_name": "NEW Badge — Hide After Viewed",
  "component_key": "ProductCard",
  "component_group": "Cards/Lists",
  "gap_type": "missing_interaction_state",
  "gap_detail": "ProductCard has no novelty indicator lifecycle. New products show no visual differentiation; once viewed, there is no mechanism to clear a 'new' indicator.",
  "proposal_type": "interaction_state",
  "proposal_detail": "Add 'viewed' tracking to ProductCard: dispatch ITEM_VIEWED on card click/open; selector selectIsNew(product) returns true only if product is recent AND not yet viewed. Render NEW badge conditionally. Persist viewed map in localStorage with 90-day TTL.",
  "required_interaction_state": "viewed",
  "required_events": ["ITEM_VIEWED"],
  "required_selector": "selectIsNew(product)",
  "persistence_tier": "localStorage",
  "ui_ux_rule_ref": "ux-guidelines#3: Active State; web-interface#21: URL Reflects State",
  "state_pattern_ref": "scenario-catalog#S1: NEW Badge — Hide After Viewed",
  "priority": "High",
  "impact": "Users can quickly identify new products vs already-browsed ones, reducing cognitive load in large catalogs",
  "proposal_basis": "state_pattern_scenario + ui_ux_guideline",
  "status": "COMPextend"
}
```

### Example 2: FilterTabs missing preference persistence

```json
{
  "scenario_id": "S7",
  "scenario_name": "Filter Preference Memory",
  "component_key": "FilterTabs",
  "component_group": "Search/Filter",
  "gap_type": "missing_persistence",
  "gap_detail": "FilterTabs selection resets to default on every page load. User must re-select their preferred filter each visit.",
  "proposal_type": "persistence",
  "proposal_detail": "Add filterPreference to interaction state. On FILTER_CHANGED, save selected filter key to localStorage. On hydration, restore last filter and set as active tab. Fallback to 'all' if stored value is invalid.",
  "required_interaction_state": "filterPreference",
  "required_events": ["FILTER_CHANGED"],
  "required_selector": "selectFilterPreference()",
  "persistence_tier": "localStorage",
  "ui_ux_rule_ref": "ux-guidelines#3: Active State; web-interface#21: URL Reflects State; web-interface#22: Deep Linking",
  "state_pattern_ref": "scenario-catalog#S7: Filter Preference Memory",
  "priority": "Medium",
  "impact": "Saves 1 click per session for returning users; demonstrates app 'remembers' user preferences",
  "proposal_basis": "state_pattern_scenario + ui_ux_guideline",
  "status": "COMPextend"
}
```

### Example 3: SearchBar missing history

```json
{
  "scenario_id": "S6",
  "scenario_name": "Search History",
  "component_key": "SearchBar",
  "component_group": "Search/Filter",
  "gap_type": "missing_interaction_state",
  "gap_detail": "SearchBar has no query history or autocomplete suggestions. Users must retype common searches.",
  "proposal_type": "interaction_state",
  "proposal_detail": "Add searchHistory array to interaction state (max 30 entries). On SEARCH_QUERY_CHANGED (debounced, query.length >= 2), prepend to history. Selector selectSearchSuggestions(prefix) returns matching entries. Render dropdown below input with history items. Add 'Clear history' action. Persist in localStorage with 30-day TTL per entry.",
  "required_interaction_state": "searchHistory",
  "required_events": ["SEARCH_QUERY_CHANGED", "SEARCH_HISTORY_CLEARED"],
  "required_selector": "selectSearchSuggestions(query)",
  "persistence_tier": "localStorage",
  "ui_ux_rule_ref": "ux-guidelines#22: Touch Target Size; ux-guidelines#23: Touch Spacing; web-interface#10: Autocomplete Attribute; web-interface#12: Never Block Paste",
  "state_pattern_ref": "scenario-catalog#S6: Search History",
  "priority": "Medium",
  "impact": "Faster repeat searches; reduced typing on mobile where text input is slower",
  "proposal_basis": "state_pattern_scenario + ui_ux_guideline",
  "status": "COMPextend"
}
```

### Example 4: InfoBox missing dismiss capability

```json
{
  "scenario_id": "S2",
  "scenario_name": "Dismissible Announcements",
  "component_key": "InfoBox",
  "component_group": "Info/Feedback",
  "gap_type": "missing_interaction_state",
  "gap_detail": "InfoBox has no dismiss capability. System messages and announcements persist indefinitely, cluttering the UI.",
  "proposal_type": "interaction_state",
  "proposal_detail": "Add dismissed map to interaction state. Render close (X) button on dismissible InfoBox instances. On ITEM_DISMISSED, store dismiss timestamp. Selector selectIsDismissed(id) filters dismissed items. Show undo toast for 5 seconds. Persist in localStorage with no TTL (permanent dismiss).",
  "required_interaction_state": "dismissed",
  "required_events": ["ITEM_DISMISSED", "UNDO"],
  "required_selector": "selectIsDismissed(id)",
  "persistence_tier": "localStorage",
  "ui_ux_rule_ref": "ux-guidelines#10: Loading States; web-interface#5: Aria Live; web-interface#23: Confirm Destructive Actions",
  "state_pattern_ref": "scenario-catalog#S2: Dismissible Announcements",
  "priority": "Low",
  "impact": "Reduces visual noise; respects user attention by allowing permanent dismiss of non-critical info",
  "proposal_basis": "state_pattern_scenario + ui_ux_guideline",
  "status": "COMPextend"
}
```

---

## 5. Markdown Output Section

In Phase 8 Markdown output, add after `UI Enrichment Proposals`:

### Section Name

`State-Pattern Extensions (interaction state)`

### Column Layout

| scenario_id | component_key | gap_type | proposal_detail | required_state | persistence | ui_ux_rule_ref | state_pattern_ref | priority | status |
|---|---|---|---|---|---|---|---|---|---|

### Placement in Output

```markdown
1.  Nguồn trích
2.  Component Registry (Unique)
3.  Component Props from Mô tả màn hình
4.  State Mapping
5.  Token Mapping
6.  Missing Components & Missing States
7.  COMPextend Components (ui-ux-pro-max)
8.  COMPextend State Extensions (ui-ux-pro-max)
9.  UI Enrichment Proposals (ui-ux-pro-max)
10. State-Pattern Extensions (interaction state)   ← NEW
11. UX Writing Proposals (ui-ux-pro-max)
12. Assumptions & Unspecified
```

---

## 6. JSON Output Key

In Phase 8 JSON output, add:

```json
{
  "meta": { "..." },
  "sources": [],
  "screen_registry": [],
  "component_registry": [],
  "component_props_from_prd": [],
  "state_matrix": [],
  "token_mapping": [],
  "missing_components": [],
  "missing_component_states": [],
  "comp_extend_components": [],
  "comp_extend_state_extensions": [],
  "ui_enrichment_proposals": [],
  "state_pattern_extensions": [],
  "ux_writing_proposals": [],
  "missing_tokens": [],
  "assumptions_unspecified": [],
  "quality_gates": {
    "citation_coverage": "number",
    "unknown_key_count": "number",
    "unspecified_count": "number",
    "ux_gap_count": "number",
    "state_pattern_gap_count": "number"
  }
}
```

New quality gate: `state_pattern_gap_count` — total number of `state_pattern_extensions` entries emitted.

---

## 7. Relationship to Existing COMPextend

| Aspect | Existing COMPextend | State-Pattern Extensions |
|---|---|---|
| Source | ui-ux-pro-max CSV rules | State-pattern scenarios + ui-ux-pro-max rules |
| Focus | Visual, accessibility, forms, layout | Interaction lifecycle, persistence, user memory |
| Reference field | `ui_ux_rule_ref` only | `ui_ux_rule_ref` + `state_pattern_ref` (dual) |
| Overlaps | Possible for same component | Merge: keep both refs in single entry |
| Status | `COMPextend` | `COMPextend` (same layer, never COMPbase) |

---

## 8. Deduplication Rules

When the same component has both a regular COMPextend proposal and a state-pattern extension:

1. If they address **different concerns** (e.g., COMPextend adds `focus` state, state-pattern adds `viewed` state): keep both as separate rows.
2. If they address **the same concern** (e.g., both propose an `active` state variant): merge into one row with:
   - `ui_ux_rule_ref` = combined references
   - `state_pattern_ref` = scenario reference
   - `proposal_detail` = merged description
   - `priority` = higher of the two

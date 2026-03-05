---
name: stateful-ux-pattern
description: "Add stateful UX features using the event-first state pattern with 4-layer architecture (source, ui, interaction, sync). Guides event definition, reducer rules, selectors, persistence tier selection, and UX quality checks. Use when adding interactive state (viewed, pinned, dismissed, history, preferences, onboarding), implementing persistence (localStorage/sessionStorage/URL), fixing missing state feedback (e.g. badge not updating), or reviewing stateful UX quality."
---

# Stateful UX Pattern

Framework-agnostic state management pattern for document-explorer web UIs. Extends interaction state (viewed, pinned, dismissed, history, preferences) on top of existing source data with persistence and UX quality guarantees.

## When to Apply

- Adding any feature that tracks **what the user has done** (viewed, dismissed, pinned, bookmarked)
- Implementing **persistence** for user preferences or interaction history
- Fixing **missing state feedback** (e.g. badge doesn't update after user action)
- Adding **undo/redo**, **recently viewed**, **search history**, or **onboarding** flows
- Reviewing or auditing stateful UX quality

## Architecture (5 principles)

1. **Event-first**: All state changes via named events. No direct mutation.
2. **Selector-first rendering**: UI reads selectors, never raw state.
3. **Layer separation**: `source` | `ui` | `interaction` | `sync` in isolated slices.
4. **Persistence-aware**: Each slice declares storage tier upfront.
5. **Extensible by addition**: New features = new events + reducer rules + selectors + persistence declaration. Zero changes to core.

## Reference Documents

All detailed specs live in `state-pattern/`:

| Doc | Read When |
|---|---|
| [00-state-map-current.md](../../../state-pattern/00-state-map-current.md) | Auditing existing state or identifying gaps |
| [01-state-contract.md](../../../state-pattern/01-state-contract.md) | Designing slices, events, reducers, selectors, effects |
| [02-scenario-catalog.md](../../../state-pattern/02-scenario-catalog.md) | Looking for concrete examples of 8 use cases |
| [03-persistence-policy.md](../../../state-pattern/03-persistence-policy.md) | Choosing storage tier, TTL, serialization, migration |
| [04-extensibility-template.md](../../../state-pattern/04-extensibility-template.md) | Adding a new feature step-by-step |
| [05-ux-quality-checklist.md](../../../state-pattern/05-ux-quality-checklist.md) | Validating quality before shipping |
| [06-component-scenario-mapping.json](../../../state-pattern/06-component-scenario-mapping.json) | Mapping components to applicable scenarios |
| [07-crossref-spec.md](../../../state-pattern/07-crossref-spec.md) | Checking gaps in comp-extract output |
| [08-pipeline-update.md](../../../state-pattern/08-pipeline-update.md) | Integrating Phase 6.5 into comp-extract |
| [09-output-schema.md](../../../state-pattern/09-output-schema.md) | Generating state_pattern_extensions[] |

## Quick Start: Add a New Feature

Follow these 7 steps. Read [04-extensibility-template.md](../../../state-pattern/04-extensibility-template.md) for full detail.

### Step 1: Define Events

```javascript
// Add to event registry. Use NOUN_PAST_TENSE naming.
const EVENTS = {
  ITEM_BOOKMARKED: 'ITEM_BOOKMARKED',     // { path }
  ITEM_UNBOOKMARKED: 'ITEM_UNBOOKMARKED',  // { path }
};
```

### Step 2: Add State Keys

```javascript
// Add to initialInteractionState with "no action yet" default
const initialInteractionState = {
  bookmarked: new Set(),  // Set<string>
};
```

### Step 3: Add Reducer Rules

```javascript
// Pure function, new case branches only. Existing cases untouched.
case 'ITEM_BOOKMARKED':
  return { ...state, bookmarked: new Set([...state.bookmarked, payload.path]) };
```

### Step 4: Add Selectors

```javascript
// Pure functions combining slices. Memoizable.
function selectIsBookmarked(state, path) {
  return state.interaction.bookmarked.has(path);
}
```

### Step 5: Declare Persistence

```javascript
// Choose tier using decision tree from 03-persistence-policy.md
PERSISTENCE_MAP.bookmarked = {
  tier: 'local', key: 'xpos_bookmarked', ttl: null, debounce: 0
};
```

### Step 6: Wire UI (selectors only)

```javascript
const badge = store.select(s => selectIsBookmarked(s, file.path)) ? 'filled' : 'outline';
```

### Step 7: Dispatch Events

```javascript
button.addEventListener('click', () => {
  store.dispatch({
    type: 'ITEM_BOOKMARKED',
    payload: { path },
    timestamp: Date.now(),
    source: 'user'
  });
});
```

**Zero modifications to**: store, event bus, persistence engine, existing reducers, existing selectors.

## Persistence Tier Decision

```
Re-fetched on every load?           -> memory  (source data)
Survives reload?
  No  -> Useful within tab session? -> session (folder expand/collapse)
         Not useful?                -> memory  (hover, current search)
  Yes -> Shareable via URL?         -> url     (current file deep-link)
         Syncs across devices?      -> remote  (future)
         Otherwise?                 -> local   (viewed, pinned, dismissed, prefs)
```

## State Slices Summary

| Slice | Contains | Tier | Examples |
|---|---|---|---|
| `source` | Manifest data | memory | files, folders, newest, meta |
| `ui` | Current view | memory + url | currentFile, filter, search, viewMode |
| `interaction` | User history | local/session | viewed, pinned, dismissed, recent, prefs |
| `sync` | Save metadata | memory | dirty flags, version, lastSaved |

## Allowed States

Only use: `default`, `focus`, `active`, `disabled`, `loading`, `error`, `success`, `empty`

## Event Shape

```typescript
interface StateEvent {
  type: string;
  payload?: Record<string, any>;
  timestamp: number;
  source: 'user' | 'system' | 'persistence';
}
```

## Quality Gate (before shipping)

Read [05-ux-quality-checklist.md](../../../state-pattern/05-ux-quality-checklist.md) for the full checklist. Minimum checks:

- [ ] Initial state correct on first visit (no persisted data)
- [ ] State updates within 100ms of event
- [ ] Idempotent: same event twice does not corrupt state
- [ ] Persists correctly per declared tier (reload test)
- [ ] Stale data filtered out (deleted files not shown)
- [ ] Undo available for destructive actions
- [ ] ARIA attributes update for screen readers
- [ ] Hydration < 50ms, flush non-blocking

## Anti-Patterns

| Do Not | Do Instead |
|---|---|
| Read localStorage in a selector | Use hydrate then state slice |
| Modify dispatch() for new feature | Add reducer rule |
| Store derived values in interaction | Compute in selector |
| Dispatch inside a reducer | Use effects for cascading |
| Read raw state in UI render | Use selectors |
| Hardcode persistence in feature code | Declare in PERSISTENCE_MAP |

## Covered Scenarios

8 pre-designed use cases in [02-scenario-catalog.md](../../../state-pattern/02-scenario-catalog.md):

1. NEW badge (hide after viewed)
2. Dismissible announcements
3. Recently viewed files
4. Pinned files
5. Onboarding checklist
6. Search history
7. Filter preference memory
8. Folder expand/collapse

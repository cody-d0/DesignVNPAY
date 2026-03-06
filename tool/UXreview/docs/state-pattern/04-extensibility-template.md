# Extensibility Template

A step-by-step template for adding any new stateful UX feature to the pattern. Following this template guarantees the new feature integrates with the existing architecture without modifying the core store, event bus, or persistence engine.

---

## 1. The Golden Rule

> **Add, never modify.**
>
> A new feature adds new events, new reducer rules, new selectors, and a persistence declaration.
> It never changes the store shape, the dispatch mechanism, or the flush/hydrate engine.

---

## 2. Template Checklist

Copy this checklist for every new feature. Fill in each section, then implement.

### Feature Card

```markdown
# Feature: [Name]

## 1. Problem Statement
What user need does this solve? What is the current gap?

## 2. Events
List all new events this feature introduces.

| Event Type | Payload | Description |
|---|---|---|
| `EVENT_NAME` | `{ key: type }` | What triggers this event |

## 3. State Keys
What new keys are added to which slice?

| Slice | Key | Type | Default | Description |
|---|---|---|---|---|
| `interaction` | `keyName` | `Type` | `default` | What it stores |

## 4. Reducer Rules
Pseudocode for each new transition.

| Event | Before | After |
|---|---|---|
| `EVENT_NAME` | `state.key = X` | `state.key = Y` |

## 5. Selectors
What derived values does the UI need?

| Selector | Inputs | Returns | Used By |
|---|---|---|---|
| `selectFeatureValue` | `slice.key, ...` | `Type` | Component |

## 6. Persistence
| Key | Tier | TTL | Debounce | Reason |
|---|---|---|---|---|
| `keyName` | local/session/memory | Xd/none | Xms | Why this tier |

## 7. UI Changes
What UI elements change? What renders differently?

## 8. Edge Cases
List unusual scenarios and expected behavior.

## 9. Undo Strategy
Can this action be undone? How?
```

---

## 3. Implementation Steps (in order)

### Step 1: Define Events

Add event type constants to the event registry. This is the only "registration" step.

```javascript
// events.js — just add new entries
const EVENTS = {
  // ... existing events ...
  MY_FEATURE_ACTIVATED: 'MY_FEATURE_ACTIVATED',
  MY_FEATURE_DEACTIVATED: 'MY_FEATURE_DEACTIVATED',
};
```

**Rule**: Event names follow `NOUN_VERB` or `NOUN_PAST_TENSE` pattern (e.g., `ITEM_PINNED`, not `PIN_ITEM`).

### Step 2: Add State Keys

Add default values to the interaction slice (or whichever slice is appropriate).

```javascript
// initialState.js — add new keys with defaults
const initialInteractionState = {
  // ... existing keys ...
  myFeatureData: {},  // or [], Set, etc.
};
```

**Rule**: New keys must have a meaningful default that represents "no user action yet" (empty object, empty array, `null`, `false`).

### Step 3: Add Reducer Rules

Add new `case` branches to the appropriate reducer. Existing cases are untouched.

```javascript
// reducers.js — add new cases
function interactionReducer(state, event) {
  switch (event.type) {
    // ... existing cases stay unchanged ...

    case 'MY_FEATURE_ACTIVATED':
      return {
        ...state,
        myFeatureData: {
          ...state.myFeatureData,
          [event.payload.id]: { activatedAt: event.timestamp }
        }
      };

    case 'MY_FEATURE_DEACTIVATED':
      const { [event.payload.id]: _, ...rest } = state.myFeatureData;
      return { ...state, myFeatureData: rest };

    default:
      return state;
  }
}
```

**Rule**: Reducers are pure functions. No side effects, no async, no DOM access.

### Step 4: Add Selectors

Create selector functions that compute derived state for the UI.

```javascript
// selectors.js — add new functions
function selectMyFeatureStatus(state, itemId) {
  return state.interaction.myFeatureData[itemId] || null;
}

function selectMyFeatureCount(state) {
  return Object.keys(state.interaction.myFeatureData).length;
}
```

**Rule**: Selectors are pure functions of state. They can combine data from multiple slices.

### Step 5: Declare Persistence

Add the new key to the persistence map.

```javascript
// persistence.js — add mapping entry
const PERSISTENCE_MAP = {
  // ... existing entries ...
  myFeatureData: {
    tier: 'local',          // or 'session', 'memory'
    key: 'xpos_my_feature',
    ttl: null,              // null = no expiry
    debounce: 0,            // 0 = immediate, 500 = debounced
  },
};
```

**Rule**: The persistence engine reads this map automatically. No changes to `hydrate()` or `flush()` are needed.

### Step 6: Wire UI

Connect selectors to rendering in the appropriate component/template.

```javascript
// In render function
const isActive = store.select(state => selectMyFeatureStatus(state, file.path));
const badge = isActive ? '<span class="my-badge">Active</span>' : '';
```

**Rule**: UI reads only from selectors. Never access `store.getState().interaction.myFeatureData` directly in render code.

### Step 7: Dispatch Events

Wire user interactions to dispatch calls.

```javascript
// In event handler
button.addEventListener('click', () => {
  store.dispatch({
    type: 'MY_FEATURE_ACTIVATED',
    payload: { id: file.path },
    timestamp: Date.now(),
    source: 'user'
  });
});
```

---

## 4. Worked Example: Adding "Bookmarked Files" Feature

Following the template step-by-step:

### Feature Card

```
Feature: Bookmarked Files
Problem: Users want to mark files for later reading, distinct from "pinned" (priority) vs "bookmarked" (read-later).
```

### Step 1: Events

```javascript
EVENTS.FILE_BOOKMARKED = 'FILE_BOOKMARKED';      // { path }
EVENTS.FILE_UNBOOKMARKED = 'FILE_UNBOOKMARKED';  // { path }
EVENTS.BOOKMARKS_CLEARED = 'BOOKMARKS_CLEARED';  // -
```

### Step 2: State Key

```javascript
initialInteractionState.bookmarked = new Set();  // Set<string> of file paths
```

### Step 3: Reducer Rules

```javascript
case 'FILE_BOOKMARKED':
  return { ...state, bookmarked: new Set([...state.bookmarked, event.payload.path]) };

case 'FILE_UNBOOKMARKED':
  const next = new Set(state.bookmarked);
  next.delete(event.payload.path);
  return { ...state, bookmarked: next };

case 'BOOKMARKS_CLEARED':
  return { ...state, bookmarked: new Set() };
```

### Step 4: Selectors

```javascript
function selectIsBookmarked(state, path) {
  return state.interaction.bookmarked.has(path);
}

function selectBookmarkedFiles(state) {
  return state.source.files.filter(f => state.interaction.bookmarked.has(f.path));
}

function selectBookmarkCount(state) {
  return state.interaction.bookmarked.size;
}
```

### Step 5: Persistence

```javascript
PERSISTENCE_MAP.bookmarked = {
  tier: 'local',
  key: 'xpos_bookmarked',
  ttl: null,
  debounce: 0,
};
```

### Step 6-7: UI + Dispatch

```html
<!-- Bookmark icon in file item -->
<button class="bookmark-btn" aria-label="Bookmark file"
        onclick="store.dispatch({ type: isBookmarked ? 'FILE_UNBOOKMARKED' : 'FILE_BOOKMARKED', payload: { path: file.path } })">
  ${isBookmarked ? '🔖' : '☆'}
</button>

<!-- Filter tab -->
<button class="filter-tab" data-filter="bookmarked">
  Bookmarked <span class="filter-badge">${bookmarkCount}</span>
</button>
```

### Changes to Existing Code: ZERO

- Store: unchanged
- EventBus: unchanged
- Persistence engine: unchanged
- Hydrate/flush: unchanged
- Other reducers: unchanged
- Other selectors: unchanged

---

## 5. Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Correct Approach |
|---|---|---|
| Adding a new `if` branch in the store's `dispatch()` | Modifies core architecture | Add a reducer rule instead |
| Reading `localStorage` directly in a selector | Breaks purity; side effect in read path | Use hydrate + state slice |
| Adding feature-specific code to `hydrate()` | Couples persistence engine to features | Use `PERSISTENCE_MAP` declaration |
| Storing derived state in interaction slice | Redundant; will go stale | Compute in selector |
| Dispatching events inside a reducer | Breaks unidirectional flow | Use effects for cascading events |
| Skipping the selector and reading raw state in UI | Tight coupling; breaks when state shape changes | Always use selectors |

---

## 6. Feature Complexity Tiers

Not all features are equal. Use this guide to calibrate effort:

| Tier | Complexity | Events | Reducer Rules | Selectors | Example |
|---|---|---|---|---|---|
| **Trivial** | 1 event, 1 key | 1 | 1 | 1 | Filter preference memory |
| **Simple** | 2-3 events, 1 key | 2-3 | 2-3 | 1-2 | Pinned files, dismissals |
| **Moderate** | 3-5 events, 2+ keys | 3-5 | 3-5 | 2-4 | Search history with suggestions |
| **Complex** | 5+ events, cross-slice | 5+ | 5+ | 4+ | Onboarding with auto-detection |

Most document-explorer features fall in the **Trivial** or **Simple** tier. This is by design -- the pattern absorbs complexity into the architecture so that individual features stay simple.

---

## 7. Registration Summary

When adding a new feature, you touch exactly these files/sections:

| File/Section | What You Add | What You Never Change |
|---|---|---|
| Event registry | New event type constants | Existing event types |
| Initial state | New key with default | Existing keys |
| Reducer | New `case` branches | Existing `case` branches, switch structure |
| Selectors | New selector functions | Existing selectors |
| Persistence map | New entry | Hydrate/flush engine |
| UI template | New rendering logic | Store API, dispatch mechanism |
| Event handlers | New `dispatch()` calls | EventBus implementation |

This is the **open/closed principle** applied to state management: open for extension, closed for modification.

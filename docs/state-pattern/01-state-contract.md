# State Contract Specification

Framework-agnostic contract for managing stateful UX in document-explorer-style web applications.

---

## 1. Design Principles

1. **Event-first**: All state changes originate from named events. No direct mutation.
2. **Selector-first rendering**: UI reads computed selectors, never raw state.
3. **Layer separation**: Source data, UI state, interaction state, and sync metadata live in isolated slices.
4. **Persistence-aware**: Each state slice declares its storage tier upfront.
5. **Extensible by addition**: New features add events, reducers, and selectors without modifying existing ones.

---

## 2. State Slices

### 2a. Slice Definitions

```
StateStore
├── source         # Data from external sources (manifest, API)
│   ├── files: FileObj[]
│   ├── folders: Record<string, FileObj[]>
│   ├── newest: FileObj[]
│   ├── meta: { total_files, total_folders, newest_count, newest_days_threshold, generated_at }
│   └── _status: 'idle' | 'loading' | 'loaded' | 'error'
│
├── ui             # Current view state (ephemeral, navigational)
│   ├── currentFile: string | null
│   ├── currentFilter: 'all' | 'newest' | 'pinned' | 'recent'
│   ├── searchQuery: string
│   ├── searchResults: FileObj[] | null    (computed, cached)
│   └── viewMode: 'list' | 'detail'
│
├── interaction    # User-intent state (long-lived, personal)
│   ├── viewed: Record<string, { at: ISO8601, count: number }>
│   ├── pinned: Set<string>                (file paths)
│   ├── dismissed: Record<string, ISO8601> (item ID -> dismiss time)
│   ├── recentlyViewed: string[]           (ordered, max N)
│   ├── folderExpanded: Record<string, boolean>
│   ├── filterPreference: string | null
│   ├── searchHistory: string[]            (ordered, max M)
│   └── onboarding: Record<string, 'pending' | 'completed'>
│
└── sync           # Metadata about persistence health
    ├── dirty: Set<string>                 (slice names with unsaved changes)
    ├── lastSaved: Record<string, ISO8601>
    └── version: number                    (schema version for migration)
```

### 2b. FileObj Shape (reference)

```typescript
interface FileObj {
  path: string;
  name: string;
  folder: string;
  size: number;
  modified: number;       // Unix timestamp
  modified_iso: string;   // ISO 8601
}
```

---

## 3. Events

Events are plain objects with `type` and optional `payload`.

### 3a. Event Registry

| Event Type | Payload | Description |
|---|---|---|
| `MANIFEST_LOAD_START` | - | Manifest fetch initiated |
| `MANIFEST_LOAD_SUCCESS` | `{ files, folders, newest, meta }` | Manifest data received |
| `MANIFEST_LOAD_ERROR` | `{ error: string }` | Manifest fetch failed |
| `FILE_OPENED` | `{ path: string }` | User navigated to a file |
| `FILE_CLOSED` | - | User returned to list view |
| `FILTER_CHANGED` | `{ filter: string }` | User switched filter tab |
| `SEARCH_QUERY_CHANGED` | `{ query: string }` | User typed in search (debounced) |
| `SEARCH_CLEARED` | - | Search input cleared |
| `ITEM_PINNED` | `{ path: string }` | User pinned a file |
| `ITEM_UNPINNED` | `{ path: string }` | User unpinned a file |
| `ITEM_DISMISSED` | `{ id: string }` | User dismissed an item (badge, tip, etc.) |
| `FOLDER_TOGGLED` | `{ folder: string }` | User expanded/collapsed a folder |
| `ONBOARDING_STEP_COMPLETED` | `{ step: string }` | User completed an onboarding step |
| `SEARCH_HISTORY_ITEM_REMOVED` | `{ query: string }` | User removed a search history entry |
| `SEARCH_HISTORY_CLEARED` | - | User cleared all search history |
| `UNDO` | `{ eventType: string }` | Undo the last event of given type |
| `STATE_RESET` | `{ slice?: string }` | Reset state (specific slice or all) |
| `STATE_HYDRATED` | `{ slice: string, data: any }` | State restored from persistence |

### 3b. Event Shape

```typescript
interface StateEvent {
  type: string;
  payload?: Record<string, any>;
  timestamp: number;   // Date.now()
  source: 'user' | 'system' | 'persistence';
}
```

---

## 4. Reducers (Transition Rules)

Each reducer is a pure function: `(currentSlice, event) => newSlice`.

### 4a. Source Reducers

```
sourceReducer(source, event):
  MANIFEST_LOAD_START   -> { ...source, _status: 'loading' }
  MANIFEST_LOAD_SUCCESS -> { ...source, ...event.payload, _status: 'loaded' }
  MANIFEST_LOAD_ERROR   -> { ...source, _status: 'error' }
  STATE_RESET           -> initialSourceState
  default               -> source
```

### 4b. UI Reducers

```
uiReducer(ui, event):
  FILE_OPENED           -> { ...ui, currentFile: event.payload.path, viewMode: 'detail' }
  FILE_CLOSED           -> { ...ui, currentFile: null, viewMode: 'list' }
  FILTER_CHANGED        -> { ...ui, currentFilter: event.payload.filter, searchQuery: '' }
  SEARCH_QUERY_CHANGED  -> { ...ui, searchQuery: event.payload.query }
  SEARCH_CLEARED        -> { ...ui, searchQuery: '', searchResults: null }
  STATE_RESET           -> initialUIState
  default               -> ui
```

### 4c. Interaction Reducers

```
interactionReducer(interaction, event):
  FILE_OPENED ->
    viewed:         { ...viewed, [path]: { at: now, count: (prev?.count || 0) + 1 } }
    recentlyViewed: [path, ...recentlyViewed.filter(p => p !== path)].slice(0, MAX_RECENT)

  ITEM_PINNED ->
    pinned:         pinned.add(path)

  ITEM_UNPINNED ->
    pinned:         pinned.delete(path); return pinned

  ITEM_DISMISSED ->
    dismissed:      { ...dismissed, [id]: now }

  FOLDER_TOGGLED ->
    folderExpanded: { ...folderExpanded, [folder]: !folderExpanded[folder] }

  FILTER_CHANGED ->
    filterPreference: event.payload.filter

  SEARCH_QUERY_CHANGED (when query.length >= 2) ->
    searchHistory:  [query, ...searchHistory.filter(q => q !== query)].slice(0, MAX_HISTORY)

  ONBOARDING_STEP_COMPLETED ->
    onboarding:     { ...onboarding, [step]: 'completed' }

  STATE_RESET ->
    if event.payload.slice === 'interaction' -> initialInteractionState
    else -> interaction

  default -> interaction
```

### 4d. Sync Reducers

```
syncReducer(sync, event):
  Any event that mutates a slice ->
    dirty: dirty.add(sliceName)

  STATE_HYDRATED ->
    dirty:     dirty.delete(event.payload.slice)
    lastSaved: { ...lastSaved, [slice]: now }

  default -> sync
```

---

## 5. Selectors

Selectors compute derived values from one or more slices. They must be pure functions and should be memoizable.

### 5a. Selector Registry

| Selector | Inputs | Returns | Purpose |
|---|---|---|---|
| `selectVisibleFiles` | `source`, `ui`, `interaction` | `FileObj[]` | Files for current filter + search, sorted |
| `selectFileWithStatus` | `source.files`, `interaction.viewed`, `source.newest` | `EnrichedFile[]` | Each file with `isNew`, `isViewed`, `isPinned` |
| `selectIsFileNew` | `file`, `interaction.viewed`, `source.newest` | `boolean` | True if file is newest AND not yet viewed |
| `selectPinnedFiles` | `source.files`, `interaction.pinned` | `FileObj[]` | Pinned files only |
| `selectRecentlyViewed` | `source.files`, `interaction.recentlyViewed` | `FileObj[]` | Last N viewed files with full metadata |
| `selectFolderState` | `interaction.folderExpanded`, folder | `boolean` | Is specific folder expanded? |
| `selectSearchSuggestions` | `interaction.searchHistory`, query | `string[]` | History entries matching current prefix |
| `selectOnboardingProgress` | `interaction.onboarding` | `{ completed, total, percent }` | Overall onboarding completion |
| `selectFilterBadgeCounts` | `source`, `interaction` | `Record<string, number>` | Badge numbers for each filter tab |
| `selectHasDirtyState` | `sync` | `boolean` | Whether any slice needs saving |

### 5b. Key Selector: `selectIsFileNew`

This is the selector that resolves the original "NEW badge doesn't disappear" issue:

```
selectIsFileNew(file, viewed, newestList):
  isInNewest = newestList.some(n => n.path === file.path)
  isViewed   = viewed[file.path] !== undefined
  return isInNewest && !isViewed
```

The NEW badge renders **only when both conditions are true**: the file is in the newest list AND the user has NOT viewed it. Once `FILE_OPENED` fires, the `viewed` map updates, and the selector returns `false`.

---

## 6. Effects (Side Effects)

Effects run after state updates. They handle persistence and other I/O.

### 6a. Effect Registry

| Effect | Trigger | Action |
|---|---|---|
| `persistInteraction` | Any event that changes `interaction` slice | Save `interaction` to localStorage |
| `persistFilterPreference` | `FILTER_CHANGED` | Save preferred filter to localStorage |
| `hydrateOnLoad` | App init (before first render) | Read localStorage, dispatch `STATE_HYDRATED` for each slice |
| `updateURLHash` | `FILE_OPENED`, `FILE_CLOSED` | Update `window.location.hash` |
| `logTransition` | Any event (dev mode) | Console.log event + state diff |
| `migrateSchema` | `hydrateOnLoad` detects old version | Transform persisted data to current schema |

### 6b. Effect Execution Order

```
dispatch(event)
  -> run all reducers (synchronous, pure)
  -> notify selectors (recompute if inputs changed)
  -> run effects (async, side-effectful)
  -> re-render UI (via selector subscriptions)
```

---

## 7. Store API

Minimal public API for the state store:

```typescript
interface StateStore {
  // Read
  getState(): FullState;
  select<T>(selector: (state: FullState) => T): T;

  // Write
  dispatch(event: StateEvent): void;

  // Subscribe
  subscribe(selector: Function, callback: Function): Unsubscribe;

  // Persistence
  hydrate(): Promise<void>;
  flush(): Promise<void>;

  // Debug
  getEventLog(): StateEvent[];
  reset(slice?: string): void;
}
```

---

## 8. Constants and Configuration

```typescript
const MAX_RECENT = 20;          // Max recently viewed entries
const MAX_SEARCH_HISTORY = 30;  // Max search history entries
const DEBOUNCE_MS = 200;        // Search debounce
const SCHEMA_VERSION = 1;       // For persistence migration
const STORAGE_PREFIX = 'xpos_'; // localStorage key prefix

const PERSISTENCE_TIERS = {
  source:      'none',        // Re-fetched on every load
  ui:          'url',         // URL hash for currentFile only
  interaction: 'localStorage',
  sync:        'memory',      // Never persisted
};
```

---

## 9. Migration Strategy

When `SCHEMA_VERSION` changes:

1. Read raw data from localStorage.
2. Check stored `version` against current `SCHEMA_VERSION`.
3. Apply migration functions sequentially: `v1_to_v2(data)`, `v2_to_v3(data)`, etc.
4. Write migrated data back.
5. Dispatch `STATE_HYDRATED` with migrated data.

---

## 10. Architecture Diagram

```
┌──────────────────────────────────────────────────────┐
│                     UI Layer                         │
│  ┌───────────┐  ┌───────────┐  ┌───────────────┐    │
│  │ FileList  │  │ DetailView│  │ FilterTabs    │    │
│  │ Component │  │ Component │  │ Component     │    │
│  └─────┬─────┘  └─────┬─────┘  └──────┬────────┘    │
│        │              │               │              │
│        └──────────────┴───────────────┘              │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │   Selectors     │  (pure, memoized)   │
│              └────────┬────────┘                     │
│                       │                              │
├───────────────────────┼──────────────────────────────┤
│                       │                              │
│              ┌────────▼────────┐                     │
│              │   State Store   │                     │
│              │  ┌───────────┐  │                     │
│              │  │  source   │  │                     │
│              │  │  ui       │  │                     │
│              │  │  interact │  │                     │
│              │  │  sync     │  │                     │
│              │  └───────────┘  │                     │
│              └────────┬────────┘                     │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │   Reducers      │  (pure functions)   │
│              └────────┬────────┘                     │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │   Event Bus     │                     │
│              └────────┬────────┘                     │
│                       │                              │
├───────────────────────┼──────────────────────────────┤
│                       │                              │
│              ┌────────▼────────┐                     │
│              │   Effects       │                     │
│              │  ┌────────────┐ │                     │
│              │  │ persist    │ │                     │
│              │  │ hydrate    │ │                     │
│              │  │ URL sync   │ │                     │
│              │  │ log        │ │                     │
│              │  └────────────┘ │                     │
│              └────────┬────────┘                     │
│                       │                              │
│         ┌─────────────┼─────────────┐                │
│         ▼             ▼             ▼                │
│   localStorage   sessionStorage   URL hash           │
└──────────────────────────────────────────────────────┘
```

This contract is the foundation for all subsequent deliverables.

# Persistence Policy

Rules for choosing the correct storage tier for each type of state. This policy ensures data survives the right amount of time without over-persisting or under-persisting.

---

## 1. Storage Tiers

| Tier | Mechanism | Lifetime | Capacity | Scope |
|---|---|---|---|---|
| **Memory** | JS variable | Until page unload | Unlimited (within RAM) | Single page instance |
| **Session** | `sessionStorage` | Until tab/window closes | ~5 MB | Single tab |
| **Local** | `localStorage` | Until explicitly cleared | ~5-10 MB | Same origin, all tabs |
| **URL** | `window.location.hash` or query params | Until navigation/bookmark | ~2000 chars | Shareable, bookmarkable |
| **Remote** | API / database | Indefinite | Unlimited | Cross-device |

---

## 2. Tier Selection Decision Tree

```
Is this state derived from source data that is re-fetched on every load?
├── YES → MEMORY (no persistence needed)
│         Examples: source.files, source.folders, source.newest
│
└── NO → Does the user expect this state to survive a page reload?
         ├── NO → Is it useful within the same tab session?
         │        ├── YES → SESSION
         │        │         Examples: folderExpanded, scroll position
         │        └── NO  → MEMORY
         │                  Examples: searchQuery (current), hover state
         │
         └── YES → Should this state be shareable via URL?
                   ├── YES → URL
                   │         Examples: currentFile, deep-link filter
                   │
                   └── NO → Should this state sync across devices?
                            ├── YES → REMOTE (future)
                            │         Examples: user preferences, cross-device bookmarks
                            │
                            └── NO → LOCAL
                                     Examples: viewed, pinned, dismissed, searchHistory,
                                               filterPreference, onboarding
```

---

## 3. State-to-Tier Mapping

### 3a. Source State Slice

| State Key | Tier | Reason |
|---|---|---|
| `source.files` | Memory | Re-fetched from `files.json` on every load |
| `source.folders` | Memory | Derived from `files.json` |
| `source.newest` | Memory | Derived from `files.json` |
| `source.meta` | Memory | Metadata from manifest, re-read on load |
| `source._status` | Memory | Transient loading indicator |

### 3b. UI State Slice

| State Key | Tier | Reason |
|---|---|---|
| `ui.currentFile` | URL | Enables deep-linking and browser back/forward |
| `ui.currentFilter` | Memory* | Restored from `interaction.filterPreference` on load |
| `ui.searchQuery` | Memory | Transient; user re-types as needed |
| `ui.searchResults` | Memory | Computed cache; re-derived from query + source |
| `ui.viewMode` | Memory | Derived from `currentFile` presence |

*`ui.currentFilter` is initialized from the persisted `interaction.filterPreference` during hydration, but the UI slice itself is not persisted.

### 3c. Interaction State Slice

| State Key | Tier | Reason | Key Pattern |
|---|---|---|---|
| `interaction.viewed` | Local | User expects "read" status to persist indefinitely | `xpos_viewed` |
| `interaction.pinned` | Local | Bookmarks are a durable personal choice | `xpos_pinned` |
| `interaction.dismissed` | Local | Dismissals should survive reloads and sessions | `xpos_dismissed` |
| `interaction.recentlyViewed` | Local | History is valuable across sessions | `xpos_recent` |
| `interaction.folderExpanded` | Session | Layout state; reasonable to reset per session | `xpos_folders` |
| `interaction.filterPreference` | Local | Preference should stick | `xpos_filter_pref` |
| `interaction.searchHistory` | Local | Search history is personal, durable | `xpos_search_hist` |
| `interaction.onboarding` | Local | Completed steps should never re-appear | `xpos_onboarding` |

### 3d. Sync State Slice

| State Key | Tier | Reason |
|---|---|---|
| `sync.dirty` | Memory | Transient flag; only meaningful while app is running |
| `sync.lastSaved` | Memory | Diagnostic info; not needed across sessions |
| `sync.version` | Local | Schema version stored alongside data for migration |

---

## 4. Serialization Rules

### 4a. Format

All persisted state uses JSON. The stored value has this envelope:

```json
{
  "v": 1,
  "t": "2026-02-11T22:00:00.000Z",
  "d": { /* actual state data */ }
}
```

- `v`: Schema version for migration compatibility.
- `t`: Timestamp of last write.
- `d`: Data payload.

### 4b. Key Naming Convention

```
{STORAGE_PREFIX}{slice_key}

Example: xpos_viewed, xpos_pinned, xpos_search_hist
```

### 4c. Type-specific Serialization

| JS Type | Serialized As | Deserialization |
|---|---|---|
| `Object` | JSON object | `JSON.parse()` |
| `Array` | JSON array | `JSON.parse()` |
| `Set` | JSON array | `new Set(JSON.parse())` |
| `Map` | JSON object (via `Object.fromEntries`) | `new Map(Object.entries(JSON.parse()))` |
| `Date/ISO` | String | Parse as-is |

---

## 5. Lifecycle: Hydrate / Flush / Migrate

### 5a. Hydrate (Read)

Runs once at app init, before first render.

```
hydrate():
  for each (key, tier) in PERSISTENCE_MAP:
    if tier === 'local':
      raw = localStorage.getItem(STORAGE_PREFIX + key)
    elif tier === 'session':
      raw = sessionStorage.getItem(STORAGE_PREFIX + key)
    elif tier === 'url':
      raw = parseURLHash()

    if raw !== null:
      parsed = JSON.parse(raw)
      if parsed.v < SCHEMA_VERSION:
        parsed = migrate(parsed)
      dispatch(STATE_HYDRATED, { slice: key, data: parsed.d })
```

### 5b. Flush (Write)

Runs as an effect after any event that changes a persistent slice.

```
flush(sliceName, data):
  envelope = { v: SCHEMA_VERSION, t: new Date().toISOString(), d: data }
  serialized = JSON.stringify(envelope)

  tier = PERSISTENCE_MAP[sliceName]
  if tier === 'local':
    localStorage.setItem(STORAGE_PREFIX + sliceName, serialized)
  elif tier === 'session':
    sessionStorage.setItem(STORAGE_PREFIX + sliceName, serialized)
  elif tier === 'url':
    updateURLHash(data)
```

### 5c. Debounced Flush

For high-frequency events (e.g., `SEARCH_QUERY_CHANGED`), flush is debounced:

```
FLUSH_DEBOUNCE_MS = 500

// Interaction slice: flush 500ms after last change
// This prevents localStorage thrashing during rapid typing
```

### 5d. Migration

```
migrate(envelope):
  while envelope.v < SCHEMA_VERSION:
    migrator = MIGRATORS[envelope.v]
    envelope = migrator(envelope)
    envelope.v += 1
  return envelope

MIGRATORS = {
  1: (env) => {
    // v1 -> v2: Example: add 'onboarding' key if missing
    if (!env.d.onboarding) env.d.onboarding = DEFAULT_ONBOARDING;
    return env;
  }
}
```

---

## 6. Conflict Resolution

### 6a. Multiple Tabs

Since `localStorage` is shared across tabs on the same origin:

- **Read**: Each tab hydrates independently on load. No live sync between tabs (acceptable for document explorer).
- **Write**: Last-write-wins. Given that this is a single-user, personal-use app, conflicts are rare.
- **Future enhancement**: Use `StorageEvent` listener to sync across tabs if needed.

### 6b. Stale Data

| Problem | Solution |
|---|---|
| Persisted file path no longer in manifest | Selector filters it out; lazy cleanup on next flush |
| Persisted filter no longer exists | Fallback to `'all'` during hydration |
| Persisted data has unknown keys | Ignored (forward-compatible); old keys pruned on next schema migration |
| Persisted data older than TTL | Per-key TTL check during hydration; expired data discarded |

### 6c. TTL Rules

| State | TTL | Reason |
|---|---|---|
| `viewed` | 90 days per entry | Very old "viewed" markers are irrelevant |
| `dismissed` | No TTL (permanent) | User chose to dismiss; respect that |
| `recentlyViewed` | 30 days per entry | Stale history is noise |
| `searchHistory` | 30 days per entry | Same as above |
| `pinned` | No TTL | Active choice; only removed by user action |
| `onboarding` | No TTL | Completed steps never re-appear |
| `filterPreference` | No TTL | Always valid |
| `folderExpanded` | Session only | Inherently short-lived |

---

## 7. Storage Budget

Estimated storage per key (generous estimates):

| Key | Max Size | Calculation |
|---|---|---|
| `xpos_viewed` | ~10 KB | 200 files * ~50 bytes per entry |
| `xpos_pinned` | ~2 KB | 50 files * ~40 bytes per path |
| `xpos_dismissed` | ~2 KB | 50 items * ~40 bytes |
| `xpos_recent` | ~1 KB | 20 paths * ~50 bytes |
| `xpos_search_hist` | ~2 KB | 30 queries * ~60 bytes |
| `xpos_filter_pref` | ~20 bytes | Single string |
| `xpos_onboarding` | ~200 bytes | Small object |
| `xpos_folders` | ~500 bytes | Folder names + booleans |
| **Total** | **~18 KB** | Well within 5 MB limit |

---

## 8. Cleanup Strategy

To prevent localStorage from growing unbounded:

1. **On hydrate**: Run TTL check; remove expired entries.
2. **On flush**: If total persisted size > `MAX_STORAGE_KB` (100 KB), prune oldest entries from `recentlyViewed` and `searchHistory` first.
3. **On version migration**: Remove deprecated keys.
4. **Manual reset**: `STATE_RESET` event clears all persisted data for the specified slice.

---

## 9. Summary Table

| Slice | Tier | Serialize | TTL | Debounce | Migration |
|---|---|---|---|---|---|
| `source` | Memory | N/A | N/A | N/A | N/A |
| `ui` | Memory + URL | Hash only | N/A | N/A | N/A |
| `interaction.viewed` | Local | JSON envelope | 90d | 500ms | Yes |
| `interaction.pinned` | Local | JSON envelope | None | Immediate | Yes |
| `interaction.dismissed` | Local | JSON envelope | None | Immediate | Yes |
| `interaction.recentlyViewed` | Local | JSON envelope | 30d | 500ms | Yes |
| `interaction.folderExpanded` | Session | JSON envelope | Session | Immediate | No |
| `interaction.filterPreference` | Local | JSON envelope | None | Immediate | Yes |
| `interaction.searchHistory` | Local | JSON envelope | 30d | 500ms | Yes |
| `interaction.onboarding` | Local | JSON envelope | None | Immediate | Yes |
| `sync` | Memory | N/A | N/A | N/A | N/A |

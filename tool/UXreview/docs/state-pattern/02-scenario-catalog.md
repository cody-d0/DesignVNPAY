# Scenario Catalog: Stateful UX Use Cases

8 concrete scenarios that exercise the State Contract. Each scenario specifies preconditions, event sequence, state transitions, expected UI outcome, and persistence behavior.

---

## Scenario 1: NEW Badge — Hide After Viewed

**Context**: The original motivating case. A file marked "newest" in the manifest should display a NEW badge until the user opens it.

### Precondition
- `source.newest` contains `{ path: "README.md", ... }`
- `interaction.viewed` does NOT have key `"README.md"`
- `selectIsFileNew("README.md")` returns `true`

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `MANIFEST_LOAD_SUCCESS` | `{ newest: [{ path: "README.md", ... }], ... }` |
| 2 | `FILE_OPENED` | `{ path: "README.md" }` |

### State Transitions

| After Event | `interaction.viewed` | `selectIsFileNew("README.md")` |
|---|---|---|
| Event 1 | `{}` | `true` |
| Event 2 | `{ "README.md": { at: "2026-02-11T...", count: 1 } }` | `false` |

### Expected UI
- **Before event 2**: File list shows `<span class="newest-badge">NEW</span>` next to README.md.
- **After event 2**: Badge is gone. File remains in "Newest" filter but without visual highlight.
- **After page reload**: Badge stays gone (persisted in localStorage).

### Persistence
- `interaction.viewed` saved to `localStorage` after event 2.
- On next load, `hydrateOnLoad` restores `viewed`, selector still returns `false`.

### Edge Cases
- User opens same file 5 times: `count` increments to 5, badge remains hidden.
- New manifest version adds file: badge appears for new file only.
- User resets state: all viewed records cleared, badges reappear.

---

## Scenario 2: Dismissible Announcements

**Context**: A banner or tooltip (e.g., "New folder grouping feature!") can be permanently dismissed by the user.

### Precondition
- Announcement ID `"announce-folder-grouping"` is defined in source data.
- `interaction.dismissed` does NOT have this ID.

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | Page load | (hydrate from localStorage) |
| 2 | `ITEM_DISMISSED` | `{ id: "announce-folder-grouping" }` |

### State Transitions

| After Event | `interaction.dismissed` | UI Shows Banner? |
|---|---|---|
| Event 1 | `{}` | Yes |
| Event 2 | `{ "announce-folder-grouping": "2026-02-11T..." }` | No |

### Expected UI
- Banner with close (X) button visible on load.
- After click X, banner slides out and never returns.
- After reload, banner remains hidden.

### Persistence
- `interaction.dismissed` -> `localStorage`, durable.

### Edge Cases
- Multiple announcements: each has its own ID, dismissed independently.
- Announcement has an expiry date: selector checks `if (now > announcement.expiry) return false` (never show expired, even if not dismissed).
- Undo dismiss within 5 seconds (toast with "Undo"): dispatch `UNDO { eventType: 'ITEM_DISMISSED' }`, remove from `dismissed`.

---

## Scenario 3: Recently Viewed Files

**Context**: A "Recent" section shows the last N files the user opened, ordered by recency.

### Precondition
- `interaction.recentlyViewed` is `["A.md", "B.md"]` (max 20).
- User opens `"C.md"`.

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `FILE_OPENED` | `{ path: "C.md" }` |
| 2 | `FILE_OPENED` | `{ path: "A.md" }` |

### State Transitions

| After Event | `interaction.recentlyViewed` |
|---|---|
| Initial | `["A.md", "B.md"]` |
| Event 1 | `["C.md", "A.md", "B.md"]` |
| Event 2 | `["A.md", "C.md", "B.md"]` |

### Expected UI
- "Recent" filter tab shows files in `recentlyViewed` order.
- Most recently opened file appears first.
- Re-opening a file moves it to the top (no duplicates).

### Persistence
- `interaction.recentlyViewed` -> `localStorage`.
- On load, list restored; files that no longer exist in manifest are filtered out.

### Edge Cases
- Open 25 files: list truncated to 20, oldest 5 dropped.
- File renamed in manifest: old path stays in `recentlyViewed` but selector filters it out (not in `source.files`).

---

## Scenario 4: Pinned Files

**Context**: User pins important files to keep them accessible at the top of any view.

### Precondition
- `interaction.pinned` is `Set {}` (empty).
- File `"QUICK-START.md"` exists in `source.files`.

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `ITEM_PINNED` | `{ path: "QUICK-START.md" }` |
| 2 | `ITEM_PINNED` | `{ path: "README.md" }` |
| 3 | `ITEM_UNPINNED` | `{ path: "QUICK-START.md" }` |

### State Transitions

| After Event | `interaction.pinned` |
|---|---|
| Initial | `Set {}` |
| Event 1 | `Set { "QUICK-START.md" }` |
| Event 2 | `Set { "QUICK-START.md", "README.md" }` |
| Event 3 | `Set { "README.md" }` |

### Expected UI
- Pinned files appear in a dedicated "Pinned" section at the top of the file list.
- Pin icon (filled) next to pinned files; outline icon for unpinned.
- "Pinned" filter tab shows only pinned files with badge count.
- Unpinning removes file from pinned section instantly.

### Persistence
- `interaction.pinned` (serialized as array) -> `localStorage`.

### Edge Cases
- Pin a file, then file is removed from manifest: selector filters out, pinned set still holds the path but UI skips it.
- Pin all files: "Pinned" section equals full list, which is valid but unusual.

---

## Scenario 5: Onboarding Checklist

**Context**: First-time users see a multi-step onboarding checklist (e.g., "Open a file", "Try search", "Switch filter"). Steps complete as actions are performed.

### Precondition
- `interaction.onboarding` is `{ "open-file": "pending", "try-search": "pending", "switch-filter": "pending" }`.

### Event Sequence

| # | Event | Derived Onboarding Event |
|---|---|---|
| 1 | `FILE_OPENED` | `ONBOARDING_STEP_COMPLETED { step: "open-file" }` |
| 2 | `SEARCH_QUERY_CHANGED` | `ONBOARDING_STEP_COMPLETED { step: "try-search" }` |
| 3 | `FILTER_CHANGED` | `ONBOARDING_STEP_COMPLETED { step: "switch-filter" }` |

### State Transitions

| After Event | `interaction.onboarding` | `selectOnboardingProgress` |
|---|---|---|
| Initial | all `"pending"` | `{ completed: 0, total: 3, percent: 0 }` |
| Event 1 | `open-file: "completed"` | `{ completed: 1, total: 3, percent: 33 }` |
| Event 2 | `+ try-search: "completed"` | `{ completed: 2, total: 3, percent: 67 }` |
| Event 3 | all `"completed"` | `{ completed: 3, total: 3, percent: 100 }` |

### Expected UI
- Checklist panel visible until all steps complete.
- Each step shows checkmark or circle.
- Progress bar updates in real-time.
- On 100% completion, panel auto-dismisses after 2s with congratulation message.
- Panel never reappears after completion (unless state reset).

### Persistence
- `interaction.onboarding` -> `localStorage`.

### Edge Cases
- User completes step 2 before step 1: checklist updates out of order (valid).
- New onboarding steps added in future version: migration adds new steps as "pending" while preserving completed ones.

---

## Scenario 6: Search History

**Context**: The search bar remembers recent queries and suggests them as the user types.

### Precondition
- `interaction.searchHistory` is `["inventory", "user flow"]`.
- User types `"deploy"`.

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `SEARCH_QUERY_CHANGED` | `{ query: "deploy" }` |
| 2 | `SEARCH_CLEARED` | - |
| 3 | `SEARCH_QUERY_CHANGED` | `{ query: "inv" }` |

### State Transitions

| After Event | `interaction.searchHistory` | `selectSearchSuggestions(query)` |
|---|---|---|
| Event 1 | `["deploy", "inventory", "user flow"]` | (not searching) |
| Event 2 | unchanged | `[]` |
| Event 3 | `["inv", "deploy", "inventory", "user flow"]`* | `["inventory"]` |

*Note: "inv" only added if length >= 2 and not a duplicate prefix of an existing entry. The exact dedup rule is configurable.

### Expected UI
- Dropdown below search input showing matching history entries.
- Click suggestion to fill search input and trigger search.
- "Clear history" button at the bottom of dropdown.
- Individual entries removable with X button.

### Persistence
- `interaction.searchHistory` -> `localStorage`.

### Edge Cases
- History reaches max (30): oldest entry dropped on new addition.
- `SEARCH_HISTORY_CLEARED`: empties array, dropdown shows "No recent searches".
- Very long query (>100 chars): truncated before storage.

---

## Scenario 7: Filter Preference Memory

**Context**: The user's last selected filter tab is remembered across page reloads.

### Precondition
- `interaction.filterPreference` is `null` (first visit).
- Default filter is `'all'`.

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `FILTER_CHANGED` | `{ filter: "newest" }` |
| 2 | Page reload | (hydrate from localStorage) |

### State Transitions

| After Event | `interaction.filterPreference` | Active Tab |
|---|---|---|
| Initial | `null` | "All" |
| Event 1 | `"newest"` | "Newest" |
| After reload | `"newest"` (hydrated) | "Newest" |

### Expected UI
- On first visit: "All" tab active.
- User clicks "Newest": tab switches, preference saved.
- On reload: "Newest" tab is pre-selected, showing newest files immediately.
- If user explicitly clicks "All": preference updated to "all".

### Persistence
- `interaction.filterPreference` -> `localStorage`.

### Edge Cases
- Stored preference for a filter that no longer exists (e.g., removed "pinned" tab): fallback to "all".
- URL hash `#view=file.md` overrides filter (user lands on detail view regardless of preference).

---

## Scenario 8: Folder Expand/Collapse State

**Context**: Folder sections in the file list can be collapsed to reduce visual clutter. The expand/collapse state persists within the session.

### Precondition
- `interaction.folderExpanded` is `{}` (all folders default to expanded = `true`).
- Three folders visible: "Root", "XPOS", ".agents".

### Event Sequence

| # | Event | Payload |
|---|---|---|
| 1 | `FOLDER_TOGGLED` | `{ folder: "Root" }` |
| 2 | `FOLDER_TOGGLED` | `{ folder: ".agents" }` |
| 3 | `FOLDER_TOGGLED` | `{ folder: "Root" }` |

### State Transitions

| After Event | `interaction.folderExpanded` |
|---|---|
| Initial | `{}` (all expanded by default) |
| Event 1 | `{ "Root": false }` (collapsed) |
| Event 2 | `{ "Root": false, ".agents": false }` |
| Event 3 | `{ "Root": true, ".agents": false }` (re-expanded) |

### Expected UI
- Folder header shows chevron icon (▶ collapsed, ▼ expanded).
- Click header toggles with smooth animation (max 200ms).
- Collapsed folder shows only the header with file count.
- Expanded folder shows all files.

### Persistence
- `interaction.folderExpanded` -> `sessionStorage` (resets on new browser session, which is appropriate for layout state).

### Edge Cases
- New folder appears in updated manifest: defaults to expanded (not in `folderExpanded` map).
- User searches: all folders auto-expand to show results, collapse state restored after search cleared.
- Print mode: all folders force-expanded.

---

## Scenario Summary Matrix

| # | Scenario | Events Used | State Slice | Persistence | Undo Support |
|---|---|---|---|---|---|
| 1 | NEW badge | `FILE_OPENED` | `interaction.viewed` | localStorage | Reset only |
| 2 | Dismissible announcements | `ITEM_DISMISSED`, `UNDO` | `interaction.dismissed` | localStorage | Yes (5s toast) |
| 3 | Recently viewed | `FILE_OPENED` | `interaction.recentlyViewed` | localStorage | No (auto-managed) |
| 4 | Pinned files | `ITEM_PINNED`, `ITEM_UNPINNED` | `interaction.pinned` | localStorage | Yes (toggle) |
| 5 | Onboarding checklist | `ONBOARDING_STEP_COMPLETED` | `interaction.onboarding` | localStorage | Reset only |
| 6 | Search history | `SEARCH_QUERY_CHANGED`, `SEARCH_HISTORY_CLEARED` | `interaction.searchHistory` | localStorage | Individual remove |
| 7 | Filter preference | `FILTER_CHANGED` | `interaction.filterPreference` | localStorage | Overwrite |
| 8 | Folder expand/collapse | `FOLDER_TOGGLED` | `interaction.folderExpanded` | sessionStorage | Toggle |

All 8 scenarios share the same State Contract architecture. No scenario requires modifying the store, event bus, or selector infrastructure -- each only adds:
1. New event type(s)
2. New reducer rule(s) in the appropriate slice
3. New selector(s)
4. Persistence tier declaration

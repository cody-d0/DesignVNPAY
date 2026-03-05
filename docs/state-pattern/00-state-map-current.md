# State Map: Current Implementation

Audit of all state variables, events, and rendering flows in `index.html` as of 2026-02-12.

## 1. State Variables (top-level `let`)

| Variable | Type | Origin | Mutated By | Persisted? |
|---|---|---|---|---|
| `allFiles` | `Array<FileObj>` | `files.json` fetch | `loadManifest()` | No (re-fetched on load) |
| `allFolders` | `Object<string, FileObj[]>` | `files.json` fetch | `loadManifest()` | No |
| `newestFiles` | `Array<FileObj>` | `files.json` fetch | `loadManifest()` | No |
| `currentFile` | `string \| null` | Hash route | `viewFile()`, `showFileList()` | URL hash only |
| `currentSort` | `'folder' \| 'lastupdate'` | User click | `handleSortChange()` | No |

## 2. Persisted State (localStorage)

| Key | Type | Values | Used For |
|---|---|---|---|
| `xpos-docs-theme` | string | `'light'` \| `'dark'` | Base theme mode |
| `xpos-docs-mesh` | string | `'true'` \| `'false'` | Mesh gradient overlay |
| `collapsedFolders` | JSON | `{ [folder: string]: boolean }` | Folder collapse state |

*Effective theme:* `data-theme` = mode + (mesh ? '-mesh' : '') → `light`, `light-mesh`, `dark`, `dark-mesh`

## 3. Implicit State (DOM-derived, not stored in JS)

| State | Where | Derived From |
|---|---|---|
| Active tab highlight | `.filter-tab.active` CSS class | `currentSort` |
| Search query | `#search-input.value` | User typing |
| Breadcrumb text | `#breadcrumb.textContent` | `currentFile` or file counts |
| File list / markdown view toggle | `display` style + `.active` class | `currentFile` presence |

## 4. Event Inventory

| User Action | Handler | State Changed | Side Effect |
|---|---|---|---|
| Page load | `init()` | All source state | Fetch manifest, setup listeners |
| Click filter tab | `handleSortChange(sort)` | `currentSort` | Re-render file list |
| Click theme Sáng/Tối | `applyTheme()` | `xpos-docs-theme` | Set data-theme |
| Click Mesh toggle | `applyTheme()` | `xpos-docs-mesh` | Toggle mesh gradient |
| Type in search | `handleSearch(e)` (debounced 200ms) | None (DOM only) | Re-render filtered list |
| Click file link | Hash change -> `handleRoute()` -> `viewFile()` | `currentFile` | Fetch + render markdown |
| Click Back button | Hash change -> `handleRoute()` -> `showFileList()` | `currentFile = null` | Restore list view |
| Press `/` key | keydown listener | None | Focus search input |

## 5. Data Flow Diagram

```
files.json
  |
  v
loadManifest() ──> allFiles, allFolders, newestFiles
                        |
                        v
                  renderFolders() / renderNewestFiles()
                        |
                        v
                  createFileItemHTML(file, isNewest)
                        |
                        v
                  DOM innerHTML replacement

User click file  ──>  hash change  ──>  viewFile(path)
                                            |
                                            v
                                      fetch(path) ──> marked.parse() ──> DOM
```

## 6. Gap Analysis: What is Missing

### 5a. No `interactionState` Layer

The app tracks **what the data is** and **what the user is looking at right now**, but never tracks **what the user has done before**. Specific gaps:

| Missing State | Example | Impact |
|---|---|---|
| `viewed` per file | NEW badge never clears after viewing | User cannot distinguish read vs unread |
| `dismissed` per item | No way to hide announcements or tips | Stale badges accumulate |
| `pinned` per file | No way to mark favorites | No personalization |
| `recentlyViewed` list | No history of navigation | User cannot retrace steps |
| `folderExpanded` map | Folders have no expand/collapse | Always fully open |
| `filterPreference` | Filter resets to "All" on reload | User must re-select every visit |
| `searchHistory` | No recall of past searches | Repeated typing |

### 5b. No Persistence

Every state variable is lost on page reload. The only surviving state is the URL hash (`#view=path`), which preserves the "currently viewed file" but nothing else.

### 5c. No Event Bus / Centralized Dispatch

Events are handled by individual listener functions that directly mutate top-level variables and call render functions. There is no central place to:
- Log state transitions
- Apply cross-cutting rules (e.g., "on FILE_OPENED, also update recentlyViewed")
- Undo/redo

### 5d. Selectors Are Inline

Rendering functions read raw state directly. There is no selector layer to compute derived values like "is this file new AND unviewed?" -- the `isNewest` check is done inline inside `renderFolders()`.

## 7. Classification of Existing State

| State | Category | Should Persist? |
|---|---|---|
| `allFiles` | sourceState | No (fetched fresh) |
| `allFolders` | sourceState | No (fetched fresh) |
| `newestFiles` | sourceState (derived) | No (fetched fresh) |
| `currentFile` | uiState | URL hash (already works) |
| `currentSort` | uiState | No |
| `xpos-docs-theme` | uiState | localStorage |
| `xpos-docs-mesh` | uiState | localStorage |
| `collapsedFolders` | interactionState | localStorage |
| search query | uiState | No (transient) |
| viewed files | interactionState | localStorage (missing) |
| pinned files | interactionState | localStorage (missing) |
| recently viewed | interactionState | localStorage (missing) |
| folder expand state | interactionState | sessionStorage (missing) |
| dismissed items | interactionState | localStorage (missing) |
| search history | interactionState | localStorage (missing) |

## 8. Summary

The current architecture has a clean **sourceState -> render** pipeline but is entirely stateless regarding user interactions. Adding any "memory" feature (viewed, pinned, history, preferences) requires introducing:

1. A state store that separates source data from interaction data.
2. An event system that allows cross-cutting updates.
3. A persistence layer with tiered storage policies.
4. Selectors that merge source + interaction state for rendering.

This gap analysis directly feeds into the State Contract design (next deliverable).

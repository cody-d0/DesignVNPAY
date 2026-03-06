# UX Quality Checklist & KPIs for Stateful Interactions

Measurement framework for evaluating stateful UX before, during, and after implementing the state pattern.

---

## 1. KPI Definitions

### 1a. Core KPIs

| KPI | Definition | How to Measure | Target |
|---|---|---|---|
| **State Consistency** | Percentage of interactions where visible UI accurately reflects internal state | Automated test: dispatch event → assert selector output matches rendered DOM | 100% |
| **Task Completion Rate** | Percentage of users who complete a stateful task (e.g., dismiss a badge, pin a file) without confusion or backtracking | Scenario walkthrough: count successful completions vs attempts | ≥ 95% |
| **Confusion Rate** | Percentage of interactions where the user performs an unexpected or redundant action due to unclear state feedback | Observe: count extra clicks, re-clicks, or "why didn't it work?" moments | ≤ 5% |
| **Recoverability** | Percentage of unintended state changes that the user can reverse within one action | Count features with undo/toggle vs total features | ≥ 80% |
| **Persistence Accuracy** | Percentage of state that correctly survives the intended lifecycle (reload, session, permanent) | Test: change state → reload/close/reopen → verify state matches expectation | 100% |
| **Load Time Impact** | Additional milliseconds added by hydration from storage | Performance test: measure `hydrate()` duration | ≤ 50ms |

### 1b. Secondary KPIs

| KPI | Definition | Target |
|---|---|---|
| **Feature Isolation** | Adding a new feature requires 0 modifications to existing features | 0 cross-feature changes |
| **State Freshness** | No stale data visible to user (e.g., badge for deleted file) | 0 stale items rendered |
| **Extensibility Score** | Number of files/sections touched to add a Trivial-tier feature | ≤ 5 touchpoints |
| **Schema Migration Success** | Percentage of users whose persisted data migrates without data loss on version update | 100% |

---

## 2. Per-Feature Quality Checklist

Run this checklist for every stateful feature before shipping.

### 2a. State Accuracy

- [ ] **Initial state is correct**: On first visit (no persisted data), the feature shows the expected default.
- [ ] **State updates immediately**: After the triggering event, the UI reflects the new state without delay (< 100ms).
- [ ] **State is idempotent**: Dispatching the same event twice does not corrupt state (e.g., pinning an already-pinned file is a no-op).
- [ ] **Derived state is consistent**: Selectors that combine multiple slices never show contradictory information.

### 2b. Persistence

- [ ] **Survives reload**: State stored in `localStorage` is intact after `F5` / `Cmd+R`.
- [ ] **Survives session close** (if applicable): State in `localStorage` persists after closing and reopening the browser.
- [ ] **Resets on new session** (if applicable): State in `sessionStorage` is gone after closing the tab.
- [ ] **URL state is bookmarkable**: Deep links (e.g., `#view=file.md`) work when shared or bookmarked.
- [ ] **No stale data**: Files removed from manifest are not shown via persisted state (selector filters them).
- [ ] **Schema migration works**: Bumping `SCHEMA_VERSION` correctly transforms old persisted data.

### 2c. User Feedback

- [ ] **Action has visible feedback**: Every dispatch results in a visible UI change within 100ms.
- [ ] **Hover/focus states exist**: Interactive elements (pin button, dismiss X, bookmark) have hover and focus indicators.
- [ ] **ARIA attributes update**: Screen readers receive updated state (e.g., `aria-pressed="true"` for pinned).
- [ ] **Loading state shown**: If a state change triggers async work, a loading indicator appears.
- [ ] **Error state shown**: If persistence fails (e.g., localStorage full), user sees a non-blocking warning.

### 2d. Recoverability

- [ ] **Undo available**: Features with significant impact (dismiss, clear history) offer undo within a time window.
- [ ] **Toggle works**: Toggle-type features (pin/unpin, expand/collapse) are reversible in one click.
- [ ] **Reset available**: User can reset a specific feature's state (e.g., "Clear all pinned files").
- [ ] **No accidental data loss**: Destructive actions (clear history, reset all) require confirmation or undo toast.

### 2e. Performance

- [ ] **Hydration is fast**: `hydrate()` completes in < 50ms for all slices combined.
- [ ] **Flush is non-blocking**: `flush()` does not freeze the UI (uses `requestIdleCallback` or similar).
- [ ] **Selectors are efficient**: Selectors used in list rendering are O(n) or better; no unnecessary recomputation.
- [ ] **No memory leaks**: Subscriptions are cleaned up when components are destroyed.

---

## 3. Scenario-Based Quality Tests

These are black-box tests that validate UX quality across the 8 scenarios.

### Test 1: NEW Badge Lifecycle

| Step | Action | Expected |
|---|---|---|
| 1 | Load app, observe file list | NEW badges visible on newest files |
| 2 | Click a file with NEW badge | Badge disappears from list when returning |
| 3 | Reload page | Badge remains hidden (persisted) |
| 4 | Wait 90+ days (simulate) | Viewed record expires; badge reappears if file still in newest |

**KPIs tested**: State Consistency, Persistence Accuracy, Task Completion

### Test 2: Dismiss + Undo

| Step | Action | Expected |
|---|---|---|
| 1 | See announcement banner | Banner visible |
| 2 | Click X to dismiss | Banner slides out; undo toast appears |
| 3 | Click Undo within 5 seconds | Banner slides back in |
| 4 | Click X again, wait > 5 seconds | Banner permanently gone |
| 5 | Reload page | Banner still hidden |

**KPIs tested**: Recoverability, Confusion Rate, Persistence Accuracy

### Test 3: Recently Viewed Ordering

| Step | Action | Expected |
|---|---|---|
| 1 | Open file A, then B, then C | Recent list shows C, B, A (most recent first) |
| 2 | Open A again | Recent list shows A, C, B |
| 3 | Reload page | Same order preserved |
| 4 | Open 21 files | Oldest entry dropped; list has exactly 20 |

**KPIs tested**: State Consistency, Persistence Accuracy, State Freshness

### Test 4: Pin Toggle Rapid Clicks

| Step | Action | Expected |
|---|---|---|
| 1 | Click pin 3 times rapidly | Final state is pinned (odd number of toggles) |
| 2 | Check state store | `pinned` set has exactly 1 entry |
| 3 | Reload | Pin state preserved correctly |

**KPIs tested**: State Consistency (idempotency), Persistence Accuracy

### Test 5: Search History + Privacy

| Step | Action | Expected |
|---|---|---|
| 1 | Search "inventory", "deploy", "user" | History shows 3 entries |
| 2 | Click "Clear history" | Confirmation or undo offered |
| 3 | Confirm clear | History empty; dropdown shows "No recent searches" |
| 4 | Reload | History still empty |

**KPIs tested**: Recoverability, Task Completion, Persistence Accuracy

### Test 6: Filter Preference Across Sessions

| Step | Action | Expected |
|---|---|---|
| 1 | Switch to "Newest" filter | Filter active |
| 2 | Close browser entirely | - |
| 3 | Reopen app | "Newest" filter pre-selected |
| 4 | Navigate to `#view=file.md` | Detail view shown (filter irrelevant) |
| 5 | Press Back | Returns to list with "Newest" filter active |

**KPIs tested**: Persistence Accuracy, State Consistency

### Test 7: Folder Collapse + Search Interaction

| Step | Action | Expected |
|---|---|---|
| 1 | Collapse "Root" folder | Folder shows collapsed state |
| 2 | Search for a file in "Root" | "Root" auto-expands to show result |
| 3 | Clear search | "Root" returns to collapsed state |
| 4 | Close tab, reopen | "Root" expanded (session-level state cleared) |

**KPIs tested**: State Consistency, Confusion Rate, Persistence (session tier)

### Test 8: Onboarding Completion

| Step | Action | Expected |
|---|---|---|
| 1 | First visit | Checklist visible, 0/3 complete |
| 2 | Open any file | "Open a file" step marked complete, 1/3 |
| 3 | Type in search | "Try search" complete, 2/3 |
| 4 | Switch filter tab | "Switch filter" complete, 3/3 |
| 5 | After 2 seconds | Checklist auto-dismisses with congratulation |
| 6 | Reload | Checklist never appears again |

**KPIs tested**: Task Completion, Persistence Accuracy, State Consistency

---

## 4. Before/After Comparison Framework

Use this matrix to evaluate UX improvement from applying the state pattern.

| Dimension | Before (Current) | After (With Pattern) | Improvement |
|---|---|---|---|
| NEW badge behavior | Always visible, even after viewing | Hides after first view | Reduces cognitive noise |
| Filter memory | Resets to "All" on every reload | Remembers last choice | Saves 1 click per visit |
| Recently viewed | None | Last 20 files accessible | Faster re-navigation |
| Pinned files | None | Persistent favorites | Personalized workspace |
| Folder state | Always expanded | Remembers collapsed | Reduced visual clutter |
| Search history | None | Recent queries suggested | Faster repeat searches |
| Onboarding | None | Guided first-use | Lower confusion for new users |
| Dismiss announcements | None | One-click permanent dismiss | Respect user attention |
| Undo capability | None | Undo for destructive actions | Safety net for mistakes |
| Cross-reload state | Lost entirely | Preserved by tier | Continuity of experience |

### Scoring

For each dimension, score 0-3:
- **0**: No stateful behavior (current state for most features)
- **1**: State exists but unreliable (bugs, stale data, no persistence)
- **2**: State works correctly with persistence and feedback
- **3**: State works + undo + accessibility + edge cases handled

**Current total**: 1/30 (only `currentFile` via URL hash scores 1)
**Target total**: ≥ 24/30 (all features at level 2+, key features at level 3)

---

## 5. Monitoring and Observability

For production apps, consider these observability measures:

| Metric | Collection Method | Purpose |
|---|---|---|
| Event dispatch count per session | In-memory counter, flushed to analytics | Understand feature usage |
| Hydration success/failure rate | Try/catch in `hydrate()`, log errors | Detect persistence issues |
| Migration trigger count | Counter in `migrate()` | Track version adoption |
| localStorage usage (bytes) | `JSON.stringify(localStorage).length` on load | Prevent quota issues |
| Stale data cleanup count | Counter in TTL check | Validate cleanup strategy |

---

## 6. Summary Scorecard Template

Use this template for periodic UX quality reviews:

```
┌─────────────────────────────────────────────┐
│         UX Quality Scorecard                │
│         Date: ___________                   │
├─────────────────────────────────────────────┤
│ State Consistency       [__] / 100%         │
│ Task Completion Rate    [__] / 100%         │
│ Confusion Rate          [__] ≤ 5%           │
│ Recoverability          [__] / 100%         │
│ Persistence Accuracy    [__] / 100%         │
│ Load Time Impact        [__] ms ≤ 50ms      │
│ Feature Isolation       [__] / 0 changes    │
│ Extensibility Score     [__] ≤ 5 files      │
├─────────────────────────────────────────────┤
│ Features Checklist Pass [__] / [__]         │
│ Scenario Tests Pass     [__] / 8            │
│ Dimension Score         [__] / 30           │
├─────────────────────────────────────────────┤
│ Overall Grade:  ___                         │
│   A: All KPIs green                         │
│   B: 1-2 KPIs yellow, 0 red                │
│   C: 1+ KPIs red                            │
└─────────────────────────────────────────────┘
```

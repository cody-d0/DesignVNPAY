---
name: overlay-detect
description: >
  Detect overlay/modal/bottom-sheet patterns in Figma artboards for accurate screen boundary
  detection. Use when: Phase 2a-bis boundary detection needs to determine if an artboard is a
  standalone screen or an overlay on another screen (modal, bottom sheet, picker, OTP dialog,
  search overlay). Triggers: "overlay detection", "boundary detection", "screen boundary",
  "bottom sheet", "modal detection", "overlay merge". Supports any domain (banking, e-commerce,
  social, enterprise). Replaces static 3-signal Bước 2.6 with 7-signal weighted vision+metadata
  detection.
---

# Overlay Detection

Classify Figma artboards as **overlay** (merge into parent boundary) or **standalone screen** (separate boundary) using a 7-signal weighted scoring model.

## Algorithm

### Step 1: Metadata Pre-Classification (cheap, deterministic)

Run the pre-classifier script:

```bash
node .agents/skills/overlay-detect/scripts/overlay-classify.js <metadata_json> <section_node_id>
```

**Input:** Figma metadata JSON (from REST API `depth=10`) + section node ID.
**Output:** `pre_classification[]` — one entry per artboard with metadata signals extracted.

### Step 2: Agent Vision Classification (per artboard)

For each artboard flagged `needs_vision: true` by Step 1, read the artboard screenshot and evaluate **7 weighted signals**:

| # | Signal | Wt | How to evaluate |
|---|--------|---:|-----------------|
| S1 | Same name as section | 1 | From pre-classifier: `s1_same_name` |
| S2 | Shared header with another artboard | 2 | **Vision:** Compare header bar (top ~120px) with the primary form artboard in same section. Same header title + back button + status bar = shared |
| S3 | Dimmed/blurred background | 3 | **Vision:** Is there a darkened/dimmed layer behind the main content? Semi-transparent overlay effect? |
| S4 | Close affordance | 2 | **Vision + metadata:** X button, swipe indicator bar, close icon in top-right. Pre-classifier provides `has_close_icon_name` hint |
| S5 | Partial screen coverage | 2 | **Vision:** Main content card/sheet doesn't start from status bar — there's a gap/dim area above. Bottom sheet pattern = content in lower 40-80% |
| S6 | Picker/selector pattern | 1 | **Vision + text:** Content is a scrollable list for selection (contacts, banks, dates). Search bar + list items |
| S7 | Supplementary action | 1 | **Text:** Title text implies a sub-action within another flow (e.g., "Xác thực giao dịch", "Danh bạ thụ hưởng", "Chọn ngân hàng") |

**Scoring:**
- `overlay_score` = sum of weighted signals that are TRUE
- Maximum possible = 12
- **Threshold: `overlay_score ≥ 5`** → IS overlay → merge into parent boundary
- **Threshold: `overlay_score < 5`** → NOT overlay → separate boundary

### Step 3: Merge Target Resolution

For each artboard classified as overlay, determine `merge_target`:

1. **If S2 (shared header) is TRUE:** merge into the artboard that shares the header (the "base" screen)
2. **If S3 (dimmed background) is TRUE:** the dimmed content behind IS the parent screen → find the form/main artboard in same section with similar background
3. **If S6 (picker pattern):** merge into the form screen that has the trigger (ic_contact → form, drop_blue → form)
4. **Fallback:** merge into the primary artboard (largest artboard, or first artboard with `screen_type=form|confirm`)

### Output Schema

```json
{
  "overlay_classifications": [
    {
      "artboard_id": "22:6081",
      "artboard_name": "Chuyển tiền nhanh 24/7 qua tài khoản",
      "is_overlay": true,
      "overlay_score": 8,
      "confidence": 0.67,
      "merge_target": "22:5976",
      "signals": {
        "s1_same_name": { "value": true, "weight": 1 },
        "s2_shared_header": { "value": true, "weight": 2, "evidence": "Same 'Xác nhận giao dịch' header as 22:5976" },
        "s3_dimmed_background": { "value": true, "weight": 3, "evidence": "Confirm screen visible behind OTP bottom sheet" },
        "s4_close_affordance": { "value": true, "weight": 2, "evidence": "X close button top-right of OTP sheet" },
        "s5_partial_coverage": { "value": false, "weight": 0 },
        "s6_picker_pattern": { "value": false, "weight": 0 },
        "s7_supplementary_action": { "value": false, "weight": 0 }
      },
      "reasoning": "OTP input is a bottom sheet overlay on Confirm screen. Shared header, dimmed background, close X."
    }
  ]
}
```

## Integration with Pipeline

**When:** Phase 2a-bis, after initial artboard grouping (Bước 2, before Bước 3 heuristic).
**Replaces:** Static Bước 2.6 (Overlay Structure Detection) with its 3-signal S1/S2/S3 checks.

### Pipeline Integration Steps

1. Run `overlay-classify.js` with Figma metadata → get `pre_classification[]`
2. For artboards with `needs_vision: true`: agent reads screenshots, evaluates S2-S7
3. Produce final `overlay_classifications[]`
4. Apply to boundary grouping: overlay artboards get **appended to parent boundary's `artboard_node_ids[]`** instead of creating new boundaries

## Known Overlay Patterns by Domain

| Domain | Common overlays |
|--------|----------------|
| Banking | OTP/PIN input, contact picker, bank selector, amount keyboard, date picker, auth method selector |
| E-commerce | Product filter, sort options, size selector, address picker, payment method, coupon input |
| Social | Comment sheet, share sheet, reaction picker, mention selector |
| Enterprise | Filter panel, column selector, export options, approval dialog |

## Edge Cases

- **Full-screen modal with close X:** Score should be ≥5 (S4=2 + S7=1 + usually S1=1 + S6=1 = 5). If `overlay_score = 4` → agent should check if there's a clear parent screen
- **Keyboard-showing state:** Keyboard overlay on a form is a **variant** of the form, not a separate overlay. The artboard showing keyboard should already be in the form boundary via name matching
- **Error/loading states:** Usually variants, NOT overlays. No dimmed background, no close X
- **Nested overlays:** (OTP on Confirm which is after Form) — each overlay merges into its **direct visual parent**, not the root form

## References

- [Visual pattern examples](references/visual-patterns.md) — load when evaluating S3/S4/S5 patterns

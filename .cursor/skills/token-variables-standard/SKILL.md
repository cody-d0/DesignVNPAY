---
name: token-variables-standard
description: Standardize and bulk-map token variables using hierarchy-aware, mode-aware workflows with strict token-reference format and missing-token reporting. Use when users ask for token mapping, variable normalization, bulk apply, or temp1.json-based token operations.
---

# Token Variables Standard

## When to Apply

Use this skill when the request involves:

- Token variable standardization
- Bulk apply token groups
- Mapping from token source like `temp1.json`
- Cross-mode token consistency checks

## Source and Hierarchy

- Source of truth: approved token source (for example `temp1.json`).
- Resolve mappings in this order:
  1. `TailwindCSS`
  2. `Theme` (`Default`, `VNPAY`)
  3. `Mode` (`Light`, `Dark`)
  4. `Custom` (`Desktop`, `Mobile`)

## Workflow

1. Confirm active theme and mode.
2. Select custom target (`Desktop` or `Mobile`) before bulk operations.
3. Group tokens by domain (`Typography`, `Layout/Spacing`).
4. Apply mappings using `{collection.token}` reference format.
5. Check for mode drift between Desktop/Mobile values.
6. Report missing tokens and proposed names.

## Token Group Guidance

- Typography group examples:
  - `heading-xl`, `heading-lg`, `heading-md`, `heading-sm`
  - properties: `font-family`, `font-size`, `line-height`, `font-weight`, `letter-spacing`
- Layout/Spacing group examples:
  - `container-padding-x`, `section-padding-y`
  - `section-title-gap-xl`, `section-title-gap-lg`, `section-title-gap-md`, `section-title-gap-sm`

## Rules for Fallback and Gaps

- Do not hardcode when token exists.
- If token is missing:
  - mark as `missing token`
  - provide proposed token name
  - include intended group and mode

## Output Template

- `Hierarchy Resolution`
- `Mode Selection`
- `Bulk Groups Applied`
- `Token Reference Mapping`
- `Mode-specific Differences`
- `Missing Token List`
- `Assumptions & Unspecified`

---
name: prd-registration-mapping
description: Map registration PRD requirements to design-system components, states, and tokens with citation-first evidence and implementation-ready outputs. Use when users ask for PRD UI mapping, registration flow mapping, component-state-token mapping, or token gap analysis.
---

# PRD Registration Mapping

## When to Apply

Use this skill when the request involves:

- Registration PRD UI mapping
- Mapping `UI -> component -> state -> token`
- Design-system handoff for registration flow
- Token gap or missing-token analysis

## Inputs and Source of Truth

- Primary source: PRD sections describing screens, actions, validation, and constraints.
- Secondary source: approved token rule/registry (for example `design-system.mdc`).
- Do not infer product behavior outside PRD scope.

## Workflow

1. Extract scope and screens from PRD.
2. Build `UI-to-Component` mapping by field/action group.
3. Add `State Mapping` for each component (`default`, `focus`, `disabled`, `loading`, `error`, `success`).
4. Assign tokens per state from approved token set.
5. Flag gaps as `missing token`.
6. Produce implementation-ready mapping summary.

## Component-State-Token Mapping Rules

- Inputs, dropdowns, checkbox, button, link, OTP, loading overlay, and feedback message should be mapped explicitly where present.
- State behavior (retry, timeout, invalid, expired, success) must cite PRD evidence.
- Reuse existing tokens before proposing any new tokens.
- If token is missing, provide:
  - missing semantic intent
  - proposed token name
  - impacted component/state

## Output Template

Return output in this structure:

- `Scope Summary`
- `UI-to-Component Mapping`
- `State Mapping`
- `Token Mapping`
- `Missing Token List`
- `Implementation Notes`
- `Assumptions & Unspecified`

## Checklist

- PRD evidence exists for each mapped behavior.
- Every mapped UI element has component and state coverage.
- Every state has token mapping or `missing token`.
- Labels/messages follow PRD wording.
- No hardcoded design value where token exists.

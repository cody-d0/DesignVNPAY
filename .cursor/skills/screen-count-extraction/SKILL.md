---
name: screen-count-extraction
description: Extract and calculate screen/timepoint cases from PRDs with citation-first counting logic, scope gating, and bounded-vs-unbounded reporting. Use when users request screen extraction, screen count, timepoint case counting, or PRD-based case estimation.
---

# Screen Count Extraction

## When to Apply

Use this skill when the request involves:

- `screen extraction`
- `screen count`
- `timepoint case counting`
- PRD-based case growth estimation

## PRD Input Only

- PRD is the only source of truth for variables, formulas, and counts.
- Extract only from template anchors:
  - Sections: `User Flow`, `User Story`, `Wireframe`, `Thiết kế Database`, `Non-functional requirement`.
  - Overview sections: `Tính năng chính`, `Phạm vi sản phẩm`, `Hệ thống cần tích hợp`, `Success Metrics`, `User Flow chính`, `Cấu trúc tài liệu PRD`.
  - Scope sub-sections: `In Scope (MVP)`, `Out of Scope & Roadmap`.
  - Common table headers:
    - `Bước | Tên màn hình | Tên hành động | Kết quả`
    - `Epic chung | Mã US | Tiêu đề | Mô tả chi tiết | Business Rule | Acceptance Criteria`
    - `STT | Tên màn hình | Loại thành phần | Mô tả`
    - `Field | Data Type | Constraint | Description`
    - `STT | Tên tính năng | Mô tả`
    - `STT | Tài liệu | Mô tả chức năng`
- Do not infer core variables from free text without anchor evidence.

## Counting Entities

- `BASE_SCREEN`: main screen from `Tên màn hình`.
- `OVERLAY`: user-visible popup/dialog/sheet.
- `RESPONSE_STATE`: user-visible state such as error/timeout/retry/success/no-result/empty when anchored.
- `CONDITIONAL_VARIABLE`: condition variable (flag/enum/status).
- `COUNTER_VARIABLE`: incrementing variable (attempt/retry/threshold).
- `ASYNC_STATE`: asynchronous state tied to integration/system behavior.
- `SCOPE_GATE`: inclusion switch from `In Scope` and `Out of Scope & Roadmap`.
- `INTEGRATION_GATE`: integration-driven switch (for example `Firebase`, `VNPAY QR MMS`) when anchored.
- `FLOW_STAGE`: step/stage in `User Flow chính` used to route and deduplicate counting across modules.

## Counting Rules

- Additive for counters: `C = C0 + n` (or threshold-aware variants when defined by PRD).
- Multiplicative for conditional branches: `C = C0 * m`, where `m` is count of valid values.
- Always respect dependency constraints; never multiply non-independent variables as full Cartesian product.
- If upper bound is missing, mark variable as `UNBOUNDED`.
- For unbounded outputs, do not return absolute max; return parameterized bounded form such as `Max(R)`.
- `Release Count` must include only `In Scope (MVP)` cases.
- If a flow appears in both overview and module PRDs, use overview for routing and module docs for detailed counting only (no double-add).
- Create `ASYNC_STATE`/`INTEGRATION_GATE` only when integration states are explicitly anchored in relevant module PRDs.

## Expansion Forecast (Overview-Based)

Use `xpos-app-overview.md` before module deep-dive:

- From `Tính năng chính` and `User Flow chính`: estimate core surface.
- From `In Scope (MVP)` and `Out of Scope & Roadmap`: define release and potential boundaries.
- From `Hệ thống cần tích hợp`: flag async-heavy expansion risk.

Classification:

- `LOW`: binary/small enum (`m <= 2`) and no async.
- `MEDIUM`: medium enum (`3 <= m <= 5`) or single dependency layer.
- `HIGH`: async states present (timeout/pending/retry) or multiple dependencies.
- `EXTREME`: unbounded variable or retry/counter without max.

Forecast expressions:

- Additive: `Delta_add = +n`
- Multiplicative: `Delta_mul = x m`
- Mixed: `Delta_total ~= (Base + n) * m_dep`
- Unbounded: report `UNBOUNDED` and optional `Max(R)` form.

## Stability Groups

- `Group A - Stable Core`
  - Source: `Tên màn hình` in `User Flow`/`Wireframe`.
  - Property: slow change baseline.
- `Group B - Controlled Branch`
  - Source: enum/flag in `Business Rule`, `Constraint`.
  - Property: bounded multiplicative growth.
- `Group C - Volatile Async`
  - Source: `Non-functional requirement`, integrations.
  - Property: volatility; isolate from baseline.
- `Group D - Counter Burst`
  - Source: retry/attempt/threshold rules.
  - Property: rapid additive burst; prefer compressed representation.

Aggregation rules:

- Always report separated values: `CoreCount (A+B)` and `VolatileCount (C+D)`.
- `ReleaseCount = CoreCount + VolatileBounded`
- `PotentialCount = ReleaseCount + Optional/Roadmap`

## Case Compression

When cases are identical except counter value:

- Use compressed notation: `CASE_KEY{counter=1..k}`.
- Example: `LOGIN_FAIL{attempt=1..5}`.
- With threshold milestone: `LOGIN_FAIL{attempt=1..4} + LOGIN_LOCK{attempt=5}`.

Counting compressed forms:

- `Count(LOGIN_FAIL{1..k}) = k`
- `Count(counter_range + threshold_event) = k + 1`

Output must include both:

- `Compressed Expression`
- `Expanded Count`

## Overview-First Extraction Pipeline

1. Read `xpos-app-overview.md` to extract:
   - feature catalog (`Tính năng chính`)
   - scope boundaries (`In Scope (MVP)`, `Out of Scope & Roadmap`)
   - flow stages (`User Flow chính`)
   - module list (`Cấu trúc tài liệu PRD`)
2. Build module registry from `STT | Tài liệu | Mô tả chức năng`.
3. For each module, extract counting variables only from approved anchors.
4. Apply `SCOPE_GATE` first, then compute additive/multiplicative growth.
5. Return 3 levels:
   - `Core Count` (without optional/roadmap)
   - `Release Count` (current scope)
   - `Potential Count` (includes optional with gate notes)

## Citation Policy

- Every variable, formula, and count must include PRD citation blocks.
- Any conclusion not fully defined by PRD must be marked `UNSPECIFIED`.
- Never return absolute max while any variable remains `UNBOUNDED`.
- Scope conclusions must cite `Phạm vi sản phẩm`.
- Integration conclusions must cite both `Hệ thống cần tích hợp` and relevant module anchors.

## Mandatory Output Schema

- `Variables Table`: `name`, `type`, `domain`, `source citation`
- `Case Growth Table`: additive/multiplicative impact with percentage
- `Min/Release/Max` or `Min/Release/Max(R)` for unbounded
- `Assumptions & Unspecified`: explicit missing data list
- `Scope Matrix`: `InScope`, `OutOfScope`, `Roadmap`, `ReleaseDecision`
- `Module Coverage`: modules with enough anchors vs missing anchors
- `Stability Group Summary`: A/B/C/D and LOW/MEDIUM/HIGH/EXTREME
- `Compressed Cases`: expression plus expanded count

## Worked Example Format (Short)

1. Extract scope and flow stage from `xpos-app-overview.md`.
2. Extract variables from module anchors (`Business Rule`, `Constraint`, `Non-functional requirement`).
3. Build additive/multiplicative formulas with dependency constraints.
4. Return growth table and `Core/Release/Potential` with `Min/Release/Max`.
5. Add citations for every variable and key formula.

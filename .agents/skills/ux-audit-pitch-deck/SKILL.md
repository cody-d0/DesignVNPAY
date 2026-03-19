---
name: ux-audit-pitch-deck
description: Generate a professional, industry-standard UX Audit Pitch Deck as a single-file HTML deliverable from ux-review-report.md and pipeline output. Use when the user requests a pitch deck, presentation, or professional deliverable from UX audit data. Triggers include "pitch deck", "presentation", "deliverable", "HTML report", "audit deck", "industry-standard report". Requires completed ux-review-report.md and .handoff/ directory with screen_inventory.json, flow_graph.json, and ddl-context.json (produced by figma-to-ux-review workflow).
---

# UX Audit Pitch Deck Generator

Generate a professional HTML pitch deck from UX audit pipeline output. Single-file, zero dependencies, offline-capable.

## Industry Standard Structure (NNg-aligned)

The deck MUST follow this 5-section structure:

| # | Section | Content |
|:--|:--------|:--------|
| 1 | **Executive Summary** | Project name, scope, macro stats (screens, checks, findings), severity breakdown |
| 2 | **Methodology** | Evaluation methods used (heuristic evaluation, component spec analysis, vision inspection, UX law cross-reference) |
| 3 | **Detailed Findings** | Each UXP as a 2-column card: phone-frame screenshot (40% width, left) + structured info (60% width, right) — severity, title, hiện trạng, tác động, heuristic violated, đề xuất cải thiện, DDL refs via `<details>` |
| 4 | **Heuristic Scorecard** | SVG score rings per heuristic category (User Flow, Error Handling, Loading States, Touch & Target, Accessibility, Consistency) |
| 5 | **Action Plan & Next Steps** | Sprint-based roadmap prioritized by severity |

## Mandatory Rules

1. **Sanitize PII**: Remove all fake account numbers, names, phone numbers, transaction IDs from the deck. Use generic descriptions instead.
2. **No abbreviations**: Write all terms in full Vietnamese — "Tài khoản" not "TK", "giao dịch" not "GD", "điện thoại" not "ĐT".
3. **Every UXP with screenshot**: Each finding card MUST embed a real screenshot from `/ui/` inside a `.phone-frame` container.
4. **NNg heuristic references**: Each finding MUST cite the violated Nielsen heuristic by number and name.
5. **Progressive disclosure**: Technical DDL references go inside `<details>` tags — executives see summary, designers expand for detail.
6. **No internal pipeline metadata**: Do NOT include quality gate sections, pipeline timestamps, or internal tooling references in the client-facing deck. These belong in internal logs only.
7. **No hardcoded dates**: Footer should contain DDL context info and product name only — no generation timestamps.

## Input Requirements

The skill reads from:
- `{dir}/ux-review-report.md` — raw UX review with findings
- `{dir}/.handoff/screen_inventory.json` — screen data + image paths
- `{dir}/.handoff/ddl-context.json` — DDL component specs + guidelines
- `{dir}/*/ui/*.png` — actual screenshots

## Output

Single file: `{dir}/pitch-deck.html`

## Design System

Use the design tokens defined in [references/design-system.md](references/design-system.md).

## Finding Card Template

Each UXP finding card follows this structure:

```html
<div class="finding-card">
  <div class="finding-accent {severity}"></div> <!-- critical|major|minor|low -->
  <div class="card-layout"> <!-- grid: 2fr 3fr (40:60 ratio) -->
    <div class="card-visual">
      <div class="phone-frame"> <!-- rounded 24px, 3px border, box-shadow -->
        <img src="path/to/screenshot.png" alt="Descriptive alt text">
        <div class="shot-overlay">⚠️ Hiện trạng</div>
      </div>
    </div>
    <div class="card-info">
      <div class="card-top">
        <span class="card-id">UXP-XXX</span>
        <span class="badge {severity}">Severity Label</span>
      </div>
      <h3>Full descriptive title (no abbreviations)</h3>
      <div class="finding-section"><h4>Hiện trạng</h4><p>...</p></div>
      <div class="finding-section"><h4>Tác động đến người dùng</h4><p>...</p></div>
      <div class="finding-section"><h4>Heuristic vi phạm</h4><p><strong>Name</strong> (Nielsen #N) — explanation</p></div>
      <div class="finding-section">
        <h4>Đề xuất cải thiện</h4>
        <div class="proposed-box">
          <h5>Action Title</h5>
          <ul><li>Improvement item 1</li><li>Improvement item 2</li></ul>
        </div>
      </div>
      <div class="finding-tags">
        <span class="card-tag">Screen Tag 1</span>
        <span class="card-tag">Screen Tag 2</span>
      </div>
      <details><summary>Xem tham chiếu kỹ thuật →</summary>
        <div class="detail-content">DDL + UX Law refs</div>
      </details>
    </div>
  </div>
</div>
```

## Score Ring SVG Formula

```
circumference = 2 × π × radius
stroke-dashoffset = circumference × (1 - score/100)

r=38 (screen rings): circumference = 239
r=28 (heuristic rings): circumference = 176
```

## Workflow Integration

This skill is invoked as Phase 4 of the `figma-to-ux-review` workflow, after `ux-review-report.md` is generated and verified by `ux-score-calculator.js`.

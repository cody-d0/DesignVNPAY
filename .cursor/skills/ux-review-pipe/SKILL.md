---
name: ux-review-pipe
description: "Pipe 3 skill song song: (A) ux-signal-inference + DDL, (B) PRD context extract + DDL — hop nhat cho (C) agent vision review anh + suy luan + de xuat cai tien cu the. Nhan payload tu figma-to-prd hoac parse folder .md. Output: ux-review-report.md voi finding co ddl_ref, evidence tu anh, va de xuat cu the."
---

# UX Review Pipe

Pipe 3 skill: **Skill A** va **Skill B** chay dong thoi, ket qua hop nhat lam input cho **Skill C** (vision review + suy luan + de xuat cai tien).

## When to Apply

- Co folder PRD .md (output tu figma-to-prd-md hoac viet tay) va can review UX design trong anh wireframe.
- Can kiem tra anh wireframe (ui/*.png) co dap ung du yeu cau use-case, state coverage, accessibility, va UX best practice chua.
- Can de xuat cai tien UX cu the (copy, component, vi tri) co can cu DDL.

## Kien truc

```
Skill A (signal inference + DDL)  ─┐
                                    ├──► Skill C (vision review + suy luan + de xuat)
Skill B (PRD context + DDL)       ─┘         │
                                              ▼
                                     ux-review-report.md
```

Skill A va B **doc lap, chay song song**. Skill C **chi chay sau khi A va B hoan thanh** (hoac degraded — xem Degraded Mode).

---

## Input Contract

| Tham so | Bat buoc | Mo ta |
|---------|----------|-------|
| `prd_folder` | Co | Folder chua .md (vd: `co-op-bank-khcn/co-op-bank-khcn`) |
| `image_folder` | Khong | Mac dinh: `ui/` relative tu feature .md |
| `consumer_payload` | Khong | Payload tu figma-to-prd (Phase 4e format): per-screen `{ text_list, context_hint, ocr_icons, ocr_screen_context }`. Khi co: Skill A dung truc tiep. Khong co: Skill A tu parse .md Section 3 |
| `domain` | Khong | Mac dinh `banking`. Dung de chon text-signals-{domain}.json |
| `product_name` | Khong | Tu overview file |
| `review_scope` | Khong | `all` (mac dinh) hoac danh sach screen_id |

### Handoff Loading (uu tien)

Khi `prd_folder` co `.handoff/`:
1. Load `screen_inventory.json` → `consumer_payload` per screen (fast-path cho Skill A).
2. Load `flow_graph.json` → edges giua cac screen (bo sung cho Skill B flow_checks).
3. Load `handoff-manifest.json` → verify `ocr_done`, `domain`, `schema_version`.

Khi **khong co** `.handoff/`: fallback parse .md. Log warning `HANDOFF_MISSING`.

---

## Skill A: UX Signal Inference + DDL

**Chay song song voi Skill B.** Suy luan UX tiem an tu text signals, cross-ref DDL, sinh `signal_ddl_report` per screen.

### Input

Nhan payload tu figma-to-prd (Phase 4e) theo input contract cua ux-signal-inference:

| Truong | Nguon | Fallback (khong co payload) |
|--------|-------|----------------------------|
| `text_list` | `consumer_payload.text_list` (flatten ocr_round1_text) | Parse Section 3 bang Mo ta man hinh: gop cot "Mo ta" + "Ngu canh man hinh (tu OCR)" |
| `context_hint` | `consumer_payload.ocr_screen_context` | Parse subsection "Ngu canh man hinh (tu OCR)" trong Section 3 |
| `ocr_icons` | `consumer_payload.ocr_icons` (ocr_round2_icons) | Khong co (bo trong) |
| `scope` | co dinh `"screen"` | -- |
| `scope_id` | `screen_id` tu file name (kebab-case) | -- |

### Xu ly (reuse ux-signal-inference quy trinh 4 buoc)

1. **Chuan hoa text** tu text_list hoac text_source → mang chuoi.
2. **Match registry**: Load `.cursor/skills/ux-signal-inference/data/text-signals-generic.json` + `text-signals-{domain}.json`. Match pattern (instruction, counter, action, cancel, tags) → inferred_ux: `flows[]`, `components[]`, `states[]`.
3. **DDL on demand**: Query scope GLOBAL tai `.agents/skills/ui-ux-pro-max/data/` (ux-guidelines.csv, web-interface.csv, ux-laws.csv) theo keyword tu inferred_ux → gan `ddl_ref` va `ux_law_ref`.
4. **Xuat `signal_ddl_report` per screen.**

### Output

```
signal_ddl_report[k] = {
  screen_id: string,
  matched_signals: [
    { pattern_group_id: string, confidence: "high"|"medium"|"low",
      inferred_flows: [string],
      inferred_components: [string],
      inferred_states: [string],
      ddl_refs: [string],
      ux_law_refs: [string] }
  ],
  ddl_rules_applied: [
    { ddl_ref: string, rule: string,
      category: string, severity: "Critical"|"Major"|"Minor",
      ux_law_ref: string|null, context: string }
  ]
}
```

---

## Skill B: PRD Context Extract + DDL

**Chay song song voi Skill A.** Doc toan bo .md, trich use-case context, cross-ref DDL, sinh `prd_ddl_report` per screen. **KHONG doc anh.**

### Xu ly

1. **Scan folder**: Tim overview (`*-overview.md`) va feature files (`.md` con lai, loai pattern `pipeline-*`, `*-stateful-ux-map.md`, `*-ui-automation*`).
2. **Parse tung feature .md** — trich 5 section:

| Section | Trich ra | DDL cross-ref |
|---------|----------|---------------|
| 1. User Flow | `flow_steps[]`: Buoc, Hanh dong, Ket qua | ux-guidelines.csv: Back Button (#4), Error Recovery, Empty State → kiem tra flow co du luong back, error, empty |
| 2. User Story | `user_stories[]`: BR, AC text | web-interface.csv: match keyword tu AC; ux-guidelines.csv: match category |
| 3. Wireframe | `components[]`: Loai thanh phan, Mo ta | web-interface.csv: match keyword (form input label → a11y rule); component taxonomy → state coverage check |
| 4. Database | `entities[]`: fields, constraints | Cross-ref voi Section 3: field co trong UI khong |
| 5. NFR | `nfr_items[]`: Bao mat, Hieu nang, Trai nghiem | ux-guidelines.csv: match severity (Touch Target, Loading Feedback, Contrast) |

3. **DDL cross-reference** — query DDL GLOBAL cho tung component/flow/AC:
   - Component → web-interface.csv: Do/Don't
   - Flow step destructive → ux-guidelines.csv: "Require confirmation" + ux_law_ref
   - AC coverage → matched/unmatched
   - NFR → ux-guidelines.csv + ux_law_ref

4. **Map wireframe images** — tu `![alt](ui/xxx.png)` trong Section 3, ghi `wireframe_images[]` per screen (de Skill C biet doc anh nao).

### Output

```
prd_ddl_report[k] = {
  screen_id: string,
  source_file: string,
  use_case_summary: string,
  wireframe_images: [string],
  flow_checks: [
    { flow: string, has_happy_path: bool, has_error: bool, has_back: bool,
      ddl_gap: string|null, ddl_ref: string|null, severity: string|null }
  ],
  component_checks: [
    { component: string, prd_type: string,
      states_in_prd: [string], ddl_required_states: [string],
      missing_states: [string],
      ddl_ref: string|null, severity: string|null }
  ],
  ac_coverage: [
    { us_id: string, ac: string, ddl_match: string|null,
      verdict: "covered"|"uncovered", ux_law_ref: string|null }
  ],
  nfr_checks: [
    { nfr: string, ddl_ref: string|null,
      ux_law_ref: string|null, verdict: "stated_in_nfr"|"missing" }
  ]
}
```

---

## Skill C: Vision Review + Suy luan + De xuat cai tien

**Chay SAU khi A va B hoan thanh.** Doc anh, doi chieu voi 2 report, suy luan them, cross-ref DDL, cho de xuat cai tien cu the.

### Input

- `signal_ddl_report[]` tu Skill A
- `prd_ddl_report[]` tu Skill B
- `ui/*.png` (wireframes) — buoc duy nhat doc anh

### Xu ly (per screen)

**Buoc 1 — Doc anh (agent vision):**
Doc tat ca PNG thuoc screen k (tu `prd_ddl_report[k].wireframe_images`). Trich xuat:
- Toan bo text nhin thay (labels, buttons, messages)
- Toan bo icon va vi tri (header, body, footer, FAB)
- Layout tong the (top-to-bottom)
- Trang thai hien thi (expanded/collapsed, selected, keyboard visible...)

**Buoc 2 — Doi chieu voi 2 report:**
Voi moi check item tu signal_ddl_report va prd_ddl_report:
- Tim evidence trong anh: text, icon, component, state tuong ung
- Gan verdict: **pass** (thay evidence), **gap** (khong thay), **unverifiable** (khong the kiem tra tu anh tinh)
- Ghi evidence_note cu the

**Buoc 3 — Suy luan them (KHONG chi doi chieu):**
Agent vision + DDL de phat hien van de ma 2 report chua noi den:
- Text bi cat (truncated)?
- Contrast mau du doc khong?
- Layout bi che (FAB che noi dung cuoi)?
- Spacing/alignment nhat quan?
- Icon-only button thieu label?

Moi phat hien → query DDL (ux-guidelines.csv, web-interface.csv) de lay can cu.

**Buoc 4 — Sinh de xuat cai tien CU THE (Case Study Format):**
Moi gap hoac phat hien → 1 de xuat theo format 3 section:

```
{
  proposal_id: "UXP-NNN",
  display_name_vi: string,    // "{main} › {sub}" — tieng Viet co dau
  screen_id: string,          // "SCR-TK-001" — internal only
  severity: "Critical"|"Major"|"Minor",
  ddl_refs: [string],         // array: ["UXG-10", "UXG-78"]
  ux_law_refs: [string|null], // array: ["doherty"]
  // 3 sections BAT BUOC:
  current_state_vi: string,   // 🔍 Hien trang — mo ta data/evidence hien co
  consequences_vi: string,    // ⚠️ Hau qua — user impact + business impact + violation
  solution_vi: string,        // ✅ Giai phap — CU THE: component, copy, vi tri, token
  evidence_images: [string],  // array anh lien quan
}
```

De xuat **KHONG generic**. 3 sections phai CU THE:
- **🔍 Hien trang**: Cite evidence (Flow X.Y, Wireframe row N, OCR text, DDL spec)
- **⚠️ Hau qua**: Impact len user (frustration, task failure) + business (conversion loss, support cost) + violation (DDL/UX Law)
- **✅ Giai phap**: Table voi cot: Component, De xuat cu the (copy text, pixel values), Vi tri (trong man hinh)

---

## Output: ux-review-report.md

Ghi tai `{prd_folder}/ux-review-report.md`. Cau truc:

```markdown
# UX Review Report — {product_name}

## Tong quan
- Folder: {prd_folder}
- So man hinh: N | Tong check: X
- Pass: Y | Gap: Z | Unverifiable: W
- UX Score (Simple): XX% (Y/X)
- UX Score (Weighted): XX%

## De xuat cai tien (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuoc tinh | Chi tiet |
|:---|:---|
| **Man hinh** | {display_name_vi} |
| **Muc do** | 🔴 Critical |
| **DDL** | {ddl_refs joined with " · "} |
| **UX Law** | {ux_law_refs joined} |

**🔍 Hien trang**

{current_state_vi}

> Evidence: {cite PRD section, wireframe, OCR, DDL spec}

**⚠️ Hau qua**

- **User impact:** {frustration, task failure, confusion}
- **Business impact:** {conversion loss, support cost, churn}
- **Violation:** {DDL rule + UX Law violated}

**✅ Giai phap de xuat**

| # | Component | De xuat | Vi tri |
|---|:---|:---|:---|
| 1 | {component} | {cu the: copy, pixel, token} | {block/area trong man hinh} |

---

### 🟡 Major
(same format per UXP)

### ⚪ Minor
(same format per UXP)

---

## Chi tiet theo man hinh

### 1. {display_name_vi}
> `{screen_id}` · {screen_type} · {N} artboards
>
> **Score: XX% | Pass: Y | Gap: Z | Unverifiable: W | Images: ...**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| ... |

(lap lai cho moi screen)

---

## DDL References su dung
| ddl_ref | Rule | UX Law | Ap dung |
|---------|------|--------|---------|
| ... |
```

### ⛔ Tool-Verified Scoring (MANDATORY)

**Sau khi ghi `ux-review-report.md`, BAT BUOC chay:**

```bash
node ux-score-calculator.js run --json {prd_folder}/ux-review-report.md
```

**Quy trinh:**
1. Chay `run` → tool parse toan bo markdown tables, count pass/gap/unverifiable tu verdict column.
2. So sanh claimed values (trong overview + per-screen headers) voi actual counted values.
3. Neu co discrepancies → chay `run --fix` → verify lai.
4. Chi report metrics tu output cua tool — KHONG dung con so tu viet bang tay.

**Scoring model:**
- **Simple Score** = pass / total_checks × 100
- **Weighted Score** = (1 − weighted_gap_penalty / max_possible_penalty) × 100
  - Critical gap = 3.0 penalty
  - Major gap = 2.0 penalty
  - Minor gap = 1.0 penalty
  - Unverifiable = excluded (no penalty, no credit)

**Anti-pattern (KHONG DUOC lap lai):**
- ❌ Viet overview header truoc khi viet per-screen tables → count lech
- ❌ Count pass/gap bang uoc chung
- ❌ Report UX Score chua qua tool verification

---

## Degraded Mode

Khi Skill A hoac B fail/timeout, pipeline van tiep tuc voi du lieu con lai:

| Tinh huong | Hanh vi | Log |
|:---|:---|:---|
| Skill A fail, Skill B ok | Skill C chay voi chi `prd_ddl_report` tu B. Report thieu signal inference coverage | `SKILL_A_DEGRADED` |
| Skill B fail, Skill A ok | Skill C chay voi chi `signal_ddl_report` tu A. Report thieu PRD context checks | `SKILL_B_DEGRADED` |
| Ca A va B fail | **DUNG pipeline**. Thong bao user. Khong chay Skill C | `PIPE_FAILED` |

Khi degraded: `ux-review-report.md` phai ghi ro warning o Tong quan: "⚠️ Degraded: Skill X khong chay — report thieu coverage tu skill do."

---

## Data & Reference (reuse, khong tao moi)

- **ux-signal-inference**: `.cursor/skills/ux-signal-inference/SKILL.md` — goi nguyen ven (Skill A)
- **Pattern registry**: `.cursor/skills/ux-signal-inference/data/text-signals-generic.json`, `text-signals-{domain}.json`
- **DDL GLOBAL**: `.agents/skills/ui-ux-pro-max/data/` — ux-guidelines.csv, web-interface.csv, ux-laws.csv
- **review-ux checklist**: `.cursor/skills/review-ux/checklist.md` — 9 nhom lam framework phan loai
- **DDL contract**: `.cursor/docs/ddl/contract.md`, `.cursor/docs/ddl/hierarchy.md`

## Ranh gioi

- **Khong** sua file .md, khong sinh PRD, khong tao mockup.
- **Chi** doc (folder .md + anh + DDL) va ghi **1 file** output (ux-review-report.md).
- Consumer payload cho phep bo qua parse .md o Skill A (truyen thang text_list, context_hint, ocr_icons).
- Skill A va B **doc lap** — co the thay the/bo qua 1 trong 2 (degraded mode).
- Skill C la buoc **duy nhat doc anh**.

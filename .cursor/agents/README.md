# Custom Subagents

## prd-full-pipeline (v3 -- Optimized)

**File:** `prd-full-pipeline.md`

**Mục đích:** Phân tích folder PRD end-to-end. Chạy tuần tự 4 skill (Skill 0 conditional), output mỗi skill bổ sung cho skill sau. Mobile-first (iOS + Android). No CSS.

**Thứ tự:**
1. `design-system-gen` (conditional — skip khi có figma_source) — design_handoff
2. `prd-crossfile-mapping` (5 bước lõi) — dependencies, shared fields, canonical contract
3. `pdr-extract-analyze` (N feature files, KHÔNG map token) — component registry, case matrix, behavior rules
4. `comp-token-augment` (1 lần duy nhất) — token mapping + state + UX augment + JSON output
5. `visual-spec-gen` — spec files + **mockup-spec.json** (deliverable chính)

**Khi nào dùng:**
- Cần phân tích toàn bộ folder PRD (cross-file + component + token)
- Task phức tạp, nhiều file PRD liên quan
- Cần output hợp nhất + mockup-spec.json cho UX improvement proposals

**Input:**
- `prd_folder` (bắt buộc): đường dẫn folder chứa file PRD .md
- `figma_source` (tùy chọn): URL Figma — khi có, skip Skill 0 + sinh figma_context_registry
- `include_files[]`, `exclude_files[]` (tùy chọn)
- `token_file` (mặc định: `temp1.json`)
- `target_platform` (mặc định: `mobile` — iOS + Android)
- `target_stack` (mặc định: `flutter`)

**Output:**
- **mockup-spec.json** (luôn tạo — deliverable chính): component UI JSON + state coverage
- Pipeline Summary (7 mục Markdown)
- UI Automation Files (.md)
- Full JSON (khi user yêu cầu)

**Cải thiện v3 so v2:**
- Gộp Skill 2b + Skill 3 → giảm ~40% trùng lặp
- Token mapping chạy 1 lần cuối (không N lần per file)
- Skill 0 conditional (skip khi có Figma)
- Output giảm 14 → 7 mục
- Tổng bước giảm ~47%

**Skills liên quan:**
- `.cursor/skills/design-system-gen/SKILL.md`
- `.cursor/skills/prd-crossfile-mapping/SKILL.md`
- `.cursor/skills/pdr-extract/SKILL.md`
- `.cursor/skills/pdr-analyze/SKILL.md`
- `.cursor/skills/comp-extraction/SKILL.md`
- `.cursor/skills/visual-spec-gen/SKILL.md`

**Rules liên quan:**
- `.cursor/rules/pdr-component-pipeline.mdc`
- `.cursor/rules/comp-extraction.mdc`

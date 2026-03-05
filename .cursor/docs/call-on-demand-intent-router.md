# Call-on-Demand Intent Router

> Bảng intent → skill chính / skill phụ + điều kiện skip để tránh gọi trùng. Áp dụng trước khi load full skill context.

## 1. Bảng Intent → Skill

| User intent (từ khóa / mục đích) | Skill chính | Skill phụ (optional) | Skip conditions |
|----------------------------------|-------------|----------------------|------------------|
| "screen count", "timepoint cases", "case estimation", "growth forecast" | `screen-count-extraction` | — | Đã có số màn hình/timepoint từ run trước và user không yêu cầu cập nhật |
| "registration", "register flow", "registration UI" | `prd-registration-mapping` | — | Task là implementation (không phải mapping); không có PRD registration |
| "cross-file", "dependencies", "shared fields", "impact analysis", "inconsistencies" | `prd-crossfile-mapping` | Sau đó: `comp-extraction` hoặc pipeline | Chỉ 1 file PRD; user không nhắc dependency |
| Single feature file + overview đã có | `pdr-extract` → `pdr-analyze` | `visual-spec-gen` (nếu cần spec) | Nhiều file / cần full pipeline → dùng pipeline |
| Multi-file PRD / full pipeline / "phân tích toàn bộ folder" | `prd-full-pipeline` (subagent) | — | Chỉ 1 file + 1 overview → dùng pdr-extract + pdr-analyze |
| "design system", "token proposal", "color/typography" khi chưa có design | `design-system-gen` | — | Đã có `design_handoff` hoặc `figma_source`; temp1.json coverage > 90% |
| "visual spec", "implementation guide", "handoff", "token dictionary" | `visual-spec-gen` | — | Chưa có output extraction/pipeline; chỉ cần extraction không cần spec |
| "implement [Figma URL]", "build component from Figma" | `figma-implement-design` | — | User cần PRD trước → dùng figma-to-prd-md |
| "convert Figma to PRD", "Figma → PRD", "generate PRD from Figma" | `figma-to-prd-md` | — | User cần code ngay → dùng figma-implement-design |
| "save Figma screenshots", "export Figma frames" | `figma-save-screenshot` | — | User cần PRD hoặc code → không chỉ capture ảnh |
| "review UX", "heuristic evaluation", "wireframe feedback" | `review-ux` | `figma` (get_design_context) nếu có URL | Task là implementation, không review |
| "review PRD", "validate requirements", "gaps" | `review-prd-nghiep-vu` | — | Task là implementation; không có PRD đính kèm |
| "create poster", "create art", "visual piece" | `canvas-design` | — | User cần UI/code → frontend-design |
| "mockup từ ảnh", "hand-drawn từ thư mục ảnh", "mockup từ ảnh wireframe" | `img-to-mockup` | — | User có file .md spec → dùng md-to-mockup |
| "deploy GitHub Pages", "publish to GitHub" | `deploy-github-pages` | — | Đã deploy; hosting khác |
| "find skill", "skill for X", "install skill" | `find-skills` / `skill-installer` | — | User đã biết skill và muốn dùng |
| "create skill", "write skill", "update skill" | `skill-creator` | — | User muốn dùng skill có sẵn |

## 2. PRD Path — Scope Gate

```
IF "screen count" / "timepoint" → screen-count-extraction (standalone) → EXIT
IF "registration" only → prd-registration-mapping → EXIT
IF "cross-file" / "dependencies" mentioned → prd-crossfile-mapping FIRST
IF single feature file + overview provided AND no cross-file need:
   → pdr-extract → pdr-analyze
   → IF need visual spec → visual-spec-gen
ELSE (multi-file OR full pipeline):
   → prd-full-pipeline (prd_folder, overview_file when multiple overviews)
   → IF design_handoff missing AND high missing_token → design-system-gen first (or figma_source)
   → IF need visual spec → already in pipeline Skill 4
```

## 3. Figma Path — Intent Gate

```
IF "implement" + Figma URL → figma-implement-design (cache design context if available)
IF "convert to PRD" / "Figma to PRD" → figma-to-prd-md → then prd-full-pipeline (prd_folder + figma_source)
IF "review" + Figma URL → review-ux (+ get_design_context)
IF "save screenshots" / "export frames" → figma-save-screenshot
```

## 4. Khi nào KHÔNG gọi skill

- **design-system-gen**: Đã có `design_handoff` hoặc `figma_source`; không gọi khi chỉ extract/analyze và token đủ.
- **prd-crossfile-mapping**: Chỉ 1 file PRD; không gọi khi user không nhắc dependency/shared fields.
- **visual-spec-gen**: User chỉ cần registry/case matrix; không cần spec files / mockup-spec.
- **comp-extraction** và **pdr-extract+pdr-analyze**: Không chạy cả hai trên cùng tập file; chọn một theo single vs multi-file.
- **figma-to-prd-md** và **figma-implement-design**: Không chạy đồng thời; chọn theo intent (PRD pack vs code).

## 5. Tham chiếu

- Pipeline v3: `.cursor/agents/prd-full-pipeline.md`
- Rule PDR component: `.cursor/rules/pdr-component-pipeline.mdc`
- Design data layer (DDL) on-demand contract: `.cursor/docs/ddl/contract.md`
- Plan: Skill On-Demand Optimization (boundary contract, quality gates, handoff).
- Metrics checklist: `.cursor/docs/call-on-demand-metrics-checklist.md`

## 6. Ownership duy nhất: Token mapping & UX augment

Mỗi luồng chỉ **một** skill chịu trách nhiệm token resolution và 6 CSV augment để tránh chạy lặp.

| Luồng | Token mapping owner | UX augment (6 CSV) owner | Ghi chú |
|-------|---------------------|---------------------------|---------|
| **Single feature** (pdr-extract → pdr-analyze) | `pdr-analyze` (Bước 3) | `pdr-analyze` (Bước 2) | Chạy 1 lần trên output Skill 1. |
| **Multi-file / full pipeline** (prd-full-pipeline) | Skill 3 `comp-token-augment` (Phase 3) | Skill 3 `comp-token-augment` (Phase 5) | Skill 2 **không** map token, **không** tra 6 CSV. |
| **Standalone comp-extraction** (nhiều file, không qua pipeline) | `comp-extraction` Phase 5 | `comp-extraction` Phase 7 | Không gọi pdr-analyze Bước 2–3 trên cùng file set. |

**Quy tắc:**
- Trong pipeline v3: Skill 2 chỉ extract + suy case ngầm; toàn bộ token + UX augment ở Skill 3.
- Khi dùng standalone pdr-extract + pdr-analyze: không gọi thêm comp-extraction trên cùng file.
- Khi dùng comp-extraction cho multi-file: không gọi pdr-analyze Bước 2–3 (6 CSV + token) riêng.

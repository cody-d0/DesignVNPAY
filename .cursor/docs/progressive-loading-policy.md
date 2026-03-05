# Progressive Context Loading (3 tầng)

> Quy tắc nạp context theo tầng: contract → section → artifact. Áp dụng cho mọi skill để giảm token, tăng cache hit.

## 1. Ba tầng

| Tầng | Nội dung nạp | Khi nào | Mục đích |
|------|--------------|---------|----------|
| **Tầng 1 — Contract** | Input/Output contract, required inputs, schema version | Trước khi quyết định gọi skill hoặc chạy phase | Xác nhận đủ input; không load full SKILL. |
| **Tầng 2 — Section** | Chỉ section liên quan intent (vd: "Phase 3", "Bước 2", "Token Resolution Chain") | Khi đã chọn skill và cần thực hiện bước cụ thể | Giảm đọc toàn bộ file; load phase/step tương ứng. |
| **Tầng 3 — Artifact** | CSV, temp1.json, design_handoff, crossfile_handoff, .handoff/*.json | Khi gate bật hoặc bước cần dữ liệu bổ sung | Chỉ load artifact cần cho bước hiện tại. |

## 2. Áp dụng theo skill

- **figma-to-prd-md**: Mỗi phase chỉ đọc file phase tương ứng (phase-N-*.md) + conventions nếu có; không load toàn bộ phases cùng lúc. Artifact: component-mapping, badge-examples, citation-quality khi vào phase tương ứng.
- **prd-full-pipeline**: Resolve Input chỉ cần contract + danh sách file; từng Skill đọc SKILL tương ứng khi đến lượt. Artifact: design_handoff, crossfile_handoff, pdr_handoff, temp1.json, 6 CSV — nạp theo Skill 0→1→2→3→4.
- **pdr-extract / pdr-analyze**: Contract trước; section "Bước N" tương ứng với step đang chạy; artifact (overview, feature .md, canonical_contract) load khi cần.
- **comp-extraction**: Contract + Phase 1–8; mỗi phase load section tương ứng; artifact (temp1.json, design_handoff, 6 CSV) theo phase.
- **prd-crossfile-mapping**: Contract + 5 bước lõi; artifact (target_dir, overview_file, include/exclude) đã có từ pipeline.

## 3. Prefix ổn định (cache)

- Phần cố định đặt đầu prompt: state set, anchor policy, token hierarchy, citation rules. Phần biến đổi (user query, file paths, runtime data) đặt cuối để tăng cache hit (OpenAI/Anthropic prompt caching).

## 4. Tham chiếu

- Call-on-demand: `.cursor/docs/call-on-demand-intent-router.md`
- Pipeline: `.cursor/agents/prd-full-pipeline.md`
- figma-to-prd-md Phase Routing: `.cursor/skills/figma-to-prd-md/SKILL.md` (Phase Routing table).

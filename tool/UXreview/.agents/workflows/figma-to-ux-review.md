---
description: "Pipeline end-to-end: Figma → PRD .md (figma-to-prd-md) → UX Review Report (ux-review-pipe). Expect ~20-40 min tuỳ số screens."
---

# Pipeline: Figma tới UX Review (.md pack + UX Report)

Workflow này kết hợp 2 pipe chính để sinh PRD .md từ link Figma, đồng thời tự động đánh giá UI/UX trên ảnh wireframe.

**MỤC TIÊU BẮT BUỘC:** Giữ nguyên toàn bộ các lượt scan, Agent Vision đọc ảnh, và cross-reference DDL của mỗi phase để đảm bảo không thất thoát dữ liệu context hay thay đổi hành vi chuẩn của pipe.

**IMAGE INTEGRITY PRINCIPLE:** Ảnh frame là **input bắt buộc** cho mọi bước Agent Vision (Phase 2 OCR + Skill C). Mọi gate phải verify ảnh thực sự tồn tại trên filesystem trước khi cho phép vision processing — tránh agent "hallucinate" OCR từ metadata.

## Skill References

| Skill / Pipe | Path | Vai trò | Vision? |
|:---|:---|:---|:---:|
| `figma-to-prd-md` | `.agents/skills/figma-to-prd-md/SKILL.md` | Pipe 1: Sinh PRD .md pack từ Figma | ✅ OCR 2 rounds |
| `ux-review-pipe` | `.agents/skills/ux-review-pipe/SKILL.md` | Pipe 2: Review UX trên ảnh wireframe | ✅ Skill C |
| `ux-signal-inference` | `.agents/skills/ux-signal-inference/SKILL.md` | Sub-skill: Suy luận UX text signals | ❌ Text only |
| `ui-ux-pro-max` | `.agents/skills/ui-ux-pro-max/SKILL.md` | DDL data source (ux-guidelines, ux-laws, web-interface) | ❌ Data only |

## Human Checkpoints & Gates — Tổng quan

Pipeline có **7 Human Checkpoints** (PREFLIGHT + HC-0 → HC-5) và **5 Automated Gates**. Các gate có severity 🔴 BLOCK sẽ **DỪNG pipeline** nếu fail.

| ID | Tên | Vị trí | Loại | Bắt buộc |
|:--|:---|:---|:---:|:---:|
| PREFLIGHT | Tool Readiness Check | **Trước mọi thứ** | 🔴 Auto + Human | ✅ |
| HC-0 | Greeting & Scope Confirmation | Đầu pipeline | 🖐️ Human | ✅ |
| HC-1 | Image Export Verification | Sau Phase 0-1 | 🔴 Gate + Human | ✅ |
| HC-2 | OCR Completeness Review | Sau Phase 2 | 🔴 Gate + Human | ✅ |
| HC-3 | PRD Draft Sanity Check | Sau Phase 3 | 🟢 Human only | Optional |
| HC-4 | Pre-Handoff Gate (Enhanced) | Sau Phase 5 | 🔴 Gate + Human | ✅ |
| HC-5 | Vision Review Confirmation | Sau Skill C | 🟢 Human | ✅ |

---

## Bước 0: PREFLIGHT — Tool Readiness Check (🔴 CRITICAL)

**Mục đích:** Verify tất cả tool dependencies hoạt động TRƯỚC KHI bắt đầu pipeline. Tránh fail giữa chừng (root cause của Co-op Bank image gap).

**Chạy ngay khi user gọi workflow, TRƯỚC cả greeting HC-0.**

### Checklist Preflight

| # | Check | Logic | Severity | Recovery |
|:--|:---|:---|:---:|:---|
| P1 | **Figma MCP** (`figma-dev-mode-mcp-server`) available | Gọi `get_metadata` hoặc `get_screenshot` với nodeId đơn giản — nếu trả kết quả = OK | 🟡 WARN | Pipeline vẫn chạy nếu dùng `figma-save` thay thế |
| P2 | **figma-save MCP** server available | Verify MCP server `figma-save` đang chạy (hoặc có thể spawn) | 🔴 BLOCK | Agent thông báo user: "figma-save MCP chưa start. Chạy lại config MCP." |
| P3 | **Figma Access Token** valid | Đọc env `FAT` hoặc `FIGMA_ACCESS_TOKEN` — nếu có, test gọi Figma API (vd: `GET /v1/me`) | 🔴 BLOCK | "Token Figma không hợp lệ hoặc hết hạn. Vui lòng cập nhật FAT trong .env" |
| P4 | **DDL data files** tồn tại | Check files: `ux-guidelines.csv`, `web-interface.csv`, `ux-laws.csv` trong `.agents/skills/ui-ux-pro-max/data/` | 🔴 BLOCK | "Thiếu DDL data files. Pipeline cần dữ liệu UX rules." |
| P5 | **Output directory** writable | `mkdir -p {output_dir} && touch {output_dir}/.preflight_test && rm {output_dir}/.preflight_test` | 🔴 BLOCK | "Không thể ghi vào thư mục output. Kiểm tra permissions." |
| P6 | **Node modules** installed cho figma-save | `test -d tools/mcp-servers/figma-save/node_modules` | 🟡 WARN | Auto-fix: `cd tools/mcp-servers/figma-save && npm install` |

### Preflight Logic

```
Agent runs preflight automatically:

1. Check P1 (Figma MCP):
   → Gọi get_metadata hoặc get_screenshot với test node
   → OK → ✅ | Error → 🟡 WARN (fallback sang figma-save)

2. Check P2 (figma-save MCP):
   → Gọi figma_save_section_screenshots hoặc list tools
   → OK → ✅ | Error → 🔴 BLOCK

3. Check P3 (Token):
   → Đọc .env file, verify FAT exists và non-empty
   → Test API call nếu cần
   → OK → ✅ | Empty/invalid → 🔴 BLOCK

4. Check P4 (DDL files):
   → ls .agents/skills/ui-ux-pro-max/data/*.csv
   → 3 files found → ✅ | Missing → 🔴 BLOCK

5. Check P5 (Output dir):
   → mkdir -p + touch test
   → OK → ✅ | Permission error → 🔴 BLOCK

6. Check P6 (node_modules):
   → test -d node_modules
   → Exists → ✅ | Missing → 🟡 WARN + auto npm install
```

### Agent Report (sau Preflight)

Agent báo kết quả: 

```
🔧 **Preflight Check — Tool Readiness**

| # | Tool | Trạng thái |
|:--|:---|:---|
| P1 | Figma MCP (dev-mode) | ✅ Available |
| P2 | figma-save MCP | ✅ Running |
| P3 | Figma Token (FAT) | ✅ Valid |
| P4 | DDL Data Files | ✅ 3/3 files |
| P5 | Output Directory | ✅ Writable |
| P6 | Node Modules | ✅ Installed |

✅ **All checks passed.** Sẵn sàng bắt đầu pipeline.
```

**Nếu có BLOCK:**
```
🔧 **Preflight Check — Tool Readiness**

| # | Tool | Trạng thái |
|:--|:---|:---|
| P1 | Figma MCP (dev-mode) | 🟡 Unavailable (sẽ dùng figma-save) |
| P2 | figma-save MCP | ✅ Running |
| P3 | Figma Token (FAT) | 🔴 MISSING |
| P4 | DDL Data Files | ✅ 3/3 files |
| P5 | Output Directory | ✅ Writable |
| P6 | Node Modules | ✅ Installed |

🛑 **Pipeline BLOCKED.** Vui lòng:
1. Thêm Figma token vào file `.env`: `FAT=figd_xxxxx`
2. Sau đó gọi lại workflow.
```

### Tool Dependency Map

| Tool | Dùng ở Phase | Vai trò | Thay thế? |
|:---|:---|:---|:---:|
| **Figma MCP** (`figma-dev-mode`) | Phase 0-1 | `get_metadata`, `get_screenshot`, `get_design_context` | Có thể thay bằng `figma-save` cho ảnh |
| **figma-save MCP** | Phase 0-1 | `figma_save_section_screenshots` — export artboards → PNG | Primary tool cho image export |
| **Figma Token** (`FAT`) | Phase 0-1 | Auth cho cả 2 Figma tools | ❌ Bắt buộc, không thay thế |
| **DDL Data** (csv files) | Phase 4, Skill A/B/C | UX rules matching | ❌ Bắt buộc cho review quality |
| **Agent Vision** | Phase 2, Skill C | Đọc ảnh PNG | ❌ Built-in, luôn available |
| **File System** | Tất cả | Read/write .md, .json, .png | ❌ Built-in |

---

## Bước 1: HC-0 — Greeting & Scope Confirmation

### 1a. Greeting (BẮT BUỘC)

Agent BẮT BUỘC mở đầu bằng greeting trước khi thu thập input:

```
👋 **Xin chào! Tôi là UX Review Pipeline Assistant.**

Tôi sẽ giúp bạn tạo **UX Review Report** từ Figma design — từ A đến Z:

📄 **Giai đoạn 1** — Sinh PRD .md pack (5 sections per screen)
🔬 **Giai đoạn 2** — Đánh giá UX tự động (Agent Vision + DDL rules)

---

### 📋 Tôi cần thông tin sau:

| # | Thông tin | Bắt buộc | Ví dụ |
|:--|:---------|:--------:|:------|
| 1 | **Figma URL** | ✅ | `https://figma.com/design/abc123/...?node-id=1-2` |
| 2 | **Tên sản phẩm** | ✅ | `Co-op Bank KHCN` |
| 3 | **Domain** | Mặc định: `banking` | `banking`, `ecommerce`, `healthcare` |
| 4 | **Thư mục output** | Tự tạo | `/co-op-bank-khcn/chuyen-tien/` |

---

### ⏱️ Ước lượng thời gian
- 5-10 screens: ~20 phút
- 10-20 screens: ~30-40 phút
- > 20 screens: ~40-60 phút (khuyên chia batch)

### 🎯 Output bạn sẽ nhận được:
1. **PRD .md pack** — Overview + feature files per screen
2. **`ux-review-report.md`** — Báo cáo UX chi tiết (Critical/Major/Minor)
3. **`.handoff/`** — Machine-readable data cho downstream pipeline

Vui lòng gửi Figma URL để bắt đầu! 🚀
```

### 1b. Input Collection & Validation

Thu thập từ user:

| Parameter | Type | Required | Default | Validation |
|:---|:---|:---:|:---|:---|
| `figma_url` | `string (URL)` | ✅ | — | Must match `figma.com/design/` pattern. Extract `file_key` + `node_id` |
| `product_name` | `string` | ✅ | — | Non-empty, sanitize to slug cho folder name |
| `domain` | `enum` | ❌ | `banking` | One of: `banking`, `ecommerce`, `healthcare`, `fintech`, `general` |
| `output_dir` | `string (path)` | ❌ | `{workspace}/{product-slug}/` | Must be writable path |

**Cờ nội bộ (luôn true trong workflow này):**

| Cờ | Giá trị | Hành vi |
|:---|:---:|:---|
| `enable_ocr_reconciliation` | `true` | Bắt buộc OCR bằng agent vision (2 rounds per screen) |
| `enable_ux_signal_inference` | `true` | Bắt buộc Phase 4e suy luận UX theo biên màn hình |

### 1c. Scope Preview (BẮT BUỘC trước khi tiếp)

Sau khi nhận input, agent **BẮT BUỘC**:
1. Gọi `get_metadata(node_id)` để lấy danh sách sections/screens
2. Echo lại cho user:
   - Figma URL đã nhận
   - Product name + domain
   - Output dir
   - Danh sách sections/screens phát hiện được
   - Ước lượng thời gian dựa trên số screens
3. **Chờ user xác nhận** trước khi bắt đầu Bước 2

**Gate HC-0:**
```
pass_condition: user_confirmed == true AND figma_url is valid
fail_action: ASK_AGAIN
```

---

## Bước 2: Chạy `figma-to-prd-md` (Sinh MD Pack)

Gọi Agent bắt đầu tiến trình sinh PRD .md.

### Phase 0 & 1: Figma Export

Lấy node, export màn hình thành ảnh, parse cấu trúc.

### HC-1: Image Export Verification (CRITICAL 🔴)

**Ngay sau Phase 0-1, TRƯỚC KHI chạy Phase 2, BẮT BUỘC verify ảnh:**

| Check | Logic | Severity |
|:---|:---|:---:|
| `ui/` directory tồn tại | `ls -la {output_dir}/{feature}/ui/` | 🔴 BLOCK |
| Số file PNG > 0 | `find ui/ -name "*.png" \| wc -l` | 🔴 BLOCK |
| Mỗi screen có matched PNG | So sánh `screen_list` vs `ui/*.png` | 🔴 BLOCK |
| File size > 5KB per PNG | `find ui/ -name "*.png" -size +5k` | 🟡 WARN |
| **Human preview** | Agent hiển thị 1-2 ảnh → user xác nhận nội dung đúng | 🔴 BLOCK |

**Agent Action:**
1. List tất cả files trong `ui/` folder
2. Report: `"Đã export N ảnh cho M screens"`
3. Hiển thị preview 1-2 ảnh đại diện (dùng `view_file` trên ảnh PNG)
4. Hỏi user xác nhận

**Human Decision:**
- ✅ Ảnh đúng → Tiếp tục Phase 2
- ❌ Ảnh sai/thiếu → Agent retry export hoặc user upload thủ công

**Fail Recovery:**
```
Nếu 🔴 BLOCK fail:
  1. Retry Figma export (get_screenshot MCP)
  2. Nếu MCP fail → yêu cầu user upload ảnh thủ công vào ui/
  3. Nếu user upload → validate lại gate
  Max retries: 2

Nếu 🟡 WARN (file size < 5KB):
  → Cảnh báo: "Ảnh screen X có kích thước nhỏ bất thường (< 5KB).
     Có thể ảnh bị lỗi hoặc chỉ là placeholder. Tiếp tục?"
```

### Phase 2: Screen Inventory & OCR

**CHỈ CHẠY SAU KHI HC-1 PASS.**

- Gom nhóm `screen_boundaries`.
- **LƯU Ý:** Agent Vision BẮT BUỘC phải soi ảnh của mỗi screen làm 2 round:
  - **Round 1:** Extract toàn bộ Text `ocr_round1_text`.
  - **Round 2:** Extract toàn bộ Icons & vị trí `ocr_round2_icons`.
- Tổng hợp ra `ocr_full_table` và các `ocr_ux_improvements` theo ngữ cảnh.

### HC-2: OCR Completeness Review

**Sau Phase 2g, verify OCR coverage:**

| Check | Logic | Severity |
|:---|:---|:---:|
| `ocr_full_table` tồn tại per screen | Loop `screen_inventory.screens[k]` | 🔴 BLOCK |
| `ocr_round1_text` non-empty | `text_list.length > 0` per screen | 🔴 BLOCK |
| `ocr_round2_icons` populated | `ocr_icons.length >= 0` | 🟡 WARN |
| Text count reasonable | `text_count >= 3` per screen | 🟡 WARN |

**Agent Action:**
1. Tổng hợp summary per screen: `"Screen X: N texts, M icons"`
2. Highlight screens có text_count < 3 (bất thường)
3. Report cho user

**Human Decision:**
- ✅ OCR coverage đủ → Tiếp Phase 3
- ⚠️ Screen X thiếu text → Rerun OCR cho screen X (Phase 2g-bis)
- ❌ OCR sai ngữ cảnh → User bổ sung context_hint

### Phase 3: PRD Structure Gen

Tạo folder section và nội dung PRD Draft ban đầu 5 sections.

### HC-3: PRD Draft Sanity Check (Optional)

**Agent Action:**
1. List overview + feature files đã tạo
2. Summary: screens covered, use cases identified, flow edges
3. Highlight: screens có nhiều flow vs. screens có 0 flow

**Human Decision:**
- ✅ Structure OK → Tiếp Phase 4
- ⚠️ Missing feature → Thêm screen vào scope
- ❌ Wrong grouping → Adjust section mapping

> Checkpoint này là **optional** — agent có thể skip nếu số screens nhỏ (< 5) hoặc user đã cho phép auto-proceed.

### Phase 4: Augment

Tăng cường PRD (`ui-ux-pro-max`).
- Đặc biệt chạy **Phase 4e**: Lấy raw text/icon ở trên feed thẳng vào `ux-signal-inference` (`.agents/skills/ux-signal-inference/SKILL.md`) → tạo `prd_extension` có `ddl_ref`. Merged vào `prd_augmented`.

### Phase 5: Output .md Pack

- Dựng cây Output Folders. Xuất toàn bộ `.md` và copy ảnh vào `/ui`.
- **Tạo Handoff (BẮT BUỘC):** Xuất ra thư mục `.handoff/` với đầy đủ files:

### Handoff Files Contract

| File | Bắt buộc | Nội dung |
|:---|:---:|:---|
| `screen_inventory.json` | **Có** | Danh sách screen + `consumer_payload` per screen (text_list, context_hint, ocr_icons, ocr_screen_context) |
| `handoff-manifest.json` | **Có** | `schema_version`, `generated_at`, `figma_source`, `flags`, `phases_completed` |
| `flow_graph.json` | Nên có | Edges giữa các screen (from, to, trigger, type) |
| `figma_context_registry.json` | Tuỳ chọn | context_label, context_type, figma_source, screen_id |

**Schema version:** `figma-prd-handoff-v1`.

---

## HC-4: Pre-Handoff Gate (Enhanced) — CRITICAL 🔴

**BẮT BUỘC verify trước khi chuyển giao sang Bước 3:**

| # | Check | Severity | Mới? |
|:--|:---|:---:|:---:|
| 1 | `.handoff/handoff-manifest.json` tồn tại + valid schema | 🔴 BLOCK | — |
| 2 | `.handoff/screen_inventory.json` tồn tại | 🔴 BLOCK | — |
| 3 | `ocr_done = true` trong manifest hoặc `.ocr_done` file | 🔴 BLOCK | — |
| 4 | Mọi screen có `ocr_full_table` populated trong `screen_inventory.json` | 🔴 BLOCK | — |
| 5 | **Mọi screen có ảnh tương ứng trong `ui/`** | 🔴 BLOCK | 🆕 |
| 6 | **File size > 0 cho mọi ảnh PNG** | 🔴 BLOCK | 🆕 |
| 7 | `flow_graph.json` tồn tại | 🟡 WARN | — |

**Agent Action:**
1. Chạy tất cả 7 checks tự động
2. Report kết quả dạng checklist: ✅/❌ per check
3. Nếu có 🔴 BLOCK fail → **DỪNG pipeline**, thông báo user cụ thể check nào fail
4. Nếu chỉ 🟡 WARN → thông báo nhưng cho phép tiếp tục

**Fail Recovery:**
```
Check 1-4 fail: "OCR chưa hoàn tất cho screen X. Chạy lại Phase 2g hoặc 2g-bis."
Check 5-6 fail: "Ảnh thiếu cho screen X. Chạy lại Phase 0-1 export hoặc upload thủ công."
```

---

## Bước 3: Chuyển giao dữ liệu (Handoff Preparation)

**CHỈ CHẠY SAU KHI HC-4 PASS.**

Khai báo nguồn data đầu vào cho UX review:
- `prd_folder`: Thư mục Output `output_dir` vừa được tạo.
- `consumer_payload`: Load object từ `.handoff/screen_inventory.json`.
  - **Fast-path (có `.handoff/`):** Skill A dùng trực tiếp `text_list`, `context_hint`, `ocr_icons`.
  - **Fallback (không có `.handoff/`):** Skill A tự parse .md Section 3 (chậm hơn, thiếu ocr_icons).
- `domain`: Truyền từ Bước 1 (hoặc mặc định từ `handoff-manifest.json`).

---

## Bước 4: Chạy `ux-review-pipe` (Đánh giá UI/UX)

Thông báo Agent tiến hành Pipeline Review.

### 4a. Chạy Song Song (Skill A & Skill B)

- **Skill A:** Inference & DDL Report. Dùng parameters từ `consumer_payload` (hoặc fallback parse Section 3) để detect signal (action, error, state) dựa vào DDL.
- **Skill B:** PRD Context DDL. Đọc nội dung Flow, User Story, và NFR để cross-ref với rules DDL (Back button logic, States mapping, Touch target, v.v.). **KHÔNG được đọc ảnh ở bước này.**

### 4b. Degraded Mode (khi Skill A hoặc B fail)

- Nếu **Skill A fail** → Skill C vẫn chạy với chỉ `prd_ddl_report` từ B. Log warning: `SKILL_A_DEGRADED`.
- Nếu **Skill B fail** → Skill C vẫn chạy với chỉ `signal_ddl_report` từ A. Log warning: `SKILL_B_DEGRADED`.
- Nếu **cả A và B fail** → **DỪNG pipeline**. Thông báo user.

### GATE: VISION_READY (CRITICAL 🔴) — Trước Skill C

**BẮT BUỘC verify trước khi Skill C đọc ảnh:**

| Check | Logic | Severity |
|:---|:---|:---:|
| `wireframe_images[]` populated trong `prd_ddl_report` | Per screen check | 🔴 BLOCK |
| Tất cả image paths resolve to existing files | `fs.existsSync(path)` cho mỗi path | 🔴 BLOCK |
| Ít nhất 1 ảnh tìm thấy | `total_images > 0` | 🔴 BLOCK |
| Test đọc được ảnh | `view_file` thử trên 1 ảnh PNG | 🔴 BLOCK |

**Fail → DỪNG pipeline:** `"Không tìm thấy ảnh wireframe cho vision review. Kiểm tra lại thư mục ui/ hoặc chạy lại Phase 0-1."`

### 4c. Skill C (Vision Review + Đề xuất)

**BẮT BUỘC CHẠY SAU KHI:**
1. A & B hoàn tất (hoặc degraded)
2. **GATE VISION_READY đã PASS**

- **Dùng Agent Vision:** Đọc trực tiếp các ảnh thư mục `ui/*.png`. (Bắt buộc dùng agent vision ở bước này để kiểm định, bất kể Pipe 1 đã chạy vision hay chưa).
- Đối chiếu chéo 2 list errors/gaps từ A và B với bức ảnh xem màn hình code/design đã có chưa. (evidence/verdict).
- Khám phá lỗi trực quan (contrast, truncation, overlap layout).
- Tự động map vấn đề với `DDL` và trả lại đề xuất **cụ thể** (thay text cục bộ, di chuyển button, bổ sung outline, v.v.).

---

## Bước 5: HC-5 — Tổng hợp và Kết thúc

### 5a. Vision Review Confirmation (HC-5)

**Trước khi ghi report cuối cùng, agent BẮT BUỘC:**
1. Tóm tắt findings: số lượng Critical / Major / Minor
2. Highlight top 3 issues có severity cao nhất
3. Cho user preview 1-2 findings kèm evidence

**Human Decision:**
- ✅ Accept → Agent ghi report cuối cùng
- ⚠️ False positive → Agent loại bỏ/adjust finding trước khi ghi
- ❌ Missing coverage → Rerun Skill C với focus area cụ thể

### 5b. Output Report

1. Tổng hợp thành `{prd_folder}/ux-review-report.md`.
2. Thông báo Output Summary (Pass, Gap, Unverifiable) cho user. Mở file Report để user kiểm tra các lỗi Critical/Major.
3. Nếu degraded mode → ghi rõ trong report: "⚠️ Degraded: Skill X không chạy được — report thiếu coverage từ skill đó."

---

## Output Specification

### Primary Outputs

| Output | Path | Format |
|:---|:---|:---:|
| Overview PRD | `{output_dir}/{product-slug}-overview.md` | Markdown |
| Feature PRDs | `{output_dir}/{FeatureName}/` | Markdown × N |
| Screen Images | `{output_dir}/{FeatureName}/ui/*.png` | PNG |
| **UX Review Report** | `{output_dir}/ux-review-report.md` | Markdown |

### Handoff Outputs (Machine-readable)

| Output | Path | Schema |
|:---|:---|:---|
| Manifest | `.handoff/handoff-manifest.json` | `figma-prd-handoff-v1` |
| Screen Inventory | `.handoff/screen_inventory.json` | Array of `{screen_id, consumer_payload}` |
| Flow Graph | `.handoff/flow_graph.json` | `{edges: [{from, to, trigger, type}]}` |

---

## Gate Summary — Quick Reference

```
Pipeline Flow:

  PREFLIGHT     HC-0          HC-1           HC-2         HC-3          HC-4
  Tools OK? →  Greeting  →  Image Gate  →  OCR Gate  →  PRD Check  →  Handoff Gate
  (🔴 auto)    (human)      (🔴+human)     (🔴+human)   (optional)    (🔴+human)
                                                                          ↓
                                                           HC-5      VISION_READY
                                                        Report  ←  Skill C  ←  Gate
                                                        (human)              (🔴 auto)

Legend:
  🔴 = BLOCK gate (pipeline stops if fail)
  🟡 = WARN (notify but continue)
  🟢 = Human-only checkpoint

Tools checked in PREFLIGHT:
  P1: Figma MCP (🟡)  P2: figma-save MCP (🔴)  P3: FAT token (🔴)
  P4: DDL data (🔴)   P5: Output dir (🔴)      P6: node_modules (🟡)
```

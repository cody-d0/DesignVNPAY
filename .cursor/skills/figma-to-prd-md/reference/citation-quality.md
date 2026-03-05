# Citation Rules, Quality Gates & UI Automation Readiness

Load file này khi thực hiện Phase 5 (validation + output).

---

## Citation Rules

### COMPbase (từ Figma)

| Loại | Format citation |
|------|----------------|
| Component từ layout | `figma:{fileKey}/{nodeId}/{layer_path}` |
| Text content | `figma:{fileKey}/{nodeId}#text` |
| Variable binding | `figma_var:{variable_name}` |
| Screenshot | `figma_screenshot:{fileKey}/{nodeId}` |
| Navigation flow (prototype) | `figma_prototype:{fileKey}/{nodeId}` |
| Navigation flow (suy luận) | `figma_inferred:{fileKey}/{nodeId}` |
| Spec từ ảnh (OCR gaps) | `ocr:{filename}` (vd. `ocr:internal-transaction.png`) |
| Design element (unmapped node) | `figma:{fileKey}/{nodeId}` — row "Design element" (Phase 2b-bis) vẫn cần citation COMPbase |

### COMPextend (từ augment) — hiển thị bằng `🤖 by AI` badge

| Loại | Format citation (trong badge) |
|------|-------------------------------|
| UX guideline | `ux-guidelines.csv#{No}: {Issue}` |
| Web interface | `web-interface.csv#{No}: {Issue}` |
| Color recommendation | `colors.csv#{No}` |
| Typography recommendation | `typography.csv#{No}` |
| Frontend-design check | `frontend-design#{check_name}` |
| Case study / competitor | `case-study:{product_name}` |
| search.py design system | `search.py --design-system "{query}"` |
| search.py domain lookup | `search.py --domain {domain} "{query}"` |
| WebSearch competitor | `web-search:{url_or_query}` |

### UNSPECIFIED / INFERRED

- `UNSPECIFIED`: không có trong Figma, không suy luận được
- `INFERRED`: suy luận từ Figma chưa confirm (đặc biệt Database schema — nằm trong `🤖 by AI` badge)

---

## Quality Gates

| Gate | Target | Mô tả |
|------|--------|-------|
| Structure coverage | 100% | Mọi feature file có đủ 5 section |
| COMPbase citation | 100% | Mọi COMPbase row có figma:* citation |
| Screenshot coverage | 100% screens | Mỗi screen có full-screen screenshot đã tải trong Wireframe |
| Sub-frame screenshots | Best effort | Sub-frame screenshots tải được → link; fail → skip |
| Component coverage | >= 90% | >= 90% Figma components được map vào bảng Mô tả màn hình |
| UNSPECIFIED transparency | 100% | Mọi UNSPECIFIED item được list trong overview summary |
| US numbering | 100% unique | Mã US không trùng, liên tục |
| AI badge completeness | 100% | Mọi `🤖 by AI` block có Nguồn + Độ tin cậy |
| AI badge summary | 100% | Mọi AI block được list trong "Tổng hợp nội dung AI đề xuất" |
| AI vs COMPbase separation | 100% | Không có AI content ngoài badge blockquote; không có COMPbase trong badge |
| Alt text coverage & format | 100% | Mọi ảnh có alt non-empty; độ dài ≤ 125 ký tự; không trùng alt giữa các ảnh khác nhau trong cùng feature file |

---

## UI Automation Readiness

Output PRD .md từ skill này phải đủ thông tin để sinh **UI automation artifacts** mà không cần đọc thêm tài liệu khác. Mapping chuẩn:

| PRD artifact | UI automation mapping |
|--------------|------------------------|
| 1 feature file .md | 1 Page Object class (1 file = 1 màn hình) |
| Bảng "Mô tả màn hình" (Section 3) | Element locator registry: STT + Loại thành phần + Mô tả → selector/locator |
| Mã US (Section 2) | Test case ID traceability: US-xxx → test method / test ID |
| Bảng User Flow (Section 1) | Test scenario / step definition: Bước → Hành động → Kết quả = step + assertion |
| DB Entity (Section 4) | Test data factory / fixture: Field + Data Type + Constraint → test data builder |
| Business Rule + Constraint | Boundary value test case (vd: "Số lần ≤ 10" → test với 9, 10, 11) |
| State (default, loading, error, disabled) | State-based test variant |

**Quality gate:** Mỗi feature file phải đủ nội dung để sinh Page Object + test scenarios (steps + assertions) mà không cần suy luận thêm từ tài liệu ngoài. Đảm bảo bằng: minimum component granularity (Phase 2b), minimum flow coverage (Section 1), minimum US granularity (Section 2), và mô tả cụ thể có sample data.

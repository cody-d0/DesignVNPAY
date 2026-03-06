# Text Signals Schema

Schema cho file JSON pattern registry (text-signals-generic.json, text-signals-{domain}.json).

## Pattern group

Mỗi pattern group mô tả một nhóm tín hiệu text/icon có thể suy ra cùng một UX pattern.

| Field | Type | Mô tả |
|-------|------|--------|
| `id` | string | Id duy nhất (vd. selection_mode, confirm_dialog). |
| `name_vi` | string | Tên tiếng Việt (vd. "Chế độ chọn nhiều"). |
| `instruction[]` | string[] | Regex hoặc chuỗi mẫu cho text hướng dẫn (vd. "Chọn danh bạ.*xóa"). |
| `counter[]` | string[] | Regex cho bộ đếm (vd. "Xóa\\s*\\(\\d+\\)", "Xóa (n)"). |
| `action[]` | string[] | Regex cho nút/CTA chính (vd. "Xóa", "Xóa \\(\\d+\\)"). |
| `cancel[]` | string[] | Regex cho nút hủy/thoát (vd. "Hủy", "Đóng"). |
| `tags[]` | string[] | Tag gắn khi match (vd. selection_mode, bulk_delete). |
| `inferred_ux` | object | Cấu trúc inferred: flow_name_vi, component_rows[], state_hint. |

**inferred_ux:**

| Field | Type | Mô tả |
|-------|------|--------|
| `flow_name_vi` | string | Tên luồng đề xuất (vd. "Xóa nhiều danh bạ"). |
| `component_rows[]` | array | Mảng row Mô tả màn hình: Loại thành phần, Mô tả. |
| `state_hint` | string | Gợi ý state (default, active, loading, …). |

## Inference rule

Áp dụng khi match pattern groups thỏa điều kiện.

| Field | Type | Mô tả |
|-------|------|--------|
| `when` | object | `pattern_groups`: id[], `require_types`: string[] (instruction, counter, action, cancel — tổ hợp cần có). |
| `then` | object | `inferred_ux` trực tiếp hoặc `use_inferred_from`: pattern_group_id. |
| `confidence` | string | high \| medium \| low. |

## Domain override

- File `text-signals-{domain}.json` (vd. text-signals-banking.json) có thể khai báo `"extends": "generic"` để merge với text-signals-generic.json.
- Các trường `instruction`, `counter`, `action`, `cancel`, `tags` được merge (append) vào pattern group cùng id; nếu không có id trùng thì thêm pattern group mới.
- `domain`: string (vd. "banking") dùng để chọn file khi consumer truyền domain.

## Regex trong JSON

Trong chuỗi JSON, ký tự backslash cần escape: `\d` → `\\d`, `\(` → `\\(`, `\)` → `\\)`. Ví dụ: `"Xóa\\\\s*\\\\(\\\\d+\\\\)"` cho pattern "Xóa\s*\(\d+\)".

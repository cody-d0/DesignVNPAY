# 📚 MarkdownSV — Content Root

Thư mục này là **content root** cho Markdown Viewer (http://localhost:9999).

## Cách hoạt động

- Server **tự động quét** toàn bộ `.md` files trong thư mục này (live mode, không cần manifest).
- Các subfolder là **symlinks** tới nội dung gốc — chỉnh sửa file gốc sẽ tự động phản ánh.

## Nội dung hiện tại

| Folder | Nguồn | Mô tả |
|--------|-------|-------|
| `Co-op-Bank-KHCN/` | `../Co-op-Bank-KHCN` | Raw PRD + UX Review Report |
| `Co-op-Bank-PRD/` | `../products/co-op-bank-khcn/prd` | PRD output đã generate (25+ files) |
| `docs/` | `../docs` | Project documentation |

## Thêm product mới

```bash
# Ví dụ: thêm sản phẩm xPOS
ln -s ../products/xpos/prd MarkdownSV/xPOS
```

Sau đó refresh browser → file mới hiện ngay.

# Hướng dẫn cài đặt Google Sheets Backend (v3)

## Kiến trúc
- **Google Sheet = Single Source of Truth** (100%)
- Không dùng localStorage cho data — chỉ dùng cho theme
- Mọi thao tác (lưu/xóa/sửa) đều gọi trực tiếp đến Sheet qua GET request
- Data hiển thị trên giao diện = lấy từ Sheet mỗi lần thao tác

## Bước 1: Tạo Google Sheet
1. Mở [Google Sheets](https://sheets.new) → tạo sheet mới
2. Đặt tên: **"Phiếu Thu DV"**
3. Không cần tạo header — script tự tạo

## Bước 2: Thêm Apps Script
1. Trong Google Sheet → **Extensions** → **Apps Script**
2. Xóa code mặc định, copy toàn bộ nội dung file `Code.gs`
3. Nhấn **💾 Save** (Ctrl+S)

## Bước 3: Chạy Setup
1. Chọn hàm `setupSheet` từ dropdown
2. Nhấn **▶ Run**
3. Lần đầu → "Review Permissions" → chọn tài khoản → "Allow"
4. Check Sheet: thấy sheet **"Receipts"** với 14 cột header

## Bước 4: Deploy Web App
1. Nhấn **Deploy** → **New deployment**
2. Chọn type: **Web app**
3. Cài đặt:
   - Description: `Receipt API v3`
   - Execute as: **Me**
   - Who has access: **Anyone**
4. Nhấn **Deploy** → **Copy URL**

## Bước 5: Cập nhật URL trong Admin
1. Mở `ticket115588/index.html`
2. Tìm dòng `const SHEET_URL = '...'` (khoảng dòng 824)
3. Paste URL vừa copy vào

## API Endpoints (tất cả dùng GET)

| Action | URL | Mô tả |
|--------|-----|-------|
| List all | `?` (không param) | Lấy toàn bộ phiếu |
| Save | `?action=save&id=...&room=...&el=...` | Lưu/cập nhật 1 phiếu |
| Delete | `?action=delete&id=...&room=...` | Xóa 1 phiếu |
| Delete All | `?action=deleteAll` | Xóa tất cả phiếu |

## ⚠️ Lưu ý quan trọng
- **Mỗi lần sửa `Code.gs`** → phải Deploy lại:
  - Deploy → **Manage deployments** → ✏️ Edit → **Version: New version** → Deploy
  - HOẶC: Deploy → **New deployment** (sẽ tạo URL mới, phải cập nhật lại `SHEET_URL`)
- Tất cả request dùng **GET** để tránh lỗi CORS/redirect của Google
- Nếu gặp lỗi "Unknown error" → kiểm tra đã chạy `setupSheet()` chưa

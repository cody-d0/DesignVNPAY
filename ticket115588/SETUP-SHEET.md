# Hướng dẫn cài đặt Google Sheets Backend

## Bước 1: Tạo Google Sheet
1. Mở [Google Sheets](https://sheets.new) → tạo sheet mới
2. Đặt tên: **"Phiếu Thu DV"**
3. **Không cần tạo header** — script sẽ tự tạo khi chạy lần đầu

## Bước 2: Thêm Apps Script
1. Trong Google Sheet → **Extensions** → **Apps Script**
2. Xóa code mặc định, copy toàn bộ nội dung file `Code.gs` (cùng thư mục)
3. Nhấn **💾 Save** (Ctrl+S)

## Bước 3: Chạy Setup
1. Trong Apps Script → chọn hàm `setupSheet` từ dropdown
2. Nhấn **▶ Run**
3. Lần đầu sẽ hỏi **quyền truy cập** → nhấn "Review Permissions" → chọn tài khoản → "Allow"
4. Check lại Sheet: sẽ thấy sheet "Receipts" với header row

## Bước 4: Deploy Web App
1. Nhấn **Deploy** → **New deployment**
2. Chọn type: **Web app**
3. Cài đặt:
   - Description: `Receipt API v1`
   - Execute as: **Me**
   - Who has access: **Anyone**
4. Nhấn **Deploy**
5. **Copy URL** dạng: `https://script.google.com/macros/s/AKfyc.../exec`

## Bước 5: Cập nhật Admin
1. Mở `ticket115588/index.html`
2. Tìm dòng `const SHEET_URL = '...'`
3. Paste URL vừa copy vào

## Lưu ý
- Mỗi lần **sửa code Apps Script** → cần **Deploy** lại (New deployment)
- Data tự động sync 2 chiều: localStorage ↔ Google Sheet
- Nút ☁️ trên sidebar để pull data từ cloud về

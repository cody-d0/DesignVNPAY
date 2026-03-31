# 📋 Thanh toán vay

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `product/`
> **Trích xuất:** 2026-03-28

---

## 31. URD_MB_COOPBANK_THANH TOÁN VAY

> **Page ID:** `85919724` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/85919724

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*5 trang con:*

### 31.1. SOW CHỨC NĂNG TẠO LỆNH THANH TOÁN KHOẢN VAY

> **Page ID:** `83876035` · **Version:** 19
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/83876035

### 1/ Nguyên tắc
falseGhi rõ các nguyên tắc về CHÍNH SÁCH mà Bank/Đối tác áp dụng cho chức năng thuộc phạm vi phân tích

### 2/ Phạm vi

#### 2.1/ Phạm vi FrontEnd
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | API Bank cấp
 | Tạo lệnh thanh toán khoản vay | Tạo lệnh thanh toán khoản vay cho chính chủ tài khoản | 

RedThêm mới
 | MB | 
• Cho phép người dùng tạo lệnh thanh toán các khoản vay tại Bank của chính chủ tài khoản
• Yêu cầu số tiền trả nợ vay phải lớn hơn số tiền tối thiểu được cài đặt
• Không kiểm tra số tiền thanh toán với Số dư khả dụng như các dịch vụ trước, mà kiểm tra với Số dư khả dụng trừ đi hạn mức thấu chi được cấp cho KH đó
• Quá trình gạch nợ khoản vay không xử lý ngay mà xử lý sau theo quy trình của Bank | 
BlueTRUNG BÌNH
 | Client, Server, Bank | 

 | 
 | Tạo lệnh thanh toán khoản vay theo địa bàn | 
RedThêm mới
 | MB | 
• Cho phép người dùng tạo lệnh thanh toán các khoản vay cho người khác theo địa bàn hoặc theo số bảng kê được Bank cung cấp trước (Hình thức người thanh toán thu hộ cho Bank và thực hiện thanh toán cho Bank sau đó)
• Yêu cầu số tiền trả nợ vay phải lớn hơn số tiền tối thiểu được cài đặt
• Không kiểm tra số tiền thanh toán với Số dư khả dụng như các dịch vụ trước, mà kiểm tra với Số dư khả dụng trừ đi hạn mức thấu chi được cấp cho KH đó
• Quá trình gạch nợ khoản vay không xử lý ngay mà xử lý sau theo quy trình của Bank | 
BlueTRUNG BÌNH
 | Client, Server, Bank | 

 | 
 | Danh sách tài khoản vay | 
RedThêm mới
 | MB | 
• Bổ sung chức năng Danh sách tài khoản vay tại chức năng "Tạo lệnh thanh toán vay" | 
BlueTRUNG BÌNH
 | 
 | 

 | 
 | Danh sách lệnh khoản vay | 
RedThêm mới
 | MB | Cho phép tra cứu các lệnh khoản vay đã tạo trên kênh MB | 
BlueTRUNG BÌNH
 | 
 | 

 | 
 | Chi tiết lệnh khoản vay | 
RedThêm mới
 | MB | Cho phép xem chi tiết trạng thái thu nợ đã được Corebank xử lý của mỗi lệnh thanh toán khoản vay đã tạo trên kênh MB | 
BlueTRUNG BÌNH
 | 
 | 

 | 
 | Danh sách tài khoản (Chức năng tài khoản cũ) | 
GreenCập nhật
 | MB | 
Cập nhật thêm thông tin về khoản vay tại Danh sách khoản vay:
- Ngày giải ngân + Ngày đáo hạn

- Thay đổi text Tổng dư nợ gốc = Tổng dư nợ gốc hiện tại

- Thay đổi text Dư nợ gốc = Dư nợ gốc hiện tại
 | 
BlueTRUNG BÌNH
 | 
 | 

 | 
 | Thông tin tài khoản vay | 
GreenCập nhật
 | MB | 
Giữ nguyên như cũ (Cần test lại ảnh hưởng)
 | 

 | 
 | 

 | 
 | Lịch sử giao dịch vay | 
GreenCập nhật
 | MB | 
Lịch sử giao dịch:
- Thay đổi khoảng thời gian tìm kiếm: 1 tháng, 2 tháng, 3 tháng

-Thay đổi khoảng thời gian tìm kiếm tối đa 1 năm
- Mặc định hiển thị dữ liệu 1 tháng gần nhất

- Thay đổi text icon chức năng Trả nợ vay = Tạo lệnh thanh toán khoản vay chính chủ

- Sửa label mô tả tại mục Lịch sử giao dịch thành "Khoảng thời gian tìm kiếm giới hạn trong vòng 1 năm" (Cũ Khoảng thời gian tìm kiếm giới hạn trong vòng 3 tháng)
 | 
BlueTRUNG BÌNH
 | 
 | 

 | 
 | Báo cáo giao dịch | 
GreenCập nhật
 | MB | 
Bổ sung thêm 2 loại giao dịch:

• Tạo lệnh thanh toán khoản vay cho chính chủ tài khoản
• Tạo lệnh thanh toán khoản vay theo địa bàn | 
BlueTRUNG BÌNH
 | 
 | 

#### 2.2/ Phạm vi Backend
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | API Bank cấp
 | Tham số | Cấu hình Số tiền trả nợ vay tối thiểu | Thêm mới | Backend | --- | -- | --
 | Cấu hình Thời gian cho phép thanh toán trả nợ vay trong ngày | Thêm mới | Backend | -- | -- | --
 | Báo cáo Tổng hợp giao dịch + Chi tiết giao dịch | 
Bổ sung dịch vụ

• Tạo lệnh thanh toán khoản vay cho chính chủ tài khoản
• Tạo lệnh thanh toán khoản vay theo địa bàn | Cập nhật | Backend | 
 | 
 | 

 | Danh mục dịch vụ | 
Bổ sung cờ đánh dấu dịch vụ được phép dùng thấu chi hay không
 | Cập nhật | Backend | 
Link tài liệu

 | 
 | 

 | Báo cáo chi tiết tạo lệnh thanh toán khoản vay theo địa bàn | 
Quản lý báo cáo chi tiết các lệnh thanh toán khoản vay theo địa bàn được phát sinh trên ứng dụng Mobile banking
 | Thêm mới | Backend | 

 | 
 | 

 | Báo cáo chi tiết tạo lệnh thanh toán khoản vay chính chủ | 
Quản lý báo cáo chi tiết các lệnh thanh toán khoản vay chính chủ được phát sinh trên ứng dụng Mobile banking
 | Thêm mới | Backend | 

 | 
 | 

#### 2.3/ Phạm vi Server

Cập nhật logic kiểm tra chung Hạn mức, phương thức xác thực. Đã mô tả tại

https://wiki.servicehub.vn/pages/viewpage.action?pageId=29894527

#### 2.4/ Đánh giá ảnh hưởng

Cần test lại các chức năng:

App

• Tài khoản
• Lịch sử giao dịch vay
• Chi tiết giao dịch vay
• Báo cáo giao dịch vay
• Do cập nhật lại logic kiểm tra số dư khả dụng nên cần test lại các luồng dịch vụ tài chính cũ
- Các dịch vụ tài chính cũ: Vẫn theo logic cũ, kiểm tra số dư khả dụng

- Các dịch vụ thanh toán khoản vay (mới): Theo logic mới, kiểm tra số tiền thanh toán với Số dư khả dụng trừ đi hạn mức thấu chi được cấp cho KH đó

Backend

• Báo cáo tổng hợp giao dịch
• Báo cáo chi tiết giao dịch
• Bảng danh mục dịch vụ bổ sung thêm cờ đánh dấu cho phép dùng thấu chi
#### 2.4/ Phạm vi API kênh cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Kênh sử dụng | Input | Output | Ghi chú
 | 1 |  queryLoanAccSum | Vấn tin danh sách các khoản vay | MB | 
 | 
 | 

 | 2 |  queryLoanAcc | Thông tin chi tiết khoản khoản vay | MB | 
 | 
 | 

 | 3 | createLoanPayment | Tạo lệnh thanh toán khoản vay chính chủ | MB | 
 | 
 | 

 | 4 | 
createLoanPaymentOnBe
half
 | 
Tạo lệnh thanh toán khoản vay theo địa bàn
 | MB | 
 | 
 | 

 | 5 |  paymentRequestInquiry | Tra cứu chi tiết lệnh thanh toán khoản vay | MB | 
 | 
 | 

### 3/ Q&A

#### 3.1/ Phạm vi Frontend

#### 3.2/ Phạm vi Backend

#### 3.3/ Phạm vi API kênh cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Câu hỏi | Trả lời | Cần xử lý tiếp | Ghi chú
 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 

 | 
 | 
 | 
 | 
 | 
 | 
 |

---

### 31.2. MB_Tạo lệnh trả nợ vay chính chủ

> **Page ID:** `85919731` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/85919731

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | 

 | 
 
 | M | Lê Thị Hồng | 
 | 
Đổi tên trường Lãi cộng dồn = Lãi đến ngày hiện tại
 | 

Mục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
Tác nhân, điều kiện, kết quả mong muốn

 | 1. Mục đích chức năng: | 
Tạo lệnh trả nợ vay chính chủ tài khoản

 | 2. Tác nhân tham gia: | 
App, MB Server, HT Bank

 | 3. Điều kiện trước: | 
• KH đăng nhập thành công vào hệ thống Mobile banking
• KH thuộc gói dịch vụ được phép sử dụng chức năng này.
• KH có tài khoản nguồn hợp lệ để thực hiện chức năng này
• KH có khoản vay chưa tất toán tại ngân hàng
 | 4. Kết quả mong muốn: | 
• Tạo lệnh thanh toán vay thành công
• Tài khoản thanh toán của khách hàng bị trừ số tiền tương ứng với số tiền trả nợ trong lệnh

### 2/ Luồng sơ đồ

### 3/ Luồng màn hình

#### Danh sách màn hình

MH1: <Trang chủ>

MH2: <Tạo lệnh thanh toán khoản vay>

MH3: <Tạo lệnh trả nợ vay chính chủ>

MH4: <Xác nhận giao dịch>

MH5: <Xác thực giao dịch>

MH6: <Kết quả giao dịch>

MH3.1 Điều kiện, điều khoản

#### Mô tả màn hình

##### MH1: <Trang chủ>

Bổ sung thêm chức năng "Khoản vay" tại nhóm chức năng Tài chính

##### MH2: <Khoản vay>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tạo lệnh trả nợ vay chính chủ
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 2 | 
Tạo lệnh trả nợ vay theo địa bàn
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 3 | 
Danh sách khoản vay khoản chính chủ
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 4 | 
Danh sách tạo lệnh trả nợ vay
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 5 | 
Icon Back
 | 
Icon
 | 
Click
 | 

 | 

 | Về màn hình trước đó

##### MH3: <Tạo lệnh trả nợ vay chính chủ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề màn hình
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Tạo lệnh trả nợ vay chính chủ

 | 
2
 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
• Hiển thị số tài khoản + Số dư tương ứng và đơn vị tiền tệ.
• (Số dư = Số dư khả dụng - Hạn mức thấu chi được cấp cho KH)
• Click vào mở ra màn hình popup “Danh sách tài khoản nguồn”, chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | Thông tin khoản vay
 | 
3
 | 
Tài khoản vay
 | 
Listbox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định trống
• Hiển thị số tài khoản + Số dư nợ gốc tương ứng và đơn vị tiền tệ.
• Cho phép chọn 1 tài khoản vay. Sau khi chọn tài khoản vay, hiển thị các thông tin tương ứng với tài khoản vay dạng ReadOnly do Bank trả về (API  queryLoanAcc)
, bao gồm: | 1 | 
Tên chủ tài khoản (fullname hay accountName )
 | 
• Bank trả về
 | 2 | 
Chi nhánh mở (branchName)
 | 
• Bank trả về
 | 3 | 
Số hợp đồng (passBook_no )
 | 
• Bank trả về
 | 4 | 
Loại khoản vay (productDesc )
 | 
• Bank trả về
 | 5 | 
Số tiền đã giải ngân (orgBalance)
 | 
• Bank trả về
• Hiển thị Số tiền + đơn vị tiền tệ
 | 6 | 
Tổng dư nợ gốc hiện tại (remainBalance)
 | 
• Bank trả về
• Hiển thị Số tiền + đơn vị tiền tệ
 | 7 | 
Tổng dư nợ gốc đến hạn thanh toán (Nextprincipal Due)
 | 
• Bank trả về
• Hiển thị Số tiền + đơn vị tiền tệ
 | 8 | 
Lãi cộng dồn (Accrued_Dr )

→ Đổi text thành "Lãi đến ngày hiện tại"
 | 
• Bank trả về
• Hiển thị Số tiền + đơn vị tiền tệ
 | 9 | 
Lãi phạt trên lãi chậm trả (citation_rate )
 | 
• Bank trả về
• Hiển thị Số tiền + đơn vị tiền tệ
 | 10 | 
Tổng lãi
 | 
= Lãi cộng dồn+ Lãi phạt trên lãi chậm trả

 | 
Thông tin thanh toán

 | 
4
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
Yes
 | 
15
 | 
• Chỉ cho nhập ký tự số, tối đa 15 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Backend cho phép thiết lập số tiền trả nợ vay tối thiểu. Khi thực hiện giao dịch => check số tiền đã nhập với số tiền tối thiểu đã set trong BE

Nếu nhập số tiền nhỏ hơn số tiền tối thiểu => hệ thống hiển thị cảnh báo “Số tiền trả nợ tối thiểu là {n} VND. Quý khách vui lòng kiểm tra lại!” 

Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 
5
 | 
Ghi chú
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Hiển thị thông báo số tiền tối thiểu ở phía dưới trường số tiền

"Số tiền trả nợ tối thiểu là {n} VND "

{n} được cấu hình tại tham số LOAN_AMOUNT_MIN tại bảng cấu hình tham số

 | 
6
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
• Mặc định: Tên khách hàng + trả nợ vay tài khoản + số tài khoản
• Cho phép sửa, nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():
• Hiển thị [số ký tự nhập]/[số ký tự tối đa] là 210 kí tự
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
• Remark giao dịch: [Ten KH] tra no vay
 | 
T7
 | 
Điều khoản & Điều kiện
 | 
Checkbox
 | 
Click
 | 
Yes
 | 
--
 | 
• Mặc định uncheck, cho phép bỏ chọn/tích chọn. 
• Trường hợp KH chưa tick chọn:  Hiển thị popup thông báo:"Quý khách chưa đồng ý với Điều khoản, điều kiện sử dụng dịch vụ tạo lệnh thanh toán khoản vay của Co-opbank Mobile Banking."
• Hiển thị nội dung "Tôi đã đọc, hiểu rõ, đồng ý và cam kết tuân thủ các Điều khoản, điều kiện sử dụng dịch vụ tạo lệnh trả nợ vay trên ứng dụng Mobile Banking của Co-opbank. "
• Click vào Điều kiện, điều khoản mở đến MH3.1 : <Điều khoản & điều kiện >
 | 
8
 | 
Ghi chú
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Co-opBank xin trân trọng thông báo đến Quý khách thời gian trả nợ vay trong ngày là trước [17:00] các ngày làm việc. Những giao dịch ngoài thời gian trên hoặc vào ngày nghỉ, lễ tết sẽ được ghi nhận vào ngày làm việc tiếp theo

{Thời gian làm việc trong ngày} được cấu hình tại tham số LOAN_WORKTIME_DAY tại bảng cấu hình tham số

 | 
9
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bấm Tiếp tục mở đến MH Xác nhận giao dịch <Tham khảo logic xử lý>

 | 
10
 | 
Nút “Back”
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Back hiển thị màn hình đang thao tác trước đó.

##### MH3.2: <Điều khoản & điều kiện >
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Điều khoản & điều kiện 

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình Trang chủ

 | 4 | 
Nội dung
 | 
html
 | 
ReadOnly
 | -- | -- | 
Hiển thị nội dung đã mô tả

##### MH4: <Xác nhận giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó và giữ nguyên giá trị đã nhập

 | 2 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | 
Câu thông báo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 5 | 
Tài khoản vay
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 

 | 6 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
---
 | 
Hiển thị số tiền và đơn vị tiền tệ. Số tiền viết bằng chữ tương ứng (bôi đỏ)

 | 7 | 
Phí giao dịch và thuế
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ (Nếu có)

 | 8 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 9 | 
Phương thức xác thực
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 10 | 
Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bấm Tiếp tục mở đến MH Xác thực giao dịch <Tham khảo logic xử lý>

##### MH5: <Xác thực giao dịch>

Xem xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH6: <Kết quả giao dịch>
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Kết quả giao dịch

 | 
3
 | 
Logo Bank
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tạo lệnh thanh toán khoản vay thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền- VND

 | 
7
 | 
Thời gian giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
 | 
Số tài khoản
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tài khoản vay

 | 
9
 | 
Mã giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
10
 | 
Phí giao dịch và thuế
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị (nếu có)

 | 
11
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 
12
 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở lại màn hình khởi tạo Tạo lệnh thanh toán khoản vay và Clear hết các thông tin của giao dịch trước

 | 
13
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
14
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

### 4/ Luồng xử lý

##### MH: <Truy cập chức năng>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Truy cập từ Home
 | 
1
 | 
Chọn chức năng "Khoản vay" 
 | MB Client | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Không hợp lệ: Danh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

• Hợp lệ:
Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Mở đến màn hình "Tạo lệnh thanh toán khoản vay" như đã mô tả

 | 
2
 | 
Chọn chức năng "Tạo lệnh trả nợ vay chính chủ"
 | MB Client | 
• Gửi yêu cầu lấy danh sách tài khoản thanh toán
• Gửi yêu cầu lấy danh sách tài khoản vay
• Lấy danh sách cấu hình tại bảng Cấu hình tham số cho chức năng VAY (Tới Backend MB)
 | 
 | 
 | MB server | 
• Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán tới Bank server
• Nhận và gửi yêu cầu lấy danh sách tài khoản Vay tới Bank server
 | 

 | 

 | Bank server | Xử lý và phản hồi lại MB server
 | 

 | 

 | MB server | Nhận và gửi phản hồi lại Client
 | 

 | 

 | MB Client | 
Nhận phản hồi:

• Không thành công → Chuyển màn hình khởi tạo và cho phép lấy lại danh sách tài khoản thanh toán và tài khoản Vay
• Thành công
- Không có tài khoản
 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán) | 
Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình hiện tại.
 | 2 | Trường hợp không có tài khoản Vay | 
Quý khách không có khoản vay tại Co-opBank. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

- Có tài khoản thanh toán + Vay→ Chuyển màn hình Khởi tạo

##### MH1: <Khởi tạo>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn Tài khoản nguồn | 
MB Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó
Mặc định hiển thị tài khoản thanh toán mặc định.

Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.

• Chưa thành công: Gửi yêu cầu lấy lại danh sách tài khoản thanh toán đến MB server
 | 
 | 
 | MB Server | Gửi yêu cầu lấy lại danh sách tài khoản thanh toán 
 | 
 | 
 | 
HT Bank
 | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản

Trả kết quả cho MB Server

 | 
 | 
 | MB Server | 
Trả kết quả cho Client

• Không thành công: Trả kết quả lỗi tương ứng
• Thành công:   Trả kết quả danh sách tài khoản thanh toán hợp lệ
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản thanh toán | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công: Hiển thị danh sách các tài khoản thanh toán do server trả về
• TimeOut: Hiển thị MH popup thông báo lỗi tương ứng
 | 2 | Chọn 1 tài khoản nguồn | 
MB Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 3 | Chọn Tài khoản vay | 
MB Client
 | 
Kiểm tra đã lấy danh sách tài khoản Vay trước đó thành công chưa?

• Đã lấy thành công trước đó
Mặc định hiển thị tài khoản Vay đầu tiên trong danh sách Bank trả về

• Chưa thành công: Gửi yêu cầu lấy lại danh sách tài khoản Vay đến MB server
 | 
 | 
 | MB Server | Gửi yêu cầu lấy lại danh sách tài khoản Vay
 | 
 | 
 | 
HT Bank
 | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản Vay

Trả kết quả cho MB Server

 | 
 | 
 | MB Server | 
Trả kết quả cho Client

• Không thành công: Trả kết quả lỗi tương ứng
• Thành công:   Trả kết quả danh sách tài khoản Vay
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản Vay | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công
- Không có tài khoản Vay
 | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 2 | Trường hợp không có tài khoản Vay | 
Quý khách không có dư nợ cần thanh toán tại Co-opBank. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

- Có tài khoản Vay: Hiển thị mặc định tài khoản vay đầu tiên trong danh sách Bank trả về

• TimeOut: Hiển thị MH popup thông báo lỗi tương ứng
 | 
4

 | 
Chọn 1 tài khoản Vay
 | 
MB Client
 | 
Fill thông tin vào ô tài khoản Vay  bao gồm:

•  Số tài khoản Vay
•  Dư nợ gốc + đơn vị tiền tệ VND
• Các thông tin khoản vay như đã mô tả
 | 
5
 | 
Nhập thông tin Số tiền
 | 
MB Client
 | 
Kiểm tra cấu hình Số tiền tối thiểu

• Không hợp lệ | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Số tiền trả nợ nhỏ hơn số tiền tối thiểu | 
Số tiền trả nợ tối thiểu là [n] VND. Quý khách vui lòng kiểm t

> ⚠️ *Nội dung đã cắt ngắn (19212 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 31.3. MB_Tạo lệnh trả nợ vay theo địa bàn

> **Page ID:** `85921700` · **Version:** 9
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/85921700

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | 

Mục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
Tác nhân, điều kiện, kết quả mong muốn

 | 1. Mục đích chức năng: | 
Tạo lệnh trả nợ vay theo địa bàn

 | 2. Tác nhân tham gia: | 
App, MB Server, HT Bank

 | 3. Điều kiện trước: | 
• KH đăng nhập thành công vào hệ thống Mobile banking
• KH thuộc gói dịch vụ được phép sử dụng chức năng này.
• KH có tài khoản nguồn hợp lệ để thực hiện chức năng này
• KH đã được Ngân hàng cung cấp Số hợp đồng, Địa bàn vay hoặc Số bảng kê của khoản vay
 | 4. Kết quả mong muốn: | 
• Tạo lệnh trả nợ vay theo địa bàn thành công
• Tài khoản thanh toán của khách hàng bị trừ số tiền tương ứng với số tiền trả nợ trong lệnh

### 2/ Luồng sơ đồ

### 3/ Luồng màn hình

#### Danh sách màn hình

MH1: <Trang chủ>

MH2: <Khoản vay>

MH3: <Tạo lệnh trả nợ vay theo địa bàn>

MH4: <Xác nhận giao dịch>

MH5: <Xác thực giao dịch>

MH6: <Kết quả giao dịch>

MH 3.1 Chọn Chi nhánh/ PGD

MH3.2 Điều kiện, điều khoản

#### Mô tả màn hình

##### MH1: <Trang chủ>

Bổ sung thêm chức năng "Khoản vay" tại nhóm chức năng Tài chính

##### MH2: <Khoản vay>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Tạo lệnh thanh toán khoản vay chính chủ
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 2 | 
Tạo lệnh trả nợ vay theo địa bàn
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 3 | 
Danh sách khoản vay chính chủ
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 4 | 
Danh sách tạo lệnh thanh toán khoản vay
 | 
Icon
 | 
Click
 | 

 | 

 | Click vào icon mở đến chức năng tương ứng
 | 5 | 
Icon Back
 | 
Icon
 | 
Click
 | 

 | 

 | Về màn hình trước đó

##### MH3: <Tạo lệnh trả nợ vay theo địa bàn>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề màn hình
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Tạo lệnh trả nợ vay theo địa bàn

 | 
2
 | 
Tài khoản nguồn
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định hiển thị tài khoản thanh toán mặc định
• Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.
• Hiển thị số tài khoản + Số dư tương ứng và đơn vị tiền tệ.
• (Số dư = Số dư khả dụng - Hạn mức thấu chi được cấp cho KH)
• Click vào mở ra màn hình popup “Danh sách tài khoản nguồn”, chọn tài khoản (Tại popup chọn tài khoản, nếu tài khoản là mặc định sẽ hiển thị thêm label nhận biết. Định dạng: số tài khoản - Tài khoản mặc định)
 | 
Thông tin khoản vay

 | 
2
 | 
Chi nhánh/ ĐGD
 | 
Listbox
 | 
Select
 | 
Yes
 | 
--
 | 
• Mặc định trống
• Click vào mở ra màn hình Popup “Danh sách Chi nhánh/ ĐGD”. Giá trị hiển thị trong danh sách được lấy tại BE , bao gồm:
         -  Type : PGD và CN. Hiển thị theo cấu trúc PGD- CN (Không lấy ATM)

         - Các điểm giao dịch có thông tin bổ sung khác N (trường POSDEL_CONTACT thuộc bảng cm_pos_detail) (Không lấy các điểm giao dịch có thông tin bổ sung = N)

• Cho phép tìm kiếm tương đối chi nhánh trong Popup danh sách chi nhánh/ ĐGD
• Cho phép chọn 1 giá trị
• Sắp xếp theo mã ĐGD từ A→ Z 
 | 
2
 | 
Địa bàn vay hoặc Số bảng kê
 | 
Textbox
 | 
Text
 | 

 | 
50
 | 
• 
Mặc định trống. Cho phép nhập ký tự số và chữ, không chặn ký tự đặc biệt.

• 
Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập

 | 
3
 | 
Số hợp đồng/ Tài khoản vay
 | 
Textbox
 | 
Text
 | 

 | 
50
 | 
• Mặc định trống. Cho phép nhập ký tự số và chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
 | 
4
 | 
Số tiền
 | 
Textbox
 | 
Number
 | 
Yes
 | 
15
 | 
• Chỉ cho nhập ký tự số, tối đa 15 ký tự (bao gồm cả dấu phẩy). Không nhập số bắt đầu bằng số 0
• Hiển thị ngăn cách hàng nghìn bằng dấu “,”
• Hiển thị đơn vị tiền tệ mặc định “VND”
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
Backend cho phép thiết lập số tiền trả nợ vay tối thiểu. Khi thực hiện giao dịch => check số tiền đã nhập với số tiền tối thiểu đã set trong BE

Nếu nhập số tiền nhỏ hơn số tiền tối thiểu => hệ thống hiển thị cảnh báo “Số tiền trả nợ tối thiểu là {n} VND. Quý khách vui lòng kiểm tra lại!” 

Có gợi ý số tiền chuyển. Quy tắc gợi ý → Tham khảo logic xử lý

 | 
5
 | 
Ghi chú
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Hiển thị thông báo số tiền tối thiểu ở phía dưới trường số tiền

"Số tiền trả nợ tối thiểu là {n} VND "

{n} được cấu hình tại tham số LOAN_AMOUNT_MIN tại bảng cấu hình tham số

 | 
6
 | 
Nội dung giao dịch
 | 
Textbox
 | 
Text
 | 
Yes
 | 
210
 | 
• Mặc định: Ten Khach hang + tra no vay + hop dong/ tai khoan+ thông tin đã nhập vào trường "Số hợp đồng/Tài khoản vay" (Nếu không nhập số hợp đồng / tài khoản vay thì bỏ trống, khi nào nhập thì app lại tự động fill vào)
• Cho phép sửa, nhập số, chữ không dấu, bao gồm cả dấu cách và các ký tự đặc biệt là -/():
• Hiển thị [số ký tự nhập]/[số ký tự tối đa] là 210 kí tự
• Hiển thị nút "x" cho phép xóa toàn bộ ký tự đã nhập
 | 
7
 | 
Điều khoản & Điều kiện
 | 
Checkbox
 | 
Click
 | 
Yes
 | 
--
 | 
• Mặc định tích chọn, cho phép bỏ chọn/tích chọn. 
• Trường hợp KH chưa tick chọn:  Hiển thị popup thông báo:"Quý khách chưa đồng ý với Điều khoản, điều kiện sử dụng dịch vụ tạo lệnh thanh toán khoản vay của Co-opbank Mobile Banking."
• Hiển thị nội dung "Tôi đã đọc, hiểu rõ, đồng ý và cam kết tuân thủ các Điều khoản, điều kiện sử dụng dịch vụ tạo lệnh trả nợ vay trên ứng dụng Mobile Banking của Co-opbank. "
• Click vào Điều kiện, điều khoản mở đến MH3.1 : <Điều khoản & điều kiện >
 | 
8
 | 
Ghi chú
 | 
Label
 | 
Readonly
 | 

 | 

 | 
Co-opBank xin trân trọng thông báo đến Quý khách thời gian trả nợ vay trong ngày là trước [17:00] các ngày làm việc. Những giao dịch ngoài thời gian trên hoặc vào ngày nghỉ, lễ tết sẽ được ghi nhận vào ngày làm việc tiếp theo

{Thời gian làm việc trong ngày} được cấu hình tại tham số LOAN_WORKTIME_DAY tại bảng cấu hình tham số

 | 
9
 | 
Tiếp tục
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bấm Tiếp tục mở đến MH Xác nhận giao dịch <Tham khảo logic xử lý>

 | 
10
 | 
Nút “Back”
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Back hiển thị màn hình đang thao tác trước đó.

##### MH3.2: <Điều khoản & điều kiện >
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 1 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | -- | -- | 
Tiêu đề: Điều khoản & điều kiện 

 | 2 | 
Icon Back
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó với các giá trị giữ nguyên.

 | 3 | 
Icon Home
 | 
Icon
 | 
Click
 | -- | -- | 
Nhấn Home, hiển thị màn hình Trang chủ

 | 4 | 
Nội dung
 | 
html
 | 
ReadOnly
 | -- | -- | 
Hiển thị nội dung đã mô tả

##### MH4: <Xác nhận giao dịch>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó và giữ nguyên giá trị đã nhập

 | 2 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Xác nhận giao dịch

 | 3 | 
Câu thông báo
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo

 | 4 | 
Tài khoản nguồn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Tài khoản nguồn đã chọn

 | 5 | 
Chi nhánh quản lý
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Chi nhánh quản lý đã nhập

 | 6 | 
Địa bàn/ Số bảng kê
 | 
Label
 | 
ReadOnly
 | 
--
 | 
---
 | 
Hiển thị Địa bàn vay/ Số bảng kê đã nhập (Nếu có) (bôi đỏ)

 | 7 | 
Số hợp đồng/TK vay
 | 
Label
 | 
ReadOnly
 | 
--
 | 
---
 | 
Hiển thị Số hợp đồng/Tài khoản vay đã nhập (Nếu có) (bôi đỏ)

 | 8 | Số tiền | 
Label
 | 
ReadOnly
 | 
--
 | 
---
 | Hiển thị số tiền và đơn vị tiền tệ. Số tiền viết bằng chữ tương ứng (bôi đỏ)
 | 9 | 
Phí giao dịch và thuế
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị số tiền và đơn vị tiền tệ (Nếu có)

 | 10 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 11 | 
Phương thức xác thực
 | 
Combobox
 | 
Select
 | 
Yes
 | 
--
 | 
Danh sách phương thức xác thực do MB server trả về

Mặc định phương thức xác thực cao nhất.

Chỉ được chọn 1 phương thức xác thực

 | 12 | 
Xác nhận
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Bấm Tiếp tục mở đến MH Xác thực giao dịch <Tham khảo logic xử lý>

##### MH5: <Xác thực giao dịch>

Xem xác thực giao dịch theo PTXT URD_MB_HẠN MỨC, PHƯƠNG THỨC XÁC THỰC (GÓI 2)

##### MH6: <Kết quả giao dịch>
 | | 
TT
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu dữ liệu
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Kết quả giao dịch

 | 
3
 | 
Logo Bank
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Logo Co-opBank

 | 
4
 | 
Icon thành công
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon giao dịch thành công

 | 
5
 | 
Tiêu đề
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Tạo lệnh thanh toán khoản vay thành công

 | 
6
 | 
Số tiền
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Số tiền- VND

 | 
7
 | 
Thời gian giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị theo định dạng dd/mm/yyyy hh:mm

 | 
8
 | Chi nhánh quản lý | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | Hiển thị Chi nhánh quản lý đã chọn
 | 
9
 | 
Địa bàn vay / Số bảng kê
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Địa bàn vay/ Số bảng kê đã nhập (Nếu có)

 | 
10
 | 
Số hợp đồng/TK vay
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị Địa bàn vay/ Số bảng kê đã nhập (Nếu có)

 | 
11
 | 
Mã giao dịch
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị thông tin mã giao dịch

 | 
12
 | 
Phí giao dịch và thuế
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị (nếu có)

 | 
13
 | 
Nội dung
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị nội dung giao dịch

 | 
14
 | 
Tạo giao dịch mới
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Trở lại màn hình khởi tạo Tạo lệnh trả nợ vay theo địa bàn và Clear hết các thông tin của giao dịch trước

 | 
15
 | 
Nhấn Icon lưu ảnh
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

 | 
16
 | 
Nhấn Nút chia sẻ
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Tham khảo tại Logic xử lý chung

### 4/ Luồng xử lý

##### MH: <Truy cập chức năng>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | Truy cập từ Home
 | 
1
 | 
Chọn chức năng "Tạo lệnh thanh toán khoản vay" 
 | MB Client | 
Kiểm tra quyền sử dụng dịch vụ của khách hàng:

• Không hợp lệ: Danh sách lỗi

 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Nếu dịch vụ được chọn không thuộc gói dịch vụ của khách hàng | Gói dịch vụ của Quý khách không bao gồm dịch vụ này. Quý khách vui lòng đến quầy giao dịch gần nhất để cập nhật thêm dịch vụ | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

• Hợp lệ:
Nếu dịch vụ được chọn thuộc gói dịch vụ của khách hàng  → Mở đến màn hình "Tạo lệnh thanh toán khoản vay" như đã mô tả

 | 
2
 | 
Chọn chức năng "Tạo lệnh trả nợ vay theo địa bàn"
 | MB Client | 
• Gửi yêu cầu lấy danh sách tài khoản thanh toán
• Lấy danh sách cấu hình tại bảng Cấu hình tham số cho chức năng VAY (Tới Backend MB)
 | 
 | 
 | MB server | 
• Nhận và gửi yêu cầu lấy danh sách tài khoản thanh toán tới Bank server
 | 

 | 

 | Bank server | Xử lý và phản hồi lại MB server
 | 

 | 

 | MB server | Nhận và gửi phản hồi lại Client
 | 

 | 

 | MB Client | 
Nhận phản hồi:

• Không thành công → Chuyển màn hình khởi tạo và cho phép lấy lại danh sách tài khoản thanh toán
• Thành công
- Không có tài khoản
 | 
 | Trường hợp | Nội dung thông báo | Xử lý (nếu có)
 | 1 | Trường hợp không có tài khoản thanh toán (đã tất toán hết tài khoản thanh toán) | 
Quý khách không có tài khoản thanh toán để thực hiện giao dịch. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

- Có tài khoản thanh toán → Chuyển màn hình Khởi tạo

##### MH1: <Khởi tạo>
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn Tài khoản nguồn | 
MB Client
 | 
Kiểm tra đã lấy danh sách tài khoản thanh toán thành công chưa?

• Đã lấy thành công trước đó
Mặc định hiển thị tài khoản thanh toán mặc định.

Nếu không có tài khoản thanh toán mặc định (đã tất toán tài khoản thanh toán mặc định) sẽ hiển thị tài khoản thanh toán VND đầu tiên trong danh sách do bank Server trả về.

• Chưa thành công: Gửi yêu cầu lấy lại danh sách tài khoản thanh toán đến MB server
 | 
 | 
 | MB Server | Gửi yêu cầu lấy lại danh sách tài khoản thanh toán 
 | 
 | 
 | 
HT Bank
 | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản

Trả kết quả cho MB Server

 | 
 | 
 | MB Server | 
Trả kết quả cho Client

• Không thành công: Trả kết quả lỗi tương ứng
• Thành công:   Trả kết quả danh sách tài khoản thanh toán hợp lệ
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản thanh toán | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công: Hiển thị danh sách các tài khoản thanh toán do server trả về
• TimeOut: Hiển thị MH popup thông báo lỗi tương ứng
 | 2 | Chọn 1 tài khoản nguồn | 
MB Client
 | 
Fill thông tin vào ô tài khoản nguồn bao gồm:

•  Số tài khoản
•  Số dư khả dụng + đơn vị tiền tệ VND
 | 3 | Chọn Chi nhánh quản lý | 
MB Client
 | 
Hiển thị danh sách chi nhánh quản lý đã lấy từ BE trước đó bao gồm Mã chi nhánh và Tên chi nhánh

 | 
4
 | 
Nhập thông tin Số tiền
 | 
MB Client
 | 
Kiểm tra cấu hình Số tiền tối thiểu

• Không hợp lệ | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Số tiền trả nợ nhỏ hơn số tiền tối thiểu | 
Số tiền trả nợ tối thiểu là [n] VND. Quý khách vui lòng kiểm tra lại
 | n cấu hình tại Backend

• Hợp lệ: Cho phép thực hiện các bước tiếp theo
 | 
5
 | 
Bấm nút Tiếp tục
 | 
MB Client
 | 
Kiểm tra validate thông tin

• Không hợp lệ | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Bỏ trống thông tin bắt buộc | 
[Tên trường ] không được bỏ trống. Quý khách vui lòng kiểm tra lại
 | Tắt thông báo giữa nguyên màn hình
 | 2 | Chưa tích chọn Điều kiện , điều khoản | 
Quý khách chưa đồng ý với Điều khoản, điều kiện sử dụng dịch vụ tạo lệnh thanh toán khoản vay của Co-opbank Mobile Banking."
 | Tắt thông báo giữa nguyên màn hình
 | 3 | Số tiền giao dịch > (Số dư khả dụng - Hạn mức thấu chi được cấp) | 
Giao dịch không thành công do số dư không đủ. Quý khách vui lòng kiểm tra lại!
 | Tắt thông báo giữa nguyên màn hình

• Hợp lệ: Gửi yêu cầu Khởi tạo giao dịch tới MB Server
 | 

 | 

 | 
MB Server
 | 
Tiếp nhận yêu cầu Khởi tạo giao dịch và Kiểm tra hạn mức gói dịch theo loại giao dịch tương ứng và tính phí giao dịch. → Tham khảo logic xử lý tính hạn mức và phí giao dịch tại Logic kiểm tra PTXT

 | 

 | 

 | 
MB Client
 | 
Nhận kết quả phản hồi từ MB server :

• Không hợp lệ:

> ⚠️ *Nội dung đã cắt ngắn (18077 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 31.4. MB_ Danh sách khoản vay chính chủ

> **Page ID:** `85922125` · **Version:** 5
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/85922125

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | 

Mục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
Tác nhân, điều kiện, kết quả mong muốn

 | 1. Mục đích chức năng: | 
Quản lý các khoản vay hiện có của khách hàng

 | 2. Tác nhân tham gia: | 
App, MB Server, HT Bank

 | 3. Điều kiện trước: | 
• KH đăng nhập thành công vào hệ thống Mobile banking
• KH có khoản vay chưa tất toán tại ngân hàng
 | 4. Kết quả mong muốn: | 
• KH xem được các khoản vay của mình tại ngân hàng

### 2/ Luồng sơ đồ

### 3/ Luồng màn hình

#### Danh sách màn hình

MH1: <Khoản vay>

MH2: <Danh sách khoản vay chính chủ>

MH3.1: <Popup sắp xếp danh sách khoản vay>

#### Mô tả màn hình

##### MH1: <Tài khoản> (Cập nhật)

Bổ sung thêm một số thông tin khoản vay trong danh sách vay đã triển khai tại Phase 1. Mô tả thay đổi so với phase 1 tại <>

##### MH2: <Danh sách khoản vay chính chủ>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon Back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Nhấn Back, hiển thị màn hình đang thao tác trước đó

 | 
2
 | 
Tiêu đề 
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Danh sách khoản vay chính chủ

 | 
3
 | 
Icon "Sắp xếp"
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Hiển thị icon sắp xếp nếu từ 3 tài khoản Vay trở lên: Cho phép sắp xếp tài khoản vay theo các tiêu chí:

- Ngày giải ngân gần nhất

- Ngày đáo hạn gần nhất

- Dư nợ tăng dần

- Dư nợ giảm dần

 | 
4
 | 
Tổng số dư nợ gốc hiện tại
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Dữ liệu Bank trả (trường totalBal)
• Là tổng số dư nợ của tất cả các khoản vay hiện có
 | Mỗi tài khoản vay sẽ có các thông tin như sau
 | 
1
 | 
Số tài khoản
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Dữ liệu Bank trả (trường accountType)
 | 
5
 | 
Ngày giải ngân
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Dữ liệu Bank trả
 | 
6
 | 
Ngày đáo hạn
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Dữ liệu Bank trả
 | 
7
 | 
Số dư nợ gốc hiện tại
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
• Dữ liệu Bank trả
• Hiển thị Số tiền + VND

### 4/ Luồng xử lý

Màn hình danh sách khoản vay chính chủ
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn Danh sách khoản vay chính chủ | 
MB Client
 | 
Kiểm tra đã lấy danh sách tài khoản Vay trước đó thành công chưa?

• Đã lấy thành công trước đó
Hiển thị danh sách tài khoản vay theo thứ tự Bank trả về.

• Chưa thành công: Gửi yêu cầu lấy lại danh sách tài khoản Vay đến MB server
 | 
 | 
 | MB Server | Gửi yêu cầu lấy lại danh sách tài khoản Vay
 | 
 | 
 | 
HT Bank
 | 
Nhận yêu cầu và truy vấn lấy danh sách tài khoản Vay

Trả kết quả cho MB Server

 | 
 | 
 | MB Server | 
Trả kết quả cho Client

• Không thành công: Trả kết quả lỗi tương ứng
• Thành công:   Trả kết quả danh sách tài khoản Vay
 | 
 | 
 | MB Client | 
Nhận kết quả:

• Không thành công | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 1 | Không lấy được danh sách tài khoản Vay | Không lấy được danh sách tài khoản. Quý khách vui lòng thử lại | Hiển thị Button Thử lại và Đóng trên thông báo. Sau khi nhấn Thử lại gọi lấy lại danh sách tài khoản.

• Thành công
- Không có tài khoản Vay
 | 
TT
 | 
Trường hợp lỗi
 | 
Nội dung 
 | 
Xử lý (nếu có)

 | 2 | Trường hợp không có tài khoản Vay | 
Quý khách không có khoản vay tại Co-opBank. Vui lòng kiểm tra lại
 | Đóng câu thông báo, giữ nguyên màn hình hiện tại.

- Có tài khoản Vay: Hiển thị danh sách tài khoản vay.

• TimeOut: Hiển thị MH popup thông báo lỗi tương ứng
 | 
2
 | 
Nhấn Back
 | 
Client MB
 | 
Hiển thị màn hình đang thao tác trước đó.

 | 
3
 | 
Nhấn Chọn 1 tài khoản vay
 | 
Client MB
 | 
Gửi yêu cầu lấy chi tiết tài khoản được yêu cầu 

Hiển thị màn hình chi tiết tài khoản < Giữ nguyên màn hình thông tin chi tiết tài khỏan vay tại phase 1

---

### 31.5. MB_ Danh sách tạo lệnh thanh toán khoản vay

> **Page ID:** `85922434` · **Version:** 6
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/85922434

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | 

Mục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
Tác nhân, điều kiện, kết quả mong muốn

 | 1. Mục đích chức năng: | 
Quản lý các lệnh thanh toán khoản vay do KH thực hiện thanh toán trên Mobile banking

 | 2. Tác nhân tham gia: | 
App, MB Server, HT Bank

 | 3. Điều kiện trước: | 
• KH đăng nhập thành công vào hệ thống Mobile banking
• KH đã tạo lệnh thanh toán khoản vay trên kênh Mobile banking
 | 4. Kết quả mong muốn: | 
• KH xem chi tiết lệnh và trạng thái thu nợ tại Bank

### 2/ Luồng sơ đồ

### 3/ Luồng màn hình

#### Danh sách màn hình

MH1: <Khoản vay>

MH2: <Danh sách tạo lệnh thanh toán khoản vay>

MH3 <Danh sách tạo lệnh thanh toán khoản vay>-Kết quả tra cứu

MH4.1: <Chi tiết giao dịch> Loại thanh toán vay chính chủ

MH4.2: <Chi tiết giao dịch> Loại thanh toán vay theo địa bàn

#### Mô tả màn hình

##### MH1: Khoản vay

##### MH2: Danh sách tạo lệnh thanh toán khoản vay
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Danh sách tạo lệnh thanh toán khoản vay

 | 
2
 | 
Nút back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
4
 | 
Tra cứu danh sách
 | 
Label
 | 
ReadOnly
 | 

 | 

 | 

 | 
5
 | 
Ghi chú
 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Fix tại Client:

Danh sách chỉ bao gồm các giao dịch trên ứng dụng Co-opBank Mobile Banking

 | 
6
 | 
Tài khoản tra cứu
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
• Giá trị hiển thị là danh sách tài khoản thanh toán của khách hàng, sắp xếp theo thứ tự Bank trả về
• Mặc định: Là tài khoản thanh toán mặc định
 | 
7
 | 
Loại giao dịch
 | 
Combobox
 | 
Select
 | 
--
 | 
--
 | 
• Mặc định: Tất cả
• Bao gồm: Tất cả, Tạo lệnh thanh toán khoản vay chính chủ, Tạo lệnh thanh toán khoản vay theo địa bàn
• Cho phép chọn 1 giá trị
 | 
8
 | 
Từ ngày
 | 
Calendar
 | 
Textbox
 | 
--
 | 
--
 | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Từ ngày phải nhỏ hơn hoặc bằng Đến ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 1 năm

Định dạng dd/MM/yyyy

Mặc định ngày hiện tại của tháng T-6

 | 
9
 | 
Đến ngày
 | 
Calendar
 | 
Textbox
 | 
--
 | 
--
 | 
Chỉ cho chọn những ngày trong quá khứ đến ngày hiện tại

Đến ngày phải lớn hơn hoặc bằng Từ ngày

Khoảng thời gian tìm kiếm: Từ ngày... đến ngày không được quá 1 năm so với ngày hiện tại

Định dạng dd/MM/yyyy

Mặc định ngày hiện tại

 | 
10
 | 
Tìm kiếm
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo logic xử lý>

##### MH3 <Danh sách tạo lệnh thanh toán khoản vay>-Kết quả tra cứu lệnh
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Danh sách tạo lệnh thanh toán khoản vay

 | 
2
 | 
Nút back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
4
 | 
Danh sách giao dịch
 | 
List
 | 
View
 | 
--
 | 
--
 | 
• Hiển thị Ngày và thời gian giao dịch theo định dạng: Định dạng hiển thị dd/mm/yyyy hh:mm
• Nội dung giao dịch: Hiển thị cắt chuỗi trong nội dung giao dịch (Hiển thị đảm bảo trên 1 dòng dữ liệu, dữ liệu thiếu hiển thị bằng dấu “…”)
• Số tiền giao dịch: Tương ứng với số tiền thực hiện trong giao dịch.
• Hiển thị danh sách các giao dịch sắp xếp dữ liệu mới nhất lên đầu. Phân trang 10 bản ghi/ trang, cho phép KH xem dữ liệu dạng loadmore
• Khi nhấn vào 1 giao dịch bất kì, hiển thị màn hình chi tiết lệnh tương ứng với loại giao dịch
• Trường hợp không có giao dịch nào, hiển thị label thông báo: Không có giao dịch nào gần đây
 | 

 | 
Ô textsearch
 | 
Textbox
 | 
Text
 | 
--
 | 
200
 | 
• 
Mặc định trống

• 
Cho phép tìm kiếm gần đúng theo: Mã giao dịch, Nội dung giao dịch, Số tiền

• Nếu kết quả tìm kiếm không có dữ liệu: hiển thị thông báo "Không tìm thấy kết quả."
• Nếu kết quả tìm kiếm có dữ liệu hiển thị theo tab dữ liệu tương ứng.
• Chỉ hiển thị khi có trên n bản ghi (xem tại Quy tắc chung)

##### MH4.1: <Chi tiết lệnh> Loại thanh toán vay chính chủ
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Chi tiết giao dịch

 | 
2
 | 
Nút back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
4
 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 5 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 6 | 
Tài khoản nguồn
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 7 | 
Tài khoản vay
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 8 | 
Chi nhánh mở
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 9 | 
Số tiền
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 10 | 
Nội dung giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 11 | 
Loại giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Tạo lệnh thanh toán khoản vay chính chủ

 | 12 | 
Trạng thái thu nợ
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Do Bank trả về, bao gồm:

• Đã thu: Bôi đậm text màu đen
• Đã hoàn: Bôi đậm, text màu xanh
• Chưa thu: Bôi đậm, text màu đỏ

##### MH4.2: <Chi tiết lệnh> Loại thanh toán vay theo địa bàn
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Chi tiết giao dịch

 | 
2
 | 
Nút back
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
3
 | 
Icon Home
 | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình trang chủ

 | 
4
 | 
Mã giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
5
 | 
Ngày giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
6
 | 
Tài khoản nguồn
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
7
 | 
Chi nhánh quản lý
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
8
 | 
Địa bàn vay/ Số bảng kê
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
9
 | 
Số hợp đồng/TK vay
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
10
 | 
Số tiền
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
11
 | 
Nội dung giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 

 | 
12
 | 
Loại giao dịch
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Tạo lệnh thanh toán khoản vay theo địa bàn

 | 
13
 | 
Trạng thái thu nợ
 | 
Label
 | 
Readonly
 | 
--
 | 
--
 | 
Do Bank trả về, bao gồm:

• Đã thu: Bôi đậm text màu đen
• Đã hoàn: Bôi đậm, text màu xanh
• Chưa thu: Bôi đậm, text màu đỏ

### 4/ Luồng xử lý

##### Màn hình danh sách tạo lệnh và tra cứu
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Chọn Danh sách tạo lệnh khoản vay | 
MB Client
 | 
Hiển thị màn hình Danh sách tạo lệnh thanh toán khoản vay như đã mô tả

 | 
2
 | 
Bấm chọn Tài khoản tra cứu
 | 
MB Client
 | 
Hiển thị popup danh sách các tài khoản thanh toán VND

 | 
2
 | 
Bấm chọn Loại giao dịch
 | 
MB Client
 | 
Hiển thị thông tin và giá trị như đã mô tả

 | 
4
 | 
Bấm chọn Từ ngày
 | 
MB Client
 | 
Hiển thị lịch cho phép chọn và cho phép chọn 1 giá trị ngày trong lịch.

Định dạng hiển thị sau khi chọn: dd/mm/yyyy

 | 
5
 | 
Bấm chọn Đến ngày
 | 
MB Client
 | 
Hiển thị lịch cho phép chọn và cho phép chọn 1 giá trị ngày trong lịch.

Định dạng hiển thị sau khi chọn: dd/mm/yyyy

 | 
6
 | 
Nhấn "Tìm kiếm"

 | 
MB Client
 | 
Kiểm tra thông tin tại màn hình:

• Không hợp lệ: hiển thị thông báo lỗi tương ứng:
• Từ ngày > Đến ngày: "Từ ngày phải nhỏ hơn hoặc bằng Đến ngày. Quý khách vui lòng chọn lại thời gian tra cứu.". Đóng câu thông báo, giữ nguyên màn hình hiện tại, ko reset các giá trị đã chọn.
• Tài khoản tra cứu trống: "Danh sách tài khoản tra cứu trống, vui lòng thử lại". Đóng câu thông báo, xử lý điều hướng về màn hình home
• Khoảng thời gian tìm kiếm lớn hơn 1 năm (tính theo thời gian trên lịch): "Quý khách vui lòng nhập khoảng thời gian nhỏ hơn 01 năm!". Đóng câu thông báo, giữ nguyên màn hình hiện tại, ko reset các giá trị đã chọn.
• Hợp lệ: gửi yêu cầu sang MB Server lấy thông tin giao dịch theo điều kiện tìm kiếm và điều kiện phân trang (hiển thị 10 giao dịch 1 trang)
 | 
MB Server
 | 
Truy vấn và tìm kiếm giao dịch theo điều kiện KH đã chọn

 | 
MB Client
 | 
Nhận kết quả:

• Có kết quả: hiển thị màn hình kết quả tìm kiếm giao dịch
• Không có kết quả: hiển thị thông báo do Server trả về: "Không có giao dịch phát sinh trong khoảng thời gian tra cứu. Quý khách vui lòng thử lại với các điều kiện tìm kiếm phù hợp". Đóng câu thông báo, giữ nguyên màn hình tìm kiếm.
 | 

 | 

 | 
MB Client
 | 
Click vào 1 giao dịch tại danh sách, gửi yêu cầu lấy chi tiết giao dịch tới MB Server

 | 

 | 

 | 
MB Server
 | 
Tiếp nhận yêu cầu và gửi yêu cầu lấy chi tiết lệnh tới HT Bank

 | 

 | 

 | 
HT Bank
 | 
Xử lý và trả kết quả cho MB Server

 | 

 | 

 | 
MB Server
 | 
Trả kết quả cho MB Client

 | 

 | 

 | 
MB Client
 | 
Nhận kết quả:

• Không thành công: Hiển thị thông báo lỗi nhận được
• Thành công: Hiển thị màn hình chi tiết lệnh tương ứng với loại giao dịch đã chọn
 | 

 | 

 | 

 | 

##### Màn hình chi tiết lệnh
 | | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Nhập dữ liệu vào ô tìm kiếm | MB Client | Tìm kiếm gần đúng các giao dịch theo Nội dung giao dịch, Loại giao dịch
 | 3 | 
Vuốt lên để xem giao dịch tiếp theo (Load more)
 | 
MB Client
 | 
Gửi yêu cầu lấy 10 giao dịch tiếp theo sang MB Server và nhận kết quả hiển thị tiếp các giao dịch phía dưới cho đến khi lấy hết.

 | 4 | 
Nhấn 1 giao dịch
 | 
MB Client
 | 
Hiển thị màn hình thông tin chi tiết lệnh theo đúng mô tả

---



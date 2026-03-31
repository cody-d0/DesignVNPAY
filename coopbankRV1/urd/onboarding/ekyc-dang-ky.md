# 📋 eKYC & Đăng ký

> **Nguồn:** Confluence wiki.servicehub.vn · Space: URDMBCOOPBANK
> **Phân loại:** `onboarding/`
> **Trích xuất:** 2026-03-28

---

## 12. URD_ĐĂNG KÝ MỞ CIF/TKTT/ MB (eKYC)

> **Page ID:** `129926233` · **Version:** 4
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/129926233

*Trang trống hoặc chỉ chứa macro/hình ảnh.*


---

*7 trang con:*

### 12.1. SOW chức năng eKYC đăng ký mở CIF/TKTT/MB

> **Page ID:** `129926287` · **Version:** 19
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/129926287

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 

 | A | HongLT | 
 | 
Tạo mới
 | V.1.0
 | 
 
 | M | HongLT | 
 | 
Cập nhật: 

• Phạm vi: App fix chỉ cho phép đăng ký eKYC với loại giấy tờ = CCCD Chip
 (Không cho phép eKYC với các loại giấy tờ khác như CCCD 12 số/ CCCD thường, Hộ chiếu)

• Đánh giá app mới/app cũ | V1.1

### 1/ Mục đích & ý nghĩa chức năng

a. eKYC là gì?

eKYC là định danh khách hàng bằng sự hỗ trợ của công nghệ như nhận diện KH nhờ trí tuệ nhân tạo (AI),  kiểm tra, đối chiếu thông tin cá nhân tức thì với cơ sở dữ liệu tập trung về danh tính người dùng, xác thực sinh trắc học ...

b. Mục đích của chức năng

• Giúp KH đăng ký mở CIF, TKTT, Đăng ký dịch vụ MB của CoopBank nhanh chóng, dễ dàng, tiện lợi, và không cần phải ra Quầy
• Giúp ngân hàng mở rộng số lượng khách hàng
### 2/ Phạm vi

#### 2.1/ Phạm vi FrontEnd
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | eKYC | 
Đăng ký online
 | RedThêm mới | MB | 
Cho phép KH đăng ký dịch vụ của Bank (Mở CIF, mở TKTT, Đăng ký MB) ngay trên ứng dụng:

• 
Bước 1: Chọn chức năng "Đăng ký" tại màn hình Login

• Bước 2: Nhập số điện thoại và xác thực OTP
• Bước 3: Chọn và Chụp ảnh giấy tờ tùy thân (Chỉ cho phép chọn loại CCCD Chip)
• Bước 4: Xác nhận kết quả đọc giấy tờ
• Bước 5: Chụp ảnh chân dung
• Bước 6: Xác nhận đăng ký dịch vụ và nhập 1 số thông tin đăng ký theo quy định của Bank như: Ngành nghề, Loại hình tổ chức, Địa chỉ nơi ở hiện tại ...
• Bước 7: Thông báo kết quả tiếp nhận yêu cầu đăng ký eKYC
• 
Bước 8: KH nhận được SMS thông báo đăng ký mở tài khoản thành công
 | 
RedKhó
 | Client, Server, Bank | 

 | 
 | 
 | 
 | 
 | 
 | 
 | 
 | 

#### 2./ Phạm vi Server
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | Phạm vi tác nhân thực hiện | Link tài liệu
 | eKYC | Job chạy Đăng ký mở CIF/ TKTT/SMS/ MB | RedThêm mới | MB | 
Sau khi KH xác nhận đăng ký dịch vụ trên App. Bản ghi đăng ký của KH sẽ được lưu tại bảng CUS_eKYC tại MB server.

• Có phân biệt kênh thực hiện eKYC: Hiện tại chỉ có kênh App
• Có phân biệt dịch vụ được thực hiện eKYC: Hiện tại chỉ có dịch vụ Đăng ký. Sau này có thể có thêm dịch vụ Quên mật khẩu, hoặc Đăng nhập trên thiết bị khác ...
• MB server thực hiện quét các bản ghi của KH tại bảng CUS_eKYC theo logic và thứ tự như sau:
• Lấy các bản ghi KH có trạng thái eKYC = Chờ đăng ký
• Gửi yêu cầu kiểm tra khuôn mặt trùng tới hệ thống eKYC
• Gửi yêu cầu mở CIF tới Bank
• Gửi yêu cầu mở TKTT tới Bank (Sau khi Bank trả kết quả mở CIF thành công)
• Gửi yêu cầu đăng ký SMS Banking tới Bank (Sau khi KH mở TKTT thành công)
• Kiểm tra thông tin GTTT/ SĐT của KH đã tồn tại tại MB server chưa (Sau khi Bank trả kết quả đăng ký SMS Banking thành công)
• Đăng ký dịch dịch vụ Mobile Banking cho KH (KH được đăng ký tự động gói dịch vụ eKYC có giới hạn hạn mức theo tháng)
• Insert thông tin KH từ bảng CUS_eKYC sang bảng CUS chính của KH. Đồng thời trả mã CIF của KH cho eKYC server để eKYC server lưu vào request ekyc của KH
• Gửi SMS/ email thông báo cho KH về kết quả đăng ký, mở tài khoản | 
RedKhó
 | Client, Server, Bank | 

 | eKYC | Job chạy dọn dẹp dữ liệu eKYC thất bại | 
RedThêm mới
 | BE | 
Dữ liệu eKYC thất bại gồm có ảnh chụp giấy tờ và ảnh chụp chân dung khách hàng

Dữ liệu eKYC thất bại sẽ được di chuyển sang DB khác để giảm tải hạ tầng lưu trữ dữ liệu eKYC

• Chỉ di chuyển ảnh đối với KH thực hiện eKYC thất bại
• Job chạy định kỳ hàng ngày để di chuyển dữ liệu trong vòng x ngày
• Dữ liệu di chuyển không thành công của ngày hôm trước sẽ được di chuyển lại sang ngày hôm sau | 
BlueTrung bình
 | Server | 

 | Hạn mức | Logic kiểm tra hạn mức/ tháng | 
RedThêm mới
 | MB | 
Bổ sung thêm Logic kiểm tra hạn mức theo tháng cho gói dịch vụ ( Theo quy định, các KH eKYC chỉ được cấp hạn mức tối đa 100tr/ tháng)
 | 
RedKhó
 | 
 | 

#### 2.2/ Phạm vi Backend
 | Nhóm chức năng | Chức năng | Loại | Kênh | Mô tả cơ bản | Độ khó | API Bank cấp
 | eKYC | 
Quản lý danh sách eKYC
 | 
RedThêm mới
 | BE | 
Chức năng này sẽ thống kê lại tất cả các lần eKYC thành công hoặc thất bại của 1 KH đã thực hiện trên App. Để dựa vào đó, Bank sẽ đưa ra các đánh giá, quyết định phù hợp. Hoặc đối với VNPay có thể biết được các mã lỗi hay gặp phải để cải thiện hệ thống eKYC. 

• Dữ liệu KH eKYC được lấy từ eKYC server
• Các tác nghiệp: Xem danh sách, Xem chi tiết bản ghi eKYC | 
BlueTRUNG BÌNH
 | 
 | eKYC | 
Duyệt kết quả eKYC (Hậu kiểm eKYC)
 | 
RedThêm mới
 | BE | 
Do sau khi KH eKYC được nhận SMS thông báo thành công, KH sẽ được sử dụng ngày tài khoản và dịch vụ Mobile Banking với hạn mức thấp. Nên đối với các KH này, Bank cần hậu kiểm lại, để đối chiếu lại các KH nghi ngờ cần xác minh lại, các KH giả mạo thì cần khóa ngay Mobile Banking, các KH đủ điều kiện thì sẽ được phép dùng bình thường.

• Dữ liệu danh sách KH được lấy từ MB server
• Bao gồm dữ liệu của các KH đã được đăng ký eKYC thành công: mở CIF, mở TKTT, đăng ký MB
• Các tác nghiệp: Xem, Xác nhận (để phân loại KH đạt tiêu chuẩn hoặc nghi ngờ giả mạo ...) | 
RedKhó
 | 
 | Quản lý khách hàng | Cập nhật dịch vụ | 
BlueCập nhật
 | BE | Bổ sung thêm cột Hình thức đăng ký (Bao gồm 2 giá trị: Tại Quầy và eKYC) | 
GreenDễ
 | 
 | Báo cáo chi tiết đăng ký khách hàng | 
BlueCập nhật
 | BE | Bổ sung thêm cột Hình thức đăng ký (Bao gồm 2 giá trị: Tại Quầy và eKYC) | 
GreenDễ
 | 
 | Phê duyệt dịch vụ | 
BlueCập nhật
 | BE | Bổ sung thêm cột Hình thức đăng ký (Bao gồm 2 giá trị: Tại Quầy và eKYC) | 
GreenDễ
 | 
 | Quản lý danh sách khách hàng | 
BlueCập nhật
 | BE | Bổ sung thêm cột Hình thức đăng ký (Bao gồm 2 giá trị: Tại Quầy và eKYC) | 
GreenDễ
 | 
 | Danh mục | Quản lý loại điểm giao dịch | 
Cấu hình thêm giá trị
 | BE | Cấu hình thêm giá trị : Quỹ tín dụng nhân dân | 
GreenDễ
 | 

 | 
 | Quản lý ngành kinh tế | 
RedThêm mới
 | BE | Quản lý các danh mục ngành kinh tế cho phép KH chọn được khi đăng ký dịch vụ trên App | 
GreenDễ
 | 
 | 
 | Dịch vụ | 
BlueCập nhật
 | BE | Bổ sung thêm checkbox "Không tính hạn mức tháng" | 
GreenDễ
 | 
 | Tham số | Quản lý gói dịch vụ | 
BlueCập nhật
 | BE | 
Tại cấu hình hạn mức theo gói, bổ sung trường Tổng hạn mức GD/ tháng

Thêm logic check --> Nếu nhập Hạn mức chuyển tiền lớn hơn Tổng hạn mức GD/tháng, khi nhấn "Thêm mới", hiển thị thông báo "Hạn mức chuyển tiền không được vượt quá hạn mức giao dịch theo tháng của gói dịch vụ. Quý khách vui lòng kiểm tra lại."
 | 
GreenDễ
 | 
 | Quản lý tham số eKYC | Danh mục tham số eKYC | 
RedThêm mới
 | BE | Chức năng này dùng để thêm mới, cập nhật tham số cấu hình cho hệ thống eKYC | 
BlueTRUNG BÌNH
 | 
 | Quản lý mã lỗi eKYC | 
RedThêm mới
 | BE | Chức năng này dùng để thêm mới, cập nhật mã lỗi cho hệ thống eKYC | 
BlueTRUNG BÌNH
 | 
 | Quản lý Black list | 
RedThêm mới
 | BE | Chức năng này dùng để thêm mới, cập nhật blacklist cho hệ thống eKYC | 
BlueTRUNG BÌNH
 | 
 | Quản lý mã tỉnh/TP | 
RedThêm mới
 | BE | Chức năng này dùng để map Tỉnh thành từ 3 số đầu đọc được trên CCCD (3 số đầu  | 
BlueTRUNG BÌNH
 | 
 | Quản lý mã Quốc gia | 
RedThêm mới
 | BE | Chức năng này dùng để map Tỉnh thành từ 3 số đầu đọc được trên CCCD | 
BlueTRUNG BÌNH
 | 
 | Báo cáo

 | Báo cáo thống kê số lượng thực hiện eKYC | 
RedThêm mới
 | BE | Chức năng này dùng để tra cứu và xuất báo cáo thống kê theo mã lỗi eKYC | 
GreenDỄ
 | 
 | Báo cáo thống kê theo mã lỗi eKYC | 
RedThêm mới
 | BE | Chức năng này dùng để tra cứu và xuất báo cáo thống kê số lượng thực hiện eKYC | 
GreenDỄ
 | 
 | Báo cáo tình hình triển khai eKYC | 
RedThêm mới
 | BE | Chức năng này dùng để tra cứu và xuất báo cáo thống kê việc triển khai eKYC | 
GreenDỄ
 | 

2.4/ Đánh giá ảnh hưởng

App/ Server

• Chức năng Đăng nhập:
             - Cần test lại Đăng nhập với các KH đăng ký tại Quầy (Do sau khi eKYC thành công, KH đăng nhập với user/ pass được cấp, cũng với trạng thái Active Standby)

             - Cần test lại trạng thái của KH theo sơ đồ trạng thái của KH (Đối với cả 2 hình thức đăng ký tại Quầy và eKYC)

             - Test lại hạn mức giao dịch/ Gói, Hạn mức giao dịch/ tháng

BE

• Chức năng Quản lý khách hàng
Cần test lại các chức năng Cập nhật KH, Xem thông tin KH, Phê duyệt, Quản lý danh sách KH ( gửi lại mật khẩu, khóa dịch vụ ...)

##### 2.4.1. Ảnh hưởng khi cập nhật chỉ cho chọn loại giấy tờ = CCCD Chip (Nếu force update thì bỏ qua)

• Đối với KH sử dụng App mới: App chỉ cho chọn 1 loại giấy tờ = CCCD Chip → KH eKYC với loại giấy tờ CCCD Chip như luồng hiện tại
• Đối với KH sử dụng App cũ: Tức là phiên bản App cũ của KH vẫn chọn được các loại giấy tờ khác như: CCCD 12 số/ CCCD thường, Hộ chiếu → Thì khi KH chọn loại giấy tờ khác CCCD Chip → Sau khi chụp ảnh giấy tờ sẽ nhận được thông báo lỗi "Loại giấy tờ không hợp lệ hoặc chưa rõ thông tin. Vui lòng kiểm tra và chụp lại!" 
#### 2.4/ Phạm vi API Bank cung cấp cung cấp (nếu có)
 | TT | Tên API | Định nghĩa API | Kênh sử dụng | Input | Output | Ghi chú
 | 1 | Check SĐT, GTTT đã tồn tại CIF, TKTT, SMS chưa? | 
 | 
 | 
• SĐT
• GTTT
• Checktype: ALL, CIF, ACC | 

 | Bank cấp bộ API mới riêng cho eKYC
 | 2 | Đăng ký mở CIF | 
 | 
 | 

 | 
 | 

 | 4 | Đăng ký TKTT | 
 | 
 | 

 | 
 | 

 | 5 | Đăng ký SMS  | 
 | 
 | 

 | 
 | Phase 1 đã có API kích hoạt lại SMS (Chưa có đăng ký mới)
 | 6 | Lấy DS Tỉnh thành | 
 | 
 | 

 | 
 | 
Để cho KH chọn lại địa chỉ nơi ở hiện tại

(Bank không cấp API này nữa, do eKYC server có Tỉnh thành rồi)

 | 7 | Lấy DS Quận Huyện | 
 | 
 | 

 | 
 | Để cho KH chọn lại địa chỉ nơi ở hiện tại
 | 9 | Lấy DS phường xã | 
 | 
 | 

 | 
 | Để cho KH chọn lại địa chỉ nơi ở hiện tại

### 3/ Q&A

#### 3.1/ Phạm vi Frontend

#### 3.2/ Phạm vi Backend

3.3/ Phạm vi API kênh cung cấp (nếu có)
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

### 12.2. Usecase Summary (Bank + VNPay)

> **Page ID:** `144540378` · **Version:** 2
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/144540378

| Use Case Name | Đăng ký dịch vụ Online (eKYC)
 | Use Case ID | UC-eKYC-01
 | Use Case Description | 
Là người dùng, tôi muốn đăng ký mở tài khoản ngân hàng và đăng ký dịch vụ Mobile Banking online, mà không cần phải ra Quầy

 | Actor | 
KH, App Client, App Server, Hệ thống eKYC, Hệ thống Bank

 | Priority | 
trueRedKhó

 | Trigger | N/A
 | 
Pre-Condition
 | 
• KH chưa đăng ký dịch vụ Mobile Banking (Bao gồm cả KH mới hoàn toàn và KH cũ chưa đăng ký MB)
 | Post-Condition | 
• KH mới hoàn toàn được mở tài khoản ngân hàng và đăng ký dịch vụ MB thành công
• KH đã có TKTT được đăng ký dịch vụ MB thành công
• Dữ liệu eKYC của KH sau khi chạy Job các job đăng ký thành công, được insert vào bảng CUS. Với trạng thái dịch vụ là Active Standby
• Sau khi nhận đc SMS/email đăng ký thành công, KH thực hiện kích hoạt trên App và được sử dụng luôn Mobile Banking với hạn mức thấp
 | Basic Flow | 
• 
Bước 1: Chọn chức năng "Đăng ký" tại màn hình Login

• Bước 2: Nhập số điện thoại và xác thực OTP
• Bước 3: Chụp ảnh giấy tờ tùy thân
• Bước 4: Xác nhận kết quả đọc giấy tờ
• Bước 5: Chụp ảnh chân dung
• Bước 6: Xác nhận đăng ký dịch vụ và nhập 1 số thông tin đăng ký theo quy định của Bank như: Ngành nghề, Loại hình tổ chức, Địa chỉ nơi ở hiện tại ...
• Bước 7: Thông báo kết quả tiếp nhận yêu cầu đăng ký eKYC
• 
Bước 8: KH nhận được SMS thông báo đăng ký mở tài khoản thành công

 | Alternative Flow | N/A
 | Exception Flow | 
• KH đã đăng ký MB
• Thông tin KH không cân khớp trên hệ thống Bank (CMND và SĐT không thuộc về 1 người )
 | Bussiness Rules | 

 | Non-Funtional Requirement |

---

### 12.3. User Action Flow (Bank + VNPay)

> **Page ID:** `144540571` · **Version:** 18
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/144540571

Phiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 
 
 | A | Lê Thị Hồng | 
 | 
Tạo mới
 | V.1.0.0
 | 
 
 | M | Thudm2 | V.1.0.0 | 
Bổ sung logic gọi xác thực với Gtel (C06)
 | V.1.0.1
 | 
 
 | M | Thudm2 | V.1.0.1 | 
Cập nhật logic xử lý NFC
 | V.1.0.2
 | 
 
 | M | ThuDM2 | V.1.0.2 | 
Cập nhật TH lỗi NFC và thông báo
 | 
V.1.0.3

Mục lục
none

### 1/ User Flow

trueeKYC Onboarding có C06falseautotoptrue13213

### 2/ Mô tả luồng

* Tham số Bank có thể cấu hình: Check NFC (SKIP_NFC: 0, 1, 2, 3), Check C06 (CHECK_GTEL: ON, OFF)

• Với luồng này yêu cầu bắt buộc cấu hình để đảm bảo có thể thu thập và check C06 thành công: CHECK_GTEL=ON, SKIP_NFC=2 (thiết bị không hỗ trợ NFC thì ko cho thực hiện luồng → thông báo cho ND)
• Nếu bank cấu hình CHECK_GTEL=ON mà cấu hình SKIP_NFC # 2 (=0,1,3) → vẫn thực hiện luồng gọi sang C06, nhưng ko đủ thông tin để check hợp lệ thì sẽ hiển thị  thông báo "Chưa xác thực BCA"
• Nếu bank cấu hình CHECK_GTEL=OFF thì chỉ thực hiện thu thập thông tin, không gọi sang C06
#### 2.1/ Truy cập chức năng

##### MH đăng nhập + MH giới thiệu đăng ký
 | 
TT
 | 
Hành động
 | 
Tác nhân
 | 
Mô tả chi tiết

 | 
1
 | 
Click vào Đăng ký
 | 
Hệ thống MB
 | 
1/ Kiểm tra thiết bị có an toàn không?

• Không hợp lệ: Thiết bị root/hook/jb/emulator Hiển thị thông báo lỗi: "Không thể thực hiện đăng ký do thiết bị của Quý khách không an toàn (Root/Jailbreak/Hook/Emulator)"
• Hợp lệ: Mở đến MH Giới thiệu eKYC (IOS) hoặc Chuyển bước 2 (Android)
2/ Kiểm tra version của hệ điều hành Android (IOS không cần kiểm tra)

• Không hợp lệ : Ver < 6: Thông báo "Thiết bị của Quý khách không đủ điều kiện để thực hiện mở tài khoản trực tuyến. Vui lòng sử dụng thiết bị khác hoặc liên hệ 1900545554 để được hỗ trợ!
• Hợp lệ: Mở đến MH Giới thiệu eKYC
 | 
2
 | 
Bấm Tiếp tục
 | 
Hệ thống MB
 | 
Bấm tiếp tục tại MH giới thiệu eKYC mở đến MH Nhập SĐT

##### MH Nhập SĐT
 | 
TT
 | 
Hành động
 | 
Tác nhân
 | 
Mô tả chi tiết

 | 1 | 
Nhập SĐT và bấm Tiếp tục

 | Hệ thống MB | 
1/ Kiểm tra số điện thoại và đã click vào ô điều kiện/ điều khoản hay chưa

• Không hợp lệ | | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | Bỏ trống số điện thoại đăng nhập | Quý khách vui lòng nhập {trường bỏ trống} | 

 | 2 | Số điện thoại sai định dạng (ko bắt đầu bằng số 0, có độ dài khác có độ dài 10 số) | [Trường] không đúng định dạng. Quý khách vui lòng kiểm tra lại | 

 | 3 | Chưa click vào ô điều kiện/ điều khoản | 
Quý khách chưa đồng ý với Thỏa thuận về mở và sử dụng tài khoản thanh toán cho khách hàng cá nhân bằng phương thức điện tử và Điều khoản, điều kiện sử dụng dịch vụ Mobile Banking
 | 

• Hợp lệ → Chuyển bước 2
 | 
 | 
 | 
2/ Thực hiện kiểm tra SĐT đã đăng ký MB chưa

• Không hợp lệ | | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | SĐT của KH đã đăng ký Mobile Banking thành công | Số điện thoại của Quý khách đã đăng ký dịch vụ Mobile Banking tại Co-opBank. Vui lòng kiểm tra lại hoặc liên hệ Hotline | 

 | 2 | SĐT của KH đang nằm trong danh sách chờ chạy Job | Yêu cầu đăng ký dịch vụ của Quý khách đang được ngân hàng xử lý. Quý khách vui lòng chờ kết quả đăng ký sẽ được gửi về SĐT/ Email sau ít phút nữa | 

• Hợp lệ: Nếu chưa đăng ký → Chuyển bước 3: Kiểm tra phiên bản ứng dụng
3/ Kiểm tra cấu hình cho phép KH đăng ký eKYC trên App không? (Cấu hình tại tham số BE: REGISTER_EKYC, gồm 2 giá trị ON/OF)
 | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | 
Giá trị tham số REGISTER_EKYC = OFF

(Ý nghĩa: Hệ thống đang chặn không cho KH thực hiện chức năng đăng ký eKYC trên App)
 | Tính năng đăng ký dịch vụ không thực hiện được trong thời gian này. Quý khách vui lòng thử lại sau | 
• Tham số này chỉ có giá trị khi thực hiện chức năng đăng ký trên App (Không liên quan đến Job gọi sang Bank để đăng ký mở CIF/TKTT)
• Tắt thông báo lỗi quay về MH Login
 | 
2
 | 
Giá trị tham số REGISTER_EKYC = ON

(Ý nghĩa: Hệ thống đang cho phép KH thực hiện chức năng đăng ký eKYC trên App)
 | 
 | Chuyển bước 3, kiểm tra phiên bản

4/ Kiểm tra phiên bản ứng dụng theo logic hiện tại <Tham khảo tại >

• Nếu không có phiên bản mới hơn → Chuyển bước 3 sinh mã OTP
• Nếu có phiên bản mới hơn → Trả thông báo tương ứng cho 2 trường hợp: Bắt buộc cập nhật App hoặc Không bắt buộc → Với chức năng eKYC lần này thì sẽ yêu cầu bắt buộc cập nhật App : "Quý khách vui lòng nâng cấp ứng dụng trước khi tiếp tục sử dụng dịch vụ" (Thông báo cấu hình được ở BE)
5/ Hệ thống MB thực hiện sinh mã OTP và gửi yêu cầu gửi OTP tới SĐT của KH (Type SMS = Activate_OTP)

 | 
 | 
 | 
Hệ thống MB server thực hiện sinh OTP và gửi yêu cầu gửi OTP tới SĐT của KH

• Nếu không có phiên bản mới hơn → Hiển thị MH Nhập mã OTP
• Nếu có phiên bản mới hơn → Hiển thị thông báo "Quý khách vui lòng nâng cấp ứng dụng trước khi tiếp tục sử dụng dịch vụ" và Button "Đồng ý"
→ Bấm Đồng ý :

iOS:

• Mở link tải ứng dụng Co-opBank Mobile Banking trên App Store.
Android:

• Mở link tải ứng dụng Co-opBank Mobile Banking trên CH Play.
<Tham khảo tại >

 | 
 | 
##### Gửi lại OTP

 | Hệ thống MB | Gửi yêu cầu nhận lại mã xác thực OTP sang MB Server + temToken (phiên tạm khi chưa có session id)
 | 
 | 
• Không hợp lệ | 1 | Thời gian gửi OTP liên tiếp trong (n) phút | 
Mã xác nhận OTP không được gửi liên tiếp trong {n} phút.

n được cấu hình tại tham số PERIOD_SEND_OTP_CODE
 | 

• Hợp lệ → Hệ thống MB server thực hiện sinh OTP và gửi yêu cầu gửi OTP tới SĐT của KH ( Tương tự luồng gửi mới SMS OTP, Type SMS = Activate_OTP)
 | 2 | 
Nhập mã OTP

 | Hệ thống MB | 
Kiểm tra mã OTP

• Không hợp lệ | | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | Bỏ trống mã xác nhận OTP | Quý khách vui lòng nhập {trường bỏ trống} | 

 | 
2
 | Mã xác nhận OTP nhỏ hơn 6 ký tự | Quý khách vui lòng nhập mã OTP bao gồm 6 ký tự số | 

 | 
3
 | OTP sai | Mã xác nhận OTP không đúng. Quý khách vui lòng kiểm tra lại. | 

 | 
4
 | OTP hết hiệu lực | Mã xác nhận đã hết thời gian hiệu lực (n) phút. Quý khách vui lòng nhấn "Gửi lại mã OTP" để nhận lại mã | 

• Hợp lệ: Hiển thị MH chọn loại giấy tờ
 | 3 | 
Chọn loại giấy tờ
 | Hệ thống MB | 
Hiển thị loại giấy tờ như đã mô tả

##### MH đồng ý lưu dữ liệu STH theo nghị định 13
 | TT | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | 
MH1.4 nhấn "Đồng ý và tiếp tục"

 
 | 
Hệ thống MB
 | 
Cập nhật trạng thái chia sẻ dữ liệu của KH

Hiển thị MH2.1

#### 2.2/ Các chức năng chính

Bắt đầu vào luồng chụp ảnh
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả xử lý

 | 2 | Hệ thống eKYC  | 
Kiểm tra SĐT đã eKYC sai liên tiếp quá số lần quy định trong ngày theo tham số "LIMIT_FAILED_EKYC" chưa và trả kết quả kiểm tra cho SDK eKYC

Note :

• Số lần sai eKYC liên tiếp trong ngày được tính theo mỗi lần gọi request lên hệ thống eKYC và nhận về kết quả là thất bại. Tính riêng request theo từng lần chụp ảnh giấy tờ và chụp ảnh chân dung
• Tại thời điểm 00h00 hằng ngày sẽ thực hiện reset lại số lần sai liên tiếp trong ngày | 

 | 3 | 
Hiển thị kết quả:

• Không hợp lệ | | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | SĐT của KH đã eKYC quá số lần | Quý khách đã thực hiện không thành công quá số lần quy định, vui lòng thực hiện lại sau n giờ" (Lưu ý: n = Số thời gian còn lại (tính đến thời điểm được reset) để được tiếp tục eKYC) | 

• Hợp lệ: Nếu chưa quá số lần, cho phép Chụp ảnh giấy tờ | 

##### Chụp ảnh mặt trước CCCD gắn chip
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1

 | 
Nhấn "Chụp"
 | 
Hệ thống eKYC 
 | 
Thực hiện chụp mặt trước CCCD theo hướng dẫn

Chụp xong hiển thị MH2.4 ảnh chụp mặt trước

 | 
 | 
Nhấn “Xác nhận”
 | 
Hệ thống eKYC 
 | 
Kiểm tra kết quả đọc mã QR trên mặt trước CCCD

• Không hợp lệ: Không đọc được thông tin hoặc thông tin không hợp lệ →  Chuyển sang màn hình quét mã QR
• Hợp lệ: 
       - Thông tin đọc QR gồm: Số GTTT, họ tên, ngày sinh, giới tính, nơi thường trú, ngày cấp, số CMND

       - Dựa vào kết quả QR, client thực hiện tính thời gian hết hạn GTTT:

          Tính theo quy định: Dựa vào ngày sinh khách hàng, khi đủ: 25 tuổi, đủ 40 tuổi và đủ 60 tuổi.

          VD: KH sinh ngày 26/01/1988 → Ngày hết hạn là 26/01/2028

                 Trên 60 tuổi, ngày hết hạn = Không thời hạn

       - Lưu thông tin KH, Chuyển sang Màn hình hướng dẫn NFC (Nếu tham số SKIP_NFC=2 - lý tưởng)

##### Quét mã QR (Nếu chụp ảnh lỗi)
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Quét mã QR trên mặt trước CCCD | Hệ thống eKYC  | 
Hệ thống tự động quét mã QR cho đến khi nhận được thông tin hợp lệ theo đúng định dạng quy định

Không thành công: Hiển thị thông báo lỗi.

• 
• QR sai định dạng. Thông báo "Mã QR không hợp lệ." Hiển thị nút Đóng Click chọn Đóng: Tắt Popup thông báo
• Sau thời gian cấu hình trên BE (Tham số ScanQR_Time). Hiển thị nút Bỏ qua. Nhấn "Bỏ qua":
• Nếu có NFC: Hiển thị màn hình Nhập thông tin Key
• Nếu không có NFC: Hiển thị màn hình chụp mặt Sau giấy tờ
• Thành công: Hiển thị thông báo "Scan QR thành công". Đồng thời: 
• Lưu thông tin khách hàng Số GTTT,  ngày hết hạn, ngày sinh
• Check tham số SKIP_NFC (Bật tắt luồng NFC)
• Nếu tham số SKIP_NFC = 0 - Tắt - Chuyển sang chụp mặt sau CCCD
• Nếu tham số SKIP_NFC = 1 - Cho phép bỏ qua sau khi tap n lần không được
• Nếu tham số SKIP_NFC = 2 - bắt buộc thực hiện luồng NFC, Client truyền 3 thông tin khách hàng gồm: Số GTTT,  ngày hết hạn, ngày sinh chuyển sang màn chạm thẻ chip 
• Nếu tham số SKIP_NFC = 3 - cho phép bỏ qua NFC nếu quét được QR, nếu k quét được QR thì bắt buộc quét quét NFC

##### Nhập thông tin NFC (Nếu QR lỗi)
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 2 | Nhập thông tin "Số CCCD", "Ngày sinh" rồi nhấn "Tiếp tục" | Hệ thống eKYC  | 
Kiểm tra validate các trường nhập vào:

• Không hợp lệ: | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (Nếu có)

 | 1 | Không nhập thông tin số GTTT | Quý khách vui lòng nhập số căn cước công dân. | 

 | 2 | Không nhập thông tin trường ngày sinh(IOS) | Quý khách vui lòng nhập ngày sinh. | 

 | 3 | Nhập sai định dạng trường ngày sinh(IOS) | Trường ngày sinh nhập theo định dạng dd/mm/yyyy. Quý khách vui lòng kiểm tra lại. | 

• Hợp lệ: Thực hiện tính ngày hết hạn CCCD dựa theo quy tắc phần mô tả chi tiết, Dựa vào 3 thông tin: Số GTTT, ngày sinh, ngày hết hạn hợp lệ là key để truyền sang đọc thông tin thẻ chip 

##### Thực hiện NFC

* Trong khi thực hiện NFC, nếu ND chọn nút Back của thiêt bị thì đưa về MH Chụp ảnh GTTT mặt trước
 | 
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Ở MH3.01, Nhấn "Đã hiểu" | 
Hệ thống eKYC 
 | 
Bước 1: Thực hiện kiểm tra trạng thái sẵn sàng đọc NFC của thiết bị:

Đối với IOS:

• 
Thực hiện kiểm tra trạng thái sẵn sàng đọc NFC của thiết bị:

Đối với IOS:

• Hiển thị màn hình có nút "Đang xử lý" 

• Nút "Đang xử lý" disable cho đến khi khởi tạo thành công phiên đọc NFC; trong quá trình chờ khởi tạo; nếu quá 60s thiết bị không phản hồi hoặc phản hồi không mở phiên mới →  hiển thị Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
• Trường hợp "ready" khởi tạo phiên đọc NFC trên thiết bị→ Hiển thị màn hình thực hiện NFC 2, thực hiện bước 2:
Đối với Android:

• Thực hiện ngay bước 2
Bước 2:

Hệ thống tự động quét thẻ chip cho đến khi nhận được thông tin hợp lệ

• Không hợp lệ:  | | 
 | 
Trường hợp
 | 
Thông báo
 | 
Xử lý (Nếu có)

 | 1 | Lỗi kết nối trong quá trình tap thẻ
(VD: tap chip nửa chừng bỏ ra) | "Kết nối tạm thời gián đoạn. Quý khách vui lòng đợi trong giây lát"- button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 2 | Lỗi đọc thông tin không thành công
(VD: mở lên nhưng không tap chip, đang tap thì bỏ tay ra không tab tiếp, khi đọc NFC bị TO do lỗi SDK, Tap thẻ atm/visa) | "Đọc thông tin không thành công. Quý khách vui lòng thử lại" - Button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 3 | Lỗi tap fail quá số lần | "Quý khách đã thực hiện quét NFC quá số lần quy định. Vui lòng thực hiện lại!" - Button Thử lại | Tính theo SKIP_NFC:
= 0,1,3 => đi tiếp mặt sau
= 2 => về MH chọn giấy tờ tùy thân
 | 4 | Lỗi lệch thông tin nhập và thông tin NFC
(VD: Tap chip CCCD khác CCCD đã chụp hoặc thông tin đọc được từ chip không match với thông tin key (đọc được từ QR/nhập tay)) | "Thông tin NFC không trùng khớp. Quý khách vui lòng thử lại"- Button Thử lại | Quay về MH chọn giấy tờ tùy thân
 | 5 | Lỗi chung (Andr) | "Thông tin quý khách không hợp lệ, xin vui lòng thử lại" - Button "Thử lại" | nếu chưa đạt ngưỡng maxtap --> tap lại
nếu đạt ngưỡng maxtap --> tương tự TH3

• Hợp lệ: Thông tin đọc NFC thành công, check tham số ON_OFF_VERSO
• Nếu tham số ON_OFF_VERSO = ON → hiển thị MH Chụp mặt sau CCCD
• Nếu tham số ON_OFF_VERSO = OFF → Gửi yêu cầu kiểm tra chất lượng ảnh GTTT trước khi hiển thị kết quả đọc giấy tờ

##### Màn hình thực hiện NFC 2+ Màn hình thực hiện NFC 3
 | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Hủy bỏ | 
SDK Client
 | 
Quay về màn hình hướng dẫn NFC có nút đã hiểu

##### Quá trình đọc KH di chuyển giấy tờ ra ngoài vùng đọc + Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
 | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 2 | Đóng | 
SDK Client
 | 
Quay về màn hình hướng dẫn NFC có nút đã hiểu

##### Chụp mặt sau CCCD
 | | 
STT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả

 | 1 | Click chọn “Chụp” | Hệ thống eKYC  | 
Thực hiện chụp ảnh trong vùng hướng dẫn chụp ảnh (Vùng có đường viền xanh)

Sau khi chụp xong, chuyển màn hình hiển thị ảnh sau khi chụp

 | 2 | 
Nhấn “Xác nhận”
 | 
Hệ thống eKYC 
 | 
Lưu ảnh đã được chụp tại client → Gửi yêu cầu kiểm tra chất lượng ảnh GTTT trước khi hiển thị kết quả đọc giấy tờ

Không hợp lệ → thông báo lỗi

• Độ tin cậy theo cấu hình Dưới ngưỡng tin cậy
• Giấy tờ hết hạn
• KH chưa đủ 18 tuổi
• KH đã eKYC sai liên tiếp quá số lần quy định trong ngày theo tham số "LIMIT_FAILED_EKYC"
Hợp lệ → Hiển thị MH4.6: KQ giấy tờ CCCD Chip

• Lớn hơn hoặc bằng ngưỡng tin cậy → Trả kết quả Đạt
• Giấy tờ chưa hết hạn → Trả kết quả Đạt
• KH đủ 18 tuổi → Trả kết quả Đạt
• KH eKYC chưa quá số lần sai liên tiếp quy định trong ngày theo tham số "LIMIT_FAILED_EKYC" 
• Đồng thời trả ID của bản ghi eKYC

##### Kiểm tra trạng thái đăng ký GTTT
 | 
TT
 | 
Thao tác
 | 
Tác nhân
 | 
Mô tả xử lý

 | 

 | 
Tại MH4.6: KQ giấy tờ CCCD Chip, bấm "Tiếp tục

 | 
Hệ thống MB
 | 
Kiểm tra số GTTT đã đăng ký tại MB server chưa (Trường hợp CCCD Chip nếu đọc được cả số CMND cũ thì thực hiện kiểm tra cả 2 số giấy tờ)

• Không hợp lệ | | 
#
 | 
Trường hợp
 | 
Nội dung thông báo
 | 
Xử lý (nếu có)

 | 
1
 | Số GTTT của KH đã đăng ký Mobile Banking thành công | Số GTTT của Quý khách đã đăng ký dịch vụ Mobile Banking tại Co-opBank. Vui lòng kiểm tra lại hoặc liên hệ Hotline 1900545554 để được hỗ trợ | 

 | 2 | Số GTTT của KH đang nằm trong danh sách chờ chạy Job | Yêu cầu đăng ký dịch vụ của Quý khách đang được ngân hàng xử lý. Quý khách vui lòng chờ kết quả đăng ký sẽ được gửi về SĐT/ Email sau ít phút nữa | 

• Hợp lệ: Nếu số GTTT chưa đăng ký tại MB → Gửi thông tin KH tới HT Bank để kiểm tra thông tin KH tại CoreBank và lưu  
Input:

• Checktype = A

> ⚠️ *Nội dung đã cắt ngắn (23179 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 12.4. Flow& Action screen (Bank + VNPay)

> **Page ID:** `153518509` · **Version:** 36
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/153518509

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 06/02/2023 | A | HongLT | 
 | 
Tạo mới
 | V.1.0
 | 
 
 | M | HongLT | V.1.0 | 
Cập nhật:

• Phạm vi: App fix chỉ cho phép đăng ký eKYC với loại giấy tờ = CCCD Chip
(Không cho phép eKYC với các loại giấy tờ khác như CCCD 12 số/ CCCD thường, Hộ chiếu)

• Hiển thị thông báo nâng cấp phiên bản khi bấm vào nút Đăng ký | V.1.1
 | 
 
 | M | ThuDM2 | V.1.1 | 
Bổ sung MH và mô tả MH:

• Luồng truy cập: 1.4
• Nhóm MH NFC: 3.3, 3.4
• Nhóm MH liveness Oval: 
• Nhóm MH đăng ký dịch vụ: 6.1, 6.2 | V.1.2
 | 
 
 | M | ThuDM2 | V.1.2 | 
Cập nhật thao tác:

• Lỗi giấy tờ: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp CCCD mặt trước
• Lỗi Liveness: Back của thiết bị + Back của App + Submit (Chụp lại): đều về màn chụp mặt 1 | V.1.3
 | 
 
 | M | ThuDM2 | V.1.3 | 
Cập nhật MH xử lý NFC
 | V.1.4
 | 
 
 | M | HongLT | 
 | 
• Do giải pháp Off mã lỗi OCR để đọc CCCD24 không đọc được trường Nơi cấp, nên eKYC server sẽ cập nhật fix Nơi cấp theo Ngày cấp và trả cho Client
• Sửa text ghi chú màn hình hướng dẫn quét QR | 

 | 
 
 | M | HongLT | 
 | Client cập nhật logic nếu trạng thái STH = Chưa xác thực BCA khi bấm tiếp tục, thông báo chặn không cho KH đăng ký | 

 | 
 
 | M | ThaoCY | 
 | Cập nhật UI màn chọn GTTT để đồng bộ với màn hình Thu thập STH | 

 | 
 
 | M | ThaoCY | 
 | Bỏ trường Quận/Huyện tại màn hình Nhập thông tin đăng ký
Truyền tỉnh để lấy Xã/Phường  | 

Mục lục
none

### 1/ Luồng di chuyển màn hình

### 2/ Luồng màn hình

Nhóm màn hình: Truy cập chức năng - 1

##### MH1.1: Đăng nhập- Đăng ký

##### MH1.2: Giới thiệu dịch vụ

##### MH1.3: Nhập SĐT - Check phiên bản - Nhập mã OTP

##### MH1.4: Màn hình đồng ý lưu dữ liệu STH

Nhóm màn hình eKYC - 2

##### MH2.1 Chọn loại giấy tờ

MH2.2: Màn hình thực hiện chụp mặt trước CCCD (tự động)

##### MH2.3: Màn hình thực hiện chụp mặt trước CCCD (thủ công)

##### MH2.4: Màn hình hiển thị ảnh chụp mặt trước

MH2.5: Hướng dẫn quét QR (Nếu không đọc đc QR từ mặt trước)

MH2.6: Kết quả đọc QR

##### Nhóm MH NFC - 3

##### MH3.01: Màn hình hướng dẫn NFC

##### MH3.02: Popup video hướng dẫn NFC

##### MH3.03: Màn hình thực hiện NFC 1 (Chờ thiết bị phản hồi khởi tạo phiên NFC)

##### MH3.1: Màn hình hướng dẫn NFC

##### MH3.2: Màn hình thực hiện NFC 2+3

  

##### MH3.2.1: Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)

##### MH3.2.2: Màn hình quá trình đọc KH di chuyển giấy tờ ra ngoài vùng đọc

##### MH3.3: Màn hình NFC không thành công

##### MH3.4: Màn hình NFC thành công

Nhóm màn hình nhập NFC (Chỉ hiển thị nếu không đọc được QR)

##### MH4.3: Màn hình nhập thông tin NFC khi QR lỗi (tuổi KH từ 58->59 tuổi)

##### MH4.4: Màn hình nhập thông tin NFC khi QR lỗi (KH < 25 tuổi, hoặc từ 26->39 tuổi)

##### MH4.5: Màn hình nhập thông tin NFC khi QR lỗi (KH>=60 tuổi)

##### MH4.6: KQ giấy tờ CCCD Chip

 

##### Nhóm màn hình chụp khuôn mặt (Liveness Oval) - 5

##### MH5.1: Màn hình Liveness 1

##### MH5.2: Màn hình Liveness 2

##### MH5.3: Màn hình Liveness thành công

##### MH5.4. Loading khi đang check C06

##### MH 5.5. Các MH kết quả Liveness bị lỗi

Nhóm MH đăng ký dịch vụ - 6

##### MH 6.1 Nhập thông tin đăng ký dịch vụ 1 - Nếu OFF check C06 hoặc ON check C06 nhưng check không thành công

##### MH 6.2 Nhập thông tin đăng ký dịch vụ 1 - Nếu ON check C06 & check thành công

##### MH 6.3. Bấm Tiếp tục,Thông báo nếu trạng thái STH = Chưa xác thực BCA

##### MH 6.3 Nhập thông tin đăng ký dịch vụ 2

 MH6.4 Thông báo khi Click vào Icon Back từ các MH Đăng ký dịch vụ 1

##### MH6.5 Kết quả đăng ký dịch vụ

### 3/ Mô tả màn hình

##### Nhóm MH truy cập chức năng

##### MH1.1: Đăng nhập - Đăng ký
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Đăng ký | 
Text link
 | 
Click
 | 
--
 | 
--
 | 
Màn hình Login hiện tại bổ sung thêm button link "Đăng ký". Click vào Đăng ký, mở đến MH1.2

##### MH1.2: Giới thiệu eKYC
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
 | Tên màn hình | 
 | 
 | 
 | 
 | Đăng ký dịch vụ
 | 1 | Label 1 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Cùng trải nghiệm công nghệ định danh số ngay trên ứng dụng Co-opBank Mobile Banking

 | 2 | Vùng ảnh | 
Image
 | 
--
 | 
--
 | 
--
 | 
Ảnh giới thiệu về dịch vụ eKYC

 | 3 | Label 2 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Mở tài khoản thanh toán dễ dàng và nhanh chóng

 | 4 | Label 3 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Đăng ký dịch vụ Co-opBank Mobile Banking với nhiều ưu đãi

 | 5 | Label 4 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Trải nghiệm hệ sinh thái đa dạng, nhiều tiện ích

 | 6 | Đăng ký ngay | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Click Đăng ký ngay mở ra MH Đăng ký dịch vụ - Nhập SĐT

##### MH1.3: Nhập SĐT - Check phiên bản
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
 | Tên màn hình | 
 | 
 | 
 | 
 | Đăng ký dịch vụ
 | 1 | Ghi chú 1 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng nhập số điện thoại để đăng ký sử dụng dịch vụ

 | 2 | Số điện thoại | Textbox | Number | Yes | 10 | 
• Mặc định trống.
• Cho phép nhập số điện thoại đúng theo quy tắc sđt chung (bàn phím số)
• Không cho phép Copy/ cho phép Paste
• Icon x cho phép xóa hết SĐT nếu đã nhập
 | 3 | Điều kiện, điều khoản | 
Checkbox
 | 
Click
 | 
--
 | 
--
 | 
• Mặc định uncheck, cho phép bỏ chọn/tích chọn. 
• Trường hợp KH chưa tick chọn:  Hiển thị popup thông báo :"Quý khách chưa đồng ý với Thỏa thuận về mở và sử dụng tài khoản thanh toán cho khách hàng cá nhân bằng phương thức điện tử và Điều khoản, điều kiện sử dụng dịch vụ Mobile Banking của Co-opBank"
• Hiển thị nội dung "Tôi đã đọc, hiểu và đồng ý với Thỏa thuận về mở và sử dụng tài khoản thanh toán cho khách hàng cá nhân bằng phương thức điện tử và Điều khoản, điều kiện sử dụng dịch vụ Mobile Banking của Co-opBank"
• Click vào "Thỏa thuận về mở và sử dụng tài khoản thanh toán cho khách hàng cá nhân bằng phương thức điện tử"
• Click vào "Điều kiện, điều khoản" mở đến MH <Điều khoản & điều kiện > (Bank cung cấp nội dung)
 | 4 | Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Click Tiếp tục mở ra MH Nhập mã xác thực OTP

 | 5 | Back | 
Icon
 | 
Click
 | 
--
 | 
--
 | 
Click back về MH trước đó

##### MH1.3: Nhập mã OTP
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
 | Tên màn hình | 
 | 
 | 
 | 
 | Đăng ký dịch vụ
 | 1 | Ghi chú 1 | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng nhập mã OTP đã được gửi đến số điện thoại xxx****xxx để xác thực đăng ký

 | 2 | Nhập mã OTP | Number | Input | Yes | 6 | 
• Hiển thị bàn phím số
• Khi nhận đc SMS OTP, nhận diện tự động mã OTP trong tin nhắn và hiển thị lên bàn phím để hỗ trợ KH nhập ngay cả dãy OTP
 | 3 | Gửi lại mã OTP | Text link | Click | -- | -- | < Thao khảo logic xử lý>
 | 4 | Back | Icon | Click | 
--
 | 
--
 | Click back về màn hình trước đó
 | 5 | Tiếp tục | Button | Click | -- | -- | Click Tiếp tục chuyển sang MH1.4

##### MH1.4: Màn hình đồng ý lưu dữ liệu STH
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Thông báo

 | 
2
 | 
Nội dung thông báo
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Fix trên client:

"Quý khách đang sử dụng dịch vụ định danh điện tử (eKYC) do VNPAY cung cấp. Trong quá trình sử dụng dịch vụ, chúng tôi (VNPAY) sẽ lưu trữ phục vụ các nghiệp vụ định danh xác thực. Các thông tin chia sẻ gồm:
- Số giấy tờ
- Họ và tên
- Ngày sinh
- Giới tính
- Quê quán
- Địa chỉ thường trú
- Ngày cấp
- Nơi cấp
- Ảnh chân dung và ảnh giấy tờ tùy thân
Quý khách vui lòng đọc kỹ quyền, nghĩa vụ của chủ thể dữ liệu và các nội dung khác liên quan tại "Chính sách bảo vệ dữ liệu cá nhân" được Co-opBank ban hành và có hiệu lực từ ngày 01/07/2023

 | 
3
 | 
Nút "Đóng"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Đóng thông báo và thoát ứng dụng

 | 
4
 | 
Nút "Đồng ý & Tiếp tục"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Hiển thị MH2.1

##### MH2.1: Màn hình chọn giấy tờ <chỉ hiển thị với KH app mới>
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 1 | Tên màn hình | 
 | 
 | 
 | 
 | Xác thực giấy tờ
 | 2 | Câu ghi chú | 
Label
 | 
ReadOnly
 | 
--
 | 
--
 | 
Quý khách vui lòng chọn loại giấy tờ xác thực

Quý khách vui lòng sử dụng CCCD gắn chip

 | 3 | Loại giấy tờ | Radio button | Click | Yes | 6 | 
• Mặc định Căn cước công dân gắn chip
 | 4 | Text + Ảnh hướng dẫn | Label + Image | ReadOnly | -- | -- | 
• Sử dụng thiết bị di động có hỗ trợ tính năng NFC để thực hiện đọc thông tin trong CCCD gắn chip
• Vui lòng sử dụng giấy tờ gốc (Bản chính) và còn hạn sử dụng
• Khách hàng không sử dụng Giấy tờ tùy thân giả mạo, không chính chủ. Khách hàng chịu hoàn toàn trách nhiệm trước pháp luật về thông tin giấy tờ tùy thân cung cấp cho ngân hàng.
 | 5 | Back | Icon | Click | 
--
 | 
--
 | Click back về màn hình trước đó
 | 6 | Tiếp tục | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Click Tiếp tục mở ra MH chụp ảnh mặt trước GTTT

##### MH2.2: Màn hình thực hiện chụp mặt trước CCCD (tự động); MH2.3: Màn hình thực hiện chụp mặt trước CCCD (thủ công); MH2.4: Màn hình hiển thị ảnh chụp mặt trước

(Đối với Mặt sau tương tự, chỉ thay tiêu đề vùng chụp từ "Mặt trước" thành "mặt sau")
 | 

 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nút “Quay lại”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
2
 | 
Tiêu đề
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix Client 

Xác thực giấy tờ tùy thân

 | 
3
 | 
Mô tả
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix tại Client

MH2.2: Vui lòng điều chỉnh thiết bị để thấy rõ giấy tờ tùy thân. Hệ thống sẽ tự động chụp khi giấy tờ nằm trong khung hình.

MH2.3: Vui lòng điều chỉnh thiết bị để thấy rõ giấy tờ tùy thân. Khi giấy tờ nằm trong khung hình, nhấn nút "Chụp ảnh".

MH2.4: Vui lòng kiểm tra lại hình ảnh đã chụp và nhấn nút "Xác nhận".

 | 
4
 | 
Tiêu đề vùng chụp
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Mặt trước

 | 
5
 | 
Vùng chụp ảnh
 | 
capture
 | 
View
 | 
--
 | 
--
 | 
Vùng chụp ảnh CCCD

 | 
6
 | 
Nội dung hướng dẫn
 | 
Label
 | 
Text
 | 
--
 | 
--
 | 
Hiển thị trên khung chụp ảnh giấy tờ; Nội dung thông báo tương ứng với các trường hợp lỗi mà client nhận diện được

-       Không phát hiện mặt trước

-       Không phát hiện được mặt sau giấy tờ

-       Giấy tờ đặt quá gần

-       Giấy tờ đặt quá xa

-       …

 | 
8
 | 
Chụp tự động
 | 
Switch button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

Chỉ hiển thị đối với Ios

Mặc định là “Chụp tự động”

 | 
9
 | 
Nút “Chụp”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

-       Mặc định hiển thị với Android

-       Đối với IOS:

o   Ẩn nếu “Chụp tự động”

o   Hiển thị nếu “Tắt chụp tự động”

 | 
5
 | 
Nút “Chụp lại”
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình chụp ảnh trước đó

 | 
6
 | 
Nút "Xác nhận"
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
<Tham khảo luồng xử lý chi tiết>

##### MH2.5: Màn hình hướng dẫn và thực hiện Scan QR
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Nút back
 | 
Button
 | 
Click
 | 
--
 | 
--
 | 
Quay trở lại màn hình thao tác trước đó

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Scan mã QR

 | 
3
 | 
Nội dung
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Di chuyển camera để thấy rõ nét mã QR tại mặt trước của giấy tờ tùy thân. Hệ thống sẽ tự động quét mã QR

Di chuyển camera để thấy rõ nét mã QR trên thẻ căn cước. Hệ thống sẽ tự động quét mã QR

 | 
3
 | 
Vùng scan mã QR
 | 
Capture
 | 
View
 | 
--
 | 
--
 | 
Tự động scan mã QR

<Tham khảo luồng xử lý> 

 | 
4
 | 
Hướng dẫn quét QR
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Hiển thị thông tin hướng dẫn bằng hình ảnh và hướng dẫn bằng chữ

• Đưa camera vào vùng mã QR ở góc phải mặt trước CCCD
• Hướng camera vào vùng mã QR trên thẻ căn cước
 | 5 | Nút "Bỏ qua" | Button | Click | -- | -- | 
Mặc định disable, hiển thị khi hết time cấu hình trên BE

Nhấn bỏ qua, chuyển sang màn hình "Chụp mặt sau"

 | 6 | Scan QR thành công | -- | -- | -- | -- | Chuyển sang MH NFC

##### MH 2.6: Màn hình Scan QR thất bại
 | 
 | Hạng mục | Kiểu hiển thị | Kiểu thao tác | Bắt buộc | Độ dài | Mô tả
 | 
1
 | 
Icon
 | 
Icon
 | 
Read Only
 | 
--
 | 
--
 | 
--

 | 
2
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Định dạng mã QR không hợp lệ, quý khách vui lòng thực hiện quét mã QR trên mặt trước của giấy tờ tùy thân

 | 
3
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
Tham khảo logic xử lý

##### MH3.01 + 3.03: Hướng dẫn NFC + Thực hiện NFC 1
 | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Đọc thẻ Căn cước bằng công nghệ không chạm (NFC)

 | 
2
 | 
Hướng dẫn thực hiện
 | 
Picture
 | 
Read Only
 | 
--
 | 
--
 | 
Fix client

 | 
3
 | 
Hướng dẫn 
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix client:

- Đưa mặt lưng của điện thoại (vị trí như trong hình hướng dẫn) vào con chip ở mặt sau của giấy tờ tùy thân
- Giữ nguyên điện thoại và căn cước khi có thông báo rung và chạy quá trình đọc thông tin
- Quý khách vui lòng xem kỹ hướng dẫn trước khi thực hiện

 | 
 4
 | Xem video hướng dẫn | Link | Click | -- | --- | 
textVIE: Xem video hướng dẫn

Link url: fix cứng tại client

VNPAY cung cấp link video hướng dẫn tương ứng từng bank 

Xử lý khi click → Chuyển sang popup video hướng dẫn NFC

 | 5 | Đã hiểu | Button | Click | -- | -- | 
Onclick chuyển sang Màn hình thực hiện NFC 1 (Chờ thiết bị phản hồi khởi tạo phiên NFC)

Tham khảo logic xử lý

 | 6 | Đang xử lý  | Button | Click | -- | -- | 
Mặc định disable

Tham khảo logic xử lý 

##### MH3.1: Màn hình hướng dẫn NFC
 | | 
 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 
Label
 | 
Read Only
 | 
--
 | 
--
 | 
Đọc thẻ Căn cước bằng công nghệ không chạm (NFC)

 | 
2
 | 
Hướng dẫn thực hiện
 | 
Picture
 | 
Read Only
 | 
--
 | 
--
 | 
Text hướng dẫn chạm thẻ

• Ảnh động hướng dẫn
• Quý khách vui lòng đọc kỹ hướng dẫn
• Đưa 2 vị trí khoanh vùng đỏ lại gần nhau (xem hình hướng dẫn: đưa phần đầu điện thoại lại gần vị trí chính giữa thẻ căn cước có biểu tượng chip xanh).
• Giữ nguyên thẻ & điện thoại khi màn hình thông báo đang đọc thông tin.
 | 
3
 | 
Hướng dẫn 
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Xin nhấn "Tôi đã hiểu và bắt đầu đọc thông tin" và đưa căn cước gần mặt sau điện thoại

 | 3 | Đọc thông tin ngay | Button | Click | -- | -- | Chuyển sang MH 3.2

##### MH3.2.1: Màn hình khởi tạo phiên NFC không thành công (Chưa tạo được section NFC mới)
 | 

 | 
Hạng mục
 | 
Kiểu hiển thị
 | 
Kiểu thao tác
 | 
Bắt buộc
 | 
Độ dài
 | 
Mô tả

 | 
1
 | 
Tiêu đề
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Fix Client 

Đọc dữ liệu từ thẻ Chíp

 | 
2
 | 
Nội dung
 | 
Lable
 | 
Read Only
 | 
--
 | 
--
 | 
Đưa điện thoại c

> ⚠️ *Nội dung đã cắt ngắn (28618 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 12.5. Job mở CIF/TKTT/Đăng ký dịch vụ MB tại BE Server (VNPay)

> **Page ID:** `155943855` · **Version:** 33
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/155943855

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới
 | 06/02/2023 | A | HongLT | 
 | 
Tạo mới
 | V0.0.1
 | 
 
 | M | ThuDM2 | V0.0.2 | 
Cập nhật mục Xử lý với các bản ghi có trạng thái "Chờ đăng ký MB"

• Ghi nhận và Insert thông tin QTNDN quản lý của KH vào bảng CUSTOMER | V0.0.2
 | 
 
 | M | HongLT | V.002 | 
Cập nhật thông tin loại giấy tờ truyền sang corebank để đăng ký mở CIF

• Nếu ngày cấp < 01/07/2024 → Truyền loại giấy tờ = CCCD
• Nếu ngày cấp >= 01/07/2024 → Truyền loại giấy tờ = CC | V.003
 | 
 
 | M | HongLT | 
 | 
Sau khi chạy Job đăng ký MB thành công, BO server lưu thêm thông tin KH từ bảng CUS_eKYC sang bảng CUS các trường : Ngày hết hạn GTTT, Trạng thái xác thực C06
 | 

 | 
 
 | M | HongLT | 
 | 
MB server cập nhật tách riêng mã lỗi kết nối tới Bank (Timeout (967) + Lỗi hệ thống do kết nối (999)) và trả về cho BE thay vì trả chung mã 999 như trước
 | 

 | 
 
 | M | ThaoCY | 
 | 
Cập nhật API createCifEkyc: bỏ truyền trường districtCode 
 | 

greywhitewhite1greysolidMục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn

 | 1. Tác nhân tham gia: | 
BE server, MB server (tham gia với vai trò đứng giữa BE server và HT Bank), eKYC Server, HT Bank

 | 2. Điều kiện trước: | 
• BE server đã lưu danh sách các KH đã đăng ký dịch vụ eKYC thành công trên App
• Trạng thái đăng ký của KH khách hàng là: 
- Job mở CIF: Chờ mở CIF, Timeout check face

- Job mở TKTT: Chờ mở TKTT , Timeout mở TKTT

- Job đăng ký SMS: Chờ đăng ký SMS, Timeout đăng ký SMS

- Job đăng ký MB: Chờ đăng ký MB

• Thời gian chạy Job không nằm trong khoảng thời gian chạy Batch (Cấu hình tại BE MB)
 | 3. Kết quả mong muốn: | 
• Job Mở CIF: KH được đăng ký mở CIF thành công
• Job Mở TKTT: KH được đăng ký mở TKTT thành công
• Job đăng ký SMS: KH được đăng ký SMS thành công
• Job Mở MB:  KH được đăng ký MB cho thành công với gói dịch vụ eKYC, trạng thái dịch vụ = Active Standby và KH nhận được kết quả thông tin đăng nhập MB qua SMS/Email
• Các SMS gửi đến KH từ Job có type SMS = eKYC

### 2/ Luồng xử lý Job

Lưu ý: Mô hình BE server thông qua MB server để kết nối tới HT Bank

greywhitewhite1greysolidDanh sách API

 | 
 | Danh sách API | Nguồn cấp API | Đầu vào | Đầu ra | Ghi chú
 | 1 | 
API Kiểm tra khuôn mặt từ BE server
 | eKYC Server | 
 | 
 | 

 | 2 | API kiểm tra thông tin KH theo GTTT, SĐT (CIF,TKTT, SMS) | Bank | 

 | 

 | 

 | 3 | API Đăng ký mở CIF từ BE server | Bank | 
 | 
 | 

 | 4 | API Đăng ký mở TKTT từ BE server | Bank | 
 | 
 | 

 | 5 | API đăng ký SMS Banking | Bank | 

 | 

 | 

### 2/ Sơ đồ trạng thái đăng ký

### 4/Mô tả Job

4.1. JOB Mở CIF

 | 
Xử lý với các bản ghi có trạng thái Chờ mở CIF

 | 1  | 
Quét danh sách có trạng thái Chờ mở CIF
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là Chờ mở CIF

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5 phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | Gửi yêu cầu kiểm tra khuôn mặt sang eKYC Server | 
BE server
 | 
Gửi yêu cầu kiểm tra khuôn mặt sang eKYC (API: http://10.22.7.197:27172/ekyc_cob/validate-ekyc)

Input: 

- sid: Số ID của bản ghi eKYC đã đăng ký trên App cho MB server

- phone: Sđt ekyc của KH

 | 
eKYC Server, eKYC AI
 | 
Kiểm tra check trùng khuôn mặt chính của KH với các khuôn mặt đã được mở CIF khác trong hệ thống eKYC, và Trả kết quả cho BE server

 | 
BE server 
 | 
BE server nhận kết quả: 

• Không hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Nếu tỷ lệ check trùng >= Ngưỡng (CONFIDENT_FACE_MAIN): Trả về kết quả trùng khuôn mặt | 
Cập nhật trạng thái đăng ký = Hủy và dừng quy trình và thông báo cho KH qua SMS "Quy khach mo tai khoan khong thanh cong do thong tin cua Quy khach da ton tai tren he thong. Ho tro: <Số điện thoại ho tro>."

 | 2 | Kết quả kiểm tra khuôn mặt = TO/ Lỗi hệ thống | 
Trạng thái bản ghi vẫn là "Chờ mở CIF"

• Hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Nếu tỷ lệ check trùng < Ngưỡng (CONFIDENT_FACE_MAIN) |  Trả về kết quả không trùng khuôn mặt → Chuyển bước 3 Gửi yêu cầu tạo CIF

 | 3 | 
Xử lý yêu cầu mở CIF
 | 
BE server / MB server 
 | 
1/ Kiểm tra cấu hình thời gian chạy Batch (Cấu hình tại tham số TIME_BATCH_EKYC ở BE)

• Không hợp lệ: Nếu thời gian chạy Job trong khoảng thời gian cấu hình chạy batch → Không gửi yêu cầu mở CIF sang Bank, giữ nguyên trạng thái bản ghi và chuyển bản ghi sang chu kỳ chạy Job lần sau cho đến khi nào hết thời gian chạy Batch
• Hợp lệ: Nếu thời gian chạy Job ngoài khoảng thời gian cấu hình chạy Batch → Gửi yêu cầu mở CIF sang Bank
2/ Gửi yêu cầu Mở CIF  đến HT Bank (API:  createCifEkyc). Các thông tin mở CIF bao gồm:
 | STT | Tên trường | Map API | Mô tả | Ghi chú
 | 1 | Loại giấy tờ tùy thân | peopleIDType | 
Loại GTTT KH đã eKYC:

• Type CCCD21 → Truyền loại giấy tờ = CCCD
• Type CCCD24 → Truyền loại giấy tờ = CC
• Nếu ngày cấp < 01/07/2024 → Truyền loại giấy tờ = CCCD
• Nếu ngày cấp >= 01/07/2024 → Truyền loại giấy tờ = CC | Việc truyền loại giấy tờ theo ngày cấp là giải pháp tạm thời cho đến khi hệ thống eKYC đọc và phân biệt được mẫu CCCD24 so với CCCD21
 | 2 | Số giấy tờ tùy thân | peopleID | Số GTTT KH đã eKYC | 

 | 3 | Tên Khách hàng | 
customerName 
 | Tên của KH theo GTTT đã eKYC | 

 | 4 | Ngày cấp | peopleIDDate | 
 | 

 | 5 | Nơi cấp | peopleIDAddre
ss | 
 | 

 | 6 | Số CMND cũ | oldPeopleID | Số CMND cũ nếu đọc được từ CCCD chip | Không bắt buộc
 | 7 | Giới tính | gender | 
 | 

 | 7 | Ngày sinh | birthDay | 
 | 

 | 8 | Tỉnh/TP (Nơi ở hiện tại) | 
provinceCode 
 | Thông tin KH đã nhập khi đăng ký | 

 | 9 | Quận/Huyện (Nơi ở hiện tại) | districtCode  | Thông tin KH đã nhập khi đăng ký | 

 | 10 | Phường/Xã (Nơi ở hiện tại) | wardCode | Thông tin KH đã nhập khi đăng ký | 

 | 11 | Địa chỉ (Nơi ở hiện tại) | addressLine | Thông tin KH đã nhập khi đăng ký | 

 | 12 | Địa chỉ thường trú | 
residenceAddre
ss
 | Đọc được từ giấy tờ | 

 | 13 | Quốc tịch | nationalty | Đọc được từ giấy tờ | 

 | 14 | Số điện thoại | mobile | SĐT thực hiện xác thực OTP để đăng ký eKYC | 

 | 15 | Email | Email | Email KH đã nhập | 

 | 16 | Chi nhánh quản lý tài khoản | branchCode | Chi nhánh  Đơn vị quản lý TKTT KH đã chọn khi đăng ký (Truyền vào cấp PGD) | 

 | 17 | Quỹ tín dụng nhân dân quản lý | pcfCode | QTDND KH đã chọn khi đăng ký (Nếu có) | 

 | 18 | Ngành kinh tế | custCat | Thông tin KH đã nhập khi đăng ký | Theo dữ liệu KH chọn 
 | 19 | Kênh | systemID | Kênh eKYC  | 

 | 21 | Ngày đăng ký | createDate | Ngày gửi yêu cầu đăng ký dịch vụ trên App thành công bằng eKYC | 

 | 
 | 

 | HT Bank | Hệ thống Bank thực hiện mở CIF và trả kết quả cho BE server. HT Bank lưu kênh mở CIF = eKYC
 | 
 | 

 | BE server / MB server  | BE server nhận kết quả do Bank trả
• Không thành công | TT | Trường hợp | Xử lý
 | 1 | Kết quả mở CIF timeout (967) + Lỗi hệ thống do kết nối (999) | 
Cập nhật trạng thái "Timeout mở CIF"

 | 2 | Các mã lỗi do Bank trả  | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Mở CIF thành công | 
1/ Cập nhật trạng thái "Chờ mở TKTT"

2/ Lưu lại thông tin số CIF đã mở thành công, bao gồm:

• Số CIF của KH (cifNo)
• Tên KH  (cifName)

4.2. JOB Mở TKTT

 | STT | 
Bước  thực hiên
 | 
Tác nhân
 | 
Mô tả xử lý

 | 
Xử lý với các bản ghi có trạng thái "Chờ mở TKTT"

 | 1 | 
Quét danh sách có trạng thái "Chờ mở TKTT"
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là "Chờ mở TKTT"

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5 phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | 
Gửi yêu cầu mở TKTT
 | BE server / MB server  | 
1/ Kiểm tra cấu hình thời gian chạy Batch (Cấu hình tại tham số TIME_BATCH_EKYC ở BE)

• Không hợp lệ: Nếu thời gian chạy Job trong khoảng thời gian cấu hình chạy batch → Không gửi yêu cầu mở TKTT sang Bank, giữ nguyên trạng thái bản ghi và chuyển bản ghi sang chu kỳ chạy Job lần sau cho đến khi nào hết thời gian chạy Batch
• Hợp lệ: Nếu thời gian chạy Job ngoài khoảng thời gian cấu hình chạy Batch → Gửi yêu cầu mở TKTT sang Bank
2/ Gửi yêu cầu mở TKTT sang HT Bank bao gồm các thông tin:
 | STT | Tên trường | Map API | Mô tả | Ghi chú
 | 1 | Mã khách hàng | cifNo | 
Là số CIF Bank đã trả ở bước đăng ký mở CIF  (API:  createCifEkyc)(Với KH mới)

Hoặc số CIF Bank trả ở API truy vấn "queryCustEkyc" (Với KH cũ)
 | 

 | 2 | Chi nhánh mở tài khoản | branchCode | Là chi nhánh KH đã chọn lúc đăng ký | 

 | 3 | Người giới thiệu | mobile | Là SĐT của người giới thiệu KH đã thêm ở lúc đăng ký (nếu có) | Không bắt buộc
 | 4 | Kênh mở | systemID | 
 | 

 | 3 | 
 Xử lý gửi yêu cầu mở tài khoản thanh toán
 | HT Bank | 
Hệ thống Bank thực hiện mở tài khoản thanh toán và trả kết quả cho BE server. Lưu kênh mở TKTT = eKYC

 |   | 
 | BE server / MB server  | 
5.1/ BE server nhận kết quả

• 
Không thành công
 | 
TT
 | 
Trường hợp
 | 
Xử lý

 | 
1
 | 
Kết quả mở TKTT timeout (967) + Lỗi hệ thống do kết nối (999)
 | 
Cập nhật trạng thái "Timeout mở TKTT"

 | 2 | Các mã lỗi do Bank trả | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• 
Thành công:
 | 
TT
 | 
Trường hợp
 | 
Xử lý

 | 
1
 | 
Mở TKTT thành công
 | 
• 
Lưu lại thông tin số TKTT đã mở và cập nhật trạng thái đăng ký = Chờ đăng ký MB

 | 
Xử lý với các bản ghi có trạng thái "Timeout mở TKTT"

 | 1 | 
Quét danh sách có trạng thái "Timeout mở TKTT"
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là "Timeout mở TKTT"

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5 phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | 
Kiểm tra KH đã mở TKTT thành công chưa
 | 
BE server / MB server 
 | 
1/ Kiểm tra cấu hình thời gian chạy Batch (Cấu hình tại tham số TIME_BATCH_EKYC ở BE)

• Không hợp lệ: Nếu thời gian chạy Job trong khoảng thời gian cấu hình chạy batch → Không gửi yêu cầu mở TKTT sang Bank, giữ nguyên trạng thái bản ghi và chuyển bản ghi sang chu kỳ chạy Job lần sau cho đến khi nào hết thời gian chạy Batch
• Hợp lệ: Nếu thời gian chạy Job ngoài khoảng thời gian cấu hình chạy Batch → Gửi yêu cầu mở TKTT sang Bank
2/ MB gửi yêu cầu kiểm tra KH đã mở TKTT chưa?

Input: Checktype = ACC, Số GTTT

 | 
 | 
 
 | 
HT Bank
 | 
Xử lý và trả kết quả

 | 3 | 
Kiểm tra và xử lý yêu cầu mở TKTT
 | BE server / MB server  | 
Nhận kết quả và xử lý

• Không hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Lỗi hệ thống do kết nối (999) | Vẫn giữ nguyên trạng thái "Timeout mở CIF"
 | 2 | Lỗi Timeout (967)
 | 3 | Nếu KH có > 1 TKTT | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• Hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Nếu KH có 1 TKTT  | Lưu thông tin số TKTT  và cập nhật trạng thái đăng ký của KH = "Chờ đăng ký SMS"
 | 2 | Nếu không có TKTT nào | Gửi yêu cầu mở TKTT sang HT Bank

 | 
 | 

 | HT Bank | 
Hệ thống Bank thực hiện mở tài khoản thanh toán và trả kết quả cho BE server

 |   | 
 | BE server / MB server  | 
BE server nhận kết quả

• Không thành công | TT | Trường hợp | Xử lý
 | 1 | Kết quả mở TKTT timeout (967) + Lỗi hệ thống do kết nối (999) | 
Cập nhật trạng thái "Timeout mở TKTT"

 | 2 | Các mã lỗi do Bank trả | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Mở TKTT thành công | 
Lưu lại thông tin số TKTT đã mở và cập nhật trạng thái đăng ký = Chờ đăng ký MB

4.3. JOB Đăng ký SMS
 | STT | 
Bước  thực hiên
 | 
Tác nhân
 | 
Mô tả xử lý

 | 
Xử lý với các bản ghi có trạng thái "Chờ đăng ký SMS"

 | 1 | 
Quét danh sách có trạng thái "Chờ đăng ký SMS"
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là "Chờ đăng ký MB"

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | 
Gửi yêu cầu đăng ký SMS Banking
 | BE server / MB server  | 
Gửi yêu cầu đăng ký dịch vụ SMS tới Bank với các thông tin (API: registerSMSEkyc)
 | STT | Tên trường | Map API | Mô tả | Ghi chú
 | 1 | Mã khách hàng | cifNo | 
Là số CIF Bank đã trả ở bước đăng ký mở CIF  (API:  createCifEkyc)(Với KH mới)

Hoặc số CIF Bank trả ở API truy vấn "queryCustEkyc" (Với KH cũ)
 | 

 | 2 | Tài khoản thanh toán | 
accountNo 
 | 
Là số TKTT đã trả ở bước đăng ký mở TKTT (API:  createCurrentAccEkyc)(Với KH mới)

Hoặc số TKTT Bank trả ở API truy vấn "queryCustEkyc" (Với KH cũ)
 | 

 | 3 | Số điện thoại | 
mobile 
 | Số điện thoại KH đang thực hiện eKYC | 

 |   | 
 
 | HT Bank | 
Thực hiện đăng ký SMS và trả kết quả cho MB Banking.

 |   | 
 
 | BE server / MB server  | 
BE server nhận kết quả đăng ký SMS 

• Không thành công | TT | Trường hợp | Xử lý
 | 1 | Kết quả đăng ký SMS timeout (967) + Lỗi hệ thống do kết nối (999) | 
Cập nhật trạng thái "Timeout đăng ký SMS"

 | 2 | Các mã lỗi do Bank trả | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Đăng ký SMS thành công | 
Cập nhật trạng thái "Chờ đăng ký MB" → Chuyển bước chạy Job đăng ký MB

 | 
Xử lý với các bản ghi có trạng thái "Timeout đăng ký SMS"

 | 1 | 
Quét danh sách có trạng thái "Timeout đăng ký SMS"
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là "Timeout đăng ký SMS"

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5 phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | Gửi yêu cầu sang HT Bank để kiểm tra KH đã đăng ký SMS thành công trên HT Bank chưa? | 
BE server / MB server 
 | 
1/ Kiểm tra cấu hình thời gian chạy Batch (Cấu hình tại tham số TIME_BATCH_EKYC ở BE)

• Không hợp lệ: Nếu thời gian chạy Job trong khoảng thời gian cấu hình chạy batch → Không gửi yêu cầu sang Bank, giữ nguyên trạng thái bản ghi và chuyển bản ghi sang chu kỳ chạy Job lần sau cho đến khi nào hết thời gian chạy Batch
• Hợp lệ: Nếu thời gian chạy Job ngoài khoảng thời gian cấu hình chạy Batch → Gửi yêu cầu sang Bank
2/ Gửi yêu cầu check thông tin KH đã đăng ký SMS tại hệ thống bank theo số GTTT chưa? (API: queryCustEk

> ⚠️ *Nội dung đã cắt ngắn (24474 ký tự gốc). Xem đầy đủ trên Confluence.*


---

### 12.6. Job xử lý riêng cho các bản ghi Timeout mở CIF

> **Page ID:** `175441454` · **Version:** 13
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/175441454

greywhitewhite1greysolidPhiên bản tài liệu
A - Tạo mới; M - Sửa đổi; D - Xóa bỏ
 | Ngày thay đổi | Lý do | Người sửa | Phiên bản cũ | Mô tả thay đổi | Phiên bản mới | Thời gian cập nhật
 | 09/03/2023 | A | HongLT | 
 | 
Tạo mới
 | V.1 | 

 | 
 
 | M | HongLT | 
 | 
MB server cập nhật tách riêng mã lỗi kết nối tới Bank (Timeout (967) + Lỗi hệ thống do kết nối (999)) và trả về cho BE thay vì trả chung mã 999 như trước
 | 
 | 

greywhitewhite1greysolidMục lục

### 1/ Tác nhân, điều kiện trước, kết quả mong muốn
greywhitewhite1greysolidTác nhân, điều kiện, kết quả mong muốn

 | 1. Tác nhân tham gia: | 
MB Server, MB server (tham gia với vai trò đứng giữa BE server và HT Bank) , eKYC Server, HT Bank

 | 2. Điều kiện trước: | 
• Các KH có trạng thái Mở CIF timeout
• Thời gian chạy Job không nằm trong khoảng thời gian chạy Batch (Cấu hình tại BE MB)
 | 3. Kết quả mong muốn: | 
• KH được đăng ký mở CIF/ TKTT/ SMS/MB thành công

### 2/ Luồng xử lý Job

Lưu ý: Mô hình BE server thông qua MB server để kết nối tới HT Bank

### 4/Mô tả Job

4.1. JOB Mở CIF
Mở CIF+ TKTT+ Dịch vụ SMB

 | 
Xử lý với các bản ghi có trạng thái "Timeout mở CIF"

 | 1 | 
Quét danh sách có trạng thái "Timeout mở CIF"
 | 
BE server 
 | 
1/ BE server truy vấn danh sách KH eKYC có trạng thái bản ghi đăng ký là "Timeout mở CIF"

2/ Số lượng quét thỏa mãn điều kiện:

- Tần suất: 5 phút/ lần

- Số lượng bản ghi trên 1 lô: 500 bản ghi

 | 2 | Gửi yêu cầu kiểm tra khuôn mặt sang eKYC Server | 
BE server 
 | 
Gửi yêu cầu kiểm tra khuôn mặt sang eKYC (Theo requestID, SĐT ...)

 |   |   | 
eKYC Server, eKYC AI
 | 
Kiểm tra check trùng khuôn mặt chính của KH với các khuôn mặt đã được mở CIF khác trong hệ thống eKYC, và Trả kết quả cho BE server

 |   |   | 
BE server
 | 
BE server nhận kết quả: 

• Không hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Nếu tỷ lệ check trùng >= Ngưỡng (CONFIDENT_FACE_MAIN): Trả về kết quả không trùng khuôn mặt | 
Cập nhật trạng thái đăng ký = Hủy và dừng quy trình và thông báo cho KH qua SMS/ Email "Quy khach mo tai khoan khong thanh cong do thong tin cua Quy khach da ton tai tren he thong. Ho tro: <Số điện thoại ho tro>."

 | 2 | Kết quả kiểm tra khuôn mặt = TO | 
Trạng thái bản ghi vẫn là Timeout mở CIF

• Hợp lệ | TT | Trường hợp | Xử lý
 | 1 | Nếu tỷ lệ check trùng >= Ngưỡng (CONFIDENT_FACE_MAIN) |  Trả về kết quả không trùng khuôn mặt → Chuyển bước 3 Gửi yêu cầu kiểm tra KH đã tạo CIF thành công chưa?

 | 3 | Gửi yêu cầu sang HT Bank để kiểm tra KH đã tạo CIF thành công trên HT Bank chưa? | 
BE server
 | 
1/ Kiểm tra cấu hình thời gian chạy Batch (Cấu hình tại tham số TIME_BATCH_EKYC ở BE)

• Không hợp lệ: Nếu thời gian chạy Job trong khoảng thời gian cấu hình chạy batch → Không gửi yêu cầu sang Bank, giữ nguyên trạng thái bản ghi và chuyển bản ghi sang chu kỳ chạy Job lần sau cho đến khi nào hết thời gian chạy Batch
• Hợp lệ: Nếu thời gian chạy Job ngoài khoảng thời gian cấu hình chạy Batch → Gửi yêu cầu sang Bank
2/ Gửi yêu cầu check thông tin KH đã có CIF tại hệ thống bank theo số GTTT chưa?

Input: 

• Checktype = ALL
• Số điện thoại eKYC
• Loại giấy tờ
• Số GTTT
 | 
 |   | 
HT Bank
 | 
Xử lý và trả kết quả gồm:

Output:
 | 
 | Thông tin | Giá trị
 | 
1
 | 
cifNo (Mã KH)
 | 
NULL: số GTTT chưa có mã CIF  trên core

Có giá trị nếu tìm được

 | 
2
 | 
Tên KH
 | 
NULL: số GTTT chưa có mã CIF  trên core

Có giá trị nếu tìm được

 | 
3
 | 
Branch_code (Mã ĐV quản lý mã KH)
 | 
NULL: số GTTT chưa có mã CIF  trên core

Có giá trị nếu tìm được và trả mã cn qly (nếu là mã được mở ở QTDND cũ_ lưu ý riêng của core)

 | 
4
 | 
Branch_name (Tên ĐV quản lý mã KH)
 | 
NULL số GTTT chưa có mã CIF  trên core

Có giá trị nếu tìm được

 | 
5
 | 
ListAccount[{accountNo, branch_code, branch_name }, {…}, …](Danh sách tài khoản)
 | 
NULL số GTTT chưa có mã CIF  trên core

NULL nếu đã có mã CIF nhưng không có TKTT ở trạng thái hoạt động

Danh sách TKTT nếu số GTTT đã có mã CIF và có TKTT ở trạng thái hoạt động

 | 
6
 | 
mobile (Số điện thoại eKYC)
 | 
NULL nghĩa là số điện thoại eKYC chưa đăng ký dịch vụ SMS.

Có giá trị nếu số điện thoại đã đăng ký SMS

 | 
7
 | 
Cif_sms (Mã KH đăng ký SMS bằng SĐT eKYC)
 | 
NULL nếu SĐT eKYC chưa đăng ký SMS

Có giá trị nếu số điện thoại eKYC đã đăng ký SMS

 | 
8
 | 
Mobile_cif (Số điện thoại SMS của mã CIF)
 | 
NULL nghĩa là số GTTT chưa sử dụng dịch vụ SMS. Nếu số GTTT đã sử dụng SMS thì trả ra số điện thoại đã đăng ký SMS của khách hàng có GTTT đó.

 | 
 |   | 
BE server
 | 
Nhận kết quả và kiểm tra

• Không thành công | TT | Trường hợp | Xử lý
 | 1 | Lỗi hệ thống do kết nối (999) | Vẫn giữ nguyên trạng thái "Timeout mở CIF"
 | 2 | Lỗi Timeout (967)

• Thành công: BE server kiểm tra và so sánh các thông tin Bank trả theo bảng dưới đây (Null : Không trả ra giá trị nào, x là có trả giá trị) | 
STT
 | 
Tình huống
 | 
CIF
 | 
Mobile(eKYC)
 | 
CIF_sms
 | 
Mobile_CIF
 | 
Kết quả

 | 
1
 | 
Số GTTT và SĐT eKYC chưa tồn tại ở corebank
 | 
Nulll
 | 
null
 | 
null
 | 
null
 | 
Hợp lệ → BE server Gửi yêu cầu mở CIF sang HT Bank

 | 
2
 | 
Số GTTT đã tồn tại, SĐT eKYC chưa tồn tại ở Corebank, KH chưa đăng ký SMS bằng số khác
 | 
x
 | 
null
 | 
null
 | 
null
 | 
Hợp lệ

BE server kiểm tra số lượng TKTT của KH mà Bank đã trả ở bước 3

• Lớn hơn 1 → Cập nhật trạng thái "Lỗi đăng ký" , gửi thông báo cho KH qua SMS "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro."--> Dừng quy trình
• Bằng 1 → Cập nhật trạng thái "Chờ đăng ký SMS" -->Chuyển bước  chạy Job đăng ký SMS, đăng ký MB đã mô tả tại <>
• Null --> Cập nhật trạng thái "Chờ mở TKTT" → Chuyển bước chạy Job đăng ký TKTT đã mô tả <>
(Nội dung SMS cấu hình được tại BE/ tách riêng mã lỗi với trường hợp 3 Không hợp lệ phía dưới)

 | 
3
 | 
Số GTTT, SĐT eKYC đã tồn tại ở Corebank và thuộc về cùng 1 người
 | 
x
 | 
x
 | 
x

(BE server kiểm tra CIF_SMS=CIF → Hợp lệ)

Nếu CIF_SMS # CIF → Không hợp lệ (Là trường hợp 4 bên dưới)
 | 
x
 | 
Hợp lệ

BE server kiểm tra số lượng TKTT của KH mà Bank đã trả ở bước 3

• Lớn hơn 1 → Cập nhật trạng thái "Lỗi đăng ký" , gửi thông báo cho KH qua SMS "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro."--> Dừng quy trình
•  Bằng 1 → Cập nhật trạng thái "Chờ đăng ký MB " → Chuyển bước  chạy Job đăng ký MB đã mô tả tại <>
• Null →Cập nhật trạng thái "Chờ mở TKTT"--> Chuyển bước chạy Job đăng ký TKTT đã mô tả <>
(Nội dung SMS cấu hình được tại BE/ tách riêng mã lỗi với trường hợp 3 Không hợp lệ phía dưới)

 | 
4
 | 
Số GTTT đã tồn tại, Số điện thoại eKYC đã đăng ký cho KH khác
 | 
X
 | 
x
 | 
x

(BE server kiểm tra CIF_SMS # CIF)
 | 
null
 | 
Không hợp lệ → Gửi thông báo lỗi cho KH qua SMS với nội dung "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro."

(Nội dung cấu hình được tại BE)

 | 
5
 | 
Số GTTT đã tồn tại, SĐT eKYC chưa tồn tại ở Corebank, nhưng KH đã đăng ký SMS bằng số khác
 | 
x
 | 
null
 | 
null
 | 
x

(BE server kiểm tra Mobile_CIF # SĐT đang thực hiện eKYC)
 | 
Không hợp lệ → Gửi thông báo lỗi cho KH qua SMS với nội dung "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro.i"

(Nội dung cấu hình được tại BE)

 | 
6
 | 
Số GTTT chưa tồn tại, nhưng SĐT eKYC đã tồn tại
 | 
Null
 | 
x
 | 
x
 | 
null
 | 
Không hợp lệ → Gửi thông báo lỗi cho KH qua SMS với nội dung "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro."

(Nội dung cấu hình được tại BE)

 | 4.  | Xử lý yêu cầu mở CIF | HT Bank | Hệ thống Bank thực hiện mở CIF và trả kết quả cho BE server. HT Bank lưu kênh mở CIF = eKYC
 | 
 |   | BE server | BE server nhận kết quả
• Không thành công | TT | Trường hợp | Xử lý
 | 1 | Kết quả mở CIF timeout (967) + Lỗi hệ thống do kết nối (999) | 
Giữ nguyên trạng thái "Timeout mở CIF"

 | 2 | Các mã lỗi do Bank trả | 
Cập nhật trạng thái đăng ký = "Lỗi đăng ký"  → Gửi thông báo cho KH qua SMS  "QK chua đang ky thanh cong dich vu Co-opBank Mobile Banking. Vui long lien he Hotline 1900545554 hoac Chi nhanh/Phong giao dich cua Co-opBank de duoc ho tro." → Dừng quy trình  

• Thành công: | TT | Trường hợp | Xử lý
 | 1 | Mở CIF thành công | 
1/ Cập nhật trạng thái Chờ mở TKTT

2/ Lưu lại thông tin số CIF đã mở thành công.

---

### 12.7. Backend eKYC

> **Page ID:** `139920523` · **Version:** 3
> **URL:** https://wiki.servicehub.vn/spaces/URDMBCOOPBANK/pages/139920523

Link tài liệu BE để tham chiếu sang Project BE CoopBank

---



# Checklist Review PRD Nghiep Vu

## 1) Scope va muc tieu
- Muc tieu kinh doanh co do luong duoc khong?
- Co out-of-scope de tranh scope creep khong?
- Persona/chanel su dung da ro rang chua?

## 2) Flow nghiep vu
- Co day du happy path?
- Co edge cases: duplicate, timeout, external service fail?
- Co xu ly rollback/compensation khi loi giua luong?

## 3) Rule va du lieu
- Input validation co ro (format, do dai, uniqueness)?
- Business rule co conflict giua cac phan?
- Data ownership, source of truth, retention da xac dinh?

## 4) UX state va thong diep
- Day du loading/disabled/error/success states?
- Message loi co huong dan thao tac tiep theo?
- Co phan biet loi user va loi he thong?

## 5) Bao mat va compliance
- Co PII/sensitive data? Da noi ro cach bao ve?
- Co yeu cau audit log, masking, phan quyen?
- Co rui ro lien quan PCI-DSS/PDPA/GDPR (neu ap dung)?

## 6) Tinh kha thi ky thuat
- Dependency API/3rd-party da duoc liet ke?
- SLA/SLO, timeout, retry policy da co?
- Assumption quan trong da duoc chot?

## 7) Acceptance criteria
- Moi FR co AC cu the, test duoc?
- AC co dung ngon ngu pass/fail?
- NFR co metric do duoc (latency, reliability, security)?

## 8) Testability
- Co bo test scenario toi thieu cho QA/UAT?
- Co du lieu test va precondition?
- Co tieu chi go/no-go cho release?

## 9) Van hanh sau go-live
- Co monitoring + alert cho KPI chinh?
- Co runbook xu ly su co?
- Co ke hoach rollout/rollback?

# Checklist Review UX

## 1) Scope va user task
- User persona va context su dung da ro chua?
- Muc tieu task co do duoc bang KPI/metric khong?
- In-scope/out-of-scope da du de tranh review lan man chua?

## 2) Information architecture
- Thong tin co sap xep dung muc uu tien khong?
- Label, heading, CTA co ro nghia va nhat quan khong?
- Co noi dung/option nao gay nham lan cho user khong?

## 3) Task flow
- Happy path co lien tuc, khong dead-end khong?
- Co xu ly back/edit/cancel de user thoat loi khong?
- Co edge case: duplicate, timeout, session het han, fail API?

## 4) Form va validation
- Required/optional fields ro rang?
- Validation message co noi ro ly do va cach sua?
- Input format, max length, masking, autofill da hop ly?

## 5) States va feedback
- Day du loading/empty/error/success/disabled?
- Sau action quan trong co feedback ngay lap tuc?
- Retry/recovery path co ro va de thao tac?

## 6) Consistency voi design system
- Pattern component co dung cung mot logic tren cac man?
- Spacing/typography/icon/mau co dong nhat?
- Interaction states (hover/focus/active) co nhat quan?

## 7) Accessibility co ban
- Contrast text va control dat nguong de doc?
- Keyboard navigation va focus visible su dung duoc?
- Error message co lien ket den field va de nhan biet?

## 8) Responsive va device behavior
- Mobile/tablet/desktop co giu dung intent UX?
- Breakpoint co lam vo layout hoac mat uu tien thong tin?
- Touch target tren mobile co du lon?

## 9) Implementation readiness
- Requirement UX co du cu the de FE build?
- Co acceptance criteria testable cho QA?
- Co can bo sung state/edge case truoc handoff?

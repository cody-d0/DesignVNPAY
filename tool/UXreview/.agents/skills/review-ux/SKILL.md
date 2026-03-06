---
name: review-ux
description: Reviews UX artifacts for clarity, usability, accessibility, consistency, and implementation readiness. Use when the user asks for a UX review, heuristic evaluation, user flow assessment, wireframe/prototype feedback, or pre-handoff UX QA.
---

# Review UX

## Muc tieu

Review UX de tim van de co tac dong cao den:
- kha nang hoan thanh task cua user
- do ro rang cua thong tin va luong thao tac
- tinh nhat quan va kha nang mo rong cua giao dien
- a11y va kha nang implement truoc handoff

Uu tien phat hien theo rui ro: blocker task > confusion > inconsistency.

## Dau vao uu tien

- Design artifact (Figma, wireframe, prototype, screenshot)
- User flow + business rule lien quan (neu co)
- Persona, context su dung, device target (neu co)
- Constraint ky thuat va design system (neu co)

Trong project nay, uu tien tham chieu khi can:
- `.agents/docs/prd-registration-mapping.mdc`
- `.agents/docs/design-system.mdc`

## Quy trinh review

1. Chot pham vi va bai toan UX
- User la ai, task chinh la gi, KPI thanh cong la gi
- In-scope/out-of-scope cho lan review nay

2. Kiem tra task flow end-to-end
- Co duoc happy path tu start den success
- Co xu ly huong quay lai, sua du lieu, thoat giua chung
- Co dead-end hoac loop gay mac ket khong

3. Kiem tra thong tin va hierarchy
- Tieu de, label, CTA co ro va dung ky vong
- Uu tien noi dung theo muc do quan trong
- Form field, helper text, error text co de hieu va co hanh dong tiep theo

4. Kiem tra state va feedback
- Loading, empty, error, success, disabled day du
- Co phan biet loi user input va loi he thong
- Co thong bao sau action (save, submit, retry)

5. Kiem tra consistency va design system
- Component pattern dung cung mot logic giua cac man
- Khoang cach, typography, icon, mau sac khong xung dot
- Hanh vi tuong tac (hover/focus/active) nhat quan

6. Kiem tra accessibility co ban
- Contrast du de doc
- Focus order hop ly, keyboard navigation kha thi
- Label/aria semantic ro rang cho control quan trong

7. Kiem tra implementation readiness
- Requirement UX du cu the de FE implement
- Edge case va validation duoc mo ta testable
- Co metric hoac acceptance criteria de QA xac nhan

## Tieu chi danh gia

Phan loai muc do:
- Critical: Chan user hoan thanh task, rui ro a11y nghiem trong, hoac sai intent nghiep vu.
- Major: Gay confusion lon, tang ty le loi/bo dở, hoac kho implement dung.
- Minor: Van de polish, consistency, copywriting, hoac tinh toi uu.

## Mau output bat buoc

Dung dung format sau:

```markdown
# UX Review - <ten man hinh/flow>

## Tong quan
- Scope: ...
- User task chinh: ...
- Danh gia nhanh: ...

## Findings
### Critical
- [UX-001] Van de:
  - Bang chung:
  - Tac dong:
  - De xuat:

### Major
- ...

### Minor
- ...

## Cau hoi can chot
- [Q1] ...
- [Q2] ...

## Acceptance criteria de xuat bo sung
- [AC-UX-01] ...
- [AC-UX-02] ...

## Test scenarios toi thieu
- [ ] Happy path
- [ ] Validation/negative
- [ ] State transitions (loading/empty/error/success)
- [ ] Keyboard + focus order
- [ ] Responsive breakpoints
```

## Nguyen tac phan hoi

- Uu tien impact va hanh dong cu the.
- Moi finding phai co bang chung + tac dong + huong sua.
- Neu de xuat thay doi, neu ro trade-off.
- Neu thieu context, ghi ro assumption.

## Tai lieu tham chieu

- Checklist chi tiet: [checklist.md](checklist.md)

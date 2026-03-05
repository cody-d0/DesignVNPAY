---
name: review-prd-nghiep-vu
description: Reviews business PRDs for clarity, completeness, consistency, feasibility, risk, and testability. Use when the user asks to review a PRD, validate business requirements, assess nghiệp vụ flows, or identify gaps before planning or implementation.
---

# Review PRD Nghiệp Vu

## Muc tieu

Review PRD theo goc nhin nghiep vu de phat hien:
- thieu yeu cau, mo ta mo ho, mau thuan logic
- rui ro van hanh, bao mat, phap ly, du lieu
- diem kho verify trong QA/UAT

Uu tien phat hien quan trong truoc, de xuat cach xu ly cu the.

## Dau vao uu tien

- PRD goc (bat buoc)
- Tai lieu mapping/rules lien quan trong repo (neu co)
- Constraint ky thuat, legal, compliance (neu co)

Trong project nay, uu tien doc cac file sau khi can:
- `.cursor/rules/prd-registration-mapping.mdc`
- `.cursor/rules/screen-count-extraction.mdc`
- `.cursor/rules/design-system.mdc`

## Quy trinh review

1. Xac dinh pham vi
- Muc tieu kinh doanh
- Doi tuong nguoi dung
- In-scope/out-of-scope

2. Kiem tra do day du nghiep vu
- Happy path va edge cases
- Error states, loading states, retry/rollback
- Rule dieu kien truoc/sau (pre/post conditions)

3. Kiem tra tinh ro rang va nhat quan
- Dinh nghia thuat ngu khong xung dot
- Input/output tung buoc ro rang
- So lieu, timeout, gioi han, threshold co cu the

4. Kiem tra tinh kha thi va phu thuoc
- Dependency giua UI/API/data/ops
- Assumption an danh
- Muc can thiet de release

5. Kiem tra compliance va rui ro
- PII/bao mat/phan quyen
- Logging/audit trail
- Fail-safe va khui phuc sau loi

6. Kiem tra testability
- Moi requirement co acceptance criteria
- Co the viet testcase xac thuc duoc
- Co metrics de do thanh cong

## Tieu chi danh gia

Phan loai muc do:
- Critical: Co the gay sai nghiep vu, vi pham compliance, hoac block release.
- Major: Lam tang rui ro go-live, kho van hanh, hoac kho test day du.
- Minor: Van de ro rang/trinh bay/tinh day du khong nghiem trong.

## Mau output bat buoc

Dung dung format sau:

```markdown
# PRD Review - <ten PRD>

## Tong quan
- Scope: ...
- Danh gia nhanh: ...

## Findings
### Critical
- [ID] Van de:
  - Bang chung:
  - Tac dong:
  - De xuat:

### Major
- ...

### Minor
- ...

## Cau hoi can chot voi Business
- [Q1] ...
- [Q2] ...

## Acceptance Criteria de xuat bo sung
- [AC-01] ...
- [AC-02] ...

## Test Scenarios toi thieu
- [ ] Happy path
- [ ] Negative/validation
- [ ] Timeout/retry
- [ ] Permission/compliance
```

## Nguyen tac phan hoi

- Ngan gon, uu tien hanh dong.
- Moi finding phai co tac dong va de xuat ro.
- Khong chi noi "thieu"; phai chi ra can bo sung gi de team implement/test duoc.
- Neu thieu thong tin nguon, neu ro assumption.

## Tai lieu tham chieu

- Checklist chi tiet: [checklist.md](checklist.md)

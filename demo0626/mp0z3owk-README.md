# 🐚 Shell Architecture — BOOKING (Vietnam Airlines)

> **Domain:** Booking & Search · **Pattern:** Transaction Flow
> **Generated:** 2026-05-08 via shell-architecture skill

## Shell Registry

| # | Shell | File | Reuse | Primary SF |
|:-:|---|---|:-:|---|
| 1 | 🐚 SearchShell | [search-shell.md](search-shell.md) | 1 SF | SF1 |
| 2 | 🐚 BookingShell | [booking-shell.md](booking-shell.md) | 1 SF | SF1 |
| 3 | 🐚 PaymentShell | [payment-shell.md](payment-shell.md) | 1 SF | SF1 |
| 4 | 🐚 ConfirmationShell | [confirmation-shell.md](confirmation-shell.md) | 1 SF | SF1 |

## Slot Inventory

| Shell | Slots |
|---|---|
| SearchShell | InputArea, DateArea |
| BookingShell | ResultsList, AddOnsArea, PriceArea |
| PaymentShell | ActionArea, AddCardArea |
| ConfirmationShell | MainContent, ShareArea |

## Variation Density (Transaction Flow)

| Shell | 🔁 SHARED | ⭐ ĐẶC THÙ | Total |
|---|:-:|:-:|:-:|
| SearchShell | 2 | 2 | 4 |
| BookingShell | 3 | 1 | 4 |
| PaymentShell | 2 | 0 | 2 |
| ConfirmationShell | 1 | 1 | 2 |
| **Total** | **8** | **4** | **12** |

⭐ < 🔁 acceptable (transaction-flow shells reuse common payment + UI patterns).

## Quality Gates

| # | Gate | Status |
|:-:|---|:-:|
| 1-12 | All 12 gates verified | ✅ PASS (12/12) |

# 🧩 Molecule Library — Booking & Search (BOOKING) — 12 Components

```
Legend: 🔁 SHARED · ⭐ ĐẶC THÙ · 🔄 REUSE
```

## Group 1 · `SearchShell.InputArea` — Search inputs

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-01 · OriginInputSmart** | 🔁 | MH-B1 + Home shortcut · OriginField · GPSLocationBadge · RecentOriginsDropdown |
| **M-02 · DestinationInput** | 🔁 | MH-B1 + Home shortcut · DestinationField · PopularDestinationChips · VoiceInputCTA |
| **M-03 · PassengerCounter** | 🔁 | MH-B1 + booking review · AdultCounter · ChildCounter · InfantCounter · GroupBookingCTA |

## Group 2 · `SearchShell.DateArea` — Flex pricing

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-04 · FlexPricingCalendar** | ⭐ | MH-B1 only · CalendarHeatmap · CheapDayHighlight · ExpensiveDayWarning · FlexibilityToggle |

## Group 3 · `BookingShell.ResultsList` — Flight options

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-05 · FlightOptionCard** | 🔁 | MH-B2 + IROP alternates · FlightTimeline · FareClassPicker · PriceDisplay · AmenitiesIcons |

## Group 4 · `BookingShell.PriceArea` — Total upfront

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-06 · TotalPriceUpfront** | 🔁 | MH-B4 + MH-B5 · BasePriceLine · TaxesBreakdown · AncillariesAdded · TotalPriceLarge · MilesEarnPreview |

## Group 5 · `BookingShell.AddOnsArea` — Seat + Meal

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-07 · SeatPicker** | 🔁 | MH-B4 + Check-in re-pick · SeatMap · SeatTypeIcons · TierFreeSeatBadge · SunlightIntegration |
| **M-08 · MealSelector** | 🔁 | MH-B4 + Check-in re-select · MealCategoryTabs · DietaryIcons · TierFreeMealBadge |

## Group 6 · `PaymentShell.ActionArea` — 1-tap pay

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-09 · OneTapPayBiometric** | 🔁 | MH-B5 + Reward redemption · SavedCardDisplay · BiometricPrompt · ApplePayGooglePayButton · AddNewCardLink |

## Group 7 · `PaymentShell.AddCardArea` — New card flow

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-10 · AddNewCardFlow** | 🔁 | MH-B5 + Profile add card · CardScanCamera · ManualEntryFields · SaveForFutureToggle · BillingAddressForm |

## Group 8 · `ConfirmationShell.MainContent` — Success card

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-11 · BookingConfirmationCard** | 🔁 | MH-B6 + IROP rebook · SuccessHeader · PNRCode · MilesEarnedConfirm · AddToWalletAuto · ShareWithFamilyCTA |

## Group 9 · `ConfirmationShell.ShareArea` — Family share

| ID · Name | Cat | Screens · Sub-elements |
|:---|:-:|:---|
| **M-12 · TripShareToFamily** | 🔁 | MH-B6 + Trip Detail share · ShareOptionsList · ShareablePreview · AddToCalendarCTA |

---

## Inventory by Category

| Category | Count | Molecules |
|:---:|:---:|:---|
| 🔁 SHARED | 11 | M-01, M-02, M-03, M-05, M-06, M-07, M-08, M-09, M-10, M-11, M-12 |
| ⭐ ĐẶC THÙ | 1 | M-04 |
| 🔄 REUSE | 0 | — |
| **Total** | **12** | M-01..M-12 sequential |

## Cross-Reference

| From | To | Purpose |
|---|---|---|
| M-07 SeatPicker | tools-ar M-SUN-01 SunlightHeatmap | Sunlight prediction during seat pick |
| M-11 BookingConfirmationCard | home M-04 FlightMiniCard | Trip becomes mini-card on Home |

## QG Verification: 12/12 PASS ✅

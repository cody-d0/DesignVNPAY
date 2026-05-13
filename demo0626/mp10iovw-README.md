# SF0 — Home Dashboard

> **Module:** Home Dashboard (HOME)
> **URD source:** [`urd/core/home-dashboard.md`](../../../urd/core/home-dashboard.md) §H
> **MH count:** 1 main MH (MH-H1) with 6 zones
> **Screens (single-screen model):** 1 screen × ~3,000 valid states

## Status

- [x] URD synthesized (urd/core/home-dashboard.md)
- [x] Deep analysis completed ([ANALYSIS.md](./ANALYSIS.md))
- [x] Screen model completed ([SCREEN-MODEL.md](./SCREEN-MODEL.md))
- [ ] Design checklist (CHECKLIST.md) — pending

## Deep Analysis: [ANALYSIS.md](./ANALYSIS.md)
## Screen Model: [SCREEN-MODEL.md](./SCREEN-MODEL.md)

## Quick reference

| Field | Value |
|---|---|
| Pre-condition | KH đăng nhập VNA app OR guest mode |
| Post-condition | Navigate to module (Search/Trips/Tools/Profile) hoặc Voice intent action |
| Server params | USER_TIER, CURRENT_TRIP_ID, WEATHER_API_KEY, CULTURAL_THEME_OVERRIDE, LOTUSMILES_BALANCE |
| Cross-cutting | Voice mic (Zone F) + Tier badge (Zone A) shared with ALL screens |
| State dimensions | 8 dimensions, ~3,000 valid combinations |

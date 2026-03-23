# 📋 Test Plan — Speechify iOS App
**Version:** 1.0  
**Author:** Rajwinder Kaur, QA Engineer  
**Date:** 2025  
**App Version:** Speechify iOS (latest)

---

## 1. Objective

This test plan defines the scope, strategy, and schedule for QA testing of the **Speechify iOS application**. The goal is to ensure the app delivers a high-quality, reliable text-to-speech experience across all supported iOS devices and versions.

---

## 2. Scope

### In Scope
- Onboarding & Authentication (sign-up, sign-in, SSO)
- Document Library (import, view, delete)
- Audio Playback (play, pause, speed control, voice selection)
- Settings & Preferences persistence
- API backend validation
- Performance on supported devices
- App Store compliance (Apple HIG, accessibility)

### Out of Scope
- Speechify Web App
- Android App
- Chrome Extension
- Payment/billing flows (handled by separate team)

---

## 3. Test Strategy

### 3.1 Test Levels

| Level | Type | Tools |
|-------|------|-------|
| Unit | Component-level | XCTest |
| Integration | API + UI | Appium + Postman |
| System | End-to-end flows | Appium + pytest |
| Regression | Pre-release | Appium automation suite |
| Exploratory | Ad-hoc manual | Manual + JIRA |

### 3.2 Priority Levels

| Priority | Definition | Action |
|----------|-----------|--------|
| P0 | App crash, data loss, core feature broken | Block release |
| P1 | Important feature degraded, workaround exists | Fix before release |
| P2 | Minor UX issue, cosmetic | Fix in next sprint |
| P3 | Nice-to-have improvement | Backlog |

---

## 4. Test Cases Summary

### 4.1 Onboarding & Auth

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| TC-001 | App launches & shows welcome screen | P0 | ✅ Automated |
| TC-002 | Valid sign-up completes successfully | P0 | ✅ Automated |
| TC-003 | Invalid email format shows error | P1 | ✅ Automated |
| TC-004 | Empty email field shows error | P1 | ✅ Automated |
| TC-005 | Wrong password shows error | P1 | ✅ Automated |
| TC-006 | Valid sign-in completes successfully | P0 | ✅ Automated |
| TC-007 | Apple SSO button present (App Store req) | P1 | ✅ Automated |
| TC-008 | Password mismatch shows error | P1 | ✅ Automated |

### 4.2 Audio Playback

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| TC-101 | Player loads when document opened | P0 | ✅ Automated |
| TC-102 | Tap Play starts audio | P0 | ✅ Automated |
| TC-103 | Tap Pause stops audio | P0 | ✅ Automated |
| TC-104 | Speed changes to 1.5x | P1 | ✅ Automated |
| TC-105 | Speed changes to max (4.5x) | P1 | ✅ Automated |
| TC-106 | Speed changes to min (0.5x) | P1 | ✅ Automated |
| TC-107 | Speed persists after restart | P1 | ✅ Automated |
| TC-108 | Document title shown in player | P2 | ✅ Automated |

### 4.3 Document Import

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| TC-201 | Add Content button visible | P0 | ✅ Automated |
| TC-202 | Tapping + shows import options | P0 | ✅ Automated |
| TC-203 | Import PDF opens file picker | P0 | ✅ Automated |
| TC-204 | Google Drive option present | P1 | ✅ Automated |
| TC-205 | Imported doc appears in library | P0 | ✅ Automated |
| TC-206 | Tapping doc opens player | P0 | ✅ Automated |
| TC-207 | Web URL import option present | P1 | ✅ Automated |

### 4.4 Edge Cases

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| EDGE-001 | Very long email handled gracefully | P2 | ✅ Automated |
| EDGE-002 | Special characters in password accepted | P2 | ✅ Automated |
| EDGE-003 | Double-tap play doesn't crash | P2 | ✅ Automated |
| EDGE-004 | Speed persists after backgrounding app | P2 | ✅ Automated |
| EDGE-005 | Unsupported file type shows error | P1 | ✅ Automated |
| EDGE-006 | Rapid speed changes don't freeze app | P2 | ✅ Automated |

---

## 5. Defect Tracking

All defects logged in **JIRA** with:
- Title: `[iOS] [P0] Short description`
- Steps to reproduce (numbered)
- Expected vs actual behavior
- Device + iOS version
- Screenshot or screen recording
- Build number

### Defect Lifecycle
```
New → Assigned → In Progress → Fixed → Verify Fix → Closed
                                    ↓
                               Cannot Reproduce → Needs Info
```

---

## 6. Entry & Exit Criteria

### Entry Criteria (before testing starts)
- Build deployed to TestFlight
- Smoke tests pass (P0 automated tests green)
- Test data / accounts prepared

### Exit Criteria (testing complete)
- All P0 defects resolved
- All P1 defects resolved or risk-accepted by PM
- Regression suite passes at ≥ 95%
- No new P0s introduced in final 48 hours

---

## 7. Devices & iOS Versions

| Device | iOS Version | Type |
|--------|------------|------|
| iPhone 15 Pro | 17.2 | Physical |
| iPhone 14 | 16.6 | Physical |
| iPhone 15 | 17.0 | Simulator (CI) |
| iPhone SE (3rd gen) | 16.4 | Simulator (CI) |
| iPad Air | 17.0 | Physical |

---

## 8. Risk & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Appium selector changes after app update | High | Medium | Use accessibility IDs (stable) |
| Simulator behaves differently from device | Medium | High | Run P0 tests on physical device before release |
| Network-dependent tests flake in CI | Medium | Low | Mock API responses for unit-level tests |
| iOS version fragmentation | Low | High | Test matrix covers last 2 major iOS versions |

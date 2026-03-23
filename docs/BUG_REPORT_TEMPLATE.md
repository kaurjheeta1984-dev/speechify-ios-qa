# 🐛 Bug Report Template

> Copy this template when filing a defect in JIRA/GitHub Issues.

---

## Bug Report

**Title:** `[iOS] [P{priority}] Short description of the issue`

**Reporter:** Rajwinder Kaur  
**Date:** YYYY-MM-DD  
**Build Version:** e.g. 10.2.1 (build 2024.11.05)  
**Environment:** Staging / Production  

---

### Device & OS Information

| Field | Value |
|-------|-------|
| Device | e.g. iPhone 15 Pro |
| iOS Version | e.g. 17.2 |
| App Version | e.g. 10.2.1 |
| Network | WiFi / 5G / Airplane Mode |

---

### Priority & Severity

| Field | Value |
|-------|-------|
| Priority | P0 / P1 / P2 / P3 |
| Severity | Critical / Major / Minor / Trivial |
| Frequency | Always / Often / Sometimes / Rarely |

---

### Description

> One-sentence summary of the problem.

---

### Steps to Reproduce

1. Launch the Speechify iOS app
2. [Action]
3. [Action]
4. [Observe the issue]

---

### Expected Result

> Describe what SHOULD happen based on the spec or intuition.

---

### Actual Result

> Describe what IS happening. Be specific.

---

### Screenshots / Screen Recording

> Attach screenshot or video here.

---

### Logs / Error Messages

```
Paste any relevant crash logs or console output here.
```

---

### Additional Notes

> Any workaround found? Related tickets? Regression (worked in previous build)?

---

## Example Completed Bug Report

**Title:** `[iOS] [P0] App crashes when PDF larger than 50MB is imported`

**Reporter:** Rajwinder Kaur  
**Date:** 2025-03-15  
**Build Version:** 10.2.1 (build 2025.03.10)  
**Environment:** Staging  

| Field | Value |
|-------|-------|
| Device | iPhone 14 |
| iOS Version | 16.6 |
| App Version | 10.2.1 |
| Network | WiFi |

**Priority:** P0 | **Severity:** Critical | **Frequency:** Always

**Description:** The app crashes immediately when a user attempts to import a PDF file larger than 50MB.

**Steps to Reproduce:**
1. Log in with any valid account
2. Tap the + Add Content button
3. Select Import PDF
4. Choose a PDF file >= 50MB from Files app
5. App crashes to home screen

**Expected Result:** PDF should either import successfully, or show an error message like "File too large. Maximum size is 50MB."

**Actual Result:** App crashes to iOS home screen with no error message. The document does not appear in the library.

**Screenshots:** [attached crash_screenshot.png]

**Logs:**
```
CRASH LOG: EXC_BAD_ACCESS KERN_INVALID_ADDRESS
Thread 1: Fatal error: Unexpectedly found nil while unwrapping an Optional value
  PDFImportService.swift line 247: let fileData = try! Data(contentsOf: fileURL)
```

**Additional Notes:** Workaround: compress PDF to under 50MB before importing. Related to ticket SPF-1102.

# 🎧 Speechify iOS App — QA Automation Framework

> A professional iOS test automation framework built with **Appium** and **Python**, simulating real-world QA testing for a text-to-speech mobile application.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run Tests](#how-to-run-tests)
- [Test Coverage](#test-coverage)
- [CI/CD Pipeline](#cicd-pipeline)
- [Sample Test Report](#sample-test-report)

---

## 🎯 Project Overview

This framework simulates QA automation testing for the **Speechify iOS App** — a text-to-speech application used by 50M+ users. It covers:

- ✅ Core feature testing (onboarding, playback, import)
- ✅ Regression test suite
- ✅ Edge case & boundary testing
- ✅ API backend validation
- ✅ CI/CD integration via GitHub Actions

Built to reflect real QA engineering work done at companies like Google/E-touch Systems — triaging defects, ensuring P0/P1 coverage, and maintaining automation regression suites.

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Primary scripting language |
| Appium 2.x | Mobile automation framework |
| XCUITest Driver | iOS-specific test driver |
| pytest | Test runner & reporting |
| pytest-html | HTML test report generation |
| Allure | Advanced test reporting |
| GitHub Actions | CI/CD pipeline |
| JIRA (simulated) | Defect tracking reference |

---

## 📁 Project Structure

```
speechify-ios-qa/
│
├── tests/
│   ├── functional/          # Core feature tests
│   │   ├── test_onboarding.py
│   │   ├── test_audio_playback.py
│   │   └── test_document_import.py
│   ├── regression/          # Full regression suite
│   │   ├── test_regression_suite.py
│   │   └── test_settings.py
│   └── edge_cases/          # Boundary & edge case tests
│       └── test_edge_cases.py
│
├── page_objects/            # Page Object Model (POM)
│   ├── base_page.py
│   ├── onboarding_page.py
│   ├── home_page.py
│   └── player_page.py
│
├── test_data/               # Test data & config
│   ├── test_config.json
│   └── sample_documents/
│
├── reports/                 # Auto-generated test reports
│
├── docs/
│   ├── TEST_PLAN.md
│   └── BUG_REPORT_TEMPLATE.md
│
├── scripts/
│   └── run_tests.sh
│
├── .github/
│   └── workflows/
│       └── ios_tests.yml    # CI/CD pipeline
│
├── conftest.py              # pytest fixtures & Appium setup
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### Prerequisites
- macOS (required for iOS testing)
- Xcode 15+ installed
- Node.js 18+
- Python 3.11+

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/speechify-ios-qa.git
cd speechify-ios-qa
```

### Step 2: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Appium
```bash
npm install -g appium
appium driver install xcuitest
```

### Step 4: Configure Test Device
Update `test_data/test_config.json` with your simulator details:
```json
{
  "deviceName": "iPhone 15",
  "platformVersion": "17.0",
  "udid": "YOUR_SIMULATOR_UDID"
}
```

### Step 5: Start Appium Server
```bash
appium --port 4723
```

---

## 🚀 How to Run Tests

```bash
# Run all tests
pytest tests/ --html=reports/report.html

# Run only functional tests
pytest tests/functional/ -v

# Run regression suite
pytest tests/regression/ -v

# Run a specific test file
pytest tests/functional/test_audio_playback.py -v

# Run tests with Allure reporting
pytest tests/ --alluredir=reports/allure-results
```

---

## 🧪 Test Coverage

### Functional Tests
| Test Case | Description | Priority |
|-----------|-------------|----------|
| TC-001 | App launch & onboarding flow | P0 |
| TC-002 | User sign-up with valid credentials | P0 |
| TC-003 | User sign-up with invalid email | P1 |
| TC-004 | Import PDF document | P0 |
| TC-005 | Audio playback — play/pause | P0 |
| TC-006 | Audio speed adjustment (0.5x–4.5x) | P1 |
| TC-007 | Voice selection | P1 |
| TC-008 | Import from Google Drive | P1 |
| TC-009 | Offline mode behavior | P2 |
| TC-010 | App behavior with no internet | P2 |

### Regression Tests
| Test Case | Description |
|-----------|-------------|
| REG-001 | Full onboarding → playback flow |
| REG-002 | Settings persistence after app restart |
| REG-003 | Library sync across sessions |

### Edge Cases
| Test Case | Description |
|-----------|-------------|
| EDGE-001 | Upload 0 KB empty file |
| EDGE-002 | Upload file > 100 MB |
| EDGE-003 | Unsupported file format (.exe) |
| EDGE-004 | Playback interrupted by phone call |
| EDGE-005 | Speed set to maximum then app restart |

---

## 🔄 CI/CD Pipeline

Automated via **GitHub Actions** on every push and pull request:

```
Push to main/PR → Install deps → Start Appium → Run tests → Generate report → Upload artifacts
```

See `.github/workflows/ios_tests.yml` for full pipeline configuration.

---

## 📊 Sample Test Report

After running tests, open `reports/report.html` in your browser to see:
- Pass/fail summary
- Test execution time
- Failure screenshots
- Defect links (JIRA references)

---

## 👩‍💻 Author

**Rajwinder Kaur** — QA Engineer  
6+ years experience | iOS & Mobile Testing | Automation  
[LinkedIn](https://www.linkedin.com/in/rajwinder-kaur-lnu-149043195)

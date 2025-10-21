# Automated Tests for Sauce Labs My Demo App (Android)

## 📱 Overview
This project contains **automated UI tests** for the **Sauce Labs My Demo App (Android)** built with **Python + Appium + Pytest + Allure**.  

The tests cover:
- ✅ Login / Logout  
- ✅ Product catalog and product details  
- ✅ Sorting by price  
- ✅ Add to cart and verify cart contents  

---

## ⚙️ Requirements

Install the following tools:

- [Python 3.10+](https://www.python.org/downloads/)
- [Appium Server](https://appium.io/)
- [Android Studio](https://developer.android.com/studio)
- Android SDK & emulator or a real Android device
- Allure

---

## 🧩 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # on Linux/macOS
venv\Scripts\activate       # on Windows

# Install dependencies
pip install -r requirements.txt
```

## 📦 Application Under Test

The test app (`mda-2.2.0-25.apk`) is located in the `app/` folder

No need to download anything manually — the tests use this file directly.

---

## 🚀 Running Tests

Make sure your **Appium server** and **Android emulator (or device)** are running:

```bash
appium
```

Then, in another terminal:
```bash
pytest -s -v --alluredir=reports
```

Or to run a specific test module:
```bash
pytest tests/test_login.py -v --alluredir=allure-reports
```
## 📊 Allure Report

Generate and open the Allure report:
```bash
allure serve allure-eports
```


## 🧾 Reporting & Stability

- Each test uses explicit waits (no hard sleeps).

- Page Object Model (POM) ensures maintainability.

- Allure steps provide detailed step-by-step reports.

- Flaky reruns are configured for unstable cases.

- Screenshots on failure are attached in Allure reports.

## 🧑‍💻 Notes for Reviewer

- The APK (app/mydemoapp.apk) is already included — no manual download needed.

- The full suite executes in ~1 minute on a standard emulator.
- ```allure-report``` directory and screenshot of test run results are committed for demo proposes

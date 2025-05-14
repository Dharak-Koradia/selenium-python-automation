# Selenium Python Automation

A step-by-step evolution of a Selenium-based automation framework in Python — showcasing both foundational and advanced skills in automated UI testing.

## 🚀 Phase 1: Basic Login Test

- [x] Uses raw Selenium WebDriver in Python
- [x] Runs a simple login test on [Practice Test Automation](https://practicetestautomation.com/practice-test-login/)
- [x] Uses ChromeDriver locally
- [x] Manual script run without test framework

## 🚀 Phase 2: Pytest + Fixtures + Parameterization

- [x] Switched to **Pytest** as the test runner
- [x] Created reusable `driver` fixture using `conftest.py`
- [x] Added **test markers** to group tests
- [x] Implemented:
  - [x] Positive test (`test_successful_login`)
  - [x] Negative test with invalid credentials
  - [x] **Parameterized test** using `@pytest.mark.parametrize` to run multiple login scenarios
- [x] Added **explicit waits** using `WebDriverWait` to avoid flaky tests

---

## 🔧 Tools Used

- Python 3.13
- Selenium 4.32.0
- ChromeDriver (compatible with Chrome 136)
- Pytest 8.x

---

### How to Run

1. Have Python on your machine (preferably **3.13.X**)
2. [Install chromedriver](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions.json) compatible with your current Chrome version.
3. Create a virtual environment
4. Install dependencies:

```bash
pip install -r requirements.txt
```

#### Run all tests:

```bash
pytest -v
```

#### Run only login tests:

```bash
pytest -m login -v
```

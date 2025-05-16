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

## 🚀 Phase 3: Introduced Page Object Model (POM) Design Pattern

In this phase:

- [x] Refactored the login test to follow the Page Object Model structure for better code organization and maintainability.

- [x] Created a dedicated LoginPage class to handle page interactions (pages/login_page.py).

- [x] Implemented explicit waits using WebDriverWait and Expected Conditions (EC) to ensure reliable test execution.

- [x] Updated test files (tests/test_login.py) to use the new POM class for cleaner, more readable test logic.

- [x] Maintained compatibility with pytest for easy execution and reporting.

- [x] Improved test stability by avoiding flakiness due to timing issues.

## 🚀 Phase 4 – Config Management, Test Data Handling & Allure Reporting

### Key Enhancements:

- [x] Centralized Test Configuration

  - [x] Moved test settings to a config/config.yaml file
    - `base_url`
    - `valid_username` (used)
    - `valid_password` (used)
    - `implicit_wait`
  - [x] This makes the tests more maintainable and avoids hardcoding values directly in test files or page objects.

- [x] Allure Reporting Integration
  - [x] Integrated allure-pytest plugin for advanced reporting.
  - [x] Generates clean, visual test reports with detailed steps and results.
  - [x] Run tests and generate report using:

```bash
pytest -v
allure serve allure-results
```

### Technologies Used:

- [x] PyYAML – to load configuration from YAML file
- [x] Allure – for rich test reporting
- [x] Updated requirements.txt using pip freeze

![Allure Report Preview](assets/allure-report-preview.png)

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

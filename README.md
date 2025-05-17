# 🤖 Selenium Automation Framework (Python)

End-to-end test automation framework using **Selenium**, built to demonstrate QA skills across key areas including:

- Pytest for test orchestration
- Page Object Model for maintainability
- YAML config for environment setup
- Allure reports for rich test insights
- Cross-browser and headless execution

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Allure Reporting
- YAML for Config Management
- GitHub Actions (CI) – \[planned]
- Requests (for API testing) – \[planned]

---

## ▶️ How to Run Tests

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run tests:

```bash
pytest --alluredir=allure-results
```

### 3. View Allure Report:

```bash
allure serve allure-results
```

---

## 🏷️ Test Labels

Tests are marked using `pytest.mark`:

- `@smoke` – Critical path tests
- `@regression` – Broader suite
- `@api` – API + UI combo (planned)

Run specific types:

```bash
pytest -m "smoke"
```

---

## 📂 Branching Strategy

- `main` – Clean final project
- `phase-X/...` – Learning/building phases

---

## 📸 Sample Screenshots

> Add screenshots of Allure reports here

---

## 🏷️ Badges

> Will add once CI setup is complete (e.g., GitHub Actions)

---

## 📄 Future Enhancements

- API + UI test integration
- CI Pipeline via GitHub Actions
- Dockerized test environment
- Test Strategy doc
- Coverage reporting

---

## 👤 Author

Built by Dharak Koradia — an aspiring QA Engineer.

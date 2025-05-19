import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path

CONFIG_PATH = Path("config/config.yaml")

# Add CLI option --browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None, help="Browser to use for tests"
    )

# Load config from YAML
@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

# WebDriver fixture
@pytest.fixture
def driver(config, request):
    # Priority: CLI option > config file
    cli_browser = request.config.getoption("--browser")
    browser = cli_browser if cli_browser else config.get("browser", "chrome")
    headless = config.get("headless", False)

    if browser.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config.get("implicit_wait", 10))
    yield driver
    driver.quit()

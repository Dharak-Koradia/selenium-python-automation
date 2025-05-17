import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pathlib import Path

CONFIG_PATH = Path("config/config.yaml")

@pytest.fixture(scope="session")
def config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

@pytest.fixture
def driver(config):
    browser = config.get("browser", "chrome").lower()
    headless = config.get("headless", False)

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # or just "--headless" for older versions
            options.add_argument("--disable-gpu")
        service = ChromeService(executable_path="drivers/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(executable_path="drivers/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config.get("implicit_wait", 10))
    yield driver
    driver.quit()

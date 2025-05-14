import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service("drivers/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver  # This is like "return" but allows teardown after test runs
    driver.quit()

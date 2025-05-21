import requests
from selenium.webdriver.common.by import By
import time
import pytest
import os

@pytest.mark.api
def test_api_and_ui_login(driver, config):
    # Step 1: Use the mock API
    payload = {
        "username": config["valid_username"],
        "password": config["valid_password"]
    }
    api_host = os.getenv("API_HOST", "127.0.0.1") # default to "127.0.0.1" locally
    api_response = requests.post(f"http://{api_host}:5000/api/login", json=payload)
    assert api_response.status_code == 200
    assert api_response.json()["status"] == "success"

    # Step 2: Use Selenium to do UI login
    driver.get(config["base_url"])
    driver.find_element(By.ID, "username").send_keys(payload["username"])
    driver.find_element(By.ID, "password").send_keys(payload["password"])
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message

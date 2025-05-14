import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

@pytest.mark.login
def test_successful_login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"

@pytest.mark.login
def test_invalid_login(driver):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    error_message = error_element.text
    assert error_message == "Your username is invalid!"
    
@pytest.mark.login
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("", "", "Your username is invalid!"),
        ("student", "", "Your password is invalid!"),
        ("", "Password123", "Your username is invalid!"),
        ("wrong", "Password123", "Your username is invalid!"),
        ("student", "wrongpass", "Your password is invalid!"),
    ]
)
def test_invalid_login_param(driver, username, password, expected_error):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    error_message = error_element.text
    assert error_message == expected_error

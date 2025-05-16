import pytest
from pages.login_page import LoginPage
from utils.config_loader import load_config

config = load_config()

@pytest.mark.login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username(config["valid_username"])
    login_page.enter_password(config["valid_password"])
    login_page.click_login()

    message = login_page.get_flash_message()
    assert "You logged into a secure area!" in message
    
    
@pytest.mark.login
@pytest.mark.parametrize("username,password,expected_error", [
    ("wronguser", config["valid_password"], "Your username is invalid!"),
    (config["valid_username"], "wrongpass", "Your password is invalid!"),
    ("", config["valid_password"], "Your username is invalid!"),
    (config["valid_username"], "", "Your password is invalid!"),
])
def test_invalid_login_param(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    message = login_page.get_flash_message()
    assert expected_error in message

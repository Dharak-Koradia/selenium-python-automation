import pytest
from pages.login_page import LoginPage

@pytest.mark.login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert "You logged into a secure area!" in login_page.get_flash_message()


@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_error", [
    ("tomsmithhhhh", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrongpass", "Your password is invalid!")
])
def test_invalid_login_param(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert expected_error in login_page.get_flash_message()

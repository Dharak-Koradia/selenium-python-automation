from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located((By.ID, "username"))).clear()
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).clear()
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    def get_flash_message(self):
        flash = self.wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        return flash.text.strip()

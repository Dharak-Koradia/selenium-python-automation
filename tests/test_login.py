from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def test_login():
    service = Service("drivers/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_message = driver.find_element(By.TAG_NAME, "h1").text
    assert success_message == "Logged In Successfully"

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    print("Running test_login manually...")
    test_login()

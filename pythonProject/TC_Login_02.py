import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService


def test_case2():
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(15)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin12")
    driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(5)


mydriver = test_case2()


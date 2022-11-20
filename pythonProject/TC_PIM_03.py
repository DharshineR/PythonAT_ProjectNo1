import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver import ActionChains

def test_case4():
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(2)
    my_actions = ActionChains(driver)
    menu_element = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']")
    my_actions.move_to_element(menu_element).click(menu_element).perform()
    checkbox = driver.find_element(By.XPATH, "//div[text()='0217']//..//../div/div/button/i[@class='oxd-icon bi-trash']//..")
    my_actions.move_to_element(checkbox).click(checkbox).perform()
    driver.find_element(By.XPATH, "// div[ @class ='orangehrm-modal-footer'] / button[@ class ='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
    time.sleep(5)


mydriver = test_case4()


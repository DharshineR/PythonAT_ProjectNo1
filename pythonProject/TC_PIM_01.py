import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select



def test_case3():
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
        element_add = driver.find_element(By.XPATH, "//button[text()=' Add ']")
        my_actions.move_to_element(element_add).click(element_add).perform()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Deepak')
        driver.find_element(By.XPATH, "//input[@name='middleName']").send_keys('raj')
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys('sekar')
        driver.find_element(By.XPATH, "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']").click()
        #my_actions.move_to_element(slider).click(slider).perform()
        time.sleep(5)
        driver.find_element(By.XPATH, "//label[text()='Username']//..//../div/input").send_keys('Rajkumar')
        driver.find_element(By.XPATH, "//label[text()='Password']//..//../div/input").send_keys('Rajkumar123@')
        driver.find_element(By.XPATH, "//label[text()='Confirm Password']//..//../div/input").send_keys('Rajkumar123@')
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)

mydriver = test_case3()


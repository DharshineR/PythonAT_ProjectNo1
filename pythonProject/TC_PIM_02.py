import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver import ActionChains
def test_case5():
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
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[text()='Employee List']").click()
        edit = driver.find_element(By.XPATH,
                                       "//div[text()='0217']//..//../div/div/button/i[@class='oxd-icon bi-pencil-fill']")
        my_actions.move_to_element(edit).click(edit).perform()
        driverLicenseNumber = driver.find_element(By.XPATH, "//label[text()='License Expiry Date']//..//..//..//../div/div/div[2]/input")
        driverLicenseNumber.send_keys("587690")
        driver.find_element(By.XPATH, "//label[text()='License Expiry Date']//..//../div[2]").send_keys("2000-12-25")
        driver.find_element(By.XPATH, "//label[text()='Date of Birth']//..//../div/div/div/input").clear()
        driver.find_element(By.XPATH, "//label[text()='SSN Number']//..//../div[2]").send_keys("29005")
        driver.find_element(By.XPATH, "//label[text()='SIN Number']//..//../div[2]").send_keys("29015")
        dropdown = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text-input' and text()='-- Select --']")
        my_actions.move_to_element(dropdown).send_keys('Indian').perform()
        #my_actions.move_to_element(gender).click(gender).perform()
        driver.find_element(By.XPATH, "//label[text()='Military Service']//..//../div[2]").send_keys("no")
        driver.find_element(By.XPATH, "//p[text()=' * Required']//../button").click()
        time.sleep(5)

mydriver = test_case5()
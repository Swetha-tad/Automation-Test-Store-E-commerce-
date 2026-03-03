import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#tag and id
"""driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Test_User03")

#tag and id
driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("test_user@03")

#tag and class
driver.find_element(By.CSS_SELECTOR, "button._42ft").click()"""

#tag and attribute
#driver.find_element(By.CSS_SELECTOR, "a[data-testid=open-registration-form-button]").click()

#tag, class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-email]").send_keys("Test_User04")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("Test_User04")
driver.find_element(By.CSS_SELECTOR, "button._42ft").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()

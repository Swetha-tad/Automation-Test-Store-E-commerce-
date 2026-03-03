import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

#launchs application url
driver.get("https://automationteststore.com/")
driver.maximize_window()
print(driver.title)

#clicks on register
driver.find_element(By.XPATH, "//a[normalize-space()='Login or register']").click()
#clicks on continue
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
#fill in the personal details
driver.find_element(By.ID,"AccountFrm_firstname").send_keys("John")
driver.find_element(By.ID,"AccountFrm_lastname").send_keys("Doe")
driver.find_element(By.ID,"AccountFrm_email").send_keys("Johndoe@gmail.com")
#fill in the address details
driver.find_element(By.ID,"AccountFrm_address_1").send_keys("Miyapur, 6th lane, H.NO: 2/614")
driver.find_element(By.ID,"AccountFrm_city").send_keys("Hyderabad")
#select country from the dropdown
select = Select(driver.find_element(By.ID, "AccountFrm_country_id"))
select.select_by_visible_text("India")  # Exact visible text from option
driver.find_element(By.ID,"AccountFrm_postcode").send_keys("50067")

driver.implicitly_wait(5)

#select state from the dropdown
state = driver.find_element(By.ID, "AccountFrm_zone_id")
select = Select(state)
select.select_by_visible_text("Andhra Pradesh")  # Exact visible text from option

#fill in the login details
driver.find_element(By.ID,"AccountFrm_loginname").send_keys("johnuser")
driver.find_element(By.ID,"AccountFrm_password").send_keys("Johnuser_01")
driver.find_element(By.ID,"AccountFrm_confirm").send_keys("Johnuser_01")

#check the privacy policy
driver.find_element(By.ID,"AccountFrm_agree").click()

#click on continue button
driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]").click()

print(driver.current_url)

driver.find_element(By.ID, "filter_keyword").send_keys("Skincare")
driver.find_element(By.XPATH, "//i[@class='fa fa-search']").click()
#driver.find_element(By.LINK_TEXT, "Login or register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Login").click()
elements = driver.find_elements(By.CLASS_NAME, "header_block")
print(len(elements))

driver.close()

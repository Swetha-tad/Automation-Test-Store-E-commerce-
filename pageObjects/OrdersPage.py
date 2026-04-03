from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.customLogger import LogGen

class OrdersPage:
    myaccount_link_xpath = "(//span[@class='menu_text' and normalize-space()='Account'])[1]"
    order_history_link_xpath = "//ul[contains(@class,'side_account_list')]//li//a[contains(@href,'https://automationteststore.com/index.php?rt=account/history')]"


    def __init__(self, driver):
        self.driver = driver

    def click_myaccount(self):
        self.driver.find_element(By.XPATH, self.myaccount_link_xpath).click()

    def click_order_history_link(self):
        self.driver.find_element(By.XPATH, self.order_history_link_xpath).click()



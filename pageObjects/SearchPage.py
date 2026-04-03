from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.customLogger import LogGen


class SearchPage:
    searchbox_id = "filter_keyword"
    textbox_criteria_id = "keyword"
    search_button_xpath ="//i[@class='fa fa-search']"


    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def set_valid_keyword(self, valid_keyword):
        self.driver.find_element(By.ID, self.searchbox_id).clear()
        self.driver.find_element(By.ID, self.searchbox_id).send_keys(valid_keyword)

    def set_invalid_keyword(self, invalid_keyword):
        self.driver.find_element(By.ID, self.searchbox_id).clear()
        self.driver.find_element(By.ID, self.searchbox_id).send_keys(invalid_keyword)

    def set_partial_keyword(self, partial_keyword):
        self.driver.find_element(By.ID, self.searchbox_id).clear()
        self.driver.find_element(By.ID, self.searchbox_id).send_keys(partial_keyword)

    def set_filter_keyword(self, filter_keyword):
        self.driver.find_element(By.ID, self.textbox_criteria_id).clear()
        self.driver.find_element(By.ID, self.textbox_criteria_id).send_keys(filter_keyword)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

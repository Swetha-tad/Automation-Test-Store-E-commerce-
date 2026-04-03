from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    homepage_url_linktext = "Home"
    productlink_xpath = "(//a[@title='BeneFit Girl Meets Pearl'][normalize-space()='BeneFit Girl Meets Pearl'])[1]"
    menu_xpath = "//div[@class='menu_text']"
    orderhistory_xpath = "(//a[@href='https://automationteststore.com/index.php?rt=account/history'])[4]"
    facebooklink_xpath = "(//a[@title='Facebook'][normalize-space()='Facebook'])[1]"



    def __init__(self, driver):
        self.driver = driver

    def click_homepage(self):
        homepage = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.homepage_url_linktext)))
        homepage.click()

    def click_productlink(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.productlink_xpath)))
        product.click()

    def click_menu(self):
        self.driver.find_element(By.XPATH, self.menu_xpath).click()

    def click_orderhistory(self):
        self.driver.find_element(By.XPATH, self.orderhistory_xpath).click()

    def click_facebook(self):
        facebook_page = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.facebooklink_xpath)))
        facebook_page.click()

        #self.driver.find_element(By.XPATH, self.facebooklink_xpath).click()









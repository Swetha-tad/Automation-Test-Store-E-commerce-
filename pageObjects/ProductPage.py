from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.customLogger import LogGen

class ProductPage:
    product_category_xpath = "(//a[contains(text(),'Men')])[3]"
    product_link_xpath = "(//a[normalize-space()='Men+Care Clean Comfort Deodorant'])[1]"
    product_quantity_id = "product_quantity"
    product_category2_xpath = "(//a[contains(text(),'Apparel & accessories')])[2]"
    out_of_stock_product_link_xpath = "//a[normalize-space()='Product with options and stock locations']"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def click_product_category_link(self):
        category = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_category_xpath)))
        category.click()
        self.logger.info("Clicked Men category")

    def click_product_link(self):
        product_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_link_xpath)))
        product_link.click()
        self.logger.info("Clicked Men+Care product")

        #self.driver.find_element(By.XPATH, self.product_link_xpath).click()

    def set_product_details(self, product_quantity):
        try:
            qty_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, self.product_quantity_id)))
            qty_field.clear()
            qty_field.send_keys(str(product_quantity))
            self.logger.info(f"Set quantity to {product_quantity}")
        except Exception as e:
            self.logger.error(f"Quantity field not found: {e}")


    def click_product_category2_link(self):
        category2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.product_category2_xpath)))
        category2.click()
        self.logger.info("Clicked Apparel & accessories Category")


    def click_out_of_stock_product_link(self):
        out_of_stock_product_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.out_of_stock_product_link_xpath)))
        out_of_stock_product_link.click()
        self.logger.info("Clicked on Out of Stock Product Link")


    def scroll_to_view(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 500).perform()
        self.logger.info("Scrolled down page")




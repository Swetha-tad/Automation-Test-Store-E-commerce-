from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.customLogger import LogGen


class CartPage:
    category_link_css = "a[href='https://automationteststore.com/index.php?rt=product/category&path=49']"
    sub_category_link_css = "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > div:nth-child(2) > a:nth-child(1)"
    women_product_link_css = "a[title='Beauty Eau de Parfum']"
    add_to_cart_button_css = ".cart"
    textbox_qty_css = "#product_quantity"
    cart_link_xpath = "//a[contains(@href,'checkout/cart')]"
    delete_btn_xpath = "(//a[@class='btn btn-sm btn-default'])[1]"
    textbox_coupon_code_id = "coupon_coupon"
    apply_btn_id = "apply_coupon_btn"


    #category_link_xpath = "//a[normalize-space()='Fragrance']"
    #sub_category_link_xpath = "//a[normalize-space()='Women']"
    #product_link_xpath = "//a[normalize-space()='Beauty Eau de Parfum']"
    #button_classname = "cart"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def click_category_link(self):
        wait = WebDriverWait(self.driver, 10)
        fragrance = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.category_link_css)))
        fragrance.click()

    def click_sub_category_link(self):
        wait = WebDriverWait(self.driver, 10)
        sub = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.sub_category_link_css)))
        sub.click()

    def click_women_product_link(self):
        wait = WebDriverWait(self.driver, 10)
        product = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.women_product_link_css)))
        product.click()

    def click_add_to_cart_button(self):
        wait = WebDriverWait(self.driver, 10)
        add_cart = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.add_to_cart_button_css)))
        add_cart.click()

    def set_product_qty(self):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_qty_css).click()

    def click_cart(self):
        self.driver.find_element(By.XPATH, self.cart_link_xpath).click()

    def delete_btn(self):
        self.driver.find_element(By.XPATH, self.delete_btn_xpath).click()

    def set_coupon_code(self, coupon_code):
        self.driver.find_element(By.ID, self.textbox_coupon_code_id).clear()
        self.driver.find_element(By.ID, self.textbox_coupon_code_id).send_keys(coupon_code)

    def click_apply_btn(self):
        self.driver.find_element(By.ID, self.apply_btn_id).click()





from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from utilities.customLogger import LogGen

class CheckoutPage:
    checkout_link_css= "ul[id='main_menu_top'] a[class='top menu_checkout']"
    edit_btn_css = "body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)"
    change_btn_css = "a[title='Change Address']"

    textbox_firstname_id = "Address2Frm_firstname"
    textbox_lastname_id = "Address2Frm_lastname"
    textbox_address_id = "Address2Frm_address_1"
    textbox_city_id = "Address2Frm_city"
    textbox_country_id = "Address2Frm_country_id"
    textbox_state_id = "Address2Frm_zone_id"
    textbox_zipcode_id = "Address2Frm_postcode"
    continue_button_css = "button[class='btn btn-orange pull-right lock-on-click']"

    checkout_btn_id = "cart_checkout1"
    edit_payment_btn_xpath = "//a[normalize-space()='Edit Payment']"
    checkbox_btn_xpath = "//input[@id='payment_agree']"
    order_continue_btn_xpath = "//button[normalize-space()='Continue']"
    confirm_btn_id = "checkout_btn"

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkout_link_css).click()

    def click_edit_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.edit_btn_css).click()

    def click_change_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.change_btn_css).click()

    def set_address_firstname(self, first_name):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(first_name)

    def set_address_lastname(self, last_name):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(last_name)

    def set_address_line(self, address_line):
        self.driver.find_element(By.ID, self.textbox_address_id).clear()
        self.driver.find_element(By.ID, self.textbox_address_id).send_keys(address_line)

    def set_address_city(self, address_city):
        self.driver.find_element(By.ID, self.textbox_city_id).clear()
        self.driver.find_element(By.ID, self.textbox_city_id).send_keys(address_city)

    def set_address_state(self, address_state):
        state_dropdown = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, self.textbox_state_id))
        )
        # Scroll to dropdown and click to open it
        self.driver.execute_script("arguments[0].scrollIntoView();", state_dropdown)
        state_dropdown.click()
        time.sleep(1)  # Let options load

        select = Select(state_dropdown)
        select.select_by_visible_text(address_state)

    def set_address_zipcode(self, address_zipcode):
        self.driver.find_element(By.ID, self.textbox_zipcode_id).clear()
        self.driver.find_element(By.ID, self.textbox_zipcode_id).send_keys(address_zipcode)

    def set_address_country(self, address_country):
        country_name = self.driver.find_element(By.ID, self.textbox_country_id)
        select = Select(country_name)
        select.select_by_visible_text(address_country)

    def click_address_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_button_css).click()

    def click_checkout_button(self):
        self.driver.find_element(By.ID, self.checkout_btn_id).click()

    def click_confirm_button(self):
        self.driver.find_element(By.ID, self.confirm_btn_id).click()

    def click_payment_button(self):
        self.driver.find_element(By.XPATH, self.edit_payment_btn_xpath).click()

    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_btn_xpath).click()

    def click_order_continue_button(self):
        self.driver.find_element(By.XPATH, self.order_continue_btn_xpath).click()








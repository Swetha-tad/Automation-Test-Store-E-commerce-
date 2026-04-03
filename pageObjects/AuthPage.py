from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AuthPage:
    # User registration info
    # personal details
    textbox_firstname_id = "AccountFrm_firstname"
    textbox_lastname_id = "AccountFrm_lastname"
    textbox_email_id = "AccountFrm_email"
    # address details
    textbox_address1 = "AccountFrm_address_1"
    textbox_city_id = "AccountFrm_city"
    drp_down_country_id = "AccountFrm_country_id"
    drp_down_state_id = "AccountFrm_zone_id"
    textbox_zipcode_id = "AccountFrm_postcode"
    # login details
    textbox_login_name_id = "AccountFrm_loginname"
    textbox_password_id = "AccountFrm_password"
    textbox_confirm_id = "AccountFrm_confirm"
    checkbox_id = "AccountFrm_agree"
    button_auth_xpath="//button[normalize-space()='Continue']"

    # User login info
    textbox_login_id = "loginFrm_loginname"
    textbox_login_password_id = "loginFrm_password"
    button_login_xpath="//button[normalize-space()='Login']"
    logout_linktext="Logoff"



    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lastname)

    def setemail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setaddress1(self, address1):
        self.driver.find_element(By.ID, self.textbox_address1).clear()
        self.driver.find_element(By.ID, self.textbox_address1).send_keys(address1)

    def setcity(self, city):
        self.driver.find_element(By.ID, self.textbox_city_id).clear()
        self.driver.find_element(By.ID, self.textbox_city_id).send_keys(city)

    def select_country(self,country_name):
        country_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.drp_down_country_id)))
        select = Select(country_dropdown)
        select.select_by_visible_text(country_name)
        time.sleep(3)

    def select_state(self,state_name):
        state_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.drp_down_state_id)))
        select = Select(state_dropdown)
        select.select_by_visible_text(state_name)

    def setzipcode(self, zipcode):
        self.driver.find_element(By.ID, self.textbox_zipcode_id).clear()
        self.driver.find_element(By.ID, self.textbox_zipcode_id).send_keys(zipcode)

    def setloginname(self, login_name):
        self.driver.find_element(By.ID, self.textbox_login_name_id).clear()
        self.driver.find_element(By.ID, self.textbox_login_name_id).send_keys(login_name)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setconfirm(self, confirm_password):
        self.driver.find_element(By.ID, self.textbox_confirm_id).clear()
        self.driver.find_element(By.ID, self.textbox_confirm_id).send_keys(confirm_password)

    def setagree(self):
        self.driver.find_element(By.ID, self.checkbox_id).click()

    def click_continue(self):
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_auth_xpath)))
        continue_btn.click()



    def setloginid(self, login_id):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.presence_of_element_located((By.ID, self.textbox_login_id)))
        elem.clear()
        elem.send_keys(login_id)
        #self.driver.find_element(By.ID, self.textbox_login_id).clear()
        #self.driver.find_element(By.ID, self.textbox_login_id).send_keys(login_id)

    def setloginpassword(self, login_password):
        self.driver.find_element(By.ID, self.textbox_login_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_login_password_id).send_keys(login_password)

    def click_login(self):
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_btn.click()

    def click_logout(self):
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.logout_linktext)))
        logout_btn.click()











import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from pageObjects.HomePage import HomePage
from pageObjects.CartPage import CartPage
from pageObjects.CartPage import CartPage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestCheckoutPage:
    category_url = ReadConfig.get_category_link()
    sub_category_url = ReadConfig.get_sub_category_link()
    product_link = ReadConfig.get_women_product_link()
    add_cart_button = ReadConfig.get_addtocart_button()

    cart_link = ReadConfig.get_cart_link()

    checkout_link = ReadConfig.getCheckoutLink()
    edit_address_btn = ReadConfig.get_edit_button()
    change_address_btn = ReadConfig.get_change_address_button()

    first_name = ReadConfig.getShippingFirstName()
    last_name = ReadConfig.getShippingLastName()
    address_line = ReadConfig.getShippingAddress1()
    address_city = ReadConfig.getShippingCity()
    address_country = ReadConfig.getShippingCountry()
    address_state = ReadConfig.getShippingState()
    address_zipcode = ReadConfig.getShippingZipcode()
    shipping_continue_btn  =ReadConfig.get_continue_button()

    checkout_btn = ReadConfig.get_checkout_button()
    payment_btn = ReadConfig.get_payment_button()
    checkbox_btn = ReadConfig.get_checkbox_button()
    order_continue_btn = ReadConfig.get_order_continue_button()
    confirm_btn = ReadConfig.get_confirm_button()

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger = LogGen.loggen()


    def test_Verify_valid_shipping_address(self, setup):

        self.logger.info("******  Verifying Valid Shipping Address  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)
        self.Checkout = CheckoutPage(self.driver)

        # 1. Login
        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        # 2. Add Product to Cart
        self.driver.get(ReadConfig.getHomepageURL())
        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.click_add_to_cart_button()

        # 3. Click checkout link
        self.Checkout.click_checkout_link()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Checkout"))

        # 4. Click Edit / Change Address
        self.Checkout.click_edit_btn()
        self.Checkout.click_change_btn()

        # 5. Fill shipping address
        self.Checkout.set_address_firstname(self.first_name)
        self.Checkout.set_address_lastname(self.last_name)
        self.Checkout.set_address_line(self.address_line)
        self.Checkout.set_address_city(self.address_city)
        self.Checkout.set_address_country(self.address_country)
        self.Checkout.set_address_state(self.address_state)
        self.Checkout.set_address_zipcode(self.address_zipcode)

        # 6. Click Continue
        self.Checkout.click_address_button()

        # 7. Wait for confirmation / next page
        WebDriverWait(self.driver, 10).until(EC.title_contains("Confirmation"))


        act_title = self.driver.title
        exp_title = "Checkout Confirmation"
        if act_title == exp_title:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_valid_shipping_address_PASS.png")
            self.logger.info("****** Valid shipping address details updated Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_valid_shipping_address_FAIL.png")
            self.logger.error("****** Valid shipping address details failed to Update *****")
            self.driver.close()
            assert False


    def test_Verify_Mandatory_shipping_details(self, setup):

        self.logger.info("******  Verifying Mandatory Shipping Address Details  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)
        self.Checkout = CheckoutPage(self.driver)

        # 1. Login
        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        # 2. Add Product to Cart
        self.driver.get(ReadConfig.getHomepageURL())
        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.click_add_to_cart_button()

        # 3. Click checkout link
        self.Checkout.click_checkout_link()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Checkout"))

        # 4. Click Edit / Change Address
        self.Checkout.click_edit_btn()
        self.Checkout.click_change_btn()

        # 5. Fill shipping address
        self.Checkout.set_address_firstname(self.first_name)
        self.Checkout.set_address_lastname(self.last_name)

        # 6. Click Continue
        self.Checkout.click_address_button()

        WebDriverWait(self.driver, 10).until(EC.title_contains("Checkout"))

        act_title = self.driver.title
        exp_title = "Checkout Address"
        if act_title == exp_title:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_Mandatory_shipping_details_PASS.png")
            self.logger.info("****** System rejected shipping address with missing mandatory detail *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_valid_shipping_address_FAIL.png")
            self.logger.error("****** System accepted shipping address with missing mandatory details *****")
            self.driver.close()
            assert False



    def test_Verify_Payment_Order_Creation(self, setup):

        self.logger.info("******  Verifying Successful Payment and Order Creation  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)
        self.Checkout = CheckoutPage(self.driver)

        # 1. Login
        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        # 2. Add Product to Cart
        #self.driver.get(ReadConfig.getHomepageURL())
        #self.Cart.click_category_link()
        #self.Cart.click_sub_category_link()
        #self.Cart.click_women_product_link()
        #self.Cart.click_add_to_cart_button()

        # 3. Go to Checkout
        self.Cart.click_cart()
        #self.Checkout.click_checkout_link()
        #WebDriverWait(self.driver, 10).until(EC.title_contains("Checkout"))

        # 4. COMPLETE SHIPPING ADDRESS (MANDATORY)
        #self.Checkout.click_edit_btn()
        #self.Checkout.click_change_btn()

        #self.Checkout.set_address_firstname(self.first_name)
        #self.Checkout.set_address_lastname(self.last_name)
        #self.Checkout.set_address_line(self.address_line)
        #self.Checkout.set_address_city(self.address_city)
        #self.Checkout.set_address_country("India")  # or your config value
        #self.Checkout.set_address_state("Delhi")  # or your config value
        #self.Checkout.set_address_zipcode(self.address_zipcode)
        #self.Checkout.click_address_button()

        self.Checkout.click_checkout_button()
        self.Checkout.click_payment_button()
        self.Checkout.click_checkbox()
        self.Checkout.click_order_continue_button()
        self.Checkout.click_confirm_button()
        time.sleep(5)

        act_title = self.driver.title
        exp_title = "Your Order Has Been Processed!"
        if act_title == exp_title:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_Payment_Order_Creation_PASS.png")
            self.logger.info("****** Payment Verified and Order Creation Successful *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Verify_Payment_Order_Creation_FAIL.png")
            self.logger.error("****** Payment Verification Failed and Order Creation Failed *****")
            self.driver.close()
            assert False
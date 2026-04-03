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
from pageObjects.OrdersPage import OrdersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestOrdersPage:
    my_account_link = ReadConfig.get_my_account_link()
    order_history_link = ReadConfig.get_order_history_link()

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger = LogGen.loggen()


    def test_OrdersPage(self, setup):

        self.logger.info("******  Verifying Orders History Page  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        #self.Cart = CartPage(self.driver)
        #self.Checkout = CheckoutPage(self.driver)
        self.Orders = OrdersPage(self.driver)

        # 1. Login
        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()


        # 2. Go to My Account
        self.Orders.click_myaccount()
        time.sleep(5)
        self.Orders.click_order_history_link()

        act_title = self.driver.title
        exp_title = "My Order History"
        if act_title == exp_title:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_OrdersPage_PASS.png")
            self.logger.info("****** Orders History Page Launched Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_OrdersPage_FAIL.png")
            self.logger.error("****** Orders History Page Failed to Launch *****")
            self.driver.close()
            assert False

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from pageObjects.CartPage import CartPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestCartPage:
    category_url = ReadConfig.get_category_link()
    sub_category_url = ReadConfig.get_sub_category_link()
    product_link = ReadConfig.get_women_product_link()
    add_cart_button = ReadConfig.get_addtocart_button()
    updated_product_qty = ReadConfig.get_updated_product_qty()
    cart_link = ReadConfig.get_cart_link()
    delete_btn = ReadConfig.get_delete_btn()
    coupon_code = ReadConfig.get_coupon_code()
    apply_btn = ReadConfig.get_apply_btn()
    invalid_coupon_code = ReadConfig.get_invalid_coupon_code()

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger = LogGen.loggen()


    def test_AddToCartPage(self, setup):

        self.logger.info("******  Verifying Add To Cart Page  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.driver.get(ReadConfig.getHomepageURL())

        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.click_add_to_cart_button()

        act_title = self.driver.title
        if act_title == "Shopping Cart":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_AddToCartPage_PASS.png")
            self.logger.info("****** Product Added to Cart Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_AddToCartPage_FAIL.png")
            self.logger.error("****** Product Failed to Add to Cart *****")
            self.driver.close()
            assert False



    def test_Cart_Update(self, setup):

        self.logger.info("******  Verifying Cart Update  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.driver.get(ReadConfig.getHomepageURL())

        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.set_product_qty()
        self.Cart.click_add_to_cart_button()

        act_title = self.driver.title
        if act_title == "Shopping Cart":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Cart_Update_PASS.png")
            self.logger.info("****** Cart Updated Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Cart_Update_FAIL.png")
            self.logger.error("****** Cart Failed to Update  *****")
            self.driver.close()
            assert False


    def test_remove_product_cart(self, setup):

        self.logger.info("******  Verifying if Product from the Cart can be removed  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.driver.get(ReadConfig.getHomepageURL())

        self.Cart.click_cart()
        self.Cart.delete_btn()
        self.driver.refresh()

        act_title = self.driver.title
        if act_title == "Shopping Cart":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_remove_product_cart_PASS.png")
            self.logger.info("****** Product removed from the Cart Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_remove_product_cart_FAIL.png")
            self.logger.error("****** Product Failed to Remove  *****")
            self.driver.close()
            assert False


    def test_Valid_Coupon_Code(self, setup):

        self.logger.info("******  Verifying Valid Coupon Code  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.driver.get(ReadConfig.getHomepageURL())

        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.click_add_to_cart_button()
        self.Cart.click_cart()
        self.Cart.set_coupon_code(self.coupon_code)
        self.Cart.click_apply_btn()

        act_title = self.driver.title
        if act_title == "Shopping Cart":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Valid_Coupon_Code_PASS.png")
            self.logger.info("****** Coupon Code updated and Discount applied Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Valid_Coupon_Code_FAIL.png")
            self.logger.error("****** Coupon Code updated but Failed to Apply  Discount  *****")
            self.driver.close()
            assert False



    def test_InValid_Coupon_Code(self, setup):

        self.logger.info("******  Verifying In-Valid Coupon Code  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Cart = CartPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.driver.get(ReadConfig.getHomepageURL())

        self.Cart.click_category_link()
        self.Cart.click_sub_category_link()
        self.Cart.click_women_product_link()
        self.Cart.click_add_to_cart_button()
        self.Cart.click_cart()
        self.Cart.set_coupon_code(self.invalid_coupon_code)
        self.Cart.click_apply_btn()

        act_title = self.driver.title
        if act_title == "Shopping Cart":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_InValid_Coupon_Code_PASS.png")
            self.logger.info("****** System rejected coupon Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_InValid_Coupon_Code_FAIL.png")
            self.logger.error("****** Invalid Coupon Code updated  *****")
            self.driver.close()
            assert False


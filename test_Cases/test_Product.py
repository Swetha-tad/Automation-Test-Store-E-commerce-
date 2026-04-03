import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from pageObjects.AuthPage import AuthPage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ProductPage:
    homepage_url= ReadConfig.getHomepageURL()
    men_product_link=ReadConfig.get_men_product_link

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger= LogGen.loggen()

    def test_Product_Category_display(self,setup):

        self.logger.info("******  Verifying Product Category Display  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Product = ProductPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Product.click_product_category_link()


        act_title = self.driver.title
        if act_title == "Men":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Product_Category_display_PASS.png")
            self.logger.info("****** Product Category displayed Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Product_Category_display_FAIL.png")
            self.logger.error("****** Product Category displayed Failed to Load *****")
            self.driver.close()
            assert False



    def test_product_details_display(self,setup):

        self.logger.info("******  Verifying Product Details Display  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Product = ProductPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Product.click_product_category_link()
        self.Product.click_product_link()
        self.Product.scroll_to_view()
        time.sleep(2)

        act_title = self.driver.title
        if act_title == "Men+Care Clean Comfort Deodorant":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_men_product_details_display_PASS.png")
            self.logger.info("****** Product Details displayed Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_men_product_details_display_FAIL.png")
            self.logger.error("****** Product Details displayed Failed *****")
            self.driver.close()
            assert False


    def test_product_details_verification(self, setup):

        self.logger.info("******  Verifying Product Details Verification  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Product = ProductPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Product.click_product_category_link()
        self.Product.click_product_link()
        self.Product.scroll_to_view()
        qty = ReadConfig.get_product_quantity()
        self.Product.set_product_details(qty)
        time.sleep(2)

        act_title = self.driver.title
        if act_title == "Men+Care Clean Comfort Deodorant":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_product_details_verification_PASS.png")
            self.logger.info("****** Product Details Updated Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_product_details_verification_FAIL.png")
            self.logger.error("****** Product Details Failed to Update *****")
            self.driver.close()
            assert False



    def test_product_out_of_stock_behaviour(self, setup):

        self.logger.info("******  Verifying Out of Stock Product Behaviour  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Product = ProductPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Product.click_product_category2_link()
        self.Product.click_out_of_stock_product_link()
        self.Product.scroll_to_view()

        act_title = self.driver.title
        if act_title == "Product with options and stock locations":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_product_out_of_stock_behaviour_PASS.png")
            self.logger.info("****** Product Out of Stock behaviour is working Fine *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_product_out_of_stock_behaviour_FAIL.png")
            self.logger.error("****** Product Out of Stock behaviour Failed *****")
            self.driver.close()
            assert False





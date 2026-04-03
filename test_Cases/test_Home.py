import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_HomePage:
    homepage_url= ReadConfig.getHomepageURL()
    product_link=ReadConfig.getproductlink()
    menu=ReadConfig.getmenu()
    orderhistory_link=ReadConfig.getorderhistory()
    facebook_link=ReadConfig.getfacebooklink()

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger= LogGen.loggen()


    def test_HomePageTitle(self,setup):

        self.logger.info("****** Test_HomePageTitle *****")
        self.logger.info("****** Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.homepage_url)

        act_title = self.driver.title
        if act_title == "A place to practice your automation skills!":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle_PASS.png")
            self.logger.info("****** Home Page launched Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle_FAIL.png")
            self.logger.error("****** Home Page Failed to Load *****")
            self.driver.close()
            assert False


    def test_product_link(self,setup):

        self.logger.info("****** Verifying Product Link *****")
        self.driver = setup
        self.driver.get(self.homepage_url)
        self.Home = HomePage(self.driver)

        self.Home.click_productlink()

        act_title = self.driver.title
        if act_title == "BeneFit Girl Meets Pearl":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_product_link_PASS.png")
            self.logger.info("****** Product link Opened Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_product_link_FAIL.png")
            self.logger.error("****** Product link Failed to Load *****")
            self.driver.close()
            assert False


    def test_orderhistory_link(self,setup):

        self.logger.info("****** Verifying Order History Link *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        #self.driver.get(self.homepage_url)
        self.Home = HomePage(self.driver)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword(self.login_password)
        self.Auth.click_login()

        self.Home.click_orderhistory()

        act_title = self.driver.title
        if act_title == "My Order History":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_orderhistory_link_PASS.png")
            self.logger.info("****** Order history link Opened Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_orderhistory_link_FAIL.png")
            self.logger.error("****** Order history link Failed to Load *****")
            self.driver.close()
            assert False



    def test_menu(self,setup):

        self.logger.info("****** Verifying Menu Link *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        #self.driver.get(self.homepage_url)
        self.Home = HomePage(self.driver)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword(self.login_password)
        self.Auth.click_login()

        self.Home.click_menu()

        act_title = self.driver.title
        if act_title == "My Account":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_menu_PASS.png")
            self.logger.info("****** Menu link Opened Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_menu_FAIL.png")
            self.logger.error("****** Menu link Failed to Load *****")
            self.driver.close()
            assert False


    def test_facebook_link(self,setup):

        self.logger.info("****** Verifying Facebook Link *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        #self.driver.get(self.homepage_url)
        self.Home = HomePage(self.driver)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword(self.login_password)
        self.Auth.click_login()

        self.Home.click_facebook()

        act_title = self.driver.title
        if act_title == "Facebook":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_facebook_link.png")
            self.logger.info("****** Facebook link Opened Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_facebook_link.png")
            self.logger.error("****** Facebook link Failed to Load *****")
            self.driver.close()
            assert False







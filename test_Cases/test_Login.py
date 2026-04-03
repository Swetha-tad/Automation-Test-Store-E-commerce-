import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Registration:
    loginURL= ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    logger= LogGen.loggen()

    def test_LoginPageTitle(self,setup):

        self.logger.info("****** Test_Login *****")
        self.logger.info("****** Verifying Login Page Title *****")
        self.driver = setup
        self.driver.get(self.loginURL)

        act_title = self.driver.title
        if act_title == "Account Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_LoginPageTitle_PASS.png")
            self.logger.info("****** Login Page loaded Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_LoginPageTitle_FAIL.png")
            self.logger.error("****** Login Page Failed to Load *****")
            self.driver.close()
            assert False


    def test_valid_Login(self,setup):

        self.logger.info("******  Verifying Valid User Login *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword(self.login_password)
        self.Auth.click_login()

        act_title = self.driver.title
        #print(act_title)
        if act_title == "My Account":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_valid_Login_PASS.png")
            self.logger.info("****** User LoggedIn Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_valid_Login_FAIL.png")
            self.logger.error("****** User LoggedIn Failed *****")
            self.driver.close()
            assert False



    def test_Invalid_Login(self,setup):

        self.logger.info("******  Verifying In-Valid User Login *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword("test..1")
        self.Auth.click_login()

        act_title = self.driver.title
        print(act_title)
        if act_title == "Account Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Invalid_Login_PASS.png")
            self.logger.info("****** Invalid User LoggedIn Failed *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Invalid_Login_FAIL.png")
            self.logger.info("****** Invalid User LoggedIn Successfully *****")
            self.driver.close()
            assert False



    def test_login_mandatory_validation(self,setup):

        self.logger.info("******  Verifying Mandatory field Login *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid("")
        self.Auth.setloginpassword("")
        self.Auth.click_login()

        act_title = self.driver.title
        if act_title == "Account Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_login_mandatory_validation_PASS.png")
            self.logger.info("****** Mandatory Field Login Successful *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_mandatory_validation_FAIL.png")
            self.logger.error("****** Mandatory Field Login Failed *****")
            self.driver.close()
            assert False



    def test_logout_validation(self,setup):

        self.logger.info("******  Verifying Mandatory field Login *****")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Auth = AuthPage(self.driver)

        self.Auth.setloginid(self.login_id)
        self.Auth.setloginpassword(self.login_password)
        self.Auth.click_login()
        self.Auth.click_logout()


        act_title = self.driver.title
        if act_title == "Account Logout":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_logout_validation_PASS.png")
            self.logger.info("****** User Logout Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_logout_validation_FAIL.png")
            self.logger.error("****** User Logout Failed *****")
            self.driver.close()
            assert False




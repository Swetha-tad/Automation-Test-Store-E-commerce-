import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Auth:
    baseURL= ReadConfig.getApplicationURL()
    firstname= ReadConfig.getFirstname()
    lastname= ReadConfig.getLastname()
    email= ReadConfig.getEmail()
    address1= ReadConfig.getAddress1()
    city= ReadConfig.getCity()
    country_name= ReadConfig.getCountry()
    state_name= ReadConfig.getState()
    zipcode= ReadConfig.getZipcode()
    login_name= ReadConfig.getLoginname()
    password= ReadConfig.getPassword()
    confirm_password= ReadConfig.getConfirmPassword()

    logger= LogGen.loggen()

    def test_RegistrationPageTitle(self,setup):

        self.logger.info("****** Test_001_Auth *****")
        self.logger.info("****** Verifying User Registration Page Title *****")
        self.driver=setup
        self.driver.get(self.baseURL)

        act_title=self.driver.title
        if act_title=="Create Account":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_RegistrationPageTitle_PASS.png")
            self.logger.info("****** Registration Page loaded Successfully *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_RegistrationPageTitle_FAIL.png")
            self.logger.error("****** Registration Page Failed to Load *****")
            self.driver.close()
            assert False



    def test_Registration_valid(self,setup):

        self.logger.info("****** Verifying Valid User Registration *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.Auth=AuthPage(self.driver)

        self.Auth.setfirstname(self.firstname)
        self.Auth.setlastname(self.lastname)
        self.Auth.setemail(self.email)
        self.Auth.setaddress1(self.address1)
        self.Auth.setcity(self.city)
        self.Auth.select_country(self.country_name)

        self.Auth.select_state(self.state_name)
        self.Auth.setzipcode(self.zipcode)
        self.Auth.setloginname(self.login_name)
        self.Auth.setpassword(self.password)
        self.Auth.setconfirm(self.confirm_password)
        self.Auth.setagree()
        self.Auth.click_continue()

        act_title = self.driver.title
        if act_title == "Your Account Has Been Created!":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_validRegistration_PASS.png")
            self.logger.info("****** Valid User Registration Successful *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_validRegistration_FAIL.png")
            self.logger.error("****** Valid User Registration Failed *****")
            self.driver.close()
            assert False



    def test_registration_mandatory_validation(self, setup):

        self.logger.info("****** Verifying Mandatory field Registration *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Auth = AuthPage(self.driver)

        self.Auth.setfirstname("")
        self.Auth.setlastname("")
        self.Auth.setemail("")
        self.Auth.setaddress1("")
        self.Auth.setcity("")
        self.Auth.select_country("")

        self.Auth.select_state("")
        self.Auth.setagree()
        self.Auth.click_continue()

        act_title = self.driver.title
        if act_title == "Create Account":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_RegistrationPageTitle_PASS.png")
            self.logger.info("****** Mandatory Field Registration Successful *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_RegistrationPageTitle_FAIL.png")
            self.logger.error("****** Mandatory Field Registration Failed *****")
            self.driver.close()
            assert False




    def teardown_method(self, method):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()







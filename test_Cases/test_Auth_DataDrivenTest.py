import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.AuthPage import AuthPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_001_DDT_Auth:
    baseURL= ReadConfig.getApplicationURL()
    path=".\\Test_data\\Registration_Test_Data.xlsx"
    logger= LogGen.loggen()


    def test_validRegistration_DDT(self,setup):
        self.logger.info("****** Test_001_DDT_Auth *****")
        self.logger.info("****** Verifying User Registration *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.Auth=AuthPage(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,'User Registration Data')
        print("No of rows:",self.rows)

        for r in range(2,self.rows+1):
            self.firstname=ExcelUtils.readData(self.path,'User Registration Data',r,1)
            self.lastname=ExcelUtils.readData(self.path,'User Registration Data',r,2)
            self.email=ExcelUtils.readData(self.path,'User Registration Data',r,3)
            self.address1=ExcelUtils.readData(self.path,'User Registration Data',r,4)
            self.city=ExcelUtils.readData(self.path,'User Registration Data',r,5)
            self.country_name=ExcelUtils.readData(self.path,'User Registration Data',r,6)
            self.state_name=ExcelUtils.readData(self.path,'User Registration Data',r,7)
            self.zipcode=ExcelUtils.readData(self.path,'User Registration Data',r,8)
            self.login_name=ExcelUtils.readData(self.path,'User Registration Data',r,9)
            self.password=ExcelUtils.readData(self.path,'User Registration Data',r,10)
            self.confirm_password=ExcelUtils.readData(self.path,'User Registration Data',r,11)
            self.status=ExcelUtils.readData(self.path,'User Registration Data',r,12)


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
                self.logger.info("****** User Registration Successful *****")
                self.driver.close()

            else:
                self.driver.save_screenshot(".\\Screenshots\\test_validRegistration_FAIL.png")
                self.logger.error("****** User Registration Failed *****")
                self.driver.close()
                assert False

        self.logger.info("****** End of Test_001_DDT_Auth *****")
        self.logger.info("****** Valid User Registration Test Completed *****")


    def test_InvalidRegistration_DDT(self,setup):
        self.logger.info("****** Test_001_DDT_Auth *****")
        self.logger.info("****** Verifying User Registration *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.Auth=AuthPage(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,'User Registration Data')
        print("No of rows:",self.rows)

        for r in range(3,self.rows+1):
            self.firstname=ExcelUtils.readData(self.path,'User Registration Data',r,1)
            self.lastname=ExcelUtils.readData(self.path,'User Registration Data',r,2)
            self.email=ExcelUtils.readData(self.path,'User Registration Data',r,3)
            self.address1=ExcelUtils.readData(self.path,'User Registration Data',r,4)
            self.city=ExcelUtils.readData(self.path,'User Registration Data',r,5)
            self.country_name=ExcelUtils.readData(self.path,'User Registration Data',r,6)
            self.state_name=ExcelUtils.readData(self.path,'User Registration Data',r,7)
            self.zipcode=ExcelUtils.readData(self.path,'User Registration Data',r,8)
            self.login_name=ExcelUtils.readData(self.path,'User Registration Data',r,9)
            self.password=ExcelUtils.readData(self.path,'User Registration Data',r,10)
            self.confirm_password=ExcelUtils.readData(self.path,'User Registration Data',r,11)
            self.status=ExcelUtils.readData(self.path,'User Registration Data',r,12)


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
            exp_title = "Your Account Has Been Created!"
            if act_title == exp_title:
                if self.status == "Pass":
                    self.logger.error("****** Test is Failed *****")
                elif self.status == "Fail":
                    self.driver.save_screenshot(".\\Screenshots\\test_validRegistration_PASS.png")
                    self.logger.info("****** User Registration Failed Successfully *****")
                    self.driver.close()

        self.logger.info("****** End of Test_001_DDT_Auth *****")
        self.logger.info("****** In----------**Valid User Registration Test Completed *****")




























































































































        self.logger.info("****** End of Test_001_DDT_Auth *****")
        self.logger.info("****** In-Valid User Registration Test Completed *****")


    def teardown_method(self, method):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()







import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.SearchPage import SearchPage
from pageObjects.AuthPage import AuthPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Search:
    homepage_url = ReadConfig.getHomepageURL()
    #men_product_link = ReadConfig.get_men_product_link

    loginURL = ReadConfig.getLoginURL()
    login_id = ReadConfig.getLoginId()
    login_password = ReadConfig.getLoginPassword()

    valid_keyword = ReadConfig.get_valid_keyword()
    filter_keyword = ReadConfig.get_filter_keyword()
    invalid_keyword = ReadConfig.get_invalid_keyword()
    partial_keyword = ReadConfig.get_partial_keyword()
    search_button = ReadConfig.get_search_button()

    logger = LogGen.loggen()

    def test_Valid_Keyword_Search(self, setup):

        self.logger.info("******  Verifying Valid Keyword Search  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Search = SearchPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Search.set_valid_keyword(self.valid_keyword)
        time.sleep(2)
        self.Search.click_search_button()
        self.Search.set_filter_keyword(self.filter_keyword)


        act_title = self.driver.title
        if act_title == "Lancome Hypnose Doll Lashes Mascara 4-Piece Gift Set":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Valid_Keyword_Search_PASS.png")
            self.logger.info("****** Valid Keyword Search PASS *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Valid_Keyword_Search_FAIL.png")
            self.logger.error("****** Valid Keyword Search FAIL *****")
            self.driver.close()
            assert False


    def test_InValid_Keyword_Search(self, setup):

        self.logger.info("******  Verifying In-Valid Keyword Search  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Search = SearchPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Search.set_invalid_keyword(self.invalid_keyword)
        time.sleep(2)
        self.Search.click_search_button()

        act_title = self.driver.title
        if act_title == "Search":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_In-Valid_Keyword_Search_PASS.png")
            self.logger.info("****** In-Valid Keyword Search PASS *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_In-Valid_Keyword_Search_FAIL.png")
            self.logger.error("****** In-Valid Keyword Search FAIL *****")
            self.driver.close()
            assert False


    def test_Partial_Keyword_Search(self, setup):

        self.logger.info("******  Verifying Partial Keyword Search  ******")
        self.driver = setup
        self.driver.get(ReadConfig.getLoginURL())

        self.Auth = AuthPage(self.driver)
        self.Search = SearchPage(self.driver)

        self.Auth.setloginid(ReadConfig.getLoginId())
        self.Auth.setloginpassword(ReadConfig.getLoginPassword())
        self.Auth.click_login()

        self.Search.set_partial_keyword(self.partial_keyword)
        time.sleep(2)
        self.Search.click_search_button()


        act_title = self.driver.title
        if act_title == "Search":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_Partial_Keyword_Search_PASS.png")
            self.logger.info("****** Partial Keyword Search PASS *****")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Partial_Keyword_Search_FAIL.png")
            self.logger.error("****** Partial Keyword Search FAIL *****")
            self.driver.close()
            assert False

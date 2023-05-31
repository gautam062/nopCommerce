import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomer:
    baseURL = ReadConfig().getApplicationURL()
    username = ReadConfig().getUserEmail()
    password = ReadConfig().getPassword()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********Test_004_SearchCustomer**********")
        self.logger.info("********test_searchCustomerByEmail**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        self.logger.info("******** Login Successful **********")

        self.logger.info("******** Starting Search Customer by Email Test **********")
        self.acp = AddCustomerPage(self.driver)
        ime.sleep(3)
        self.acp.clickOnCustomerMenu()
        self.acp.clickOnCustomerMenuItem()
        time.sleep(3)
        self.logger.info("******** Providing Customer Email for Search **********")
        self.scp = SearchCustomer(self.driver)
        self.scp.setEmail("victoria_victoria@nopCommerce.com")
        self.scp.clickSearch()
        time.sleep(3)
        status = self.scp.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("******** test_searchCustomerByEmail Completed **********")
        self.driver.quit()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********Test_004_SearchCustomer**********")
        self.logger.info("********test_searchCustomerByName**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        self.logger.info("******** Login Successful **********")

        self.logger.info("******** Starting Search Customer by Name Test **********")
        self.acp = AddCustomerPage(self.driver)
        self.acp.clickOnCustomerMenu()
        self.acp.clickOnCustomerMenuItem()
        time.sleep(3)
        self.logger.info("******** Providing Customer Name for Search **********")
        self.scp = SearchCustomer(self.driver)
        self.scp.setFirstName("Victoria")
        self.scp.setLastName("Terces")
        self.scp.clickSearch()
        time.sleep(3)
        status = self.scp.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("******** test_searchCustomerByName Completed **********")
        self.driver.quit()
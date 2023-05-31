from pageObjects.LoginPage import LoginPage
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig().getApplicationURL()
    username = ReadConfig().getUserEmail()
    password = ReadConfig().getPassword()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********Test_001_Login**********")
        self.logger.info("********test_homePageTitle**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.logger.info("********test_homePageTitle Passed**********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("********test_homePageTitle Failed**********")
            assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********Test_001_Login**********")
        self.logger.info("********test_login**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("********test_login Passed**********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("********test_login Failed**********")
            assert False
        self.driver.close()

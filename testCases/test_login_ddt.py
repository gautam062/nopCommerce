import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig().getApplicationURL()
    path = ".\\Testdata\\LoginTestData.xlsx"
    username = ReadConfig().getUserEmail()
    password = ReadConfig().getPassword()
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********Test_002_DDT_Login**********")
        self.logger.info("********test_login_ddt**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        list_status = []

        for r in range(2, self.rows+1):
            self.username= XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected_result = XLUtils.readData(self.path, 'Sheet1', r, 3)

            lp = LoginPage(self.driver)
            lp.set_username(self.username)
            lp.set_password(self.password)
            lp.click_login_button()
            time.sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            if actual_title == expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("******** Passed **********")
                    print(self.username, self.password, self.expected_result)
                    lp.click_logout()
                    list_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.logger.info("******** Failed **********")
                    print(self.username, self.password, self.expected_result)
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.expected_result == "Pass":
                    self.logger.info("******** Failed **********")
                    print(self.username, self.password, self.expected_result)
                    list_status.append("Pass")
                elif self.expected_result == "Fail":
                    self.logger.info("******** Passed **********")
                    print(self.username, self.password, self.expected_result)
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DDT test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test Failed *****")
            self.driver.close()
            assert False

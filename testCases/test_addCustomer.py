import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig().getApplicationURL()
    username = ReadConfig().getUserEmail()
    password = ReadConfig().getPassword()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********Test_003_AddCustomer**********")
        self.logger.info("********test_addCustomer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        self.logger.info("******** Login Successful **********")

        self.logger.info("******** Starting Add Customer Test **********")
        self.acp = AddCustomerPage(self.driver)
        self.acp.clickOnCustomerMenu()
        self.acp.clickOnCustomerMenuItem()
        self.acp.clickOnAddNew()

        self.logger.info("******** Providing Customer details **********")
        self.email = random_generator() + "@gmail.com"
        self.logger.info(self.email)
        self.acp.setEmail(self.email)
        self.acp.setPassword("test123")
        self.acp.setFirstName("Gautam")
        self.acp.setLastName("Kumar")
        self.acp.setGender("male")
        self.acp.setDOB("1/25/1993")  # M/DD/YYYY
        self.acp.setCompanyName("busyQA Team")
        self.acp.setTaxExempt("yes")
        self.acp.setNewsLetter("Your store name")
        self.acp.setCustomerRole("Guests")
        self.acp.setManagerOfVendor("Vendor 1")
        self.acp.setActiveStatus("yes")
        self.acp.setAdminComment("This is for Pytest Testing")
        self.acp.clickSaveButton()
        self.logger.info("******** Saved Customer details **********")

        self.logger.info("******** Add Customer validation Started **********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'new customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("******** Add Customer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("******** Add Customer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("******** Ending AddCustomer **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

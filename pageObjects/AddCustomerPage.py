import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    link_Customers_menu_xpath = "//div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_Customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btn_Add_new_xpath = "//a[@class='btn btn-primary']"
    txt_Email_xpath = "//input[@id='Email']"
    txt_Password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rd_MaleGender_xpath = "//input[@id = 'Gender_Male']"
    rd_FemaleGender_xpath = "//input[@id = 'Gender_Female']"
    txt_Dob_xpath = "//input[@name='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@name='Company']"
    chk_TaxExempt_xpath = "//input[@name='IsTaxExempt']"
    txt_Newsletter_xpath = "//div[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    lst_YourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    lst_TestStore2_xpath = "//li[contains(text(),'Test store 2')]"
    txt_CustomerRoles_xpath = "//div[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lst_RegisteredCust_xpath = "//ul[@id = 'SelectedCustomerRoleIds_listbox']/li[contains(text(),'Registered')]"
    lst_AdministratorsCust_xpath = "//ul[@id = 'SelectedCustomerRoleIds_listbox']/li[contains(text(),'Administrators')]"
    lst_ForumModeratorsCust_xpath = "//ul[@id = 'SelectedCustomerRoleIds_listbox']/li[contains(text(),'Forum " \
                                    "Moderators')]"
    lst_GuestsCust_xpath = "//ul[@id = 'SelectedCustomerRoleIds_listbox']/li[contains(text(),'Guests')]"
    lst_VendorsCust_xpath = "//span[contains(text(),'Vendors')]"
    drp_ManagerOfVendor_xpath = "//select[@id='VendorId']"
    chk_Active_xpath = "//input[@id='Active']"
    txt_AdminComment_xpath = "//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_Add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lastName)

    def setGender(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.rd_MaleGender_xpath).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, self.rd_FemaleGender_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_Dob_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txt_CompanyName_xpath).send_keys(companyName)

    def setTaxExempt(self, taxExempt):
        if taxExempt == "yes":
            self.driver.find_element(By.XPATH, self.chk_TaxExempt_xpath).click()

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.txt_Newsletter_xpath).click()
        time.sleep(3)
        if newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.lst_YourStoreName_xpath).click()
        elif newsletter == "Test Store 2":
            self.driver.find_element(By.XPATH, self.lst_TestStore2_xpath).click()

    def setCustomerRole(self, role):

        time.sleep(3)

        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lst_RegisteredCust_xpath)
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_AdministratorsCust_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id = 'SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_GuestsCust_xpath)
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_ForumModeratorsCust_xpath)
        else:
            self.driver.find_element(By.XPATH, "//*[@id = 'SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lst_GuestsCust_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("argument[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_ManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setActiveStatus(self, activeStatus):
        if activeStatus == "no":
            self.driver.find_element(By.XPATH, self.chk_Active_xpath).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_AdminComment_xpath).send_keys(comment)

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()

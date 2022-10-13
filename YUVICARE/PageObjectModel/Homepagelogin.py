from selenium.webdriver.common.by import By

from PageObjectModel.Registration import Registrationpage


class Homepage:
    def __init__(self,driver):
        self.driver=driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")


    def enteruserdid(self):
        return self.driver.find_element(*Homepage.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Homepage.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Homepage.loginclick)




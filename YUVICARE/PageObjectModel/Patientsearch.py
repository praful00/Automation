from selenium.webdriver.common.by import By


class Searchpatient:

    def __init__(self,driver):
        self.driver=driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    registrationclick = (By.XPATH, "//div[@class='col-2 card-small-1']/a/p")
    searchpopup=(By.ID,"searchtxt")
    search=(By.ID,"searchText")
    searchbutton=(By.XPATH,"//button[@onclick='searchPatient()']")

    def enteruserdid(self):
        return self.driver.find_element(*Searchpatient.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Searchpatient.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Searchpatient.loginclick)

    def click_registration(self):
        return self.driver.find_elements(*Searchpatient.registrationclick)

    def click_searchpopup(self):
        return self.driver.find_element(*Searchpatient.searchpopup)

    def enterid(self):
        return self.driver.find_element(*Searchpatient.search)

    def clicksearchbutton(self):
        return self.driver.find_element(*Searchpatient.searchbutton)
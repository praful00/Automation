from selenium.webdriver.common.by import By

from PageObjectModel.Checkout import Checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    checkme = (By.ID, 'exampleCheck1')
    gender = (By.ID, "exampleFormControlSelect1")
    submitbutton = (By.XPATH, "//input[@type='submit']")
    successmsg = (By.CLASS_NAME, 'alert-success')


    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutpage = Checkoutpage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*Homepage.name)

    def getemail(self):
        return self.driver.find_element(*Homepage.email)

    def getpassword(self):
        return self.driver.find_element(*Homepage.password)

    def getcheckme(self):
        return self.driver.find_element(*Homepage.checkme)

    def getgender(self):
        return self.driver.find_element(*Homepage.gender)

    def submitButton(self):
        return self.driver.find_element(*Homepage.submitbutton)

    def getSuccessmessage(self):
        return self.driver.find_element(*Homepage.successmsg)
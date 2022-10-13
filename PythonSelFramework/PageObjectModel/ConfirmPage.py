from selenium.webdriver.common.by import By


class Confirmpage:

    def __init__(self, driver):
        self.driver = driver

    itemlocation = (By.ID, "country")
    gotlocation = (By.LINK_TEXT, "India")
    confirmcheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmpurchase = (By.CSS_SELECTOR, "input[type='submit']")
    successmessage = (By.CLASS_NAME, "alert-success")

    def getItemlocation(self):
        return self.driver.find_element(*Confirmpage.itemlocation)

    def gotItemloaction(self):
        return self.driver.find_element(*Confirmpage.gotlocation)

    def getcheckbox(self):
        return self.driver.find_element(*Confirmpage.confirmcheckbox)

    def confirmPurchase(self):
        return self.driver.find_element(*Confirmpage.confirmpurchase)

    def confirmmessage(self):
        return self.driver.find_element(*Confirmpage.successmessage)
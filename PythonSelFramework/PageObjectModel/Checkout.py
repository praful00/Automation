from selenium.webdriver.common.by import By


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    carditem = (By.XPATH, "//div[@class='card h-100']")
    checkoutitem = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirmcheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCarditem(self):
        return self.driver.find_elements(*Checkoutpage.carditem)

    def getcheckoutitem(self):
        return self.driver.find_element(*Checkoutpage.checkoutitem)

    def getconfirmcheckout(self):
        return self.driver.find_element(*Checkoutpage.confirmcheckout)

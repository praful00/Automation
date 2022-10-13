import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel import HomePage
from PageObjectModel.Checkout import Checkoutpage
from PageObjectModel.ConfirmPage import Confirmpage
from PageObjectModel.HomePage import Homepage
from utility.baseclass import Baseclass



class Testing(Baseclass):

    def test_framework(self):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        checkoutpage = homepage.shopItem()
        log.info("getting all the card title")
        products = checkoutpage.getCarditem()
        time.sleep(3)

        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productname)
            if productname == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        checkoutpage.getcheckoutitem().click()
        checkoutpage.getconfirmcheckout().click()

        itemLocation = Confirmpage(self.driver)
        log.info("Entering country name as ind")
        itemLocation.getItemlocation().send_keys("ind")

        self.waitcondition("India")

        itemLocation.gotItemloaction().click()
        itemLocation.getcheckbox().click()
        itemLocation.confirmPurchase().click()
        successmsg = itemLocation.confirmmessage().text
        log.info("success message"+successmsg)

        assert "Success! Thank you! " in successmsg

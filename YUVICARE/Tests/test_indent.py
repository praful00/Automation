import time

import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.Indent import Indentpage
from Testdata.Indentdata import Indentdata


@pytest.mark.usefixtures("setup")
class Testindent:

    def test_indent(self,getdata):

        indent = Indentpage(self.driver)
        indent.enteruserdid().send_keys(getdata["userdid"])
        indent.enterpassword().send_keys(getdata["password"])
        indent.clickloginbutton().click()
        lists = indent.click_indent()
        print(len(lists))
        for itemlist in lists:
            if itemlist.text == "Indent":
                itemlist.click()
                time.sleep(3)
                try:
                    indent.click_new().click()
                    time.sleep(3)
                    indent.select_store().click()
                    time.sleep(3)
                    store = indent.select_store_dropdown()
                    for stores in store:
                        if stores.text == "Dental Store":
                            stores.click()
                    time.sleep(5)
                    indent.select_product().click()
                    time.sleep(3)
                    product = indent.select_product_dropdown()
                    for products in product:
                        if products.text == "POCO - 5796 - Avail. Stock( 1 )":
                            products.click()
                    time.sleep(5)
                    indent.enter_qty().send_keys(getdata["quantity"])
                    indent.click_expecteddate().click()
                    time.sleep(3)
                    indent.select_date().click()
                    time.sleep(3)
                    indent.click_addbutton().click()
                    time.sleep(3)
                    indent.enter_comment().send_keys(getdata["comment"])
                    time.sleep(3)
                    indent.click_requestbutton().click()
                    time.sleep(3)
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    time.sleep(5)
                    indent.click_requestindent().click()
                    time.sleep(3)
                    indent.enter_notes().send_keys(getdata["comment"])
                    time.sleep(3)
                    indent.click_approvedbutton().click()
                    time.sleep(3)
                    alert1 = self.driver.switch_to.alert
                    alert1.accept()
                    time.sleep(3)
                    indent.click_approved().click()
                    time.sleep(3)
                    indent.click_deliverbutton().click()
                    time.sleep(3)
                    alert2 = self.driver.switch_to.alert
                    alert2.accept()
                    time.sleep(3)
                    indent.click_deliveredbutton().click()
                    time.sleep(3)
                    indent.click_receivedbutton().click()
                except StaleElementReferenceException as Exception:
                    indent.click_new().click()
                    time.sleep(3)
                    indent.select_store().click()
                    time.sleep(3)
                    store = indent.select_store_dropdown()
                    for stores in store:
                        if stores.text == "Dental Store":
                            stores.click()
                    time.sleep(5)
                    indent.select_product().click()
                    time.sleep(3)
                    product = indent.select_product_dropdown()
                    for products in product:
                        if products.text == "POCO - 5796 - Avail. Stock( 1 )":
                            products.click()
                    time.sleep(5)
                    indent.enter_qty().send_keys(getdata["quantity"])
                    indent.click_expecteddate().click()
                    time.sleep(3)
                    indent.select_date().click()
                    time.sleep(3)
                    indent.click_addbutton().click()
                    time.sleep(3)
                    indent.enter_comment().send_keys(getdata["comment"])
                    time.sleep(3)
                    indent.click_requestbutton().click()
                    time.sleep(3)
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    time.sleep(5)
                    indent.click_requestindent().click()
                    time.sleep(3)
                    indent.enter_notes().send_keys(getdata["comment"])
                    time.sleep(3)
                    indent.click_approvedbutton().click()
                    time.sleep(3)
                    alert1 = self.driver.switch_to.alert
                    alert1.accept()
                    time.sleep(3)
                    indent.click_approved().click()
                    time.sleep(3)
                    indent.click_deliverbutton().click()
                    time.sleep(3)
                    alert1 = self.driver.switch_to.alert
                    alert1.accept()
                    time.sleep(3)
                    indent.click_deliveredbutton().click()
                    time.sleep(3)
                    indent.click_receivedbutton().click()
















    @pytest.fixture(params=Indentdata.indent_data)
    def getdata(self, request):
        return request.param



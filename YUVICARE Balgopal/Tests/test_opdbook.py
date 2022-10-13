import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.opdbook import Opdbook
from TestData.Pagelogindata import HomepageData
from TestData.opdbookdata import OpdBook

@pytest.mark.usefixtures("setup")
class Testopdbook:

    def test_opdbook(self,getdata):
        bookopd= Opdbook(self.driver)
        bookopd.enteruserdid().send_keys(getdata["userdid"])
        bookopd.enterpassword().send_keys(getdata["password"])
        bookopd.clickloginbutton().click()
        lists=bookopd.opdclick()

        for itemlist in lists:
            if itemlist.text=="OPD":
                itemlist.click()
                time.sleep(3)
        windowlist=self.driver.window_handles
        self.driver.switch_to.window(windowlist[1])
        bookopd.selectdoctorclick().click()
        time.sleep(3)
        bookopd.selectdoctorlist().click()
        time.sleep(3)
        bookopd.bookappointmentclick().click()
        time.sleep(3)
        bookopd.selectpatientclick().click()
        time.sleep(3)
        bookopd.addnewpatientclick().click()
        time.sleep(3)

        initial=Select(bookopd.selectinitial())
        initial.select_by_value(getdata["initial"])
        bookopd.enterfirstname().send_keys(getdata["firstname"])
        bookopd.enterlastname().send_keys(getdata["lastname"])
        bookopd.enterage().send_keys(getdata["age"])
        bookopd.enteraddress().send_keys(getdata["address"])
        bookopd.selectcityclick().click()
        city=bookopd.selectcity()
        for citys in city:
            if citys.text =="NAGPUR":
               citys.click()
        bookopd.savebutton().click()
        time.sleep(3)
        bookopd.selectpatientfrompopup().click()
        time.sleep(3)
        bookopd.selectappointment().click()
        time.sleep(3)
        lists=bookopd.selectappointmentfromdropdown()
        for appointment in lists:
            if appointment.text == "OPD FIRST CONSULTATION":
                appointment.click()
        time.sleep(3)
        bookopd.bookwithpaymentclick().click()
        time.sleep(3)
        dropdown=Select(bookopd.selectpaymentmode())
        dropdown.select_by_value(getdata["paymentmode"])
        bookopd.recordpaymentclick().click()
        time.sleep(3)
        alert=self.driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        bookopd.paymentrecievedclick().click()
    @pytest.fixture(params=OpdBook.test_opdbook_data)
    def getdata(self, request):
        return request.param

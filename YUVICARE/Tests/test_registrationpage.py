import time

import pytest
from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.Registration import Registrationpage
from Testdata import Registrationdata
from Testdata.Registrationdata import RegistrationData


@pytest.mark.usefixtures("setup")
class Testregistration:

    def test_registrations(self,getdata):
        regpage = Registrationpage(self.driver)
        regpage.enteruserdid().send_keys(getdata["userdid"])
        regpage.enterpassword().send_keys(getdata["password"])
        regpage.clickloginbutton().click()
        lists = regpage.click_registration()
        print(len(lists))
        for itemlist in lists:
            if itemlist.text == "Registration":
                itemlist.click()
        windowslist = self.driver.window_handles
        print(windowslist)
        self.driver.switch_to.window(windowslist[1])

        sel=regpage.selectsalutation()
        dropdown=Select(sel)
        dropdown.select_by_index(getdata["salutation"])

        regpage.enterfirstname().send_keys(getdata["firstname"])
        regpage.enterlastname().send_keys(getdata["lastname"])
        regpage.dobfilterclick().click()

        selmonth=Select(regpage.selectmonth())
        selmonth.select_by_visible_text(getdata["entermonth"])

        selyear=Select(regpage.selectyear())
        selyear.select_by_visible_text(getdata["enteryear"])

        dates = regpage.selectdobdate()
        print(len(dates))
        for date in dates:
            if date.text == "13":
                date.click()
        regpage.entercontactno().send_keys(getdata["contactno"])
        regpage.enteraddress().send_keys(getdata["address"])

        regpage.selectcitylclick().click()
        regpage.choosecitytext().send_keys("nag")
        time.sleep(3)
        citys = regpage.selectcitydropdown()
        print(len(citys))
        for city in citys:
            if city.text == "Nagpur":
                city.click()

        regpage.selectpayertype().click()
        payertype=regpage.selectpayertypess()
        for types in payertype:
            if types.text =="Self":
                types.click()

        time.sleep(2)


        time.sleep(3)

        regpage.selectpayer().click()
        payers=regpage.payerdropdown()
        for payer in payers:
            if payer.text =="General":
                payer.click()

        regpage.selectdepartment().click()
        dept=regpage.seldeptdropdown()
        for department in dept:
            if department.text =="Orthodontics":
                department.click()
        regpage.clicksavebutton().click()
        self.driver.close()

    @pytest.fixture(params=RegistrationData.test_registration_data)
    def getdata(self, request):
        return request.param


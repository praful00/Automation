import time

import pytest
from select import select
from selenium.webdriver.support.select import Select

from PageObjectModel import Addclinicalpatient
from PageObjectModel.Addclinicalpatient import Addclinical
from Testdata import AddClinicalData
from Testdata.AddClinicalData import AddclinicalData


@pytest.mark.usefixtures("setup")
class Testaddclinicalpatient:

    def test_addclinicalpatient(self,getdata):
        #self.driver.implicitly_wait(5)
        depopd=Addclinical(self.driver)
        depopd.enteruserdid().send_keys(getdata["userdid"])
        depopd.enterpassword().send_keys(getdata["password"])
        depopd.clickloginbutton().click()
        lists = depopd.click_departmentopd()
        print(len(lists))
        for itemlist in lists:
            if itemlist.text == "Department OPD":
                itemlist.click()
        windowslist = self.driver.window_handles
        print(windowslist)
        self.driver.switch_to.window(windowslist[1])

        depopd.clickaddclinicalpatient().click()
        time.sleep(3)

        windowslist1 = self.driver.window_handles
        self.driver.switch_to.window(windowslist1[2])
        depopd.enternoofpatient().send_keys(getdata["noofpatient"])

        dropdown=Select(depopd.click_selectdepartment())
        dropdown.select_by_index(getdata["department"])
        depopd.click_gobutton().click()
        depopd.click_saveshift().click()
        self.driver.close()

        windowslist1 = self.driver.window_handles
        self.driver.switch_to.window(windowslist1[1])
        depopd.click_departmentlist().click()

        dept=depopd.list_department()
        for deptlist in dept:
            if deptlist.text=="Orthodontics":
                deptlist.click()

        depopd.click_go().click()
        doctor=Select(depopd.selectdoctordropdown())
        doctor.select_by_index(getdata["doctor"])
        time.sleep(3)
        #windowslist1 = self.driver.window_handles
        #self.driver.switch_to.window(windowslist1[2])

        depopd.click_yesbutton().click()
        time.sleep(3)
        depopd.click_referto().click()
        time.sleep(3)
        depopd.checkboxclick().click()
        time.sleep(3)
        depopd.submit_click().click()
        time.sleep(3)

        depopd.addsittingclick().click()
        time.sleep(3)

        # windowslist1 = self.driver.window_handles
        # self.driver.switch_to.window(windowslist1[2])

        depopd.selectsittingclick().click()
        sit=depopd.selectsittingdropdown()
        for sits in sit:
            if sits.text=="ORTH":
                sits.click()
        time.sleep(3)

        depopd.selectproceduremasterclick().click()
        time.sleep(3)

        masterlist=depopd.selectmasterdropdown()
        for master in masterlist:
            if master.text=="FIXED APPLIANCE":
                master.click()
        time.sleep(3)
        depopd.clickselectprocedure().click()
        procedure=depopd.procedureselect()
        for procedures in procedure:
            if procedures.text=="RECORDS TAKEN":
                procedures.click()
        time.sleep(3)
        depopd.dateclick().click()
        time.sleep(3)
        depopd.selectdate().click()
        time.sleep(3)
        depopd.savebuttonclick().click()
        time.sleep(3)
        alert=self.driver.switch_to.alert
        alert.accept()


    @pytest.fixture(params=AddclinicalData.test_addclinical_data)
    def getdata(self, request):
        return request.param
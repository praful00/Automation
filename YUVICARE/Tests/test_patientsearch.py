import time

import pytest

from PageObjectModel.Patientsearch import Searchpatient
from Testdata.Patientsearchdata import patientsearchdata


@pytest.mark.usefixtures("setup")
class Testpatientsearch:

    def test_patientsearch(self,getdata):
        search=Searchpatient(self.driver)
        search.enteruserdid().send_keys(getdata["userdid"])
        search.enterpassword().send_keys(getdata["password"])
        search.clickloginbutton().click()
        lists = search.click_registration()
        print(len(lists))
        for itemlist in lists:
            if itemlist.text == "Registration":
                itemlist.click()
        windowslist = self.driver.window_handles
        print(windowslist)
        self.driver.switch_to.window(windowslist[1])
        search.click_searchpopup().click()
        time.sleep(3)
        search.enterid().send_keys(getdata["id"])
        search.clicksearchbutton().click()
        self.driver.close()




    @pytest.fixture(params=patientsearchdata.patient_search_data)
    def getdata(self, request):
        return request.param







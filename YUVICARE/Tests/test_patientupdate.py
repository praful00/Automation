import time

import pytest

from PageObjectModel.Patientupdate import Patientupdate
from PageObjectModel.Registration import Registrationpage
from Testdata.Registrationdata import RegistrationData

@pytest.mark.usefixtures("setup")
class Testpatientupdate:

    def test_patientupdate(self,getdata):
        updatepatient=Patientupdate(self.driver)
        updatepatient.enteruserdid().send_keys(getdata["userdid"])
        updatepatient.enterpassword().send_keys(getdata["password"])
        updatepatient.clickloginbutton().click()
        lists = updatepatient.click_registration()
        print(len(lists))
        for itemlist in lists:
            if itemlist.text == "Registration":
                itemlist.click()
        windowslist = self.driver.window_handles
        print(windowslist)
        self.driver.switch_to.window(windowslist[1])

        updatepatient.patientsearchpop().click()
        time.sleep(2)
        updatepatient.clickonpatient().click()
        updatepatient.updatepatientonly().click()
        updatepatient.clicksavebutton().click()

    @pytest.fixture(params=RegistrationData.test_registration_data)
    def getdata(self, request):
        return request.param





import pytest
from selenium.webdriver.common.by import By

from PageObjectModel.Pagelogin import Homepage
from TestData.Pagelogindata import HomepageData
@pytest.mark.usefixtures("setup")
class Testloginpage:

    def test_login(self,getdata):
        homepage = Homepage(self.driver)
        homepage.enteruserdid().send_keys(getdata["userdid"])
        homepage.enterpassword().send_keys(getdata["password"])
        homepage.clickloginbutton().click()


    @pytest.fixture(params= HomepageData.test_homepage_data)
    def getdata(self, request):
        return request.param
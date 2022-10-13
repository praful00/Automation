
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.HomePage import Homepage
from TestData.HomePageData import Homepagedata
from utility.baseclass import Baseclass


class Testhomepage(Baseclass):

    def test_formsubmission(self,getdata):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        log.info("Enter first name :"+getdata["firstname"])
        homepage.getname().send_keys(getdata["firstname"])
        homepage.getemail().send_keys(getdata["email"])
        homepage.getpassword().send_keys(getdata["password"])
        homepage.getcheckme().click()

        self.selectbytextoption(homepage.getgender(), getdata["gender"])                     # static dropdown operation

        homepage.submitButton().click()

        message = homepage.getSuccessmessage().text
        log.info(message)
        assert ("Success" in message)
        self.driver.refresh()

    @pytest.fixture(params= Homepagedata.test_Homepage_data)
    def getdata(self, request):
        return request.param









        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Praful")
        # driver.find_element(By.NAME, 'email').send_keys("hello@gmail.com")
        # driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456")
        # driver.find_element(By.ID, 'exampleCheck1').click()

        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
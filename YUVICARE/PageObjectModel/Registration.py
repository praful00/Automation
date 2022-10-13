from selenium.webdriver.common.by import By

from PageObjectModel.Patientupdate import Patientupdate


class Registrationpage:

    def __init__(self,driver):
        self.driver=driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    salutations= (By.ID,"title1")
    registrationclick =(By.XPATH, "//div[@class='col-2 card-small-1']/a/p")
    firstname=(By.NAME,"firstName")
    lastname=(By.NAME,"lastName")
    dobclick=(By.NAME,"dob")
    selectmonths=(By.XPATH,"//select[@class='ui-datepicker-month']")
    selectyears=(By.CSS_SELECTOR,".ui-datepicker-year")
    contactno=(By.NAME,"mobNo")
    address=(By.NAME,"address")
    selectcityclick=(By.XPATH,"//span[contains(text(),'Select City')]")
    choosecity=(By.ID,"chosenText")
    selectpayertypes=(By.XPATH,"//span[contains(text(),'Select Payer')]")
    selectpayertypetext=(By.ID,"chosenText")
    selpayer = (By.XPATH, "//span[contains(text(),'Select Payer')]")
    selectpayertext = (By.ID, "chosenText")

    selectdepartments = (By.XPATH, "//span[contains(text(),'Select Department')]")
    selectdepartmenttext = (By.ID, "chosenText")
    clicksavebuttons=(By.XPATH,"//input[@type='submit']")
    selectdate=(By.CSS_SELECTOR,".ui-state-default")
    selectcity=(By.CSS_SELECTOR,".active-result")
    selectpayers=(By.CSS_SELECTOR,".active-result")
    selectdept=(By.CSS_SELECTOR,".active-result")
    selectpayerdropdown=(By.CSS_SELECTOR,".active-result")


    def enteruserdid(self):
        return self.driver.find_element(*Registrationpage.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Registrationpage.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Registrationpage.loginclick)

    def click_registration(self):
        return self.driver.find_elements(*Registrationpage.registrationclick)

    def selectsalutation(self):
        return self.driver.find_element(*Registrationpage.salutations)

    def enterfirstname(self):
        return self.driver.find_element(*Registrationpage.firstname)

    def enterlastname(self):
        return self.driver.find_element(*Registrationpage.lastname)

    def dobfilterclick(self):
        return self.driver.find_element(*Registrationpage.dobclick)

    def selectmonth(self):
        return self.driver.find_element(*Registrationpage.selectmonths)

    def selectyear(self):
        return self.driver.find_element(*Registrationpage.selectyears)

    def entercontactno(self):
        return self.driver.find_element(*Registrationpage.contactno)

    def enteraddress(self):
        return self.driver.find_element(*Registrationpage.address)

    def selectcitylclick(self):
        return self.driver.find_element(*Registrationpage.selectcityclick)

    def choosecitytext(self):
        return self.driver.find_element(*Registrationpage.choosecity)

    def selectstateclick(self):
        return self.driver.find_element(*Registrationpage.selectstateclick)

    def choosestatetext(self):
        return self.driver.find_element(*Registrationpage.choosestate)

    def selectpayertype(self):
        return self.driver.find_element(*Registrationpage.selectpayertypes)

    def selectpayertypetext(self):
        return self.driver.find_element(*Registrationpage.selectpayertypetext)

    def selectpayer(self):
        return self.driver.find_element(*Registrationpage.selpayer)

    def selectpayertext(self):
        return self.driver.find_element(*Registrationpage.selectpayertext)

    def selectdepartment(self):
        return self.driver.find_element(*Registrationpage.selectdepartments)

    def selectdepartmenttext(self):
        return self.driver.find_element(*Registrationpage.selectdepartmenttext)

    def clicksavebutton(self):
        return self.driver.find_element(*Registrationpage.clicksavebuttons)

    def selectdobdate(self):
        return self.driver.find_elements(*Registrationpage.selectdate)

    def selectcitydropdown(self):
        return self.driver.find_elements(*Registrationpage.selectcity)

    def selectpayertypess(self):
        return self.driver.find_elements(*Registrationpage.selectpayers)

    def payerdropdown(self):
        return self.driver.find_elements(*Registrationpage.selectpayerdropdown)

    def seldeptdropdown(self):
        return self.driver.find_elements(*Registrationpage.selectdept)


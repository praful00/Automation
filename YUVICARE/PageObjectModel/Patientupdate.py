from selenium.webdriver.common.by import By


class Patientupdate:
    def __init__(self,driver):
        self.driver=driver

    patientsearch= (By.NAME,"serachtxt")
    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    registrationclick = (By.XPATH, "//div[@class='col-2 card-small-1']/a/p")
    patientclick=(By.XPATH,"//tbody/tr[2]")
    radiobutton=(By.ID,"onlyreg")
    clicksavebuttons = (By.XPATH, "//input[@type='submit']")

    def enteruserdid(self):
        return self.driver.find_element(*Patientupdate.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Patientupdate.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Patientupdate.loginclick)

    def click_registration(self):
        return self.driver.find_elements(*Patientupdate.registrationclick)

    def patientsearchpop(self):
        return self.driver.find_element(*Patientupdate.patientsearch)

    def clickonpatient(self):
        return self.driver.find_element(*Patientupdate.patientclick)

    def updatepatientonly(self):
        return self.driver.find_element(*Patientupdate.radiobutton)

    def clicksavebutton(self):
        return self.driver.find_element(*Patientupdate.clicksavebuttons)
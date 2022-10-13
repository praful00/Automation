from selenium.webdriver.common.by import By


class Opdbook:
    def __init__(self,driver):
        self.driver=driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    opdclicks=(By.XPATH,"//div[@class='col-2 card-small-1']/a/p")
    clickselectdoctor=(By.XPATH,"//span[contains(text(),'Select Doctor')]")
    selectdoctor=(By.XPATH,"//*[@id='diaryUsersss_chosen']/div/ul/li[6]")
    bookappointment=(By.XPATH,"/html/body[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[3]/input[1]")
    selectpatient=(By.XPATH,"//input[@value='Select Patient']")
    patientselect=(By.CSS_SELECTOR,"table[id='allPatient'] tr:nth-child(2) td:nth-child(2)")
    bookwithpayment=(By.CSS_SELECTOR,"#btnBookWithPayment")
    selectappointmentclick = (By.XPATH, "//span[contains(text(),'Select Appointment Type')]")
    selectappointmentfromlist=(By.CSS_SELECTOR,".active-result")
    paymentmode=(By.XPATH,"//div[@class='form-group']//select[@id='howpaid']")
    recordpayment=(By.CSS_SELECTOR,"#rcdpymnt")
    paymentrecieve=(By.CSS_SELECTOR,"[id='vieworprintnvoice'] div div div:nth-child(3) button:nth-child(2)")


    addnewpatient=(By.CSS_SELECTOR,"#addpatientbtn")
    initial=(By.CSS_SELECTOR,"#title")
    firstname=(By.NAME,"firstName")
    lastname=(By.NAME,"lastName")
    dob=(By.NAME,"age")
    address=(By.CSS_SELECTOR,"#address")
    city = (By.XPATH, "//span[contains(text(),'Select City')]")
    cityselect=(By.CSS_SELECTOR,".active-result")
    save=(By.CSS_SELECTOR,"#savePatientNow")


    def enteruserdid(self):
        return self.driver.find_element(*Opdbook.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Opdbook.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Opdbook.loginclick)

    def opdclick(self):
        return self.driver.find_elements(*Opdbook.opdclicks)

    def selectdoctorclick(self):
        return self.driver.find_element(*Opdbook.clickselectdoctor)

    def selectdoctorlist(self):
        return self.driver.find_element(*Opdbook.selectdoctor)

    def bookappointmentclick(self):
        return self.driver.find_element(*Opdbook.bookappointment)

    def selectpatientclick(self):
        return self.driver.find_element(*Opdbook.selectpatient)

    def selectpatientfrompopup(self):
        return self.driver.find_element(*Opdbook.patientselect)

    def bookwithpaymentclick(self):
        return self.driver.find_element(*Opdbook.bookwithpayment)

    def selectappointment(self):
        return self.driver.find_element(*Opdbook.selectappointmentclick)

    def selectappointmentfromdropdown(self):
        return self.driver.find_elements(*Opdbook.selectappointmentfromlist)

    def selectpaymentmode(self):
        return self.driver.find_element(*Opdbook.paymentmode)

    def recordpaymentclick(self):
        return self.driver.find_element(*Opdbook.recordpayment)

    def paymentrecievedclick(self):
        return self.driver.find_element(*Opdbook.paymentrecieve)

    def addnewpatientclick(self):
        return self.driver.find_element(*Opdbook.addnewpatient)

    def selectinitial(self):
        return self.driver.find_element(*Opdbook.initial)

    def enterfirstname(self):
        return self.driver.find_element(*Opdbook.firstname)

    def enterlastname(self):
        return self.driver.find_element(*Opdbook.lastname)

    def enterage(self):
        return self.driver.find_element(*Opdbook.dob)

    def enteraddress(self):
        return self.driver.find_element(*Opdbook.address)

    def selectcityclick(self):
        return self.driver.find_element(*Opdbook.city)

    def selectcity(self):
        return self.driver.find_elements(*Opdbook.cityselect)

    def savebutton(self):
        return self.driver.find_element(*Opdbook.save)
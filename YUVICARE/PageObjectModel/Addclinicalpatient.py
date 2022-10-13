from selenium.webdriver.common.by import By


class Addclinical:
    def __init__(self,driver):
        self.driver=driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    departmentopdclick=(By.XPATH,"//div[@class='col-2 card-small-1']/a/p")
    addclinicalpatient=(By.LINK_TEXT,"Add Clinical Patient")
    noofpatient=(By.XPATH,"//input[@name='count']")
    selectdepartmentclick=(By.XPATH,"//select[@id='dept']")
    go=(By.LINK_TEXT,"Go")
    saveshift=(By.CSS_SELECTOR,"#savenshift")
    departmentlist=(By.XPATH,"//div[@id='deptfrm_dept_chosen']//span[contains(text(),'All Department')]")
    selectdepartment=(By.CSS_SELECTOR,".active-result")
    selectdoctor=(By.XPATH,"//tbody/tr[1]/td[18]/select[1]")
    gobutton=(By.XPATH,"//input[@value='Go']")
    yes=(By.XPATH,"//button[@class='btn btn-primary'][contains(text(),'Yes')]")
    referto=(By.XPATH,"//input[@value='Refer To ']")
    checkbox=(By.XPATH,"//input[@value='116']")
    submit=(By.LINK_TEXT,"Submit")



    def enteruserdid(self):
        return self.driver.find_element(*Addclinical.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Addclinical.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Addclinical.loginclick)

    def click_departmentopd(self):
        return self.driver.find_elements(*Addclinical.departmentopdclick)

    def clickaddclinicalpatient(self):
        return self.driver.find_element(*Addclinical.addclinicalpatient)

    def enternoofpatient(self):
        return self.driver.find_element(*Addclinical.noofpatient)

    def click_selectdepartment(self):
        return self.driver.find_element(*Addclinical.selectdepartmentclick)

    def click_gobutton(self):
        return self.driver.find_element(*Addclinical.go)

    def click_saveshift(self):
        return self.driver.find_element(*Addclinical.saveshift)

    def click_departmentlist(self):
        return self.driver.find_element(*Addclinical.departmentlist)

    def list_department(self):
        return self.driver.find_elements(*Addclinical.selectdepartment)

    def selectdoctordropdown(self):
        return self.driver.find_element(*Addclinical.selectdoctor)

    def click_yesbutton(self):
        return self.driver.find_element(*Addclinical.yes)

    def click_referto(self):
        return self.driver.find_element(*Addclinical.referto)

    def checkboxclick(self):
        return self.driver.find_element(*Addclinical.checkbox)

    def submit_click(self):
        return self.driver.find_element(*Addclinical.submit)

    def click_go(self):
        return self.driver.find_element(*Addclinical.gobutton)

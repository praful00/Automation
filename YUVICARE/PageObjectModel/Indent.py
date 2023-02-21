from selenium.webdriver.common.by import By


class Indentpage:

    def __init__(self, driver):
        self.driver = driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    indentclick = (By.XPATH, "//div[@class='col-2 card-small-1']/a/p")
    new = (By.LINK_TEXT, "New")
    clickselectstore = (By.XPATH, "//*[@id='warehouse_id_chosen']/a/span")
    selectstore = (By.CSS_SELECTOR, ".active-result")
    clickselectproduct = (By.XPATH, "//*[@id='product_id_chosen']/a/span")
    selectproduct = (By.CSS_SELECTOR, ".active-result")
    productquantity = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div/div[1]/div/div[5]/div/input")
    expecteddate = (By.ID, "expected_date")
    date = (By.LINK_TEXT, "28")
    addbutton=(By.LINK_TEXT, "Add")
    buissnesscoment=(By.NAME, "comment5801")
    requestbutton=(By.XPATH, "//*[@id='ireq']/div/div/div[2]/button")
    requestindent=(By.XPATH, "//*[@id='masterbodycontainer']/div/div/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[14]/a")
    notes=(By.ID,"notes")
    approvedbutton=(By.XPATH, "//*[@id='btndiv']/input[1]")
    approved = (By.XPATH, "//*[@id='masterbodycontainer']/div/div/div[1]/div[3]/div[3]/table/tbody/tr/td[14]/a")
    deliver=(By.XPATH,"//*[@id='btnhideid']/input")
    delivered=(By.XPATH,"//*[@id='masterbodycontainer']/div/div/div[1]/div[3]/div[3]/table/tbody/tr[4]/td[14]/a")
    received=(By.XPATH,"//*[@id='page_printer2']/form/div[6]/div/input[2]")


    def enteruserdid(self):
        return self.driver.find_element(*Indentpage.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Indentpage.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Indentpage.loginclick)

    def click_indent(self):
        return self.driver.find_elements(*Indentpage.indentclick)

    def click_new(self):
        return self.driver.find_element(*Indentpage.new)

    def select_store(self):
        return self.driver.find_element(*Indentpage.clickselectstore)

    def select_store_dropdown(self):
        return self.driver.find_elements(*Indentpage.selectstore)

    def select_product(self):
        return self.driver.find_element(*Indentpage.clickselectproduct)

    def select_product_dropdown(self):
        return self.driver.find_elements(*Indentpage.selectproduct)

    def enter_qty(self):
        return self.driver.find_element(*Indentpage.productquantity)

    def click_expecteddate(self):
        return self.driver.find_element(*Indentpage.expecteddate)

    def select_date(self):
        return self.driver.find_element(*Indentpage.date)

    def click_addbutton(self):
        return self.driver.find_element(*Indentpage.addbutton)

    def enter_comment(self):
        return self.driver.find_element(*Indentpage.buissnesscoment)

    def click_requestbutton(self):
        return self.driver.find_element(*Indentpage.requestbutton)

    def click_requestindent(self):
        return self.driver.find_element(*Indentpage.requestindent)

    def enter_notes(self):
        return self.driver.find_element(*Indentpage.notes)

    def click_approvedbutton(self):
        return self.driver.find_element(*Indentpage.approvedbutton)

    def click_approved(self):
        return self.driver.find_element(*Indentpage.approved)

    def click_deliverbutton(self):
        return self.driver.find_element(*Indentpage.deliver)

    def click_deliveredbutton(self):
        return self.driver.find_element(*Indentpage.delivered)

    def click_receivedbutton(self):
        return self.driver.find_element(*Indentpage.received)






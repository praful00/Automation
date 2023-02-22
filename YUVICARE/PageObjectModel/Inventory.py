from selenium.webdriver.common.by import By


class Inventory:
    def __init__(self, driver):
        self.driver = driver

    userdid = (By.NAME, "userId")
    password = (By.NAME, "password")
    loginclick = (By.ID, "lgnbtn")
    inventoryclick = (By.XPATH, "//div[@class='col-2 card-small-1']/a/p")
    navigation = (By.XPATH, "//*[@id='his']/section/div/div/div[1]/span")
    procurement = (By.XPATH, "//*[@id='menutt']/div[2]/ul/li[3]/span/a/span")
    selectlocation = (By.XPATH, "//*[@id='location_chosen']/a/span")
    location = (By.CSS_SELECTOR, ".active-result")
    grnwithpo = (By.XPATH, "/html/body/div[1]/section/div/section/div/div[1]/div[2]/form/div[1]/div[2]/div/div[3]/a")
    selectproduct = (By.XPATH, "//*[@id='product_id_chosen']/a/span")
    product = (By.CSS_SELECTOR, ".active-result")




    def enteruserdid(self):
        return self.driver.find_element(*Inventory.userdid)

    def enterpassword(self):
        return self.driver.find_element(*Inventory.password)

    def clickloginbutton(self):
        return self.driver.find_element(*Inventory.loginclick)

    def click_inventory(self):
        return self.driver.find_elements(*Inventory.inventoryclick)

    def click_navigation(self):
        return self.driver.find_element(*Inventory.navigation)

    def click_procurement(self):
        return self.driver.find_element(*Inventory.procurement)

    def click_selectlocation(self):
        return self.driver.find_element(*Inventory.selectlocation)

    def select_location(self):
        return self.driver.find_elements(*Inventory.location)

    def click_grnwithpo(self):
        return self.driver.find_element(*Inventory.grnwithpo)

    def click_selectproduct(self):
        return self.driver.find_element(*Inventory.selectproduct)

    def select_productdropdown(self):
        return self.driver.find_elements(*Inventory.product)

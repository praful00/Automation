from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://117.236.76.142:8080/YUVICARETEST/")
driver.maximize_window()
print("page title:",driver.title)
print("page url:",driver.current_url)
driver.find_element(By.ID,"email").send_keys("vspmdemo")
driver.find_element(By.NAME,"password").send_keys("Expert#100")
driver.find_element(By.ID,"lgnbtn").click()
lists=driver.find_elements(By.XPATH,"//div[@class='col-2 card-small-1']/a/p")
print(len(lists))

for itemlist in lists:
    if itemlist.text == "Registration":
        itemlist.click()

    sel=Select(driver.find_element(By.ID,"title1"))
    sel.select_by_index(2)






#driver.back()
#driver.forward()

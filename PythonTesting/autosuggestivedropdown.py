import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(3)

#DYNAMIC DROPDOWN SELECTION/AUTOUGGESTIVE DROPDOWN

slc=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")   #len function is used to get the size of obj
print(len(slc))

for country in slc:
    if country.text=="India":
        country.click()
        break


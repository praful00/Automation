from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

drop1 = driver.find_element(By.NAME,'radioButton')
print("Element is selected:",drop1.is_selected())

disp = driver.find_element(By.ID,'autocomplete')
print("Element is diplay:",disp.is_displayed())

getvalue= driver.find_element(By.ID,'autocomplete')
print("Get text value:",getvalue.get_attribute("placeholder"))
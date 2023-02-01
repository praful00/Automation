from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

row=len(driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr"))
print(row)

col=len(driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr/th"))
print(col)
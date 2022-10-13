import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="Praful"
name1="Akash"

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)     #click on the ok button
driver.find_element(By.ID, "alertbtn").click()
alert=driver.switch_to.alert
msg=alert.text
print(msg)
assert name in msg
alert.accept()



driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name1)    #click on the cancel button
driver.find_element(By.ID, "confirmbtn").click()
alert1=driver.switch_to.alert
message=alert1.text
print(message)
assert name1 in message
alert1.dismiss()






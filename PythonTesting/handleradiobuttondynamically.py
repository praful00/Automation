from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

button=driver.find_elements(By.XPATH, "//input[@class='radioButton']")
print(len(button))
button[2].click()                              #click on the radio button by using index
assert button[2].is_selected()

for radiobutton in button:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

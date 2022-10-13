from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

veglist=[]

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggielist = driver.find_elements(By.XPATH, "//tr/td[1]")

for list in veggielist:
    veglist.append(list.text)

    originallist= veglist.copy()
    veglist.sort()
assert veglist == originallist
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#mouse over action by using actionchains() method
action = ActionChains(driver)
m=driver.find_element(By.ID, "mousehover")
action.move_to_element(m).perform()

#double click on element
d=driver.find_element(By.XPATH, "//button[text()='Home']")
action.double_click(d).perform()
driver.back()

#rigtclick on the particular element by using context_click() method
r=driver.find_element(By.XPATH, "//button[text()='Home']")
action.context_click(r).perform()


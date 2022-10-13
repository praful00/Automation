from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert(driver.find_element(By.ID, "displayed-text").is_displayed())
driver.find_element(By.ID, "hide-textbox").click()
assert not (driver.find_element(By.ID, "displayed-text").is_displayed())

#is_displayed() method is used to verify the element is display on web page or not

#The isDisplayed() method is used to check whether an element is displayed on a web page or not.
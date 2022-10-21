from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

action=ActionChains(driver)  
webelement=driver.find_element(By.ID,"mousehover")
action.move_to_element(webelement).perform()
#webelement1=driver.find_element((By.LINK_TEXT,"Reload"))
#action.move_by_offset(webelement1).perform()
import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

element=driver.find_element(By.ID,'dropdown-class-example')
dropdown=Select(element)
dropdown.select_by_index(2)

time.sleep(3)

dropdown.select_by_value('option3')

time.sleep(3)

dropdown.select_by_visible_text('Option1')
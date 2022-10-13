from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Static.html")
driver.implicitly_wait(5)
action = ActionChains(driver)
drag = driver.find_element(By.CSS_SELECTOR, "#mongo")
drop = driver.find_element(By.CSS_SELECTOR, "#droparea")
action.drag_and_drop(drag, drop).perform()
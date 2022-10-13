from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://tus.io/demo.html")

fileinput = driver.find_element(By.ID, "js-file-input")
fileinput.send_keys("E:\\bill.jpg")
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("kunal@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("kunal12345")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("kunal12345")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.ID,"firstName").send_keys("praful")
driver.find_element(By.ID,"lastName").send_keys("shinde")
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("praful@gmail.com")
driver.find_element(By.ID,"userMobile").send_keys("9545847025")
time.sleep(3)

element = driver.find_element(By.XPATH,"/html/body/app-root/app-register/div[1]/section[2]/div/div[2]/form/div[3]/div[1]/select")
dropdown= Select(element)
dropdown.select_by_index(3)

driver.find_element(By.XPATH,"//input[@value='Male']").click()
time.sleep(3)
driver.find_element(By.ID,"userPassword").send_keys("Praful@12345")
driver.find_element(By.ID,"confirmPassword").send_keys("Praful@12345")
driver.find_element(By.XPATH,"//input[@formcontrolname='required']").click()
time.sleep(3)
driver.find_element(By.ID,"login").click()

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service('C:\\Users\\PrafulS\\PycharmProjects\\PythonTesting\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Praful")
driver.find_element(By.NAME,'email').send_keys("hello@gmail.com")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("123456")
driver.find_element(By.ID,'exampleCheck1').click()

dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))   #static dropdown operation
dropdown.select_by_index(0)
time.sleep(3)
dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type='submit']").click()

message=driver.find_element(By.CLASS_NAME,'alert-success').text
print(message)

assert "Success" in message



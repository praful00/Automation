from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import ActionsChain

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(3)
#how can we check if control enabled or not
ttt=driver.find_element(By.ID,"twotabsearchtextbox").is_enabled()
print(ttt)

#how can we enter the value in the text box
#driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile phone")

#how can we get the text from web element
txt=(driver.find_element(By.LINK_TEXT,"Customer Service").text)
print(txt)

#other way to retrieve text from webelement
atr=driver.find_element(By.ID,"twotabsearchtextbox").get_attribute("autocomplete")
print(atr)

driver.get_screenshot_as_file("pro.png")
driver.save_screenshot("E:\ppp.png")

#driver.get("http://demo.automationtesting.in/Static.html")
#driver.implicitly_wait(5)
#action =ActionChains(driver)
#drag=driver.find_element(By.ID,"mongo")
#drop=driver.find_element(By.ID,"droparea")
#action.drag_and_drop(drag,drop).perform()

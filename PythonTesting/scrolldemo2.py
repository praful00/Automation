import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

#Scroll by using pixel
#driver.execute_script('window.scrollBy(0,3000)')

#srl=driver.find_element(By.ID,"Methods")
#driver.execute_script("arguments[0].scrollIntoView()",srl)

#scroll end to the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#scroll to top
driver.execute_script("window.scrollTo(0,0)")


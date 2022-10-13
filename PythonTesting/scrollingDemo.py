import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

#By using pixel
#driver.execute_script('window.scrollBy(0,3000)')

#scroll by using specific element
sroll= driver.find_element(By.CSS_SELECTOR, "#Methods")
driver.execute_script("arguments[0].scrollIntoView()",sroll)

time.sleep(3)

## scroll till the end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)

## scroll to top of the page
driver.execute_script("window.scrollTo(0,0)") 
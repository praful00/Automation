from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

#child window handle

windowslist=driver.window_handles                 #return the list of all window within current the current window
print(windowslist)
driver.switch_to.window(windowslist[1])

print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windowslist[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


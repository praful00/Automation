from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")

action= ActionChains(driver)
m=driver.find_element(By.LINK_TEXT, "More")
action.move_to_element(m).perform()

driver.switch_to.default_content()
driver.find_element(By.ID, "autocomplete").send_keys("Praful shinde")


#We can switch back from a frame to default in Selenium webdriver using the switchTo().
# defaultContent() method. Initially, the webdriver control remains on the main web page.
# In order to access elements within the frame, we have to shift the control from the main page to the frame
# with the help of the switchTo()


from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#option1
driver.get_screenshot_as_file("E:\\protest.png")

#option2
driver.save_screenshot('prafultest.png')
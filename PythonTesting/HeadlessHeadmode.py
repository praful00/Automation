from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get("http://yuvicare.com:8080/YUVICARETEST/")


#when using the headless browser nothing will appear on the screen.
#Everything is done on the backend side invisible to the user.
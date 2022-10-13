from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service('C:\\Users\\PrafulS\\PycharmProjects\\PythonTesting\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

#s=Service('E:\\geckodriver.exe')
#driver = webdriver.Firefox(service=s)   #for firefox browser

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()


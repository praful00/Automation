import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


expectedresult=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actuallist=[]

driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH, "//div[@class='products']/div")  #return list of web element
count=len(results)
assert count > 0
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()    #use chaining concept in to find element by using xpath
assert expectedresult == actuallist
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
driver.refresh()
prices=driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum+int(price.text)
print(sum)
totalamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalamt

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".promoInfo")))
text=driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(text)
assert "Code" in text

discountamount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalamt > discountamount
driver.implicitly_wait(5)




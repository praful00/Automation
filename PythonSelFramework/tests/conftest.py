import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


#passing command line option to select browser at run time
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s=Service(executable_path="C:\\Users\\PrafulS\\PycharmProjects\\PythonTesting\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s1= Service(executable_path="C:\\Users\\PrafulS\\PycharmProjects\\PythonTesting\\geckodriver.exe")
        driver = webdriver.Firefox(service=s1)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver




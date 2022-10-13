import pytest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    s=Service(executable_path="C:\\Users\\PrafulS\\PycharmProjects\\PythonTesting\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("http://yuvicare.com:8080/YUVICARETEST/")
    request.cls.driver = driver
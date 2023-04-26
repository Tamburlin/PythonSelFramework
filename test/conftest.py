import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_experimental_option('detach', True)
    chromeoptions.add_argument("--start-maximized")
    service_obj = Service("C:\selenium-drivers\chrome\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chromeoptions)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


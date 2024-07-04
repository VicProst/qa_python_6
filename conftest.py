import pytest
from selenium import webdriver
# from constants import Constants
# from locators import Locators
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


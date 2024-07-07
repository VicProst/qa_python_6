import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators



@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def filling_out_for_whom_scooter_form_with_valid_data(driver):
    driver.get(Constants.URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.HOME_PAGE_HEADER))
    driver.find_element(*BasePageLocators.EVERYONE_IS_USED_TO_IT_BUTTON).click()
    driver.find_element(*BasePageLocators.ORDER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PAGE_HEADER))
    driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(Constants.NAME)
    driver.find_element(*OrderPageLocators.LAST_NAME_FIELD).send_keys(Constants.LAST_NAME)
    driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(Constants.ADDRESS)
    driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).send_keys(Constants.METRO_STATION)
    driver.find_element(*OrderPageLocators.METRO_STATION).click()
    driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(Constants.PHONE)
    driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

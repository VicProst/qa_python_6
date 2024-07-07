import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class YandexScooterBasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт {base_url}')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('Ожидание загрузки {locator}')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Ожидание кликабельности {locator}')
    def find_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not found {locator}')

    @allure.step('Кликнуть по кнопке "Заказать" вверху страницы"')
    def click_order_button_at_top_of_page(self):
        self.driver.find_element(*BasePageLocators.ORDER_BUTTON).click()

    @allure.step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Вывести адрес текущей страницы')
    def check_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Вывести адрес сайта по которому перейдешь по клику на логотип "Яндекс"')
    def check_site_link_yandex_logo(self):
        address = self.driver.find_element(*BasePageLocators.YANDEX_LOGO).get_attribute('href')
        return address

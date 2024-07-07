import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import YandexScooterBasePage


class YandexScooterOrderPage(YandexScooterBasePage):

    @allure.step('Подождать загрузки заголовка "Для кого самокат" на странице заказа')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PAGE_HEADER))

    @allure.step('Подождать загрузки заголовка "Для кого самокат" на странице заказа, и вывести его текст')
    def wait_for_load_order_page_and_get_text(self):
        title = self.find_element_located(OrderPageLocators.ORDER_PAGE_HEADER)
        return title.text

    @allure.step('Заполненить форму "Для кого самокат" и кликнуть кнопку "Далее"')
    def filling_out_form_for_whom_is_scooter(self, name, last_name, address, metro_station, phone):
        self.find_element_located(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).send_keys(metro_station)
        self.find_element_located((By.XPATH, f'//div[contains(text(), "{metro_station}")]')).click()
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Подождать загрузки заголовка "Про аренду" на странице заказа')
    def wait_for_title_about_rent(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.ABOUT_RENT_HEADER))

    @allure.step('Подождать загрузки заголовка "Про аренду" на странице заказа, и вывести его текст')
    def wait_for_title_about_rent_and_get_text(self):
        title = self.find_element_located(OrderPageLocators.ABOUT_RENT_HEADER)
        return title.text

    @allure.step('Заполненить форму "Про аренду" и кликнуть кнопку "Заказать"')
    def filling_out_form_about_rent(self, when_bring, rental_period, color_of_scooter, comment):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.find_element_located((By.XPATH, f'//div[text()="{rental_period}"]')).click()
        self.find_element_located(OrderPageLocators.WHEN_BRING_FIELD).send_keys(when_bring)
        self.driver.find_element(By.XPATH, f'//input[@id="{color_of_scooter}"]').click()
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подождать загрузки заголовка "Хотите оформить заказ?" на странице заказа')
    def wait_for_title_do_you_want_to_place_an_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.DO_YOU_WANT_TO_PLACE_AN_ORDER_HEADER))

    @allure.step('Подождать загрузки заголовка "Хотите оформить заказ?" на странице заказа, и вывести его текст')
    def wait_for_title_do_you_want_to_place_an_order_and_get_text(self):
        title = self.find_element_located(OrderPageLocators.DO_YOU_WANT_TO_PLACE_AN_ORDER_HEADER)
        return title.text

    @allure.step('Кликнуть на кнопку "Да" на странице заказа')
    def click_on_yes_button(self):
        self.find_element_located(OrderPageLocators.YES_BUTTON).click()

    @allure.step('Подождать загрузки кнопки "Посмотреть статус" на странице заказа, и вывести ее текст')
    def wait_for_view_status_button_and_get_text(self):
        button = self.find_element_located(OrderPageLocators.VIEW_STATUS_BUTTON)
        return button.text

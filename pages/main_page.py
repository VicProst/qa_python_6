import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import YandexScooterBasePage


class YandexScooterMainPage(YandexScooterBasePage):

    @allure.step('Подождать загрузки заголовка "Самокат на пару дней"')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.HOME_PAGE_HEADER))

    @allure.step('Кликнуть по кнопке "Заказать" внизу страницы')
    def click_order_button_at_bottom_of_page(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    @allure.step('Перейти к элементу - кнопке "Сколько это стоит? И как оплатить?" и кликнуть по ней')
    def go_to_element_how_much_does_it_cost_and_how_do_i_pay_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Сколько это стоит? И как оплатить?" в разделе "Вопросы о важном" и вывести его текст')
    def wait_for_drop_down_list_how_much_does_it_cost_and_how_do_i_pay_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON))
        # drop_down_list = self.find_element_located(*MainPageLocators.DROP_DOWN_LIST_HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON)
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Хочу сразу несколько самокатов! Так можно?" и кликнуть по ней')
    def go_to_element_want_several_scooters_at_once_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.WANT_SEVERAL_SCOOTERS_AT_ONCE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Хочу сразу несколько самокатов! Так можно?" и вывести его текст')
    def wait_for_drop_down_list_want_several_scooters_at_once_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_WANT_SEVERAL_SCOOTERS_AT_ONCE_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Как рассчитывается время аренды?" и кликнуть по ней')
    def go_to_element_how_is_the_rental_time_calculated_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.HOW_IS_THE_RENTAL_TIME_CALCULATED_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Как рассчитывается время аренды?" и вывести его текст')
    def wait_for_drop_down_list_how_is_the_rental_time_calculated_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_HOW_IS_THE_RENTAL_TIME_CALCULATED_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Можно ли заказать самокат прямо на сегодня?" и кликнуть по ней')
    def go_to_element_is_it_possible_to_order_a_scooter_right_for_today_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_RIGHT_FOR_TODAY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Можно ли заказать самокат прямо на сегодня?" и вывести его текст')
    def wait_for_drop_down_list_is_it_possible_to_order_a_scooter_right_for_today_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_RIGHT_FOR_TODAY_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Можно ли продлить заказ или вернуть самокат раньше?" и кликнуть по ней')
    def go_to_element_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Можно ли продлить заказ или вернуть самокат раньше?" и вывести его текст')
    def wait_for_drop_down_list_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Вы привозите зарядку вместе с самокатом?" и кликнуть по ней')
    def go_to_element_you_bring_the_charger_along_with_the_scooter_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Вы привозите зарядку вместе с самокатом?" и вывести его текст')
    def wait_for_drop_down_list_you_bring_the_charger_along_with_the_scooter_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Можно ли отменить заказ?" и кликнуть по ней')
    def go_to_element_is_it_possible_to_cancel_the_order_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.IS_IT_POSSIBLE_TO_CANCEL_THE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Можно ли отменить заказ?" и вывести его текст')
    def wait_for_drop_down_list_is_it_possible_to_cancel_the_order_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_CANCEL_THE_ORDER_BUTTON))
        return drop_down_list.text

    @allure.step('Перейти к элементу - кнопке "Я жизу за МКАДом, привезёте?" и кликнуть по ней')
    def go_to_element_i_live_across_the_mkad_will_you_bring_me_button_and_click(self):
        element = self.driver.find_element(*MainPageLocators.I_LIVE_ACROSS_THE_MKAD_WILL_YOU_BRING_ME_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Подождать загрузки выпадающего списка у кнопки "Я жизу за МКАДом, привезёте?" и вывести его текст')
    def wait_for_drop_down_list_i_live_across_the_mkad_will_you_bring_me_button_and_get_text(self):
        drop_down_list = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.DROP_DOWN_LIST_I_LIVE_ACROSS_THE_MKAD_WILL_YOU_BRING_ME_BUTTON))
        return drop_down_list.text




    def aaa(self):
        element = self.driver.find_element(*MainPageLocators.HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def bbb(self):
        drop_down_list = self.find_element_located(*MainPageLocators.DROP_DOWN_LIST_HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON)
        return drop_down_list.text


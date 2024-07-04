import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import YandexScooterBasePage


class YandexScooterOrderPage(YandexScooterBasePage):

    # Подождать загрузки заголовка "Для кого самокат"
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PAGE_HEADER))

    # Заполнить поле "Имя"
    # Заполнить поле "Фамилия"
    # Заполнить поле "Адрес: куда привезти заказ"
    # Заполнить поле "Станция метро"
    # Подождать загрузки станции метров в выпадающем списке find_element_located
    # Кликнуть на странцию метро в выпадающем списке
    # Заполнить поле "Телефон: на него позвонит курьер"
    # Кликнуть на кнопку "Далее"
    # Заполнение формы "Для кого самокат"


    # Подождать загрузки заголовка "Про аренду"


    # Заполнить поле "Когда привезти самокат"
    # Кликнуть на поле "Срок аренды"
    # Подождать загрузки списка количества суток find_element_located
    # Кликнуть на выпадающий список количество суток
    # Кликнуть на чекбокс "Цвет самоката"
    # Заполнить поле "Комментарий для курьера"
    # Кликнуть на кнопку "Заказать"
    # Заполнение формы "Про аренду"



    # Подождать загрузки заголовка "Хотите оформить заказ?" find_element_located
    # Кликнуть на кнопку "Да"
    # Подождать загрузки заголовка "Заказ оформлен"



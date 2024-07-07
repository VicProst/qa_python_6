import allure
import pytest
import datetime
from constants import Constants
from pages.main_page import YandexScooterMainPage
from pages.order_page import YandexScooterOrderPage
from conftest import driver
from conftest import filling_out_for_whom_scooter_form_with_valid_data


@allure.epic('test_yandex_scooter_order_page')
class TestYandexScooterOrderPage:

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = today + datetime.timedelta(days=2)
    today_plus10_days = today + datetime.timedelta(days=10)

    @allure.title('12-30. Проверка валидации формы "Для кого самокат"')
    @allure.description('При заполнении формы "Для кого самокат" на странице заказа валидными данными, можно перейти в форму "Про аренду"')
    @pytest.mark.parametrize('name, last_name, address, metro_station, phone',
                             [['ви', 'пр', 'хорош', 'поле', '12345678901'],
                              ['вик', 'про', 'хороше', 'жаев', '123456789012'],
                              ['виктор', 'простяков', 'хорошевскоехорошевскоехор', 'ская', '00000000000'],
                              ['викторвикторви', 'простяковпрост', 'хорошевскоехорошевскоехорошевскоехорошевскоехорош', 'Баррикадная', '00000000001'],
                              ['викторвикторвик', 'простяковпростя', 'хорошевскоехорошевскоехорошевскоехорошевскоехорош', 'Пушкинская', '55555555555'],
                              [' виктор', 'простяков', ' хорошевское', 'Кузнецкий Мост', '999999999998'],
                              ['вик тор', 'простяков', 'хорошевское шоссе', 'Орехово', '999999999999'],
                              ['виктор ', 'простяков', 'хорошевское ', 'Таганская', '+1234567890'],
                              ['виктор', 'простяков', '-хорошевское', 'Сокольники', '12345678901'],
                              ['виктор', 'простяков', 'хорошевское-', 'Лубянка', '12345678901'],
                              ['виктор', 'простяков', '.хорошевское', 'Спортивная', '12345678901'],
                              ['виктор', 'простяков', 'хорошевское.шоссе', 'Университет', '12345678901'],
                              ['виктор', 'простяков', 'хорошевское.', 'Сокол', '12345678901'],
                              ['виктор', 'простяков', ',хорошевское', 'Аэропорт', '12345678901'],
                              ['виктор', 'простяков', 'хорошевское,шоссе', 'Динамо', '12345678901'],
                              ['виктор', 'простяков', 'хорошевское,', 'Тверская', '12345678901'],
                              ['ВИКТОР', 'ПРОСТЯКОВ', 'ХОРОШЕВСКОЕ', 'Киевская', '12345678901'],
                              ['Виктор', 'Простяков', 'Хорошевское', 'Арбатская', '12345678901'],
                              ['Виктор', 'Простяков', 'хорошевское34', 'Курская', '12345678901']])
    def test_validation_of_who_is_scooter_for_form_valid_parameters_about_rent_form_opens(self, driver, name, last_name, address, metro_station, phone):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.click_order_button_at_top_of_page()
        order_page = YandexScooterOrderPage(driver)
        order_page.filling_out_form_for_whom_is_scooter(name, last_name, address, metro_station, phone)
        title = order_page.wait_for_title_about_rent_and_get_text()
        assert title == 'Про аренду'

    @allure.title('31-48. Проверка оформления заказа')
    @allure.description('При заполнении форм "Для кого самокат" и "Про аренду" на странице заказа валидными данными, можно оформить заказ')
    @pytest.mark.parametrize('when_bring, rental_period, color_of_scooter, comment',
                             [[f'{tomorrow}', 'сутки', 'black', 'й'],
                              [f'{day_after_tomorrow}', 'двое суток', 'grey', 'йфяцычувскамеп'],
                              [f'{today_plus10_days}', 'трое суток', 'black', 'йцукенгшщзйцукенгшщзйцу'],
                              [f'{tomorrow}', 'четверо суток', 'black', 'йцукенгшщзйцукенгшщзйцук'],
                              [f'{tomorrow}', 'пятеро суток', 'black', ' хорошевское'],
                              [f'{tomorrow}', 'шестеро суток', 'black', 'хорошевское шоссе'],
                              [f'{tomorrow}', 'семеро суток', 'black', 'хорошевское '],
                              [f'{tomorrow}', 'сутки', 'black', '-хорошевское'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское-'],
                              [f'{tomorrow}', 'сутки', 'black', '.хорошевское'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское.шоссе'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское.'],
                              [f'{tomorrow}', 'сутки', 'black', ',хорошевское'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское,шоссе'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское,'],
                              [f'{tomorrow}', 'сутки', 'black', 'ХОРОШЕВСКОЕ'],
                              [f'{tomorrow}', 'сутки', 'black', 'Хорошевское'],
                              [f'{tomorrow}', 'сутки', 'black', 'хорошевское34']])
    def test_placing_an_order_valid_parameters_view_status_button_opens(self, driver, filling_out_for_whom_scooter_form_with_valid_data, when_bring, rental_period, color_of_scooter, comment):
        order_page = YandexScooterOrderPage(driver)
        order_page.filling_out_form_about_rent(when_bring, rental_period, color_of_scooter, comment)
        order_page.click_on_yes_button()
        button_text = order_page.wait_for_view_status_button_and_get_text()
        assert button_text == 'Посмотреть статус'

    @allure.title('49. Проверка кнопки логотипа "Самокат"')
    @allure.description('При нажатии на логотип "Самокат", попадёшь на главную страницу "Самоката"')
    def test_click_scooter_logo_open_main_page(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.click_order_button_at_top_of_page()
        order_page = YandexScooterOrderPage(driver)
        order_page.click_scooter_logo()
        main_title = main_page.wait_for_load_main_page_and_get_text()
        assert main_title == 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

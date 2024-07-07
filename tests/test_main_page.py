import allure
from constants import Constants
from pages.main_page import YandexScooterMainPage
from pages.order_page import YandexScooterOrderPage
from conftest import driver


@allure.epic('test_yandex_scooter_main_page')
class TestYandexScooterMainPage:

    @allure.title('1. Проверка выпадающего текста у кнопки "Сколько это стоит? И как оплатить?"')
    @allure.description('При клике на кнопку "Сколько это стоит? И как оплатить?" на главной странице, выпадает текст "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def test_drop_down_list_click_how_much_does_it_cost_and_how_do_i_pay_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_how_much_does_it_cost_and_how_do_i_pay_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_how_much_does_it_cost_and_how_do_i_pay_button_and_get_text()
        assert drop_down_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'


    @allure.title('2. Проверка выпадающего текста у кнопки "Хочу сразу несколько самокатов! Так можно?"')
    @allure.description('При клике на кнопку "Хочу сразу несколько самокатов! Так можно?" на главной странице, выпадает текст "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    def test_drop_down_list_click_want_several_scooters_at_once_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_want_several_scooters_at_once_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_want_several_scooters_at_once_button_and_get_text()
        assert drop_down_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('3. Проверка выпадающего текста у кнопки "Как рассчитывается время аренды?"')
    @allure.description('При клике на кнопку "Как рассчитывается время аренды?" на главной странице, выпадает текст "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    def test_drop_down_list_click_how_is_the_rental_time_calculated_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_how_is_the_rental_time_calculated_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_how_is_the_rental_time_calculated_button_and_get_text()
        assert drop_down_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('4. Проверка выпадающего текста у кнопки "Можно ли заказать самокат прямо на сегодня?"')
    @allure.description('При клике на кнопку "Можно ли заказать самокат прямо на сегодня?" на главной странице, выпадает текст "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')
    def test_drop_down_list_click_is_it_possible_to_order_a_scooter_right_for_today_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_is_it_possible_to_order_a_scooter_right_for_today_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_is_it_possible_to_order_a_scooter_right_for_today_button_and_get_text()
        assert drop_down_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('5. Проверка выпадающего текста у кнопки "Можно ли продлить заказ или вернуть самокат раньше?"')
    @allure.description('При клике на кнопку "Можно ли продлить заказ или вернуть самокат раньше?" на главной странице, выпадает текст "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."')
    def test_drop_down_list_click_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_and_get_text()
        assert drop_down_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('6. Проверка выпадающего текста у кнопки "Вы привозите зарядку вместе с самокатом?"')
    @allure.description('При клике на кнопку "Вы привозите зарядку вместе с самокатом?" на главной странице, выпадает текст "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    def test_drop_down_list_click_you_bring_the_charger_along_with_the_scooter_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_you_bring_the_charger_along_with_the_scooter_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_you_bring_the_charger_along_with_the_scooter_button_and_get_text()
        assert drop_down_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('7. Проверка выпадающего текста у кнопки "Можно ли отменить заказ?"')
    @allure.description('При клике на кнопку "Можно ли отменить заказ?" на главной странице, выпадает текст "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."')
    def test_drop_down_list_click_is_it_possible_to_cancel_the_order_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_is_it_possible_to_cancel_the_order_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_is_it_possible_to_cancel_the_order_button_and_get_text()
        assert drop_down_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('8. Проверка выпадающего текста у кнопки "Я жизу за МКАДом, привезёте?"')
    @allure.description('При клике на кнопку "Я жизу за МКАДом, привезёте?" на главной странице, выпадает текст "Да, обязательно. Всем самокатов! И Москве, и Московской области."')
    def test_drop_down_list_click_i_live_across_the_mkad_will_you_bring_me_button_correct_text(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.go_to_element_i_live_across_the_mkad_will_you_bring_me_button_and_click()
        drop_down_text = main_page.wait_for_drop_down_list_i_live_across_the_mkad_will_you_bring_me_button_and_get_text()
        assert drop_down_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @allure.title('9. Проверка работы кнопки "Заказать" внизу страницы')
    @allure.description('При клике по кнопке "Заказать" внизу страницы открывается форма "Для кого самокат" на странце заказа')
    def test_click_order_button_at_bottom_of_page_order_page_opens(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.click_order_button_at_bottom_of_page()
        order_page = YandexScooterOrderPage(driver)
        title = order_page.wait_for_load_order_page_and_get_text()
        assert title == 'Для кого самокат'

    @allure.title('10. Проверка работы кнопки "Заказать" вверху страницы')
    @allure.description('При клике по кнопке "Заказать" вверху страницы открывается форма "Для кого самокат" на странце заказа')
    def test_click_order_button_at_top_of_page_order_page_opens(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        main_page.click_order_button_at_top_of_page()
        order_page = YandexScooterOrderPage(driver)
        title = order_page.wait_for_load_order_page_and_get_text()
        assert title == 'Для кого самокат'

    @allure.title('11. Проверка редиректа на главную страницу Дзена по логотипу "Яндекс"')
    @allure.description('При клике на логотип "Яндекс", в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_logo_zen_home_page_opens(self, driver):
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Constants.URL)
        main_page.wait_for_load_main_page_and_click_everyone_is_used_to_it_button()
        site = main_page.check_site_link_yandex_logo()
        main_page.go_to_site(site)
        url = main_page.check_url()
        assert url == 'https://dzen.ru/?yredirect=true'

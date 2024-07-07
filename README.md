# Проект автоматизации тестирования сервиса Яндекс Самокат
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 

Содержание проекта:

В корне:
- .gitignore.
- conftest.py.
- constants.py.
- README.md.
- requirements.txt.

Папка locators:
- base_page_locators.py.
- main_page_locators.py.
- order_page_locators.py.

Папка pages:
- base_page.py.
- main_page.py.
- order_page.py.

Папка tests:
- test_main_page.py.
- test_order)page.py.

Тесты главной страницы - test_main_page.py.

    1. Проверка выпадающего текста у кнопки "Сколько это стоит? И как оплатить?" - test_drop_down_list_click_how_much_does_it_cost_and_how_do_i_pay_button_correct_text.
    2. Проверка выпадающего текста у кнопки "Хочу сразу несколько самокатов! Так можно?" - test_drop_down_list_click_want_several_scooters_at_once_button_correct_text.
    3. Проверка выпадающего текста у кнопки "Как рассчитывается время аренды?" - test_drop_down_list_click_how_is_the_rental_time_calculated_button_correct_text.
    4. Проверка выпадающего текста у кнопки "Можно ли заказать самокат прямо на сегодня?" - test_drop_down_list_click_is_it_possible_to_order_a_scooter_right_for_today_button_correct_text.
    5. Проверка выпадающего текста у кнопки "Можно ли продлить заказ или вернуть самокат раньше?" - test_drop_down_list_click_is_it_possible_to_extend_the_order_or_return_the_scooter_earlier_button_correct_text.
    6. Проверка выпадающего текста у кнопки "Вы привозите зарядку вместе с самокатом?" - test_drop_down_list_click_you_bring_the_charger_along_with_the_scooter_button_correct_text.
    7. Проверка выпадающего текста у кнопки "Можно ли отменить заказ?" - test_drop_down_list_click_is_it_possible_to_cancel_the_order_button_correct_text.
    8. Проверка выпадающего текста у кнопки "Я жизу за МКАДом, привезёте?" - test_drop_down_list_click_i_live_across_the_mkad_will_you_bring_me_button_correct_text.
    9. Проверка работы кнопки "Заказать" внизу страницы - test_click_order_button_at_bottom_of_page_order_page_opens.
    10. Проверка работы кнопки "Заказать" вверху страницы - test_click_order_button_at_top_of_page_order_page_opens.
    11. Проверка редиректа на главную страницу Дзена по логотипу "Яндекс" - test_click_yandex_logo_zen_home_page_opens.

Тесты страницы заказа - test_order_page.py.

    12-30. Проверка валидации формы "Для кого самокат" - test_validation_of_who_is_scooter_for_form_valid_parameters_about_rent_form_opens.
    31-48. Проверка оформления заказа - test_placing_an_order_valid_parameters_view_status_button_opens.
    49. Проверка кнопки логотипа "Самокат" - test_click_scooter_logo_open_main_page.


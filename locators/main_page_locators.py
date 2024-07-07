from selenium.webdriver.common.by import By


class MainPageLocators:

        # Заголовок "Самокат на пару дней"
    HOME_PAGE_HEADER = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')

        # Кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

        # Кнопка "Сколько это стоит? И как оплатить?"
    HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON = (By.XPATH, '//div[@id="accordion__heading-0"]')
        # Кнопка "Хочу сразу несколько самокатов! Так можно?"
    WANT_SEVERAL_SCOOTERS_AT_ONCE_BUTTON = (By.XPATH, '//div[@id="accordion__heading-1"]')
        # Кнопка "Как рассчитывается время аренды?"
    HOW_IS_THE_RENTAL_TIME_CALCULATED_BUTTON = (By.XPATH, '//div[@id="accordion__heading-2"]')
        # Кнопка "Можно ли заказать самокат прямо на сегодня?"
    IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_RIGHT_FOR_TODAY_BUTTON = (By.XPATH, '//div[@id="accordion__heading-3"]')
        # Кнопка "Можно ли продлить заказ или вернуть самокат раньше?"
    IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON = (By.XPATH, '//div[@id="accordion__heading-4"]')
        # Кнопка "Вы привозите зарядку вместе с самокатом?"
    YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER_BUTTON = (By.XPATH, '//div[@id="accordion__heading-5"]')
        # Кнопка "Можно ли отменить заказ?"
    IS_IT_POSSIBLE_TO_CANCEL_THE_ORDER_BUTTON = (By.XPATH, '//div[@id="accordion__heading-6"]')
        # Кнопка "Я жизу за МКАДом, привезёте?"
    I_LIVE_ACROSS_THE_MKAD_WILL_YOU_BRING_ME_BUTTON = (By.XPATH, '//div[@id="accordion__heading-7"]')

        # Выпадающий список кнопки "Сколько это стоит? И как оплатить?"
    DROP_DOWN_LIST_HOW_MUCH_DOES_IT_COST_AND_HOW_DO_I_PAY_BUTTON = (By.XPATH, '//div[@id="accordion__panel-0"]/p')
        # Выпадающий список кнопки "Хочу сразу несколько самокатов! Так можно?"
    DROP_DOWN_LIST_WANT_SEVERAL_SCOOTERS_AT_ONCE_BUTTON = (By.XPATH, '//div[@id="accordion__panel-1"]/p')
        # Выпадающий список кнопки "Как рассчитывается время аренды?"
    DROP_DOWN_LIST_HOW_IS_THE_RENTAL_TIME_CALCULATED_BUTTON = (By.XPATH, '//div[@id="accordion__panel-2"]/p')
        # Выпадающий список кнопки "Можно ли заказать самокат прямо на сегодня?"
    DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_ORDER_A_SCOOTER_RIGHT_FOR_TODAY_BUTTON = (By.XPATH, '//div[@id="accordion__panel-3"]/p')
        # Выпадающий список кнопки "Можно ли продлить заказ или вернуть самокат раньше?"
    DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_EXTEND_THE_ORDER_OR_RETURN_THE_SCOOTER_EARLIER_BUTTON = (By.XPATH, '//div[@id="accordion__panel-4"]/p')
        # Выпадающий список кнопки "Вы привозите зарядку вместе с самокатом?"
    DROP_DOWN_LIST_YOU_BRING_THE_CHARGER_ALONG_WITH_THE_SCOOTER_BUTTON = (By.XPATH, '//div[@id="accordion__panel-5"]/p')
        # Выпадающий список кнопки "Можно ли отменить заказ?"
    DROP_DOWN_LIST_IS_IT_POSSIBLE_TO_CANCEL_THE_ORDER_BUTTON = (By.XPATH, '//div[@id="accordion__panel-6"]/p')
        # Выпадающий список кнопки "Я жизу за МКАДом, привезёте?"
    DROP_DOWN_LIST_I_LIVE_ACROSS_THE_MKAD_WILL_YOU_BRING_ME_BUTTON = (By.XPATH, '//div[@id="accordion__panel-7"]/p')

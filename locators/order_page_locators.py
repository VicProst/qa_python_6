from selenium.webdriver.common.by import By


class OrderPageLocators:

        # Заголовок "Для кого самокат"
    ORDER_PAGE_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
        # Поле "Имя"
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
        # Поле "Фамилия"
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
        # Поле "Адрес: куда привезти заказ"
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
        # Поле "Станция метро"
    METRO_STATION_FIELD = (By.XPATH, '//input[@class="select-search__input"]')
        # Станция метро "Полежаевская" в выпадающем списке
    METRO_STATION = (By.XPATH, '//div[text()="Полежаевская"]')
        # Поле "Телефон: на него позвонит курьер"
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
        # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

        # Заголовок "Про аренду"
    ABOUT_RENT_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
        # Поле "Когда привезти самокат"
    WHEN_BRING_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
        # Поле "Срок аренды"
    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[@class="Dropdown-control"]')
        # Графа "двое суток" в выпадающем списке
    RENTAL_PERIOD = (By.XPATH, '//div[text()="двое суток"]')
        # Чекбокс "чёрный жемчуг" в поле "Цвет самоката"
    COLOR_OF_SCOOTER = (By.XPATH, '//input[@id="black"]')
        # Поле "Комментарий для курьера"
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
        # Кнопку "Заказать"
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

        # Заголовок "Хотите оформить заказ?"
    DO_YOU_WANT_TO_PLACE_AN_ORDER_HEADER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
        # Кнопку "Да"
    YES_BUTTON = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

        # Кнопка "Посмотреть статус"
    VIEW_STATUS_BUTTON = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]')

from selenium.webdriver.common.by import By


class BasePageLocators:

        # Кнопка "Заказать" вверху страницы
    ORDER_BUTTON =(By.XPATH, '//button[@class="Button_Button__ra12g"]')
        # Логотип «Самокат»
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
        # логотипу "Яндекс"
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')


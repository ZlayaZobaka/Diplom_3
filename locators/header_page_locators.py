from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class HeaderPageLocator(CommonLocators):
    # кнопка Конструктор
    header_builder_btn = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'
                                    '[text() = "Конструктор"]')

    # кнопка Лента Заказов
    header_feed_btn = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'
                                 '[text() = "Лента Заказов"]')

    # логотип Stellar Burgers
    header_main_logo = (By.XPATH, './/div[@class = "AppHeader_header__logo__2D0X2"]')

    # кнопка Личный кабинет в заголовке
    header_login_btn = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'
                                  '[text() = "Личный Кабинет"]')


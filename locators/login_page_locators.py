from selenium.webdriver.common.by import By
from locators.header_page_locators import HeaderPageLocator


class LoginPageLocators(HeaderPageLocator):

    # поле для ввода Email
    email_input = (By.XPATH, './/input[@type = "text"][@name = "name"]')

    # поле для ввода пароля
    password_input = (By.XPATH, './/input[@type = "password"][@name = "Пароль"]')

    # кнопка Войти
    login_btn = (By.CSS_SELECTOR, '.button_button_size_medium__3zxIa')

    # ссылка Восстановить пароль
    forgot_pass_link = (By.LINK_TEXT, 'Восстановить пароль')

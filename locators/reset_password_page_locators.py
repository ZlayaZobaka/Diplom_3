from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class ResetPasswordPageLocator(CommonLocators):

    # поле для ввода Email
    email_input = (By.XPATH, './/label[text()="Email"]/parent::div/input')

    # кнопка Восстановить
    restore_btn = (By.XPATH, './/button[text() = "Восстановить"]')

    # поле для ввода нового пароля
    new_password_input = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')

    # кнопка показать/скрыть пароль
    see_hidden_btn = (By.CSS_SELECTOR, '.input__icon')

    # поле для ввода кода из письма
    code_input = (By.XPATH, './/label[text()="Введите код из письма"]/parent::div/input')

    # кнопка Сохранить
    save_btn = (By.XPATH, './/button[text() = "Сохранить"]')

    # ссылка Войти
    login_link = (By.LINK_TEXT, 'Войти')

    # класс активности поля
    active_status_class = "input_status_active"

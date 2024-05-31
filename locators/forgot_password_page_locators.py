from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class ForgotPasswordPageLocator(CommonLocators):
    # поле для ввода Email
    email_input = (By.XPATH, './/label[text()="Email"]/parent::div/input')

    # кнопка Восстановить
    restore_btn = (By.XPATH, './/button[text() = "Восстановить"]')


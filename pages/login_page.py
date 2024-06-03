import allure
from locators.login_page_locators import LoginPageLocators
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class LoginPage(HeaderPage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Вводим емейл")
    def set_email(self, text):
        self.find_element(LoginPageLocators.email_input).send_keys(text)

    @allure.step("Вводим пароль")
    def set_password(self, text):
        self.find_element(LoginPageLocators.password_input).send_keys(text)

    @allure.step("Логинимся")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)

        return self.click_login_btn()

    @allure.step("Кликаем по кнопке Войти")
    def click_login_btn(self):
        self.find_element(LoginPageLocators.login_btn).click()
        self.wait_invisibility_of_element(LoginPageLocators.modal_overlay)

        return MainPage(self.driver)

    @allure.step("Кликаем по ссылке Восстановить пароль")
    def click_forgot_pass_link(self):
        self.find_element(LoginPageLocators.forgot_pass_link).click()

        return ResetPasswordPage(self.driver)


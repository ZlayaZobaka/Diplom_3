import allure
from locators.login_page_locators import LoginPageLocators
from pages.header_page import HeadersPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage


class LoginPage(HeadersPage):

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, text):
        self.find_element(LoginPageLocators.email_input).send_keys(text)

    def set_password(self, text):
        self.find_element(LoginPageLocators.password_input).send_keys(text)

    def click_login_btn(self):
        self.find_element(LoginPageLocators.login_btn).click()

        return MainPage(self.driver)

    def click_forgot_pass_link(self):
        self.find_element(LoginPageLocators.forgot_pass_link).click()

        return ForgotPasswordPage(self.driver)


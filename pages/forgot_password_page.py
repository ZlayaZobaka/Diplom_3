import time

import allure
import pytest
from data import Urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocator
from pages.header_page import HeadersPage
from pages.reset_password_page import ResetPasswordPage


class ForgotPasswordPage(HeadersPage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, text):
        self.find_element(ForgotPasswordPageLocator.email_input).send_keys(text)

    def click_restore_btn(self):
        self.find_element(ForgotPasswordPageLocator.restore_btn).click()

        return ResetPasswordPage(self.driver)



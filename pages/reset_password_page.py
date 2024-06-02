import time

import allure
import pytest
from data import Urls
from locators.reset_password_page_locators import ResetPasswordPageLocator
from pages.header_page import HeadersPage


class ResetPasswordPage(HeadersPage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_password(self, text):
        self.find_element(ResetPasswordPageLocator.new_password_input).send_keys(text)

    def set_code(self, text):
        self.find_element(ResetPasswordPageLocator.code_input).send_keys(text)

    def is_password_input_active(self):
        element = self.find_element(ResetPasswordPageLocator.new_password_input)
        class_ = element.find_element(*ResetPasswordPageLocator.parent).get_attribute('class')

        return True if ResetPasswordPageLocator.active_status_class in class_ else False

    def click_see_hidden_btn(self):
        self.find_element(ResetPasswordPageLocator.see_hidden_btn).click()

    def set_email(self, text):
        self.find_element(ResetPasswordPageLocator.email_input).send_keys(text)

    def click_restore_btn(self):
        self.find_element(ResetPasswordPageLocator.restore_btn).click()

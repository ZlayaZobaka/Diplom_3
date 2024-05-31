import allure
from locators.header_page_locators import HeaderPageLocator
from pages.base_page import BasePage


class HeadersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_builder_btn(self):
        self.find_element(HeaderPageLocator.header_builder_btn).click()

    def click_feed_btn(self):
        self.find_element(HeaderPageLocator.header_feed_btn).click()

    def click_main_logo(self):
        self.find_element(HeaderPageLocator.header_main_logo).click()

    def click_login_btn(self):
        self.find_element(HeaderPageLocator.header_login_btn).click()

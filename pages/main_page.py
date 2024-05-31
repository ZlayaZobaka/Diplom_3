import allure
from locators.main_page_locators import MainPageLocators as Locators
from pages.header_page import HeadersPage


class MainPage(HeadersPage):

    def __init__(self, driver):
        super().__init__(driver)


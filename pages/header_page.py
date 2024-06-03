import allure
from locators.header_page_locators import HeaderPageLocator
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликаем по кнопке Конструктор")
    def click_builder_btn(self):
        self.find_element(HeaderPageLocator.header_builder_btn).click()

    @allure.step("Кликаем по кнопке Лента заказов")
    def click_feed_btn(self):
        self.find_element(HeaderPageLocator.header_feed_btn).click()

    @allure.step("Кликаем по кнопке с логотипом изделия")
    def click_main_logo(self):
        self.find_element(HeaderPageLocator.header_main_logo).click()

    @allure.step("Кликаем по кнопке Личный кабинет")
    def click_lk_btn(self):
        self.find_element(HeaderPageLocator.header_login_btn).click()

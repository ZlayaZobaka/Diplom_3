import allure
from pages.header_page import HeadersPage
from locators.account_page_locators import AccountPageLocators


class AccountPage(HeadersPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_order_history_btn(self):
        self.find_element(AccountPageLocators.order_history_link).click()

    def click_exit_account_btn(self):
        self.find_element(AccountPageLocators.exit_btn).click()

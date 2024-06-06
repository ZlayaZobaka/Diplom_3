import allure
from pages.header_page import HeaderPage
from locators.account_page_locators import AccountPageLocators


class AccountPage(HeaderPage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликаем по кнопке История заказов")
    def click_order_history_btn(self):
        self.find_element(AccountPageLocators.order_history_link).click()

    @allure.step("Кликаем по кнопке Выход")
    def click_exit_account_btn(self):
        self.wait_invisibility_of_element(AccountPageLocators.modal_overlay)
        self.find_element(AccountPageLocators.exit_btn).click()

    @allure.step("Возвращаем список заказов из раздела История заказов")
    def get_user_orders_list(self):
        order_list = self.find_element(AccountPageLocators.user_order_list)

        return order_list.find_elements(*AccountPageLocators.children)

    @allure.step("Получаем номер заказа")
    def get_user_order_id(self, order):
        return order.find_element(*AccountPageLocators.order_id).text

    @allure.title("Проверяем, доступно ли кнопка Выход")
    def is_exit_btn_visible(self):
        return self.is_element_visible(AccountPageLocators.exit_btn)

    @allure.title("Проверяем, доступно ли форма со списком заказов")
    def is_order_history_form_present(self):
        return self.is_element_present(AccountPageLocators.order_history_form)
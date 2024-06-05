import allure
import random
from locators.feed_page_locators import FeedPageLocators
from pages.header_page import HeaderPage


class FeedPage(HeaderPage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получаем список заказов")
    def get_orders_list(self):
        orders_list = self.find_element(FeedPageLocators.orders_list)

        return orders_list.find_elements(*FeedPageLocators.children)

    @allure.step("Получаем номера заказов")
    def get_orders_ids_list(self):
        orders_list = self.get_orders_list()

        return [x.find_element(*FeedPageLocators.order_id).text for x in orders_list]

    @allure.step("Выбираем случайный заказ")
    def get_random_order(self):
        orders = self.get_orders_list()

        return random.choice(orders)

    @allure.step("Получаем значение общего счетчика заказов")
    def get_common_order_counter(self):
        return int(self.find_element(FeedPageLocators.common_order_counter).text)

    @allure.step("Получаем значение счетчика заказов за сегодня")
    def get_today_order_counter(self):
        return int(self.find_element(FeedPageLocators.today_order_counter).text)

    @allure.step("Получаем номера заказов в статусе В работе")
    def get_in_work_orders_ids(self):
        return self.find_element(FeedPageLocators.in_work_section).text

import allure
import random
from pages.header_page import HeaderPage
from locators.main_page_locators import MainPageLocators


class MainPage(HeaderPage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выбираем случайный ингредиент")
    def get_random_ingredient(self, parent_locator):
        parent = self.find_element(parent_locator)
        children = parent.find_elements(*MainPageLocators.children)

        return random.choice(children)

    @allure.step("Закрываем окно с описанием ингредиента")
    def close_description_window(self):
        self.find_element(MainPageLocators.close_description_btn).click()
        self.wait_invisibility_of_element(MainPageLocators.ingredient_desc)

    @allure.step("Закрываем окно с описанием заказа")
    def close_order_window(self):
        self.wait_invisibility_of_element(MainPageLocators.modal_overlay)
        self.find_element(MainPageLocators.close_description_btn).click()

    @allure.step("Получаем номер заказа")
    def get_order_id(self):
        self.wait_invisibility_of_element(MainPageLocators.modal_overlay)
        return self.find_element(MainPageLocators.order_id).text

    @allure.step("Получаем значение счетчика ингредиента")
    def get_ingredient_counter(self, parent_element):
        return int(parent_element.find_element(*MainPageLocators.ingredient_counter).text)

    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient):
        dest_element = self.find_element(MainPageLocators.order_basket)
        self.drag_and_drop(ingredient, dest_element)

    @allure.step("Создаем случайный рецепт")
    def get_random_recipe(self):
        return \
            [
                self.get_random_ingredient(MainPageLocators.builder_bread_list),
                self.get_random_ingredient(MainPageLocators.builder_sauce_list),
                self.get_random_ingredient(MainPageLocators.builder_topping_list)
            ]

    @allure.step("Делаем заказ")
    def make_an_order(self):
        self.find_element(MainPageLocators.make_an_order_btn).click()


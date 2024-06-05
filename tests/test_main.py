import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators


class TestMain:

    @allure.title('Тест перехода с ленты заказов по клику на «Конструктор»')
    @allure.description('Открываем ленту заказов, кликаем на кнопку «Конструктор», '
                        'проверяем, что странице есть форма конструктора')
    def test_from_feed_go_to_builder_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_btn()

        main_page.click_builder_btn()

        assert main_page.is_element_visible(MainPageLocators.build_burger_section)

    @allure.title('Тест перехода на ленту заказов')
    @allure.description('На главной странице кликаем на кнопку «Лента заказов», '
                        'проверяем, что странице есть форма со списком заказов')
    def test_go_to_feed_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_feed_btn()

        assert main_page.is_element_visible(FeedPageLocators.feed_form)

    @allure.title('Тест всплывающего окно с деталями ингредиента')
    @allure.description('На главной странице в форме конструктора кликаем на произвольный ингредиент, '
                        'проверяем, что всплывает окно с описанием')
    @pytest.mark.parametrize('section',
                             [
                                 MainPageLocators.builder_bread_list,
                                 MainPageLocators.builder_sauce_list,
                                 MainPageLocators.builder_topping_list
                             ])
    def test_open_ingredient_window_successful(self, driver, section):
        main_page = MainPage(driver)

        ingredient = main_page.get_random_ingredient(section)
        main_page.click_to_element(ingredient)

        assert main_page.is_element_visible(MainPageLocators.ingredient_desc)

    @allure.title('Тест закрытия всплывающего окно с деталями ингредиента')
    @allure.description('На главной странице в форме конструктора кликаем на произвольный ингредиент, '
                        'закрываем окно с описанием, проверяем, что всплывающее окно пропало')
    @pytest.mark.parametrize('section',
                             [
                                 MainPageLocators.builder_bread_list,
                                 MainPageLocators.builder_sauce_list,
                                 MainPageLocators.builder_topping_list
                             ])
    def test_close_ingredient_window_successful(self, driver, section):
        main_page = MainPage(driver)

        ingredient = main_page.get_random_ingredient(section)
        main_page.click_to_element(ingredient)
        old_state_window_openness = main_page.is_element_visible(MainPageLocators.ingredient_desc)
        main_page.close_description_window()
        new_state_window_openness = main_page.is_element_visible(MainPageLocators.ingredient_desc)

        assert old_state_window_openness is True and new_state_window_openness is False

    @allure.title('Тест инкремента счетчика ингредиента')
    @allure.description('На главной странице в форме конструктора добавляем в заказ на произвольный ингредиент, '
                        'проверяем, что его счетчик увеличился')
    @pytest.mark.parametrize('section',
                             [
                                 MainPageLocators.builder_bread_list,
                                 MainPageLocators.builder_sauce_list,
                                 MainPageLocators.builder_topping_list
                             ])
    def test_add_ingredient_to_order_increment_counter(self, driver, section):
        main_page = MainPage(driver)

        ingredient = main_page.get_random_ingredient(section)

        old_count = main_page.get_ingredient_counter(ingredient)
        main_page.add_ingredient_to_order(ingredient)
        new_count = main_page.get_ingredient_counter(ingredient)

        assert 0 == old_count < new_count

    @allure.title('Авторизованный пользователь может оформить заказ')
    @allure.description('Логинимся, создаем произвольный заказ, проверяем, что его можно оформить')
    def test_logged_user_make_an_order_show_order_id(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        recipe = main_page.get_random_recipe()
        for i in recipe:
            main_page.add_ingredient_to_order(i)

        main_page.make_an_order()

        assert main_page.is_element_visible(MainPageLocators.order_id)

import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators


class TestFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('С главной страницы переходим в Ленту заказов, кликаем в произвольный заказ'
                        'проверяем, что открылось окно с деталями заказа')
    def test_open_order_description_window_successful(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_btn()
        feed_page = FeedPage(driver)
        order = feed_page.get_random_order()

        feed_page.click_to_element(order)

        assert feed_page.is_element_visible(FeedPageLocators.order_window)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Авторизуемся, создаем заказ'
                        'проверяем, id заказа в профиле есть в «Ленте заказов» ')
    def test_user_order_exist_in_common_order_feed(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        recipe = main_page.get_random_recipe()
        for i in recipe:
            main_page.add_ingredient_to_order(i)
        main_page.make_an_order()
        main_page.close_order_window()

        main_page.click_lk_btn()
        account_page = AccountPage(driver)
        account_page.click_order_history_btn()

        user_orders = account_page.get_user_orders_list()
        order_id = account_page.get_user_order_id(user_orders[0])

        main_page.click_feed_btn()
        feed_page = FeedPage(driver)
        orders = feed_page.get_orders_ids_list()

        assert order_id in orders

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Авторизуемся, создаем заказ'
                        'проверяем, что в «Ленте заказов» счётчик Выполнено за всё время увеличился')
    def test_create_order_increment_common_order_counter(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        main_page.click_feed_btn()
        feed_page = FeedPage(driver)
        old_common_order_counter = feed_page.get_common_order_counter()

        feed_page.click_builder_btn()
        recipe = main_page.get_random_recipe()
        for i in recipe:
            main_page.add_ingredient_to_order(i)
        main_page.make_an_order()
        main_page.close_order_window()

        main_page.click_feed_btn()
        new_common_order_counter = feed_page.get_common_order_counter()

        assert old_common_order_counter + 1 == new_common_order_counter

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Авторизуемся, создаем заказ'
                        'проверяем, что в «Ленте заказов» счётчик Выполнено за сегодня увеличился')
    def test_create_order_increment_today_order_counter(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        main_page.click_feed_btn()
        feed_page = FeedPage(driver)
        old_today_order_counter = feed_page.get_today_order_counter()

        feed_page.click_builder_btn()
        recipe = main_page.get_random_recipe()
        for i in recipe:
            main_page.add_ingredient_to_order(i)
        main_page.make_an_order()
        main_page.close_order_window()

        main_page.click_feed_btn()
        new_today_order_counter = feed_page.get_today_order_counter()

        assert old_today_order_counter + 1 == new_today_order_counter

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Авторизуемся, создаем заказ'
                        'проверяем, номер заказа появился в разделе "В работе" ленты заказов')
    def test_user_order_exist_in_common_order_feed(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        recipe = main_page.get_random_recipe()
        for i in recipe:
            main_page.add_ingredient_to_order(i)
        main_page.make_an_order()
        order_id = main_page.get_order_id()
        main_page.close_order_window()

        main_page.click_feed_btn()
        feed_page = FeedPage(driver)
        orders = feed_page.get_in_work_orders_ids()

        assert order_id in orders

import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestLogin:

    @allure.title('Тест перехода на страницу ЛК по клику на кнопку «Личный кабинет»,')
    @allure.description('Логинимся, на главной странице кликаем на кнопку «Личный кабинет», '
                        'проверяем, что странице есть кнопка Выход')
    def test_go_to_login_page(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        main_page.click_lk_btn()

        assert AccountPage(driver).is_exit_btn_visible

    @allure.title('Тест перехода на страницу История заказов из личного кабинета')
    @allure.description('Логинимся, переходим в личный кабинет, кликаем на кнопку История заказов'
                        'проверяем, что странице есть форма со списком заказов')
    def test_go_to_order_history(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        main_page.click_lk_btn()
        account_page = AccountPage(driver)
        account_page.click_order_history_btn()

        assert account_page.is_order_history_form_present()

    @allure.title('Тест выхода из аккаунта')
    @allure.description('Логинимся, переходим в личный кабинет, кликаем на кнопку Выход'
                        'проверяем, что открылась форма логина')
    def test_exit_from_account(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])

        main_page.click_lk_btn()
        account_page = AccountPage(driver)
        account_page.click_exit_account_btn()

        assert login_page.is_login_btn_present

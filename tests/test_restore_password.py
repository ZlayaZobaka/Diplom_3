import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from locators.reset_password_page_locators import ResetPasswordPageLocator


class TestRestorePassword:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Переходим по ссылками на страницу восстановления пароля, '
                        'проверяем, что есть кнопка Восстановить')
    def test_go_to_the_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_lk_btn()

        login_page = LoginPage(driver)
        login_page.click_forgot_pass_link()

        assert ResetPasswordPage(driver).is_element_visible(ResetPasswordPageLocator.restore_btn)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Переходим по ссылками на страницу восстановления пароля, вводим пароль, нажимаем Восстановить'
                        'проверяем, что появляется кнопка Сохранить')
    def test_on_password_recovery_page_enter_email_and_click_restore_btn(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.click_forgot_pass_link()
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.set_email(user['email'])

        reset_pass_page.click_restore_btn()

        assert reset_pass_page.is_element_visible(ResetPasswordPageLocator.save_btn)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @allure.description('Переходим по ссылками на страницу восстановления пароля, вводим пароль, нажимаем Восстановить'
                        'проверяем, что нажатие кнопки показать/скрыть пароль делает поле активным')
    def test_on_password_reset_page_click_show_hide_password_btn(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_lk_btn()
        login_page = LoginPage(driver)
        login_page.click_forgot_pass_link()
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.set_email(user['email'])
        reset_pass_page.click_restore_btn()

        old_state = reset_pass_page.is_password_input_active()
        reset_pass_page.click_see_hidden_btn()
        new_state = reset_pass_page.is_password_input_active()

        assert (old_state is False and new_state is True)

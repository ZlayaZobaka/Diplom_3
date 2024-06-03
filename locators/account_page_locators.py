from selenium.webdriver.common.by import By
from locators.header_page_locators import HeaderPageLocator


class AccountPageLocators(HeaderPageLocator):

    # поле для ввода Name
    name_input = (By.XPATH, './/input[@type = "text"][@name = "Name"]')

    # поле для ввода Email
    email_input = (By.XPATH, './/input[@type = "text"][@name = "name"]')

    # поле для ввода пароля
    password_input = (By.XPATH, './/input[@type = "password"][@name = "name"]')

    # кнопка Выход
    exit_btn = (By.XPATH, './/button[text()="Выход"]')

    # ссылка История заказов
    order_history_link = (By.LINK_TEXT, 'История заказов')

    # форма со списком заказов
    order_history_form = (By.XPATH, './/div[@class = "OrderHistory_orderHistory__qy1VB"]')

    # список заказов пользователя
    user_order_list = (By.XPATH, './/ul[@class ="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]')

    # id заказа
    order_id = (By.XPATH, './/p[@class = "text text_type_digits-default"]')

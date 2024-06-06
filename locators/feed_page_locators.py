from selenium.webdriver.common.by import By
from locators.header_page_locators import HeaderPageLocator


class FeedPageLocators(HeaderPageLocator):

    # Форма ленты заказов
    feed_form = (By.XPATH, './/div[@class = "OrderFeed_orderFeed__2RO_j"]')

    # Окно с деталями заказа
    order_window = (By.XPATH, './/div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')

    # Список заказов
    orders_list = (By.XPATH, './/ul[@class = "OrderFeed_list__OLh59"]')

    # id заказа
    order_id = (By.XPATH, './/p[@class = "text text_type_digits-default"]')

    # счетчик Выполнено за все время
    common_order_counter = (By.XPATH, './/p[text() = "Выполнено за все время:"]/following-sibling::p')

    # счетчик Выполнено за сегодня
    today_order_counter = (By.XPATH, './/p[text() = "Выполнено за сегодня:"]/following-sibling::p')

    # раздел В работе
    in_work_section = (By.XPATH, './/ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]'
                                 '/li[@class = "text text_type_digits-default mb-2"]')


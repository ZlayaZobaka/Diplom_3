import allure
#from locators.feed_page_locators import F
from pages.header_page import HeaderPageLocator


class FeedPage(HeaderPageLocator):
    def __init__(self, driver):
        super().__init__(driver)
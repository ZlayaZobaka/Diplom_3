import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

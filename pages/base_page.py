import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
            not_found = True
        except TimeoutException:
            not_found = False

        return not_found

    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
            not_found = True
        except TimeoutException:
            not_found = False

        return not_found

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_invisibility_of_element(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            pass

        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator))

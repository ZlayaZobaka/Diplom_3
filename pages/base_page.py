import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ищем web-элемент")
    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Проверяем, что web-элемент видим")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
            not_found = True
        except TimeoutException:
            not_found = False

        return not_found

    @allure.step("Проверяем, что web-элемент существует")
    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
            not_found = True
        except TimeoutException:
            not_found = False

        return not_found

    @allure.step("Скролируем к web-элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем по web-элементу")
    def click_to_element(self, element):
        self.scroll_to_element(element)
        element.click()

    @allure.step("Ждем исчезновение web-элемента")
    def wait_invisibility_of_element(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            pass

        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator))

    @allure.step("Делаем drag&drop web-элемента")
    # ActionChains не отрабатывает release() в Firefox
    # обходное решение из https://github.com/SeleniumHQ/selenium/issues/8003
    def drag_and_drop(self, source_element, dest_element):
        f = open("scripts/drag_and_drop.js", "r")
        javascript = f.read()
        f.close()
        self.driver.execute_script(javascript, source_element, dest_element)

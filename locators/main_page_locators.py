from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class MainPageLocators(CommonLocators):

    # кнопка Войти в аккаунт
    enter_to_profile_btn = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # секция Соберите бургер
    build_burger_section = (By.CSS_SELECTOR, '.BurgerIngredients_ingredients__1N8v2')

    # кнопка Оформить заказ
    make_an_order_btn = (By.XPATH, './/button[text() = "Оформить заказ"]')

    # закладка Булки
    builder_bread_tab = (By.XPATH, './/span[text() = "Булки"]')

    # закладка Соусы
    builder_sauce_tab = (By.XPATH, './/span[text() = "Соусы"]')

    # закладка Начинки
    builder_topping_tab = (By.XPATH, './/span[text() = "Начинки"]')
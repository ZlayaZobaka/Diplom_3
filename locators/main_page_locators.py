from selenium.webdriver.common.by import By
from locators.common_locators import CommonLocators


class MainPageLocators(CommonLocators):

    # кнопка Войти в аккаунт
    enter_to_profile_btn = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # секция Соберите бургер
    build_burger_section = (By.CSS_SELECTOR, '.BurgerIngredients_ingredients__1N8v2')

    # кнопка Оформить заказ
    make_an_order_btn = (By.XPATH, './/button[text() = "Оформить заказ"]')

    # список булок
    builder_bread_list = (By.XPATH, './/h2[text() = "Булки"]/following-sibling::ul')

    # список соусов
    builder_sauce_list = (By.XPATH, './/h2[text() = "Соусы"]/following-sibling::ul')

    # список начинок
    builder_topping_list = (By.XPATH, './/h2[text() = "Начинки"]/following-sibling::ul')

    # окно с описанием ингредиента
    ingredient_desc = (By.XPATH, './/section[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
                                 '/div[@class = "Modal_modal__container__Wo2l_"]')

    # кнопка закрытия окна с описанием ингредиента
    close_description_btn = (By.XPATH, './/section[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button')

    # счетчик ингредиента
    ingredient_counter = (By.XPATH, './/p[@class = "counter_counter__num__3nue1"]')

    # корзина заказа
    order_basket = (By.XPATH, './/section[@class = "BurgerConstructor_basket__29Cd7 mt-25 "]')

    # название ингредиента
    ingredient_name = (By.XPATH, './/p[@class = "BurgerIngredient_ingredient__text__yp3dH"]')

    # идентификатор заказа
    order_id = (By.CSS_SELECTOR, '.text_type_digits-large')

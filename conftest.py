import allure
import pytest
import helpers
from selenium import webdriver
from data import Urls
from api import Api


@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    driver.get(Urls.BASE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()


@allure.step(f'Создаем нового пользователя')
@pytest.fixture(scope='function')
def user():
    user = helpers.register_user_payload()

    with allure.step('Регистрируем пользователя'):
        Api().register_user(user)

    yield user

    with allure.step('Удаляем пользователя'):
        Api().delete_user(user)

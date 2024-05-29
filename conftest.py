import allure
import pytest
import helpers
from selenium import webdriver
from data import Urls
from api import Api


@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()


@allure.step(f'Создаем нового пользователя')
@pytest.fixture(scope='function')
def user():
    user = helpers.register_user_payload()

    with allure.step('Регистрируем пользователя'):
        Api().register_user(user)

    yield user

    with allure.step('Удаляем пользователя'):
        Api().delete_user(user)

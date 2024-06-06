import allure
import requests
import json
from data import Urls


class Api:

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    @allure.step('Отправляем запрос на создание пользователя')
    def register_user(self, payload):
        response = requests.post(
            url=Urls.BASE_URL + Urls.AUTH_REGISTER_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

        self.headers['Authorization'] = response.json().get('accessToken')

    @allure.step('Отправляем запрос на удаление пользователя')
    def delete_user(self, payload):
        del payload['name']
        del payload['password']
        requests.delete(
            url=Urls.BASE_URL + Urls.AUTH_USER_ENDPOINT,
            data=json.dumps(payload),
            headers=self.headers)

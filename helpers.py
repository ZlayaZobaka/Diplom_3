import allure
from faker import Faker
from data import WellKnownConstants


@allure.step(f'Создаем запрос на создание пользователя')
def register_user_payload() -> dict:
    payload = {
        'email': generate_random_mail(),
        'name': generate_random_string(),
        'password': generate_random_string()
    }
    return payload


@allure.title('Создаем случайную строку')
def generate_random_string() -> str:
    return Faker().text(WellKnownConstants.RANDOM_STRING_LEN)


@allure.title('Создаем случайный email')
def generate_random_mail() -> str:
    return Faker().email(domain=WellKnownConstants.MAIL_DOMAIN)
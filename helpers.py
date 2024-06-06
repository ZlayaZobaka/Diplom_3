import allure
from faker import Faker
from data import WellKnownConstants


@allure.step(f'Создаем запрос на создание пользователя')
def register_user_payload() -> dict:
    payload = {
        'email': Faker().email(domain=WellKnownConstants.MAIL_DOMAIN),
        'name': Faker().name(),
        'password': Faker().pystr(min_chars=WellKnownConstants.RANDOM_STRING_LEN_MIN)
    }
    return payload


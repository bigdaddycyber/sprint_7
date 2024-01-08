import allure
import requests
import pytest
from typing import Any
from data_fake import Data
from generate_new_user import register_new_courier_and_return_login_password, generate_random_string

data = Data()

class TestCreateCourier:

    @allure.title("Создание курьера")
    def test_create_courier_yes(self):
        payload = {
            'login': generate_random_string(10),
            'password': generate_random_string(10),
            'firstName': generate_random_string(10)
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert 201 == response.status_code and response.text == '{"ok":true}'

    @allure.title("Ошибка создания курьера с одинаковыми данными")
    def test_nocreate_two_same_courier_error(self):
        generate_courier = register_new_courier_and_return_login_password()

        payload = {
            'login': generate_courier[0],
            'password': generate_courier[1],
            'first_name': generate_courier[2]
        }
        
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert 409 == response.status_code and r["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title("Ошибка создания курьера без заполнения одного из полей")
    @pytest.mark.parametrize("payload", [{'login': data.EMPTY_FIELD,'password': generate_random_string(10),'first_name': generate_random_string(10)}, {'login': generate_random_string(10), 'password':data.EMPTY_FIELD, 'first_name':generate_random_string(10)}])
    def test_nocreate_courier_with_empty_field(self, payload: Any):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()
        assert 400 == response.status_code and r['message'] == 'Недостаточно данных для создания учетной записи'
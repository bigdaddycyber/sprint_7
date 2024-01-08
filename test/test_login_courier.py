import requests
import pytest
import allure
from data_fake import Data
from typing import Any
from generate_new_user import register_new_courier_and_return_login_password

data = Data()


class TestLoginCourier:
    @allure.title("Успешная авторизация")
    def test_login_courier_successful(self):
        generate_courier = register_new_courier_and_return_login_password()
        login = generate_courier[0]
        password = generate_courier[1]

        payload = {
            'login': login,
            'password': password
        }
    
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert 200 == response.status_code and "id" in response.text

    @allure.title("Ошибка в авторизации при не верном логине и пароле")
    @pytest.mark.parametrize("payload", [{'login': data.LOGIN,'password': data.WRONG_PASSWORD}, {'login': data.WRONG_LOGIN, 'password':data.PASSWORD}])
    def test_login_courier_error_data_login_and_password(self, payload: Any):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        r = response.json()
        assert 404 == response.status_code and r["message"] == 'Учетная запись не найдена'

    @allure.title("Ошибка авторизации при пустых полях логина и пароля")
    @pytest.mark.parametrize("payload", [{'login': data.LOGIN,'password': data.EMPTY_FIELD}, {'login': data.EMPTY_FIELD, 'password':data.PASSWORD}])
    def test_login_courier_with_empty_field_in_login_and_password(self, payload: Any):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        r = response.json()
        assert 400 == response.status_code and r["message"] == 'Недостаточно данных для входа'

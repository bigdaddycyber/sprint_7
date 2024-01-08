import allure
import requests
import pytest
import json
from data_fake import Data
from generate_new_user import generate_random_string

data = Data()


class TestCreateOrder:
    
    @pytest.mark.parametrize('firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color', [
                              (generate_random_string(10), generate_random_string(10), data.ADRESS_GEN, data.METRO_STATION_GEN, data.PHONE_GEN, data.RENT_TIME_GEN, data.DELIVERY_DATE_GEN, generate_random_string(10), [data.EMPTY_FIELD]),
                              (generate_random_string(10), generate_random_string(10), data.ADRESS_GEN, data.METRO_STATION_GEN, data.PHONE_GEN, data.RENT_TIME_GEN, data.DELIVERY_DATE_GEN, generate_random_string(10), ["BLACK"]),
                              (generate_random_string(10), generate_random_string(10), data.ADRESS_GEN, data.METRO_STATION_GEN, data.PHONE_GEN, data.RENT_TIME_GEN, data.DELIVERY_DATE_GEN, generate_random_string(10), ["GREY"]),
                              (generate_random_string(10), generate_random_string(10), data.ADRESS_GEN, data.METRO_STATION_GEN, data.PHONE_GEN, data.RENT_TIME_GEN, data.DELIVERY_DATE_GEN, generate_random_string(10), ["BLACK", "GREY"])])
    @allure.title("Успешное создание заказа")    
    def test_create_mew_order_sucessful(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        payload_string = json.dumps(payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload_string)
        r = response.json()
        assert 201 == response.status_code and "track" in response.text
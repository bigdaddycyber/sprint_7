import requests
import allure


class TestListOrder:
    @allure.title("Получение списка заказов")
    def test_list_order(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        r = response.json()
        assert 200 == response.status_code and r["order"] in response.text
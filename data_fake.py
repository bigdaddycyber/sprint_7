import random
from faker import Faker

fake = Faker(locate="ru_RU")

class Data:
    LOGIN = 'ninjaqwerty123'
    PASSWORD = '1234'
    WRONG_LOGIN = 'ninjaqwerty1234'
    WRONG_PASSWORD = '12345'
    EMPTY_FIELD = ''
    ADRESS_GEN = fake.address()
    METRO_STATION_GEN = random.randint(1,112)
    PHONE_GEN = f'+7{random.randint(9000000000, 9999999999)}'
    RENT_TIME_GEN = random.randint(1, 7)
    DELIVERY_DATE_GEN = f'2024-01-{random.randint(8, 31)}'


    
    
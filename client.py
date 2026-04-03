import requests
import json

print("##### Создаем пользователя №1 #####")
data = requests.post(
    "http://localhost:80/api/v1/user",
    json={
        "name": "user_1",
        "password": "password_1"
        }
)
print(data.status_code)
print(data.json(), "\n")

print("##### Создаем объявление №1 #####")
data = requests.post(
    "http://localhost:80/api/v1/advertisement",
    json={
        "title": "Продается товар №1",
        "description": "Очень хороший товар? берите не пожалеете.",
        "price": 1293.36,
        "user_id": 1
        }
)
print(data.status_code)
print(data.json(), "\n")

print("##### Создаем объявление №2 #####")
data = requests.post(
    "http://localhost:80/api/v1/advertisement",
    json={
        "title": "Продается товар №2",
        "description": "Очень хороший товар, берите не пожалеете.",
        "price": 1293.36,
        "user_id": 1
        }
)
print(data.status_code)
print(data.json(), "\n")

print("##### Создаем объявление №3 #####")
data = requests.post(
    "http://localhost:80/api/v1/advertisement",
    json={
        "title": "Продается товар №3",
        "description": "Очень хороший товар, берите не пожалеете.",
        "price": 1293.36,
        "user_id": 1
        }
)
print(data.status_code)
print(data.json(), "\n")


print("##### Получаем объявление с id=1 #####")
data = requests.get("http://localhost:80/api/v1/advertisement/1")
print(data.status_code)
print(data.json(), "\n")

print("##### Изменяем объявление с id=1 #####")
data = requests.patch(
    "http://localhost:80/api/v1/advertisement/1",
    json={
        "description": "Очень хороший товар, лучше не найдете.", 
        "price": 1500.00
        }
)
print(data.status_code)
print(data.json(), "\n")
data = requests.get("http://localhost:80/api/v1/advertisement/1")
print(data.json(), "\n")

print("##### Ищем объявления с наименованием, содержащим текст 'товар №1' #####")
data = requests.get("http://localhost:80/api/v1/advertisement", params={"title": "товар №1"})
print(data.status_code)
print(data.json(), "\n")

print("##### Ищем объявления описанием, содержащим текст 'хороший' #####")
data = requests.get("http://localhost:80/api/v1/advertisement", params={"description": "хороший", "limit": 2, "offset": 1})
print(data.status_code)
print(data.json(), "\n")

print("##### Ищем объявления с ценой в интервале от 1300 до 1500 включительно #####")
data = requests.get("http://localhost:80/api/v1/advertisement", params={"price_min": 1300, "price_max": 1500})
print(data.status_code)
print(data.json(), "\n")

print("##### Удаляем объявление с id=1 #####")
data = requests.delete("http://localhost:80/api/v1/advertisement/1")
print(data.status_code)
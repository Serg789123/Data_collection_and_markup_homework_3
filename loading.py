"""Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и 
создайте базу данных и коллекции для их хранения. Поэкспериментируйте с различными методами запросов."""

import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных и коллекции
db = client['bookstore']
collection = db['books']

with open('box_office_data.json', 'r') as file:
    data = json.load(file)

collection.insert_many(data)
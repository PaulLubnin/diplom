import vk_api
from pymongo import MongoClient
import re

ACCESS_TOKEN = ''
APP_ID = 7145158

class SessionConnection:
    """
    Класс для создания подключения и запросов к ВК API, для сбора необходимых данных,
    которые будут записаны в базу для дальнейшей обработки
    """
    def __init__(self):
        pass

    def login_vk(self):
        """
        Подключение к ВК по логину/паролю, либо токену
        """
        pass

    def get_photos(self):
        """
        Получить фотографии для записи в JSON
        """
        pass

    def search_by_age(self):
        """
        Поиск по возрасту
        """
        pass

    def search_by_gender(self):
        """
        Поиск по полу
        """
        pass

    def group_search(self):
        """
        Поиск по группам
        """
        pass

    def city_search(self):
        """
        Поиск по городу
        """
        pass

class DataBase:
    """
    Класс для записи и обработки(хранения) информации в/из базы данных
    """
    def __init__(self):
        """
        Входные параметры для подключения к базе
        """
        pass

    def database_connection(self):
        """
         Подключение к базе
        """
        pass

    def data_loading(self):
        """
        Загрузка данных в базу
        """
        pass

    def data_upload(self):
        """
        Получение данных из базы
        """
        pass

class Selection:
    """
    Класс для отбора по заданным критериям
    """
    def __init__(self):
        """
        Параметры для отбора
        """
        pass

    def selection_by_music(self):
        """
        Отбор по музыке
        """
        pass

    def selection_by_books(self):
        """
        Отбор по книгам
        """
        pass

    def selection_by_interests(self):
        """
        Отбор по интересам
        """
        pass


if __name__ == '__main__':
    pass

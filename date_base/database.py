from pymongo import MongoClient
from pprint import pprint


class ClientDataBase:
    """
    Класс для записи и обработки(хранения) информации в/из базы данных
    """
    def __init__(self):
        """
        Входные параметры для подключения к базе
        """
        self.client = MongoClient('localhost', 27017)
        self.vkinder_db = self.client.vkinder_db
        self.users_collection = self.vkinder_db.users

    def data_loading(self, user_list):
        """
        Загрузка данных в базу
        """
        self.users_collection.all_people.insert_many(user_list)
        print('...данные о пользователях загружены в базу')

    def data_upload(self):
        """
        Получение данных из базы
        """
        for found_users in self.users_collection.all_people.find():
            pprint(found_users)
        print('...данные о пользователях загружены из базы')

    def drop_db(self):
        self.users_collection.all_people.drop()
        print('...база очищена')

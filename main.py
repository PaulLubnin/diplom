import vk_api
from pprint import pprint
from pymongo import MongoClient
import re

class SessionConnection:
    """
    Класс для создания подключения и запросов к ВК API, для сбора необходимых данных,
    которые будут записаны в базу для дальнейшей обработки
    """
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.vk_session = None
        self.vk = None

        self.users = ''
        self.fields = 'sex, bdate, home_town, interests, music, books'

    def login_vk(self):
        """
        Подключение к ВК по логину/паролю
        """
        self.vk_session = vk_api.VkApi(self.login, self.password)
        try:
            self.vk_session.auth(token_only=False)
            print('Подключение прошло успешно')
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return
        self.vk = self.vk_session.get_api()

class User(SessionConnection):
    """
    Пользователь приложение и методы для поиска на основе информации о пользователе
    """
    def get_application_user_information(self):
        """
        Получение и проверка информации о пользователе приложения
        """
        print('\n\tДля корректного поиска необходимо проверить Ваши данные:\n'
              '\tдату рождения, город проживания и Ваши увлечения\n')
        user_info = []
        for info in self.vk.users.get(fields=self.fields):
            if 'bdate' not in info.keys():
                bdate = input('Укажите Вашу дату рождения в формате Д.М.Г: ')
                info.update({'bdate': bdate})
                print('Дата рождения принята')
            else:
                print('Дата рождения принята')
            if len(info['home_town']) == 0:
                home_town = input('Укажите Ваш город: ')
                info.update({'home_town': home_town})
                print('Город проживания принят')
            else:
                print('Город проживания принят')
            if len(info['music']) == 0:
                music = input('Любимые музыкальные группы (через запятую): ')
                info.update({'music': music})
                print('Музыкальные предпочтения учтены')
            else:
                print('Музыкальные предпочтения учтены')
            if len(info['books']) == 0:
                books = input('Любимые книги (через запятую): ')
                info.update({'books': books})
                print('Книжные предпочтения учтены')
            else:
                print('Книжные предпочтения учтены')
            if len(info['interests']) == 0:
                interests = input('Чем Вы увлекаетесь: ')
                info.update({'interests': interests})
                print('Ваши увлечения учтены')
            else:
                print('Ваши увлечения учтены')
            info.update({'groups': self.vk.groups.get(user_id=info['id'])})
            info.pop('can_access_closed')
            info.pop('is_closed')
            user_info = info
        # pprint(user_info)
        return user_info

    def get_users(self):
        """
        Получение списка пользователей ВК для пользователя приложения
        """
        print('Кого будем искть')
        # input()
        # sex =
        # age_from =
        # age_to =
        self.users = self.vk.users.search(count=100, fields=self.fields, sex=1, hometown='Тюмень',
                                          age_from=30, age_to=35)
        # pprint(self.users)
        return self.users

    # def get_photos(self):
    #     """
    #     Получить фотографии для записи в JSON
    #     """
    #     pass
    #
    # def search_by_age(self):
    #     """
    #     Поиск по возрасту
    #     """
    #     pass
    #
    # def search_by_gender(self):
    #     """
    #     Поиск по полу
    #     """
    #     pass
    #
    # def group_search(self):
    #     """
    #     Поиск по группам
    #     """
    #     pass
    #
    # def city_search(self):
    #     """
    #     Поиск по городу
    #     """
    #     pass

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
    Отбор по музыке, книгам, интересам для пользователя приложения
    """
    def __init__(self, for_whom_to_find):
        """
        Параметры для отбора
        """
        self.user = for_whom_to_find
        return

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
    # connection = SessionConnection('', '')
    # connection.login_vk()
    user = User('', '')
    user.login_vk()
    user.get_application_user_information()
    user.get_users()


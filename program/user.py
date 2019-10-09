from ADPY4.diplom.program.connection import SessionConnection
from pprint import pprint


class User(SessionConnection):
    """
    Пользователь приложение и методы для поиска на основе информации о пользователе
    """
    def __init__(self, login='', password=''):
        SessionConnection.__init__(self, login, password)
        self.fields = 'sex, bdate, home_town, interests, music, books, common_count'

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
        pprint(user_info)
        return user_info

    def get_users(self):
        """
        Получение списка пользователей ВК для пользователя приложения
        """
        print('Кого будем искать?')
        sex = int(input('Мужчину - 2, женщину - 1, просто друга - 0 '))
        print('Какого возраста?')
        age_from = int(input('От: '))
        age_to = int(input('До: '))
        town = input('В каком городе? ')
        users = self.vk.users.search(count=1000, fields=self.fields,
                                     sex=sex, hometown=town,
                                     age_from=age_from, age_to=age_to)
        # pprint(users)
        return users

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
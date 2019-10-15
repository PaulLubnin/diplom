from collections import Counter
from pprint import pprint


class Selection:
    """
    Отбор по музыке, книгам, интересам для пользователя приложения
    """
    def __init__(self, info_main_user, weight=0):
        """
        Переменные для отбора
        """
        self.info_main_user = info_main_user
        # self.found_users = found_users
        # self.fields = fields
        # self.multiplier = multiplier
        # self.info = info
        # self.weight = weight

    def count_weight(self, users, field='interests', multiplier=1):
        if self.info_main_user[0][field] != '':
            splitted_main_user_info = self.info_main_user[0][field].split(', ')
            for user in users:
                weight = 0
                counter = 0
                if field in user:
                    splitted_info = user[field].split(', ')
                    word_counter = Counter(splitted_info)
                    for interest in splitted_main_user_info:
                        counter += word_counter[interest]
                weight += counter * multiplier
                user['weight'] += weight
                # user.update({'weight': weight})
                # pprint(users)
        return users

    def sort_users(self, users):
        self.count_weight(users, 'interests', 3)
        self.count_weight(users, 'music', 2)
        self.count_weight(users, 'books', 1)
        user_list = sorted(users, key=lambda user: user['weight'], reverse=True)
        return user_list[0:10]

    # def selection_by_music(self):
    #     """
    #     Отбор по музыке
    #     """
    #     self.count_weight(self.found_users, 'music', 2)
    #     return
    #
    # def selection_by_books(self):
    #     """
    #     Отбор по книгам
    #     """
    #     self.count_weight(self.found_users, 'books', 1)
    #     return
    #
    # def selection_by_interests(self):
    #     """
    #     Отбор по интересам
    #     """
    #     self.count_weight(self.found_users, 'interests', 3)
    #     return

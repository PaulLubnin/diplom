from pprint import pprint

from ADPY4.diplom.program.selection import Selection
from ADPY4.diplom.program.user import User
from ADPY4.diplom.date_base.database import ClientDataBase


def start_program(class_user, class_selection, class_database):
    while True:
        print(
            f'\nДоступные команды:\n'
            f'"1" - запрос в ВК на поиск и запись результата в базу\n'
            f'"2" - загрузить из базы\n'
            f'"3" - сбросить базу\n'
            f'"e" - окончание работы\n'
        )
        input_command = input('Введите команду: ')

        if input_command == '1':
            print('Кого будем искать?')
            sex = int(input('Мужчину - 2, женщину - 1, просто друга - 0 '))
            print('Какого возраста?')
            age_from = int(input('От: '))
            age_to = int(input('До: '))
            town = input('В каком городе? ')
            found_users = class_user.get_users(sex, age_from, age_to, town)
            print(f'Количество найденных пользователей: {len(found_users)}\n')
            sorted_found_users = class_selection.sort_users(found_users)
            photos = class_user.get_photos(sorted_found_users)
            pprint(photos)
            class_database.data_loading(photos)

        elif input_command == '2':
            print(f'Загрузка базы...')
            class_database.data_upload()

        elif input_command == '3':
            print(f'\nСброс базы...')
            class_database.drop_db()

        elif input_command == 'e':
            print('Работа завершена')
            break
        else:
            print('Такой команды нет!!!')


if __name__ == '__main__':

    login = input('Введите логин ВК: ')
    password = input('Введите пароль: ')

    user = User(login, password)
    user.login_vk()
    info_main_user = user.get_application_user_information()

    selection = Selection(info_main_user)
    database = ClientDataBase()

    start_program(user, selection, database)

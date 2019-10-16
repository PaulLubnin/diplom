from pprint import pprint

from ADPY4.diplom.program.selection import Selection
from ADPY4.diplom.program.user import User
from ADPY4.diplom.date_base.database import ClientDataBase


if __name__ == '__main__':
    login = input('Введите логин ВК: ')
    password = input('Введите пароль: ')
    user = User(login, password)
    user.login_vk()

    info_main_user = user.get_application_user_information()
    selection = Selection(info_main_user)
    # pprint(info_main_user)

    while True:
        print(
            f'\nДоступные команды:\n'
            f'"1" - запрос ВК на поиск\n'
            f'"2" - ???\n'
            f'"3" - ???\n'
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
            found_users = user.get_users(sex, age_from, age_to, town)
            print(f'Количество найденных пользователей: {len(found_users)}\n')
            sorted_found_users = selection.sort_users(found_users)
            photos = user.get_photos(sorted_found_users)
            pprint(photos)

        elif input_command == '2':
            print(f'\nКоманда номер 2: {info_main_user}\n')
        elif input_command == '3':
            print(f'Команда номер 3: {info_main_user}\n')
        elif input_command == 'e':
            print('Работа завершена')
            break
        else:
            print('Такой команды нет!!!')

    # db_base = ClientDataBase()
    # db_base.drop_db()
    # db_base.data_loading(user.get_users()['items'])
    # db_base.data_upload()


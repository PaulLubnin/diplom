from ADPY4.diplom.program.user import User
from ADPY4.diplom.program.selection import Selection
from ADPY4.diplom.date_base.database import ClientDataBase
from pprint import pprint


if __name__ == '__main__':
    login = input('Введите логин ВК: ')
    password = input('Введите пароль: ')
    user = User(login, password)
    user.login_vk()

    info_main_user = user.get_application_user_information()
    pprint(info_main_user)

    print('Кого будем искать?')
    sex = int(input('Мужчину - 2, женщину - 1, просто друга - 0 '))
    print('Какого возраста?')
    age_from = int(input('От: '))
    age_to = int(input('До: '))
    town = input('В каком городе? ')

    found_users = user.get_users(sex, age_from, age_to, town)
    # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # pprint(found_users)

    selection = Selection(info_main_user)
    # selection.selection_user()

    sorted_found_users = selection.sort_users(found_users)
    # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # pprint(sorted_found_users)

    photos = user.get_photos(sorted_found_users)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    pprint(photos)

    # db_base = ClientDataBase()
    # db_base.drop_db()
    # db_base.data_loading(user.get_users()['items'])
    # db_base.data_upload()


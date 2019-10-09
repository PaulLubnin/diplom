from ADPY4.diplom.program.user import User
from ADPY4.diplom.date_base.database import ClientDataBase


if __name__ == '__main__':
    login = input('Введите логин ВК: ')
    password = input('Введите пароль: ')

    user = User(login, password)
    user.login_vk()
    user.get_application_user_information()
    user.get_users()

    db_base = ClientDataBase()
    db_base.drop_db()
    db_base.data_loading(user.get_users()['items'])
    db_base.data_upload()


import vk_api

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

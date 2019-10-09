from ADPY4.diplom.program.user import User


class Selection(User):
    """
    Отбор по музыке, книгам, интересам для пользователя приложения
    """
    def __init__(self):
        """
        Параметры для отбора
        """
        User.__init__(self)
        # self.user = for_whom_to_find
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


select = Selection()
select.get_application_user_information()

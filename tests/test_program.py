import unittest

from ADPY4.diplom.program.selection import Selection
from ADPY4.diplom.program.user import User


class TestProgram(unittest.TestCase):
    def setUp(self) -> None:
        self.login = " "
        self.password = " "
        self.user = User(self.login, self.password)
        self.user.login_vk()
        self.sex = '0'
        self.age_from = 30
        self.age_to = 31
        self.town = 'Москва'
        self.selection = Selection(self.user.get_application_user_information())
        self.users = self.user.get_users(self.sex, self.age_from, self.age_to, self.town)

    def test_is_instance(self):
        self.assertIsInstance(self.user, User)

    def test_get_application_user_information(self):
        self.assertIsNotNone(self.user.get_application_user_information)

    def test_get_users(self):
        self.assertIsNotNone(self.users)

    def test_sort_users(self):
        self.assertNotEqual(self.selection.sort_users(self.users), self.users)

    def test_get_photo(self):
        sorted_users = self.selection.sort_users(self.users)
        self.assertIsNotNone(self.user.get_photos(sorted_users))


if __name__ == '__main__':
    unittest.main()

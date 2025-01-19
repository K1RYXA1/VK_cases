import unittest
import hashlib
from descriptors import User


class TestDescriptors(unittest.TestCase):

    def test_set_nickname(self):

        user_1 = User("wow")
        self.assertEqual(user_1.nickname, "wow")

        user_1.nickname = "WOW"
        self.assertEqual(user_1.nickname, "WOW")

    def test_del_nickname(self):

        user_2 = User("ww")
        del user_2.nickname

        self.assertEqual(user_2.nickname, None)

    def test_set_same_nickname(self):

        with self.assertRaises(ValueError) as err:
            User("WOW")

            self.assertEqual(str(err.exception), "Никнейм 'WOW' уже существует")

    def test_set_invalid_nickname(self):

        with self.assertRaises(ValueError):
            User(23)

    def test_set_password(self):

        user_1 = User("wow", 'WalterWhite50')

        with self.assertRaises(AttributeError) as err:
            print(user_1.password)

        self.assertEqual(str(err.exception), "Пароль можно только установить")

    def test_set_invalid_password(self):

        with self.assertRaises(ValueError):
            User("Hello", 'walterwhite50')

        with self.assertRaises(ValueError):
            User("Hello", 'WalterWhite')

        with self.assertRaises(ValueError):
            User("Hello", '12345678')

    def test_del_password(self):

        user_1 = User("wow1", 'WalterWhite50')
        del user_1.password

        self.assertNotIn('password', user_1.__dict__)

    def test_hash_password(self):

        user_1 = User("wow2", 'WalterWhite50')
        self.assertEqual(user_1.__dict__['password'], hashlib.sha256('WalterWhite50'.encode('utf-8')).hexdigest())

    def test_set_age(self):

        user_1 = User("Walt", 'WalterWhite50', 50)
        self.assertEqual(user_1.age, 50)

    def test_set_invalid_age(self):

        with self.assertRaises(ValueError) as err:
            User("Walt", 'WalterWhite50', 11)

            self.assertEqual(str(err.exception), "Возрастное ограничение 12+")

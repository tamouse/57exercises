import unittest
from ex15_password_validation.password_checker.password_checker import PasswordChecker


class TestPasswordChecker(unittest.TestCase):
    def test_valid_pw_p(self):
        checker = PasswordChecker()

        user = 'me'
        password = 'password'

        self.assertTrue(checker.valid_pw_p(user, password))

    def test_invalid_pw(self):
        checker = PasswordChecker()

        user = 'you'
        password = 'password'

        self.assertFalse(checker.valid_pw_p(user, password))

    def test_invalid_user(self):
        checker = PasswordChecker()

        user = 'bogus'
        password = 'anything'

        self.assertFalse(checker.valid_pw_p(user, password))

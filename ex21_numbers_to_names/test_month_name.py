import unittest
from ex21_numbers_to_names.month_name import month_to_name

class TestMonthName(unittest.TestCase):
    def test_january(self):
        self.assertEqual('January', month_to_name(1))

    def test_december(self):
        self.assertEqual('December', month_to_name(12))

    def test_zero(self):
        with self.assertRaises(IndexError, msg='Month must be between 1 and 12! 0'):
            month_to_name(0)

from ex17_blood_alcohol_calculator.blood_alcohol_calculator.blood_alcohol_calculator import BloodAlcoholCalculator
import unittest


class TestBloodAlcoholCalculator(unittest.TestCase):
    def setUp(self):
        self.bac = BloodAlcoholCalculator()

    def test_under(self):
        self.assertTrue(self.bac.is_legal(2, 150, 'female', 2))

    def test_over(self):
        self.assertFalse(self.bac.is_legal(30, 120, 'male', 1))


if __name__ == '__main__':
    unittest.main()

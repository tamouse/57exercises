from ex16_legal_driving_age.legal_driving_age.legal_driving_age_calculator import LegalDrivingAgeCalculator
import unittest

class TestLegalDrivingAgeCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = LegalDrivingAgeCalculator(16)

    def test_underage(self):
        self.assertFalse(self.calculator.is_legal(14))

    def test_overage(self):
        self.assertTrue(self.calculator.is_legal(18))

    def test_at_age(self):
        self.assertTrue(self.calculator.is_legal(16))

    def test_float_underage(self):
        self.assertFalse(self.calculator.is_legal(15.99))

    def test_float_overage(self):
        self.assertTrue(self.calculator.is_legal(16.01))

if __name__ == '__main__':
    unittest.main()

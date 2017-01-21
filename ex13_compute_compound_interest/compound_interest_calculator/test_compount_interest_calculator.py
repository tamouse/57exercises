import unittest
from ex13_compute_compound_interest.compound_interest_calculator.compound_interest_calculator import CompoundInterestCalculator

class TestCompoundInterestCalculator(unittest.TestCase):

    def test_calc(self):
        calculator = CompoundInterestCalculator()
        principle = 1500
        rate = 4.3
        time = 6
        periods = 4

        amount = calculator.calc(principle, rate, time, periods)
        self.assertAlmostEqual(1938.84, amount, 2)

import unittest
import logging
from ex12_compute_simple_interest.simple_interest_calculator.sicalc import SICalc

class TestSICalc(unittest.TestCase):

    def test_calc(self):
        sicalc = SICalc(log_level=logging.DEBUG)
        p = '1500'
        r = '4.3'
        t = '4'
        expected = 1758
        actual = sicalc.calc(p, r, t)
        self.assertEqual(expected, actual)


import unittest
from ex14_tax_calculator.tax_calculator.tax_calculator import TaxCalculator


class TestTaxCalculator(unittest.TestCase):

    def test_calc(self):
        calculator = TaxCalculator()
        order_amount = 10.00
        state = 'WI'
        subtotal, tax_amount, total = calculator.calc(order_amount, state)

        self.assertEqual(order_amount, subtotal)
        self.assertAlmostEqual(0.55, tax_amount, 2)
        self.assertAlmostEqual(10.55,  total, 2)

    def test_calc_not_wisconsin(self):
        calculator = TaxCalculator()
        order_amount = 10.00
        state = 'MN'

        subtotal, tax_amount, total = calculator.calc(order_amount, state)

        self.assertEqual(order_amount, subtotal)
        self.assertAlmostEqual(0.0, tax_amount, 2)
        self.assertAlmostEqual(order_amount, total, 2)

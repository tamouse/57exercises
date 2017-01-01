
from decimal import Decimal

from ex11_currency_exchange.Converter import Converter

import unittest
from unittest.mock import MagicMock, patch

class TestConverter(unittest.TestCase):

    def test_converter_with_exercise_case(self):
        test_currency_table = {
            'USD': 1,
            'EUR': 0.956803
        }
        beginning_amount = 81
        beginning_currency = 'EUR'
        ending_currency = 'USD'
        expected_ending_currency = Decimal('84.66')

        self.assertEqual(expected_ending_currency,
                         Converter(test_currency_table).convert(beginning_amount,
                                                                from_currency_type=beginning_currency,
                                                                to_currency_type=ending_currency))


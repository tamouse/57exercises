
from ex11_currency_exchange.currency_exchanger import CurrencyExchanger
import unittest
from unittest.mock import MagicMock, patch
from io import StringIO

class CurrencyExchangerUnitText(unittest.TestCase):

    def test_exchanger(self):
        test_input = """EUR
81
USD

"""
        mock_input = StringIO(test_input)
        mock_output = MagicMock()

        exchanger = CurrencyExchanger()

        with patch('sys.stdin', mock_input), patch('sys.stdout', mock_output):
            exchanger.run()

        self.assertTrue(mock_output.write.called)
        self.assertEqual('81 in EUR is 84.66 in USD', mock_output.write.call_args_list[3][0][0])

from io import StringIO
from decimal import Decimal
import unittest
from unittest.mock import MagicMock, patch
from self_checkout import SelfCheckout

TAX_RATE = Decimal(0.055)
THREE_ITEMS = """item 1
1
2.99
item 2
3
0.55
item 3
10
0.10
"""
EXPECTED_SUBTOTAL = (1 * Decimal(2.99)) + (3 * Decimal(0.55)) + (10 * Decimal(0.10))
EXPECTED_TAXES = EXPECTED_SUBTOTAL * TAX_RATE
EXPECTED_TOTAL = EXPECTED_SUBTOTAL + EXPECTED_TAXES


class SelfCheckoutTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_initialize_no_params(self):
        co = SelfCheckout()
        self.assertEqual(0, co.tax_rate)
        self.assertEqual(0, co.cart.item_count())

    def test_initialize_with_tax_rate(self):
        co = SelfCheckout(tax_rate=TAX_RATE)
        self.assertEqual(TAX_RATE, co.tax_rate)
        self.assertEqual(0, co.cart.item_count())

    def test_initialize_with_bogus_tax_rate(self):
        try:
            SelfCheckout(tax_rate='BOGUS')
            self.fail()
        except RuntimeError as ex:
            self.assertEqual("Tax Rate is not a float: 'BOGUS'", ex.args[0])

    def test_gather_items(self):
        input_buffer = THREE_ITEMS
        num_input_lines = input_buffer.count("\n")
        num_items = num_input_lines / 3
        mock_input = StringIO(input_buffer)
        mock_output = MagicMock()

        co = SelfCheckout(tax_rate=TAX_RATE, my_input=mock_input, my_output=mock_output)
        co.gather_items()
        self.assertEqual(num_items, co.cart.item_count())
        self.assertEqual((num_input_lines + 1), mock_output.write.call_count)
        self.assertEqual(EXPECTED_SUBTOTAL, co.cart.subtotal())
        self.assertEqual(EXPECTED_TAXES, co.cart.tax_on_items())
        self.assertEqual(EXPECTED_TOTAL, co.cart.grand_total())

    def test_print_invoice(self):
        input_buffer = THREE_ITEMS
        mock_input = StringIO(input_buffer)
        mock_output = MagicMock()

        co = SelfCheckout(tax_rate=TAX_RATE, my_input=mock_input, my_output=mock_output)
        co.gather_items()
        co.print_invoice()
        invoice_header = mock_output.write.call_args_list[10][0][0]
        item1_line = mock_output.write.call_args_list[11][0][0]
        self.assertRegex(item1_line, r"\n\n +1 +item 1 +1 +\$2\.99 +\$2\.99\n\n")
        item2_line = mock_output.write.call_args_list[12][0][0]
        self.assertRegex(item2_line, r"\n\n +2 +item 2 +3 +\$0\.55 +\$1\.65\n\n")
        item3_line = mock_output.write.call_args_list[13][0][0]
        self.assertRegex(item3_line, r"\n\n +3 +item 3 +10 +\$0\.10 +\$1\.00\n\n")
        invoice_footer = mock_output.write.call_args_list[14][0][0]
        self.assertRegex(invoice_footer, r"Subtotal: +\$5\.64")
        self.assertRegex(invoice_footer, r"Taxes: +\$0\.31")
        self.assertRegex(invoice_footer, r"Total: +\$5\.95")
        print(invoice_header, item1_line, item2_line, item3_line, invoice_footer)


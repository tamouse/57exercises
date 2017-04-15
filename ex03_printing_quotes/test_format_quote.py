import unittest
from ex03_printing_quotes.format_quote import *

class TestFormatQuote(unittest.TestCase):

    def test_format_quote(self):
        quote = 'These are not the droids you are looking for'
        cite = 'Obi Wan Kenobi'
        expected = 'Obi Wan Kenobi said: "These are not the droids you are looking for"'
        self.assertEqual(expected, format_quote(quote, cite))


if __name__ == '__main__':
    unittest.main()

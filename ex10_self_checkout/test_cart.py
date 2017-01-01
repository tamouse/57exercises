import unittest
from decimal import Decimal

from cart import Cart

class CartTestCase(unittest.TestCase):

    def test_add_item(self):
        cart = Cart(0)
        cart.add_item('test item', 3, Decimal(1.00))
        self.assertEqual(1, cart.item_count())

    def test_subtotal(self):
        cart = Cart(0)
        cart.add_item('item 1', 2, Decimal(1.00))
        cart.add_item('item 2', 1, Decimal(3.50))
        expected = (2*Decimal(1.00)) + (1*Decimal(3.50))
        self.assertEqual(expected, cart.subtotal())

    def test_tax_on_items(self):
        tax_rate=Decimal(0.08)
        cart = Cart(tax_rate)
        cart.add_item('item 1', 2, Decimal(1.00))
        cart.add_item('item 2', 1, Decimal(3.50))
        expected = ((2 * Decimal(1.00)) + (1 * Decimal(3.50))) * tax_rate
        self.assertEqual(expected, cart.tax_on_items())

    def test_grand_total(self):
        tax_rate = Decimal(0.08)
        cart = Cart(tax_rate)
        cart.add_item('item 1', 2, Decimal(1.00))
        cart.add_item('item 2', 1, Decimal(3.50))
        subtotal = (2 * Decimal(1.00)) + (1 * Decimal(3.50))
        expected = subtotal + (subtotal * tax_rate)
        self.assertEqual(expected, cart.grand_total())

    def test_empty_cart_subtotal(self):
        cart = Cart(0)
        self.assertEqual(0.0, cart.subtotal())

    def test_empty_cart_tax_on_items(self):
        cart = Cart(0.08)
        self.assertEqual(0, cart.tax_on_items())

    def test_empty_cart_grand_total(self):
        cart = Cart(0.08)
        self.assertEqual(0, cart.grand_total())

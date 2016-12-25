import sys
from decimal import Decimal, InvalidOperation

from ex10_self_checkout.cart import Cart
from utils.moneyfmt import moneyfmt

INVOICE_HEADER = """
Invoice:
-----------------------------------------------------------------------------------------------------------
 {:<5s} {:<30s} {:<10s} {:<12s} {:<12s}
""".format('Item', 'Description', 'Quantity', 'Unit Price', 'Line Price')
INVOICE_FOOTER = """
-----------------------------------------------------------------------------------------------------------
 Subtotal: {:>12s}
 Taxes:    {:>12s}
 Total:    {:>12s}
"""
INVOICE_ITEM = """

 {:>5s} {:<30s} {:>10s} {:>12s} {:>12s}

"""

class SelfCheckout:

    def __init__(self, tax_rate='0.055'):
        try:
            self.tax_rate = Decimal(tax_rate)
        except InvalidOperation:
            raise RuntimeError("Tax Rate is not a float: '%s'" % str(tax_rate))

        self.cart = Cart(self.tax_rate)

    def run(self):
        self.gather_items()
        self.print_invoice()

    def gather_items(self):

        while True:
            item = input("Item: ")
            if len(item) < 1:
                break
            quantity = int(input("Quantity: "))
            unit_price = Decimal(input("Unit Price: "))
            self.cart.add_item(item, quantity, unit_price)

    def print_invoice(self):
        sys.stdout.write(INVOICE_HEADER)
        for item_no in range(0, self.cart.item_count()):
            item = self.cart.items[item_no]
            sys.stdout.write(INVOICE_ITEM.format(
                str(item_no+1),
                str(item['item']),
                str(item['quantity']),
                moneyfmt(item['unit_price']),
                moneyfmt(item['item_cost'])
            ))

        subtotal = self.cart.subtotal()
        taxes = self.cart.tax_on_items()
        total = self.cart.grand_total()
        sys.stdout.write(INVOICE_FOOTER.format(
            moneyfmt(subtotal),
            moneyfmt(taxes),
            moneyfmt(total)))


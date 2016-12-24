import sys
import decimal

from ex10_self_checkout.cart import Cart

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
    # TODO: figure out how to do this without passing in std*
    def __init__(self, tax_rate=0.0, my_input=sys.stdin, my_output=sys.stdout):
        try:
            self.tax_rate = float(tax_rate)
        except ValueError:
            raise RuntimeError("Tax Rate is not a float: '%s'" % str(tax_rate))

        self.cart = Cart(self.tax_rate)
        self.input = my_input
        self.output = my_output

    def run(self):
        self.gather_items()
        self.print_invoice()

    def gather_items(self):

        while True:
            self.output.write('Item: ')
            item = self.input.readline().strip()
            if len(item) < 1:
                break
            self.output.write('Quantity: ')
            quantity = int(self.input.readline().strip())
            self.output.write('Unit Price: ')
            unit_price = float(self.input.readline().strip())
            self.cart.add_item(item, quantity, unit_price)

    def print_invoice(self):
        self.output.write(INVOICE_HEADER)
        for item_no in range(0, self.cart.item_count()):
            item = self.cart.items[item_no]
            self.output.write(INVOICE_ITEM.format(
                str(item_no+1),
                str(item['item']),
                str(item['quantity']),
                self.moneyfmt(item['unit_price']),
                self.moneyfmt(item['item_cost'])
            ))

        subtotal = self.cart.subtotal()
        taxes = self.cart.tax_on_items()
        total = self.cart.grand_total()
        self.output.write(INVOICE_FOOTER.format(
            self.moneyfmt(subtotal),
            self.moneyfmt(taxes),
            self.moneyfmt(total)))

    def moneyfmt(self, value, places=2, curr='$', sep=',', dp='.',
                 pos='', neg='-', trailneg=''):

        """from: https://docs.python.org/3/library/decimal.html#recipes

        Convert Decimal to a money formatted string.

        places:  required number of places after the decimal point
        curr:    optional currency symbol before the sign (may be blank)
        sep:     optional grouping separator (comma, period, space, or blank)
        dp:      decimal point indicator (comma or period)
                 only specify as blank when places is zero
        pos:     optional sign for positive numbers: '+', space or blank
        neg:     optional sign for negative numbers: '-', '(', space or blank
        trailneg:optional trailing minus indicator:  '-', ')', space or blank

        >>> d = Decimal('-1234567.8901')
        >>> moneyfmt(d, curr='$')
        '-$1,234,567.89'
        >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
        '1.234.568-'
        >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
        '($1,234,567.89)'
        >>> moneyfmt(Decimal(123456789), sep=' ')
        '123 456 789.00'
        >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
        '<0.02>'

        """
        q = decimal.Decimal(10) ** -places  # 2 places --> '0.01'
        sign, digits, exp = value.quantize(q).as_tuple()
        result = []
        digits = list(map(str, digits))
        build, next = result.append, digits.pop
        if sign:
            build(trailneg)
        for i in range(places):
            build(next() if digits else '0')
        if places:
            build(dp)
        if not digits:
            build('0')
        i = 0
        while digits:
            build(next())
            i += 1
            if i == 3 and digits:
                i = 0
                build(sep)
        build(curr)
        build(neg if sign else pos)
        return ''.join(reversed(result))

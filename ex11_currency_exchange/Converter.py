
from decimal import Decimal

from ex11_currency_exchange.OpenExchangeRatesGateway.Gateway import Gateway

class Converter():
    def __init__(self, currency_table=None, currency_base='USD'):
        if currency_table:
            self.currency_table = currency_table
        else:
            self.currency_table = Gateway().get_rates(static=True)
        self.currency_base = currency_base

    def convert(self, from_amount, from_currency_type, to_currency_type):
        base = Decimal(self.currency_table[self.currency_base])
        from_rate = Decimal(self.currency_table[from_currency_type])
        base_amount = from_amount * base / from_rate

        to_rate = Decimal(self.currency_table[to_currency_type])
        to_amount = base_amount / to_rate

        to_amount = Decimal(to_amount).quantize(Decimal('0.01'))
        return to_amount

    def available_currencies(self):
        return sorted(list(self.currency_table.keys()))


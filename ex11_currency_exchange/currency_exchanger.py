
from decimal import Decimal
from ex11_currency_exchange.Converter import Converter

class CurrencyExchanger:
    def __init__(self):
        self.converter = Converter()

    def gather_input(self):
        currency_from = input('What currency do you have? ').strip()
        if len(currency_from) < 1:
            raise EOFError
        amount_from = Decimal(input('How much of this currency do you have? '))
        currency_to = input('What currency do you want? ').strip()

        return [currency_from, amount_from, currency_to]

    def run(self):

        while True:
            try:
                from_currency_type, from_amount, to_currency_type = self.gather_input()
            except EOFError:
                break
            to_amount = self.converter.convert(from_amount, from_currency_type, to_currency_type)
            print("%s in %s is %s in %s" % (
                str(from_amount),
                str(from_currency_type),
                str(to_amount),
                str(to_currency_type)
            ))





class TaxCalculator:

    TAXTABLE = {
        'WI': 5.5 / 100.0
    }

    def calc(self,
             amount,
             state):
        """
        Calculate tax for Wisconsin residents only
        :param amount: (float) amount of order
        :param state: (str) state 2-char code
        :return: (tuple) subtotal, tax amount, total amount
        """

        tax_rate = 0.0

        if state in self.TAXTABLE.keys():
            tax_rate = self.TAXTABLE[state]

        tax_amount = amount * tax_rate
        total_amount = amount + tax_amount

        return (amount, tax_amount, total_amount)


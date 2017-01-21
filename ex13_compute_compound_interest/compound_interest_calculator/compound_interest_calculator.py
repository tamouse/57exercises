


class CompoundInterestCalculator:

    def __init__(self):
        pass

    def calc(self,
             principal,
             rate,
             time,
             periods):
        """
        Calculate compount interest. Formula is A = (P * (1 + r/n)) ^ (n*t)

        :param principal: the principal amount P
        :param rate: the annual rate of interest as a percentage r
        :param time: the number of years the amount is invested t
        :param periods: the number of periods of compounding per year n
        :return: the amount at the end of investment A
        """

        rate = rate / 100.0

        return principal * (1 + rate / periods) ** (periods * time)

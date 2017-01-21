
from decimal import Decimal
import logging
from utils.moneyfmt import moneyfmt
from ex12_compute_simple_interest.simple_interest_calculator.sicalc import SICalc


class Cli:
    def __init__(self, log_level=logging.INFO):
        logging.basicConfig(level=log_level)
        self.calculator = SICalc(log_level=log_level)

    def gather_input(self):
        principle = input('Principle: ').strip()
        rate = input('Rate Percentage: ').strip()
        time_span = input('Time (in years): ').strip()
        logging.debug("""
        inputs:

        Principle: {p}
        Rate: {r}
        Time: {t}
        """.format(p=principle, r=rate, t=time_span))

        return {
            'principle': principle,
            'rate': rate,
            'time': time_span
        }

    def repl(self):
        while True:
            inputs = self.gather_input()
            if inputs['principle'] == '':
                break

            accrued_interest = self.calculator.calc(
                principle=inputs['principle'],
                rate=inputs['rate'],
                time=inputs['time']
            )

            print("After {t} years at {r} interest, the investment will be worth {p}".format(
                p=moneyfmt(accrued_interest),
                r=inputs['rate'],
                t=inputs['time']
            ))

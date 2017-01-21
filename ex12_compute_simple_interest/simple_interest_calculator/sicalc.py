import logging

class SICalc:
    def __init__(self, log_level=logging.INFO):
        logging.basicConfig(level=log_level)

    def calc(self,
             principle,
             rate,
             time):

        p = float(principle)
        logging.debug("Principle: %0.2f" % p)
        r = float(rate) / 100.0
        logging.debug("Rate: %0.4f" % r)
        t = float(time)
        logging.debug("Time: %0.1f" % t)

        accrued = p * (1 + r * t)
        logging.debug("Accrued: %0.2f" % accrued)
        return accrued

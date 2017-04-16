import unittest
import datetime
from ex06_retirement_calculator.retire_calc import *

class TestRetireCalc(unittest.TestCase):

    def test_retire_calc(self):
        retire_age = 70.0
        current_age = 60.0
        current_year = datetime.date.today().year
        years_to_retire = 10.0
        retire_year = int(current_year + years_to_retire)
        self.assertEqual((years_to_retire, retire_year), retire_calc(retire_age, current_age) )


if __name__ == '__main__':
    unittest.main()

"""
“Create a program that prompts for your weight, gender, number of drinks, the amount of alcohol by volume of the drinks
consumed, and the amount of time since your last drink. Calculate your blood alcohol content (BAC) using this formula

BAC = (A * 5.14 / W * r) - 0.015 * H

where

- A is total alcohol consumed, in ounces (oz).
- W is body weight in pounds.
- r is the alcohol distribution ratio:
  - 0.73 for men
  - 0.66 for women
- H is number of hours since the last drink.

Display whether or not it’s legal to drive by comparing the blood
"""

FEMALE_ALCOHOL_DISTRIBUTION_RATIO = 0.66
MALE_ALCOHOL_DISTRIBUTION_RATIO = 0.73
DEFAULT_LEGAL_LIMIT = 0.08
DEFAULT_LEGAL_LIMIT_COMMERCIAL = 0.04


class BloodAlcoholCalculator:
    def __init__(self,
                 female_adr=FEMALE_ALCOHOL_DISTRIBUTION_RATIO,
                 male_adr=MALE_ALCOHOL_DISTRIBUTION_RATIO,
                 legal_limit=DEFAULT_LEGAL_LIMIT):
        self.female_adr = female_adr
        self.male_adr = male_adr
        self.legal_limit = legal_limit
        self.bac = 0.0

    def is_legal(self,
                 total_alcohol_consumed,
                 weight_in_pounds,
                 gender,
                 hours_since_last_drink):
        self.bac = self.calc(
            total_alcohol_consumed=total_alcohol_consumed,
            weight_in_pounds=weight_in_pounds,
            gender=gender,
            hours_since_last_drink=hours_since_last_drink
        )
        return self.bac < self.legal_limit

    def calc(self,
             total_alcohol_consumed=0.0,
             weight_in_pounds=0.0,
             gender=None,
             hours_since_last_drink=0.0):
        gender = str(gender).lower()
        if gender == 'female':
            self.bac = self._calc(total_alcohol_consumed,
                                  weight_in_pounds,
                                  self.female_adr,
                                  hours_since_last_drink)
        else:
            self.bac = self._calc(total_alcohol_consumed,
                                  weight_in_pounds,
                                  self.male_adr,
                                  hours_since_last_drink)
        return self.bac

    @staticmethod
    def _calc(alc_consumed,
              weight,
              dist_ratio,
              hours):
        return (
            (
                (alc_consumed * 5.14) /
                (dist_ratio * weight)
            ) -
            (0.015 * hours)
        )


if __name__ == '__main__':
    calculator = BloodAlcoholCalculator()

    total_alc = float(input("Total Alcohol consumed in ounces: "))
    person_weight = float(input("Weight of person in pounds: "))
    person_gender = str(input("Gender of person (female / male): "))
    last_drink_hours_ago = float(input("Number of hours since last drink: "))

    results = calculator.is_legal(
        total_alcohol_consumed=total_alc,
        weight_in_pounds=person_weight,
        gender=person_gender,
        hours_since_last_drink=last_drink_hours_ago
    )

    print("Current blood alcohol is {bac}".format(bac=calculator.bac))
    if results:
        print("You are still legal to drive")
    else:
        print("You are not legal to drive")

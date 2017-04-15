"""

“Create a program that determines how many years you have left until retirement and the year you can retire. It should prompt for your current age and the age you want to retire”

Excerpt From: Brian P. Hogan. “Exercises for Programmers (for Tamara Temple).” iBooks.

"""

import datetime


def retire_calc(retire_age, current_age):
    retire_age = float(retire_age)
    current_age = float(current_age)

    current_year = datetime.date.today().year
    years_to_retire = retire_age - current_age
    retire_year = current_year + years_to_retire

    return years_to_retire, retire_year

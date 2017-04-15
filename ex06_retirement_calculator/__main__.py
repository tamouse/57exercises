

from ex06_retirement_calculator.retire_calc import *

retire_age = input("At what age do you want to retire? ")
current_age = input("How old are you now? ")

(years_to_retire, retire_year) = retire_calc(retire_age, current_age)

print("You will retire in the year {}".format(retire_year))
print("You have {} years to retirement".format(years_to_retire))

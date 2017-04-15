

DEFAULT_LEGAL_DRIVING_AGE = 16

class LegalDrivingAgeCalculator:
    def __init__(self,
                 legal_driving_age=DEFAULT_LEGAL_DRIVING_AGE):
        self.legal_driving_age = legal_driving_age

    def is_legal(self,
              driving_age):
        return (float(driving_age) >= self.legal_driving_age)



if __name__ == "__main__":
    age = input("What is your age? --> ")
    legal = LegalDrivingAgeCalculator().is_legal(age)
    if (legal):
        print("You are legal to drive")
    else:
        print("You may not drive")



import random


NUMBERS_OF_COLUMNS = 6
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1


row = int(input("How many quick picks? "))
while row < 0:
    print("Error")
    row = int(input("How many quick picks? "))

for i in range(row):
    quick_pick = []
    for x in range(NUMBERS_OF_COLUMNS):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))




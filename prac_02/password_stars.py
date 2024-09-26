""" Random amount of smiley faces between random number of smiley faces """

import random

low = int(input("Low: "))
high = int(input("High: "))
while low > high:
        print("Invalid Number")
        low = int(input("Low: "))
random_number = random.randint(low, high)
print("*" * random_number )



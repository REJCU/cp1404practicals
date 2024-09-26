""" Random amount of smiley faces between random number of smiley faces """

import random


def main():
        high, low = get_password()
        while low > high:
                print("Invalid Number")
                low = int(input("Low: "))
        random_number = random.randint(low, high)
        print_password(random_number)


def print_password(random_number):
        print("*" * random_number)


def get_password():
        low = int(input("Low: "))
        high = int(input("High: "))
        return high, low


main()



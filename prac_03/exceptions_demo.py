"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Entering anything but a value e.g. letters or other symbols

2. When will a ZeroDivisionError occur?
When zero is entered for the denominator but not the numerator.
When it is inputted on both inputs.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


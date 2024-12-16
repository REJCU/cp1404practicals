"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = calculate_fahrenheit()
            print(f"Result: {fahrenheit:.2f} Fahrenheit")
        elif choice == "F":
            celsius = calculate_celsius()
            print(f"Result: {celsius:.2f} Celsius")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius():
    fahrenheit = float(input("fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()

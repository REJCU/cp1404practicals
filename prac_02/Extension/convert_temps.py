

def main():
    MENU = """
    G - Get input
    C - Convert to Output
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
             list_of_temp = get_input()
             print(list_of_temp)
        elif choice == "C":
            convert_output()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_input():
    fahrenheit = open("temps_input.txt", "r")
    return fahrenheit



def convert_output():
    print(l)


main()
""" Menus """

"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""

# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print(f"Result: {fahrenheit:.2f} F")
#     elif choice == "F":
#         fahrenheit = float(input("fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print(f"Result: {celsius:.2f} F")
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")



name = input("Enter Name: ")
menu = "(H)ello \n(G)oodbye \n(Q)uit "
print(menu)
choice = input(">>> ").upper()
while choice != "Q".upper():
    if choice == "H".upper():
        print(f"hello {name}")
    elif choice == "G".upper():
        print(f"goodbye {name}")
    else:
        print("Invalid Choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")

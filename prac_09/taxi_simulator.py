"""
Taxi Simulator program
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"

def main():
    bill_of_taxi = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(f"Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            taxi_choice = choose_taxi(taxis, bill_of_taxi)
        elif choice == "D":
            try:
                current_taxi = taxis[taxi_choice]
                bill_of_taxi += drive_taxi(current_taxi)
            except UnboundLocalError:
                print("You need to choose before you drive")
        else:
            print("Invalid Choice")
        print(MENU)
        print(f"Total cost trip: ${bill_of_taxi: .2f}")
        choice = input(">>> ").upper()
    display_taxi(taxis)


def choose_taxi(taxis, bill_of_taxi):
    """ Choose the taxi from available choices """
    print("Taxi available:")
    number_of_taxi = - 1
    for taxi in taxis:
        number_of_taxi += 1
        print(f"{number_of_taxi} - {taxi}")
    chosen_taxi = int(input("Choose Taxi: "))
    print(f"Bill to date: ${bill_of_taxi}")
    return chosen_taxi

def drive_taxi(current_taxi):
    """ uses classes to simulate driving """
    current_taxi.start_fare()
    driving_distance = float(input("Drive how far? "))
    current_taxi.drive(driving_distance)
    cost_of_trip = current_taxi.get_fare()
    print(f"Your {current_taxi.name} cost you ${cost_of_trip}")
    return cost_of_trip

def display_taxi(taxis):
    """ Refactored from chose_taxi to display end of session stats   """
    number_of_taxi = - 1
    print(f"Taxis are now:")
    for taxi in taxis:
        number_of_taxi += 1
        print(f"{number_of_taxi} - {taxi}")


main()
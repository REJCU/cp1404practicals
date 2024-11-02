"""
programming_languages
Estimate: 60 minutes
Actual:  45  minutes
"""

from guitar import Guitar

guitars = []


def main():
    print("my guitars")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        guitars_append = Guitar(name, year, cost)
        guitars.append(guitars_append)
        print(guitars_append, " appeneded.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars: ")
        for i, guitar in enumerate(guitars, 1):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(is vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")
    else:
            print("No guitars")


main()
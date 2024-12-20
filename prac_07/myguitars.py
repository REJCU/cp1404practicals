from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = []

    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: ")
        guitar_to_append = Guitar(name,int(year),cost)
        guitars.append(guitar_to_append)
        name = input("Name: ")


    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0],int(parts[1]), parts[2])
        guitars.append(guitar)
    in_file.close()

    with open(FILENAME, "a") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}")
    out_file.close()

    sorted_age = sorted(guitars)

    for guitar in sorted_age:
        print(guitar)


main()


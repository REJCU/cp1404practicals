import csv
from guitar import Guitar

def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        print(parts[0], parts[1], parts[2])
    in_file.close()

main()
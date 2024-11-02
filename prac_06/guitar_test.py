from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)

print(f"{guitar.name}get_age() - Expected {100} - got {guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected TRUE - got {guitar.is_vintage()} ")
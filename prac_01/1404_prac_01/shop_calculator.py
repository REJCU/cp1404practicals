""" Shop Calculator """

total = 0
list_of_number = []

number_of_items = int(input("Number of Items: "))

while number_of_items < 0:
    print("Invalid Item")
    number_of_items = int(input("Number of Items: "))

for number_of_items in range(number_of_items):
    price_of_item = float(input("Price:"))
    total = total + price_of_item
    number_of_items +=1

if total > 100:
    total = total * 0.9

print(f"Total price for {number_of_items} items is ${total:.2f}")



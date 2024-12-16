"""
Test using unreliable car
Uses Inheritance
"""

from unreliable_car import UnreliableCar

worn_down_car = UnreliableCar("worn_down_car", 100, 25)
slightly_less_worn_down_car  = UnreliableCar("Slightly_less_worn_down_car", 100, 50)

for i in range(1, 12):
    print(f"Attempting to drive {i}km:")
    print(f"{worn_down_car.name:12} drove {worn_down_car.drive(i):2}km")
    print(f"{slightly_less_worn_down_car.name:12} drove {slightly_less_worn_down_car.drive(i):2}km")

print(worn_down_car)
print(slightly_less_worn_down_car)
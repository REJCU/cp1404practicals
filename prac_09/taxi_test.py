from taxi import Taxi

my_taxi = Taxi("Prius",100, 1.23 )
my_taxi.drive(40)
print(f"{my_taxi}, \nTaxi fare: ${my_taxi.price_per_km * my_taxi.odometer}")

print("\nNew Fare")
my_taxi.get_fare()
my_taxi.drive(100)
print(f"{my_taxi}, \nTaxi fare: ${my_taxi.price_per_km * my_taxi.odometer}")

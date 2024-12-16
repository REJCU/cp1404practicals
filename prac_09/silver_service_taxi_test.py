from prac_09.silver_service_taxi import SilverServiceTaxi

""" assert Test """


""" Driving Test """
t1 = SilverServiceTaxi("Ute", 100, 5)
t1.drive(40)
print(t1)
print(f"${t1.get_fare()}")

""" 18km trip """
t2 = SilverServiceTaxi("SUV", 100, 2)
t2.drive(18)
print(t2)
print(f"${t2.get_fare()}")



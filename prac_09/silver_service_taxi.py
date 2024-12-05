"""
Silver Service Taxi
Time to complete:
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self,name, fuel, fanciness):
        """ Specialised version using fanciness to increase cost """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus {self.flag_fall:.2f}"

    def fare(self):
        return self.flag_fall + super().get_fare()

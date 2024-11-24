"""
Band class
"""
from prac_09.musician import Musician


class Band(Musician):

    def __init__(self, name):
        super().__init__(name)
        self.bands = []

    def __str__(self):
        return f"{self.name}, {self.bands}"

    def add(self, member):
        self.bands.append(member)

    def play(self):
        return '\n'.join([band.play() for band in self.bands])

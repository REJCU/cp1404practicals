from tkinter import PanedWindow

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    """ Miles to Kilometres conversion """
    output_of_km = StringProperty()

    def build(self):
        """Get structure from Kivy kv file"""
        self.title = "Convert Miles Km App"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_increment(self,text,swap):
        miles = self.convert_to_number(text) + swap
        self.root.ids.input_number = str(miles)

    def change_result(self, miles):
        self.output_of_km = str(miles * MILES_TO_KM)

    def handle_calculation(self, text):
        miles = self.convert_to_number(text)
        self.change_result(miles)

    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()

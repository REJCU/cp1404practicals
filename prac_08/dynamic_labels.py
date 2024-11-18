from kivy.app import App
from kivy.lang import Builder


class DynamicLabelApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.label_to_name = ["Jon", "Tom", "Charles", "Mike"]
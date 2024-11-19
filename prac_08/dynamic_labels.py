from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names_to_label = ["Jon", "Tom", "Charles", "Mike"]

    def build(self):
        """ Loads kivy file to use as outline """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root


    def create_labels(self):
        for name in self.names_to_label:
            label_name = Label(text=f"Name:{name}")
            self.root.add_widget(label_name)


DynamicLabelApp().run()

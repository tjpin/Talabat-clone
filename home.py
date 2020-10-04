from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout


class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)


class HomeApp(MDApp):
    def build(self):
        return HomePage()




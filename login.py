from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivymd.uix.button import MDRoundFlatIconButton


class MyMDRoundFlatIconButton(MDRoundFlatIconButton):
    width = NumericProperty(100)
    height = NumericProperty(100)


class LoginWin(Screen):
    pass


class LoginApp(MDApp):
    def build(self):
        return LoginWin()



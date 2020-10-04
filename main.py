from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from login import LoginWin
from home import HomePage



class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        items = ['Home', 'Your Orders', 'Notifications', 'talabat Pay', 'Get help', 'About']
        icons = ['home-variant-outline', 'file-document-outline', 'tag-outline', 'card-bulleted-outline', 'chat-outline', 'alert-circle-outline']

        for item, icon in zip(items, icons):
            lists = OneLineIconListItem(text=item, divider=None)
            image = IconLeftWidget(icon=icon)
            lists.add_widget(image)
            self.ids.nav_items.add_widget(lists)

    def home(self):
        self.ids.root_manager.current = 'home'


class MainApp(MDApp):
    def build(self):
        return MainWindow()


MainApp().run()
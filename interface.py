import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class PittodoMain(Widget):
    pass


class PittodoApp(App):
    def build(self):
        return PittodoMain()

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class PittodoMain(Widget):
    pass


class PittodoApp(App):
    global model

    def build(self):
        return PittodoMain()

    def run(self, model):
        self.model = model
        App.run(self)

    def add_task(self):
        print("[PittodoApp] add_task()")
        self.model.add_task()

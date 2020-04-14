import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from debug import tic, toc

class PittodoMain(Widget):
    pass


class PittodoApp(App):
    def build_config(self, config):
        pass

    def build(self):
        config = self.config
        return PittodoMain()

    def run(self, model):
        self.model = model
        App.run(self)

    def add_task(self):
        print("[PittodoApp] add_task()")
        self.model.add_task()

    def on_start(self, **kwargs):
        print('\nWindow loading time:')
        toc()  # for debug window loading time

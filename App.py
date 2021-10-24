from kivy.app import App
from kivy.uix.label import Label

#App().run()

class TextApp(App):
    def build(self):
        return Label(text='HELLO')

TextApp().run()
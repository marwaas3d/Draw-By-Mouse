from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
import random

class DrawingPad(Widget):

    def get_color(self, touch):
        if 'color' not in touch.ud:
            random.seed(touch.uid)
            touch.ud['color'] = (random.random(), random.random(), random.random())
        return touch.ud['color']

    def on_touch_down(self, touch):
        color = self.get_color(touch)
        with self.canvas:
            Color(*color)
            d = 30
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            touch.ud['line'] = Line(points=[touch.x, touch.y], width=2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]




class TouchDrawApp(App):
    def build(self):
        return DrawingPad()

TouchDrawApp().run()
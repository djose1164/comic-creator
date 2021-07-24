from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.graphics import Color

kv = """
#:kivy 1.9.1
BoxLayout:
    orientation: 'vertical'
    Widget:
        id: w_canvas
        my_color: (0, 1, 1)
        canvas:
            Color:
                rgb: self.my_color
            Rectangle:
                pos: self.pos
                size: (self.width/2, self.height/2)
            Color:
                group: 'b'
                rgb: (0, .8, 0)
            Ellipse:
                group: 'a'
                pos: (self.pos[0], self.pos[1] + self.height/2)
                size: (self.width/4, self.height/4)
            Ellipse:
                group: 'b'
                pos: (self.pos[0]+ self.width/2, self.pos[1] + self.height/2)
                size: (self.width/4, self.height/4)
    Button:
        text: 'Click me'
        on_release: app.handle_button()
"""
class Test(App):
    def build(self):
        return Builder.load_string(kv)
    def handle_button(self):
        # binding Canvas instruction property to Widget property
        self.root.ids.w_canvas.my_color = (.5, .2, 0)
        # Access single item of canvas instruction group
        an_ellipse = self.root.ids.w_canvas.canvas.get_group('a')[0]
        an_ellipse.pos = (an_ellipse.pos[0] + 10, an_ellipse.pos[1])
        # loop through all elements of canvas instruction group
        for gitem in self.root.ids.w_canvas.canvas.get_group('b'):
            if isinstance(gitem, Color):
                gitem.rgb = (0, .5, 1)
            try:
                gitem.size = (gitem.size[0] / 2.0, gitem.size[1])
            except:
                pass

Test().run()
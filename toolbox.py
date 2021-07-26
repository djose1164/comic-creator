import math
import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets import Stickman, DraggableWidget

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space
        if self.state == "down" and ds.collide_point(touch.x, touch.y):
            (x, y) = ds.to_widget(touch.x, touch.y)
            self.draw(ds, x, y)
            return True
        return super().on_touch_down(touch)

    def draw(self, ds, x, y):
        '''For being implemented in the subclass.'''
        pass
    
class ToolStickMan(ToolButton):
    def draw(self, ds, x, y):
        sm = Stickman(width=48, height=48)
        sm.center = (x, y)
        ds.add_widget(sm)
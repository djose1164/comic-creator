from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line


class DraggableWidget(RelativeLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.selected = None  # To know if the widget was selected.

    def on_touch_down(self, touch):
        """To verify if the event was in the widget.

        Args:
            touch (MotionEvent): An input event front the mouse, the screen or a magic pen.

        Returns:
            bool: I'm not sure. If true do some work? To review later.
        """
        if self.collide_point(touch.x, touch.y):
            self.select()
            return True
        return super().on_touch_down(touch)

    def select(self):
        """If the widget was selected draw a rectangle that serround it.
        """
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(
                    rectangle=(0, 0, self.width, self.height), dash_off=2
                )

    def on_touch_move(self, touch):
        (x,y) = self.parent.to_parent(touch.x, touch.y)
        if self.selected and self.parent.collide_point(
            x - self.width/2, y - self.height/2):
            self.translate(touch.x - self.ix, touch.y - self.iy)
            return True
        return super().on_touch_move(touch)
    
    def translate(self, x, y):
        self.center_x = self.ix = self.ix + x
        self.center_y = self.iy = self.iy + y
    
    def on_touch_up(self, touch):
        if self.selected:
            self.unselected()
            return True
        return super().on_touch_up(touch)
    
    def unselected(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None
        
class Stickman(DraggableWidget):
    pass
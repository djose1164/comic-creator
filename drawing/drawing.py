from kivy import require
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("drawing/drawing.kv")
# Builder.load_file("drawing/drawing_line.kv")
# Builder.load_file("drawing/drawing_img.kv")
# Builder.load_file("./kv/drawing/drawing_order.kv")
require("1.11.1")


class DrawingSpace(RelativeLayout):
    pass


class DrawingApp(App):
    def build(self):
        return DrawingSpace()


def main():
    Window.size = 300, 100
    app = DrawingApp()
    app.run()


if __name__ == "__main__":
    main()

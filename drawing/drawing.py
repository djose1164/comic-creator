from kivy import require
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.core.window import Window

# Builder.load_file("drawing.kv")
# Builder.load_file("drawing_line.kv")
# Builder.load_file("drawing_img.kv")
Builder.load_file("drawing_order.kv")
require("1.11.1")


class DrawingSpace(RelativeLayout):
    pass


class _DrawingApp(App):
    def build(self):
        return DrawingSpace()


def main():
    Window.size = 300, 100
    app = _DrawingApp()
    app.run()


if __name__ == "__main__":
    main()

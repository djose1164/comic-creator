from kivy import require
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from os import listdir

kv_path: str = "./kv/"
for kv in listdir(kv_path):
    print(kv)
    Builder.load_file(kv_path + kv)

require("1.11.1")


class ComicCreator(AnchorLayout):
    pass


class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()


def main():
    app = ComicCreatorApp()
    app.run()


if __name__ == "__main__":
    main()

"""test module
"""
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class Test(AnchorLayout):
    pass

class TestApp(App):
    def build(self):
        return Test()

def main():
    app = TestApp()
    app.run()
    
if __name__ == '__main__':
    main()
    
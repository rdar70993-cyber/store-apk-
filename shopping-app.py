from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ShoppingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text="Add to Cart"))
        layout.add_widget(Button(text="Checkout"))
        layout.add_widget(Button(text="View Orders"))
        return layout

if __name__ == "__main__":
    ShoppingApp().run()

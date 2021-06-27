import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.button import Button

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
class ConnectPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout
        super().__init__(**kwargs)
        
        self.cols = 2  # used for our grid

        # widgets added in order, so mind the order.
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.join = Button(text="Login")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.join)

        self.register = Button(text="Register")
        self.register.bind(on_press=self.register_button)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.register)

    def join_button(self, instance):
        username = self.username.text
        password = self.password.text
        print(f"Joining as {username}")
        with open("prev_details.txt","w") as f:
            f.write(f"{password},{username}")

    def register_button(self, instance):
        print(f"New account")
        
        
class RepairTool(App):
    def build(self):
        # return Label(text='Hello world')
        return ConnectPage()
    
if __name__ == '__main__':
    RepairTool().run()

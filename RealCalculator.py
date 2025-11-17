#Program to make a calculator
# import
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #this helps us in creating rows and columns
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window #Window lives in kivy.core.window, not in kivy.uix. The core module deals with lower-level components like windows, input providers, etc., while uix handles the user interface widgets.

Window.size =(300,500)

class Calculator(BoxLayout):
    def __init__(self,**kwargs): # **kwargs lets you pass a dictionary of keyword arguments to a function or class. In Kivy, this is often used in widget constructors to allow customization of properties like size, pos, text, color, etc.

        super().__init__(orientation='vertical',**kwargs) # Orientation is given to change the box layout to vertical as default layout is horizontal
        # Build Out the App
        self.result =TextInput(
            font_size=45,
            size_hint_y=0.2,
            readonly=True,
            halign='right',
            multiline=False,
            background_color=[0.2,0.2,0.2,1],
            foreground_color=[1,1,1,1]
        )
        self.add_widget(self.result)
        
        # Create the Buttons
        buttons = [
            ['C', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '00', '.', '=']
        ]
        
        grid=GridLayout(cols=4,spacing=5,padding=10)
        for row in buttons:
            for item in row:
                button = Button(
                    text=item,
                    font_size=32,
                    background_color=self.set_button_color(item),
                    on_press=self.button_click
                    
                )
                grid.add_widget(button)
                
        self.add_widget(grid)
        
    def set_button_color(self,label):
        if label in {'C', '+/-', '%', '/'}:
            return [0.6,0.6,0.6,1]
        elif label in {"/","*","-","+","="}:
            return [1,0.65,0,1]
        return [0.3,0.3,0.3,1]
        
        
        
        
        
        
        
        
       
    def button_click(self,instance):
        text=instance.text
        
        if text =="C":
            self.result.text =""
        elif text =="=":
            self.calculate()
        elif text =="+/-":
            self.toggle_neg()
        elif text =="%":
            self.convert_percent()
        else:
            self.result.text += text
        
    #Calculate
    def calculate(self):
        try:
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error!"
            
    def toggle_neg(self):
        if self.result.text:
            self.result.text = self.result.text[1:] if self.result.text[0] == "-"else"-" + self.result.text
            
    def convert_percent(self):
        try:
            self.result.text = str(float(self.result.text)/100)
        except ValueError:
            self.result.text = "Error!"   
    
class CalculatorApp(App):
    def build(self):
        return Calculator()
    
if __name__ =="__main__":
    CalculatorApp().run()


'''
# Program to make a calculator

# Import necessary Kivy modules
from kivy.app import App                         # Core Kivy App class
from kivy.uix.boxlayout import BoxLayout         # Layout that arranges widgets in rows/columns
from kivy.uix.textinput import TextInput         # For user input or displaying text
from kivy.uix.button import Button               # For clickable buttons
from kivy.uix.gridlayout import GridLayout       # Layout that arranges widgets in a grid
from kivy.core.window import Window              # Allows window customization like size and title

# Set initial window size to 300x500 pixels
Window.size = (300, 500)

# Define the main Calculator class, inheriting from BoxLayout
class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        # Initialize the superclass with vertical layout
        super().__init__(orientation='vertical', **kwargs)

        # Create the display area for input and output
        self.result = TextInput(
            font_size=45,                        # Large font for readability
            size_hint_y=0.2,                     # Occupies 20% of vertical space
            readonly=True,                       # Prevent typing directly into it
            halign='right',                      # Align text to the right
            multiline=False,                     # Single line display
            background_color=[0.2, 0.2, 0.2, 1], # Dark background
            foreground_color=[1, 1, 1, 1]        # White text
        )
        self.add_widget(self.result)             # Add the result TextInput to layout

        # Define calculator button layout as a list of rows
        buttons = [
            ['C', '+/-', '%', '/'],              # Special and division operations
            ['7', '8', '9', '*'],                # Multiplication row
            ['4', '5', '6', '-'],                # Subtraction row
            ['1', '2', '3', '+'],                # Addition row
            ['0', '00', '.', '=']                # Zero, decimal and equals
        ]

        # Create grid to hold buttons: 4 columns, spacing, and padding
        grid = GridLayout(cols=4, spacing=5, padding=10)

        # Loop through each row and item to create button widgets
        for row in buttons:
            for item in row:
                button = Button(
                    text=item,
                    font_size=32,
                    background_color=self.set_button_color(item),  # Set color based on type
                    on_press=self.button_click                    # Bind click handler
                )
                grid.add_widget(button)       # Add button to grid layout

        self.add_widget(grid)                 # Add grid layout to main screen

    # Decide button colors based on label type
    def set_button_color(self, label):
        if label in {'C', '+/-', '%', '/'}:
            return [0.6, 0.6, 0.6, 1]         # Light gray for modifiers
        elif label in {"/", "*", "-", "+", "="}:
            return [1, 0.65, 0, 1]            # Orange for operators
        return [0.3, 0.3, 0.3, 1]             # Dark gray for numbers and decimal

    # Handle button click events
    def button_click(self, instance):
        text = instance.text                  # Get label of clicked button

        if text == "C":
            self.result.text = ""             # Clear display
        elif text == "=":
            self.calculate()                  # Compute result
        elif text == "+/-":
            self.toggle_neg()                 # Toggle sign
        elif text == "%":
            self.convert_percent()            # Convert to percentage
        else:
            self.result.text += text          # Add pressed digit/operator to display

    # Evaluate expression in display
    def calculate(self):
        try:
            self.result.text = str(eval(self.result.text))  # Use eval to compute result
        except Exception:
            self.result.text = "Error!"       # Catch invalid expressions

    # Toggle sign of current number
    def toggle_neg(self):
        if self.result.text:
            # Remove minus if present, else add it
            self.result.text = self.result.text[1:] if self.result.text[0] == "-" else "-" + self.result.text

    # Convert number to percentage (divide by 100)
    def convert_percent(self):
        try:
            self.result.text = str(float(self.result.text) / 100)
        except ValueError:
            self.result.text = "Error!"       # If not a number, show error

# Main application class
class CalculatorApp(App):
    def build(self):
        return Calculator()                   # Return instance of our calculator layout

# Run the app
if __name__ == "__main__":
    CalculatorApp().run()
'''
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import pyperclip

# Morse Code Dictionary: maps letters and numbers to their respective Morse code symbols
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    text = text.upper()  # Convert the text to uppercase
    morse_code = []  # Initialize an empty list to store the Morse code symbols
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])  # Append Morse code for each letter
        else:
            morse_code.append('')  # If the letter isn't found in the dictionary, add an empty string
    return ' '.join(morse_code)  # Join the Morse code symbols with spaces between them

# Function to convert Morse code to text
def morse_to_text(morse):
    morse_code = morse.split(' ')  # Split the Morse code string by spaces
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}  # Create a reverse dictionary for Morse to Text
    text = []  # Initialize an empty list to store the decoded text
    for code in morse_code:
        if code in reverse_dict:
            text.append(reverse_dict[code])  # Append the corresponding letter from the reverse dictionary
        elif code == '':
            text.append(' ')  # If there's an empty string (space), append a space to the result
    return ''.join(text)  # Join the list of letters to form the final text

# Function to copy text to clipboard using the pyperclip library
def copy_to_clipboard(text):
    pyperclip.copy(text)  # Copy the provided text to the system clipboard

# Kivy UI Layout for the Morse Code Converter App
class MorseCodeApp(App):
    def build(self):
        # Set the window background color to a light grey color
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light grey color for background

        # Set window size to simulate a compact mobile screen (close to Samsung Galaxy A02's 720x1520 resolution)
        Window.size = (300, 500)  # Adjusted to simulate a 5.7-inch screen size

        # Root layout with vertical BoxLayout for stacking widgets
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Define colors for various UI elements
        primary_color = (0.18, 0.45, 0.70, 1)  # Deep blue color for primary UI elements
        secondary_color = (0.12, 0.62, 0.45, 1)  # Teal color for secondary elements (Copy button)
        text_color = (0.2, 0.2, 0.2, 1)  # Dark grey color for text
        button_color = (0.18, 0.45, 0.70, 1)  # Deep blue color for buttons
        button_text_color = (1, 1, 1, 1)  # White color for button text

        # Create input label and text field
        self.input_label = Label(text='Enter Text or Morse Code:', color=text_color, size_hint_y=None, height=40)
        self.input_text = TextInput(hint_text='Type here', multiline=False, size_hint_y=None, height=40,
                                    background_color=(1, 1, 1, 1), foreground_color=text_color)

        # Create output label and text field (no scrollable area)
        self.output_label = Label(text='Output:', color=text_color, size_hint_y=None, height=40)
        self.output_text = TextInput(text='', multiline=True, readonly=True, size_hint_y=None, height=100,
                                     background_color=(1, 1, 1, 1), foreground_color=text_color)

        # Create buttons with associated styles
        self.convert_button = Button(text='Convert to Morse', size_hint_y=None, height=50, background_normal='',
                                     background_color=button_color, color=button_text_color)
        self.reverse_button = Button(text='Convert to Text', size_hint_y=None, height=50, background_normal='',
                                     background_color=button_color, color=button_text_color)
        self.copy_button = Button(text='Copy to Clipboard', size_hint_y=None, height=50, background_normal='',
                                  background_color=secondary_color, color=button_text_color)
        self.clear_button = Button(text='Clear', size_hint_y=None, height=50, background_normal='',
                                   background_color=(0.9, 0.3, 0.3, 1), color=button_text_color)  # Red color for Clear button

        # Bind buttons to their respective functions
        self.convert_button.bind(on_press=self.convert_to_morse)
        self.reverse_button.bind(on_press=self.convert_to_text)
        self.copy_button.bind(on_press=self.copy_output)
        self.clear_button.bind(on_press=self.clear_input)

        # Add widgets to the root layout
        self.root.add_widget(self.input_label)  # Add the input label
        self.root.add_widget(self.input_text)  # Add the input text field
        self.root.add_widget(self.output_label)  # Add the output label
        self.root.add_widget(self.output_text)  # Add the output text field
        self.root.add_widget(self.convert_button)  # Add the Convert to Morse button
        self.root.add_widget(self.reverse_button)  # Add the Convert to Text button
        self.root.add_widget(self.copy_button)  # Add the Copy to Clipboard button
        self.root.add_widget(self.clear_button)  # Add the Clear button

        return self.root

    # Method to convert text to Morse code
    def convert_to_morse(self, instance):
        text = self.input_text.text  # Get the text entered by the user
        morse_code = text_to_morse(text)  # Convert the text to Morse code
        self.output_text.text = morse_code  # Display the Morse code in the output field

    # Method to convert Morse code to text
    def convert_to_text(self, instance):
        morse = self.input_text.text  # Get the Morse code entered by the user
        text = morse_to_text(morse)  # Convert the Morse code to text
        self.output_text.text = text  # Display the decoded text in the output field

    # Method to copy the output text to the clipboard
    def copy_output(self, instance):
        output = self.output_text.text  # Get the output text
        copy_to_clipboard(output)  # Copy the output text to the clipboard
        print("Copied to clipboard!")  # Print a confirmation message in the console

    # Method to clear both input and output fields
    def clear_input(self, instance):
        self.input_text.text = ''  # Clear the input text field
        self.output_text.text = ''  # Clear the output text field

# Run the application
if __name__ == "__main__":
    MorseCodeApp().run()  # Launch the Morse Code App

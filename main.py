import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import pyperclip

# Morse Code Dictionary
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
    text = text.upper()
    morse_code = []
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])
        else:
            morse_code.append('')
    return ' '.join(morse_code)

# Function to convert Morse code to text
def morse_to_text(morse):
    morse_code = morse.split(' ')
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    text = []
    for code in morse_code:
        if code in reverse_dict:
            text.append(reverse_dict[code])
        elif code == '':
            text.append(' ')
    return ''.join(text)

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Kivy UI Layout
class MorseCodeApp(App):
    def build(self):
        # Set the window background color to a light theme
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # Light grey color

        # Set window size to simulate a compact mobile screen (close to Samsung Galaxy A02's 720x1520 resolution)
        Window.size = (300, 500)  # Adjusted to approximate a 5.7-inch screen

        # Root layout with vertical BoxLayout
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Define colors
        primary_color = (0.18, 0.45, 0.70, 1)  # Deep blue color
        secondary_color = (0.12, 0.62, 0.45, 1)  # Teal color
        text_color = (0.2, 0.2, 0.2, 1)  # Dark grey color
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

        # Create buttons
        self.convert_button = Button(text='Convert to Morse', size_hint_y=None, height=50, background_normal='',
                                     background_color=button_color, color=button_text_color)
        self.reverse_button = Button(text='Convert to Text', size_hint_y=None, height=50, background_normal='',
                                     background_color=button_color, color=button_text_color)
        self.copy_button = Button(text='Copy to Clipboard', size_hint_y=None, height=50, background_normal='',
                                  background_color=secondary_color, color=button_text_color)
        self.clear_button = Button(text='Clear', size_hint_y=None, height=50, background_normal='',
                                   background_color=(0.9, 0.3, 0.3, 1), color=button_text_color)  # Red color for Clear button

        # Bind buttons to actions
        self.convert_button.bind(on_press=self.convert_to_morse)
        self.reverse_button.bind(on_press=self.convert_to_text)
        self.copy_button.bind(on_press=self.copy_output)
        self.clear_button.bind(on_press=self.clear_input)

        # Add widgets to the root layout
        self.root.add_widget(self.input_label)
        self.root.add_widget(self.input_text)
        self.root.add_widget(self.output_label)
        self.root.add_widget(self.output_text)
        self.root.add_widget(self.convert_button)
        self.root.add_widget(self.reverse_button)
        self.root.add_widget(self.copy_button)
        self.root.add_widget(self.clear_button)

        return self.root

    def convert_to_morse(self, instance):
        text = self.input_text.text
        morse_code = text_to_morse(text)
        self.output_text.text = morse_code

    def convert_to_text(self, instance):
        morse = self.input_text.text
        text = morse_to_text(morse)
        self.output_text.text = text

    def copy_output(self, instance):
        output = self.output_text.text
        copy_to_clipboard(output)
        print("Copied to clipboard!")

    def clear_input(self, instance):
        """Clear both input and output fields"""
        self.input_text.text = ''
        self.output_text.text = ''

# Run the application
if __name__ == "__main__":
    MorseCodeApp().run()

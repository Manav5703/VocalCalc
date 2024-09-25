from voice_input import listen_for_command
from calculator_logic import parse_command
from ui import create_gui
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def calculate():
    """Capture voice command, parse it, and provide results."""
    command = listen_for_command()
    if command:
        result = parse_command(command)
        if isinstance(result, str):
            # Speak the result if it's a string (like an error message)
            speak(result)
            result_label.config(text=result)  # Use the result_label defined below
        else:
            # Speak and display the numeric result
            speak(f"The result is {result}")
            result_label.config(text=str(result))

if __name__ == "__main__":
    # Create the GUI and pass the calculate function as a callback
    gui, result_label = create_gui(calculate)
    gui.mainloop()

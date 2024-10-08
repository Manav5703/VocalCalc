import threading
from voice_input import listen_for_command
from calculator_logic import parse_command
from ui import create_gui
import pyttsx3
import sys

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def calculate():
    """Capture voice command, parse it, and provide results."""
    window.update_result("Listening for command...")
    
    # Start a new thread to listen for commands to avoid blocking the GUI
    thread = threading.Thread(target=process_voice_command)
    thread.start()

def process_voice_command():
    """Process the voice command asynchronously."""
    command = listen_for_command()
    
    if command:
        window.update_result(f"You said: {command}")
        result = parse_command(command)
        if isinstance(result, str):
            # Speak and show error message
            speak(result)
            window.update_result(f"You said: {command}\n{result}")
        else:
            # Speak and show result
            speak(f"The result is {result}")
            window.update_result(f"You said: {command}\nResult: {result}")
    else:
        # Handle case where no command was captured
        window.update_result("No command heard. Please try again.")
        speak("I didn't hear a command. Please try again.")

if __name__ == "__main__":
    # Create the GUI and pass the calculate function as a callback
    app, window = create_gui(calculate)
    sys.exit(app.exec_())

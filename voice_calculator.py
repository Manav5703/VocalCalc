import threading
from voice_input import listen_for_command  # Custom voice input module
from calculator_logic import parse_command  # Custom command parsing module
from ui import create_gui  # UI creation module using Tkinter
import pyttsx3

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
        # Update the result with the spoken command
        window.update_result(f"You said: {command}")
        result, history_entry = parse_command(command)

        if isinstance(result, str):
            # Speak and show error message
            speak(result)
            window.update_result(f"You said: {command}\n{result}")
        else:
            # Format result for main result box based on operation
            if 'divide' in command or 'by' in command:
                formatted_result = f"{result:.2f}"  # Show two decimal points for division
            else:
                formatted_result = str(result)  # Show as integer for other operations

            # Speak and show result
            speak(f"The result is {formatted_result}")
            window.update_result(f"You said: {command}\nResult: {formatted_result}")

            # Add to history
            window.add_to_history(history_entry)  # Add to history

    else:
        # Handle case where no command was captured
        window.update_result("No command heard. Please try again.")
        speak("I didn't hear a command. Please try again.")

if __name__ == "__main__":
    # Create the Tkinter GUI and pass the calculate function as a callback
    root, window = create_gui(calculate)
    root.mainloop()  # Start the Tkinter event loop

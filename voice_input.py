import speech_recognition as sr

def listen_for_command():
    """Listen for a voice command and return it as a string."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for a command...")
        try:
            audio = recognizer.listen(source)
            print("Audio captured, processing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None



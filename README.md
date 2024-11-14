# VocalCalc

VocalCalc is a Voice-Activated Calculator that allows users to perform basic arithmetic operations using voice commands. This application processes voice input to perform operations like addition, subtraction, multiplication, and division, while providing both visual and audible feedback.

## Features
- Perform basic arithmetic using voice commands:
  - Addition, subtraction, multiplication, and division.
  - Handles error cases such as division by zero and invalid commands.
- Performs scientific calculations:
  - Trigonometric functions.
  - Logarithmic, square root, cube root, and power.
- Voice recognition using Python’s `SpeechRecognition` library.
- Provides audio feedback using the `pyttsx3` library.
- Simple graphical user interface built with `tkinter`.

## Example Commands
- "What is 5 plus 3?"
- "Subtract 10 from 7."
- "What is cosine 45?"
- "What is cube root of 81?"

## Technologies Used
- **Python**: Main programming language.
- **SpeechRecognition**: For voice input processing.
- **pyttsx3**: For text-to-speech feedback.
- **tkinter**: For the graphical user interface.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Manav5703/VocalCalc.git
   cd VocalCalc
2. Install the required libraries:
   ```bash
   pip install SpeechRecognition pyttsx3 tk pillow
3. Run the application:
   ```bash
   python voice_calculator.py

## Usage
- Upon running the app, you can give voice commands like the ones mentioned in the examples.
- The calculator will display the result and provide audio feedback.

## Future Improvements
- Extend support for more complex operations.
- Improve voice recognition accuracy.
- Add support for multiple languages.

## Contributors
- Manav Patel 
- Mohammad Shajjad Hossen

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

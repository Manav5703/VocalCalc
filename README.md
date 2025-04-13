# VocalCalc - Web Edition

VocalCalc is a Voice-Activated Calculator web application that allows users to perform basic arithmetic and scientific operations using voice commands. This application processes voice input to perform calculations while providing both visual and audible feedback.

## Features
- **Voice-Activated Calculations**: Perform calculations using natural language voice commands
- **Basic Arithmetic Operations**:
  - Addition, subtraction, multiplication, and division
  - Handles error cases such as division by zero and invalid commands
- **Scientific Calculations**:
  - Trigonometric functions (sine, cosine, tangent)
  - Logarithmic functions
  - Square root, cube root, and exponentiation
- **Web-Based Interface**:
  - Responsive design that works on desktop and mobile devices
  - Dark/Light theme toggle
  - Keyboard shortcuts for improved accessibility
- **History Tracking**: Save and view your calculation history
- **Accessibility Features**:
  - Voice feedback using browser's text-to-speech
  - Keyboard navigation support

## Example Commands
- "What is 5 plus 3?"
- "Subtract 10 from 7"
- "What is cosine 45?"
- "What is cube root of 81?"

## Technologies Used
- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Web Speech API for voice recognition and synthesis
  - Responsive design with CSS Grid and Flexbox
- **Backend**:
  - Python with Flask framework
  - RESTful API architecture

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
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage
1. Click the microphone button or press 'M' key
2. Speak your calculation command clearly
3. View the result on screen and hear the spoken response
4. Access history, formulas, and scientific functions using the navigation buttons

## Deployment
The application can be deployed to various cloud platforms:

### Heroku Deployment
```bash
heroku create vocalcalc
git push heroku main
```

### Docker Deployment
A Dockerfile is provided for containerized deployment.

## Future Improvements
- Add support for multiple languages
- Implement user accounts to save calculation history
- Create a Progressive Web App (PWA) version
- Develop native mobile applications
- Add more advanced mathematical operations
- Implement equation solving capabilities

## Contributors
- Manav Patel 
- Mohammad Shajjad Hossen

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

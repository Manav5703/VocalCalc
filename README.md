# VocalCalc - Web Edition

VocalCalc is a Voice-Activated Calculator web application that allows users to perform basic arithmetic and scientific operations using voice commands. This application processes voice input to perform calculations while providing both visual and audible feedback.

## Live Demo

Try VocalCalc now: [https://vocalcalc.onrender.com](https://vocalcalc.onrender.com)

The application is deployed on Render and is ready to use. Simply click the link above to access the live version.

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

## Deployment Status

### Current Deployment
VocalCalc is currently deployed on Render and accessible at:
- **URL**: [https://vocalcalc.onrender.com](https://vocalcalc.onrender.com)
- **Platform**: Render
- **Deployment Type**: Web Service
- **Branch**: main

The application is automatically updated whenever changes are pushed to the main branch of the GitHub repository.

### Deployment Instructions
If you want to deploy your own instance of VocalCalc, you can use one of the following methods:

#### Render Deployment (Recommended)
1. Create an account on [Render](https://render.com/)
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: vocalcalc
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

#### Heroku Deployment
1. Install the Heroku CLI and log in:
   ```bash
   npm install -g heroku
   heroku login
   ```
2. Create a new Heroku app:
   ```bash
   heroku create vocalcalc
   ```
3. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
4. Open the deployed app:
   ```bash
   heroku open
   ```

#### Docker Deployment
A Dockerfile is provided for containerized deployment:

1. Build the Docker image:
   ```bash
   docker build -t vocalcalc .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 vocalcalc
   ```

#### AWS Elastic Beanstalk Deployment
1. Install the EB CLI:
   ```bash
   pip install awsebcli
   ```
2. Initialize your EB application:
   ```bash
   eb init -p python-3.11 vocalcalc
   ```
3. Create an environment and deploy:
   ```bash
   eb create vocalcalc-env
   ```
4. Open the deployed application:
   ```bash
   eb open
   ```

## Recent Improvements
- Added a professional landing page with interactive demo
- Implemented favicon for better browser identification
- Enhanced error handling for network and API issues
- Improved command parsing for better voice recognition
- Added deployment configuration for various platforms

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

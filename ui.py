from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class CalculatorGUI(QMainWindow):
    def __init__(self, calculate_callback):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Voice-Activated Calculator")
        self.setGeometry(100, 100, 400, 300)  # Window size

        # Create the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a label to display results
        self.result_label = QLabel("Result", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18px;")  # Simple font size for the label
        layout.addWidget(self.result_label)

        # Create the 'Speak Command' button
        self.speak_button = QPushButton("Speak Command", self)
        self.speak_button.setStyleSheet("font-size: 14px; padding: 8px;")  # Simple button style
        self.speak_button.clicked.connect(calculate_callback)
        layout.addWidget(self.speak_button)

        # Create an info label
        self.info_label = QLabel("Press the button and speak your command.", self)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("font-size: 12px;")  # Simple, minimal font for the info label
        layout.addWidget(self.info_label)

        # Create the 'Quit' button
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setStyleSheet("font-size: 14px; padding: 8px;")  # Simple button style
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

    def update_result(self, text):
        """Update the result label."""
        self.result_label.setText(text)

def create_gui(calculate_callback):
    """Create and return the PyQt5 GUI application."""
    app = QApplication(sys.argv)
    window = CalculatorGUI(calculate_callback)
    window.show()
    return app, window

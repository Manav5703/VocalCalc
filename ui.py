import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CalculatorGUI:
    def __init__(self, root, calculate_callback):
        self.root = root
        self.root.title("Voice-Activated Calculator")
        self.root.geometry("500x400")  # Larger window size

        # Dark theme setup
        self.root.configure(bg="#2e2e2e")  # Dark gray background

        # Top bar frame
        top_frame = tk.Frame(root, bg="#2e2e2e")
        top_frame.pack(fill="x", pady=5)

        # "I" button for instructions
        instruction_button = tk.Button(
            top_frame, text="I", command=self.show_instructions, font=("Helvetica", 12),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        instruction_button.pack(side="right", padx=10)

        # "Formulas" button to display mathematical formulas
        formulas_button = tk.Button(
            top_frame, text="Formulas", command=self.show_formulas, font=("Helvetica", 12),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        formulas_button.pack(side="right", padx=10)

        # Create a canvas for the result display
        self.result_canvas = tk.Canvas(root, width=450, height=100, bg="#4e4e4e", highlightthickness=0)
        self.result_canvas.pack(pady=20)

        # Create the result label on the canvas
        self.result_label = ttk.Label(
            self.result_canvas, text="Result", anchor="center", font=("Helvetica", 24), background="#4e4e4e", foreground="#ffffff"
        )
        self.result_label.place(relx=0.5, rely=0.5, anchor="center")

        # Load and create the mic icon button
        mic_image = Image.open("mic_icon.png")
        mic_image = mic_image.resize((50, 50), Image.ANTIALIAS)  # Resize image to fit button
        mic_photo = ImageTk.PhotoImage(mic_image)

        self.mic_button = tk.Button(
            root, image=mic_photo, command=calculate_callback, bg="#3b3b3b", activebackground="#505050", bd=0
        )
        self.mic_button.image = mic_photo  # Keep a reference to avoid garbage collection
        self.mic_button.pack(pady=20, ipadx=10, ipady=10)

        # Info label
        self.info_label = ttk.Label(
            root, text="Press the mic and speak your command.", anchor="center", font=("Helvetica", 12), background="#2e2e2e", foreground="#ffffff"
        )
        self.info_label.pack(pady=10)

        # Apply custom styles for buttons
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14), padding=10)

    def update_result(self, text):
        """Update the result label with calculation result."""
        self.result_label.config(text=text)

    def show_instructions(self):
        """Display instructions in a new window similar to the formulas window."""
        instructions = [
            "1. Click the microphone button and speak a calculation.",
            "2. Supported commands include addition, subtraction, multiplication, and division.",
            "3. Example: 'What is 5 plus 3' or 'Calculate 12 divided by 4'."
        ]

        instructions_window = tk.Toplevel(self.root)
        instructions_window.title("Instructions")
        instructions_window.geometry("400x300")
        instructions_window.configure(bg="#2e2e2e")

        instructions_label = tk.Label(instructions_window, text="Instructions", font=("Helvetica", 16, "bold"), bg="#2e2e2e", fg="#ffffff")
        instructions_label.pack(pady=10)

        instructions_text = tk.Text(instructions_window, wrap="word", bg="#4e4e4e", fg="#ffffff", font=("Helvetica", 12), bd=0)
        instructions_text.pack(expand=True, fill="both", padx=20, pady=10)

        # Insert instructions into the Text widget
        for line in instructions:
            instructions_text.insert("end", f"{line}\n\n")
        instructions_text.config(state="disabled")  # Make the text box read-only

    def show_formulas(self):
        """Display a list of mathematical formulas in a new window."""
        formulas = [
            "Area of a circle: A = πr²",
            "Pythagorean theorem: a² + b² = c²",
            "Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a",
            "Slope formula: m = (y₂ - y₁) / (x₂ - x₁)",
            "Simple interest: SI = P * R * T / 100",
        ]

        formulas_window = tk.Toplevel(self.root)
        formulas_window.title("Mathematical Formulas")
        formulas_window.geometry("400x300")
        formulas_window.configure(bg="#2e2e2e")

        formula_label = tk.Label(formulas_window, text="Mathematical Formulas", font=("Helvetica", 16, "bold"), bg="#2e2e2e", fg="#ffffff")
        formula_label.pack(pady=10)

        formula_text = tk.Text(formulas_window, wrap="word", bg="#4e4e4e", fg="#ffffff", font=("Helvetica", 12), bd=0)
        formula_text.pack(expand=True, fill="both", padx=20, pady=10)

        # Insert formulas into the Text widget
        for formula in formulas:
            formula_text.insert("end", f"{formula}\n\n")
        formula_text.config(state="disabled")  # Make the text box read-only

def create_gui(calculate_callback):
    """Create and return the Tkinter GUI application."""
    root = tk.Tk()
    gui = CalculatorGUI(root, calculate_callback)
    return root, gui

# Example usage
if __name__ == "__main__":
    def dummy_calculate():
        # Placeholder for the calculation function
        print("Calculating...")

    app, gui = create_gui(dummy_calculate)
    app.mainloop()

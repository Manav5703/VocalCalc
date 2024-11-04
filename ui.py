import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ToolTip:
    """Tooltip class to display messages on hover."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        """Display the tooltip."""
        if self.tooltip_window is not None:
            return  # Tooltip already visible

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20

        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip_window, text=self.text, background="lightyellow", borderwidth=1, relief="solid")
        label.pack()

    def hide_tooltip(self, event=None):
        """Hide the tooltip."""
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


class CalculatorGUI:
    def __init__(self, root, calculate_callback):
        self.root = root
        self.root.title("Voice-Activated Calculator")
        self.root.geometry("600x500")  # Adjusted size for the whole window

        # Dark theme setup
        self.root.configure(bg="#2e2e2e")

        # Top bar frame for "I", "Formulas", and "History" buttons
        top_frame = tk.Frame(root, bg="#2e2e2e")
        top_frame.pack(fill="x", pady=5, anchor="w")

        # Load images for buttons
        self.formulas_image = ImageTk.PhotoImage(Image.open("formula.png").resize((24, 24)))
        self.instructions_image = ImageTk.PhotoImage(Image.open("info.png").resize((24, 24)))
        self.history_image = ImageTk.PhotoImage(Image.open("history.png").resize((24, 24)))
        self.scientific_image = ImageTk.PhotoImage(Image.open("science.png").resize((24, 24)))
        

        # Buttons for Instructions, Formulas, and History with icons
        formulas_button = tk.Button(
            top_frame, image=self.formulas_image, command=lambda: self.toggle_info("formulas"),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        formulas_button.pack(side="left", padx=10)
        ToolTip(formulas_button, "View mathematical formulas")

        instruction_button = tk.Button(
            top_frame, image=self.instructions_image, command=lambda: self.toggle_info("instructions"),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        instruction_button.pack(side="right", padx=10)
        ToolTip(instruction_button, "View instructions for using the calculator")

        # History button
        history_button = tk.Button(
            top_frame, image=self.history_image, command=lambda: self.toggle_info("history"),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        history_button.pack(side="left", padx=10)
        ToolTip(history_button, "View calculation history")
        
        scientific_button = tk.Button(
            top_frame, image=self.scientific_image, command=lambda: self.toggle_info("scientific"),
            bg="#2e2e2e", fg="#ffffff", activebackground="#505050", bd=0
        )
        scientific_button.pack(side="left", padx=10)
        ToolTip(scientific_button, "View scientific functions")

        # Result display area
        self.result_canvas = tk.Canvas(root, bg="#4e4e4e", highlightthickness=0)
        self.result_canvas.pack(pady=20, fill=tk.X)  # Allow it to fill horizontally

        self.result_label = ttk.Label(
            self.result_canvas, text="Result", anchor="center", font=("Helvetica", 24), background="#4e4e4e", foreground="#ffffff"
        )
        self.result_label.pack(expand=True)  # Allow label to expand within canvas

        # Mic icon button
        mic_image = Image.open("mic_icon.png")
        mic_image = mic_image.resize((50, 50), Image.ANTIALIAS)
        mic_photo = ImageTk.PhotoImage(mic_image)

        self.mic_button = tk.Button(
            root, image=mic_photo, command=calculate_callback, bg="#2e2e2e", activebackground="#505050", bd=0
        )
        self.mic_button.image = mic_photo
        self.mic_button.pack(pady=20, ipadx=10, ipady=10)

        # Frame to hold the content display
        self.content_frame = tk.Frame(root, bg="#4e4e4e")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Initialize history list
        self.history = []

    def update_result(self, text):
        """Update the result label with calculation result and adjust size."""
        self.result_label.config(text=text)
        self.adjust_result_box_size(text)

    def adjust_result_box_size(self, text):
        """Adjust the size of the result box based on the text length."""
        # Calculate width based on the length of the text
        lines = text.splitlines()
        max_length = max(len(line) for line in lines)  # Get the longest line length
        text_width = max_length * 12  # Approximate width (adjust multiplier as needed)

        # Update the canvas width to fit the text
        self.result_canvas.config(width=max(450, text_width + 20))  # Add padding

    def toggle_info(self, content_type):
        """Show or hide the info panel with the given content type (instructions, formulas, or history)."""
        # Clear the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if content_type == "instructions":
            instructions = [
                "1. Click the microphone button and speak a calculation.",
                "2. Supported commands include basic arithmetic operations\n  and scientific functions.",
                "3. Example: 'What is 5 plus 3' or 'Calculate 12 divided by 4'."
            ]
            self.create_label("Instructions", instructions)

        elif content_type == "formulas":
            formulas = [
                "Area of a circle: A = πr²",
                "Pythagorean theorem: a² + b² = c²",
                "Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a",
                "Slope formula: m = (y₂ - y₁) / (x₂ - x₁)",
                "Simple interest: SI = P * R * T / 100",
            ]
            self.create_label("Mathematical Formulas", formulas)

        elif content_type == "history":
            if self.history:
                self.create_label("Calculation History", self.history)
            else:
                self.create_label("Calculation History", ["No history available."])
                    
        elif content_type == "scientific":
            scientific_functions = [
                "sin(x): Sine of x (in degrees)",
                "cos(x): Cosine of x (in degrees)",
                "tan(x): Tangent of x (in degrees)",
                "log(x): Logarithm of x",
                "sqrt(x): Square root of x",
                "cbrt(x): Cube root of x ",
            ]
            self.create_label("Scientific Functions", scientific_functions)  # Move this line inside the block


    def create_label(self, title, items):
        """Create a label with a title and a list of items formatted nicely."""
        title_label = ttk.Label(self.content_frame, text=title, font=("Helvetica", 18, "bold"), background="#4e4e4e", foreground="#ffffff")
        title_label.pack(anchor="w", padx=10, pady=(10, 0))

        for item in items:
            item_label = ttk.Label(self.content_frame, text=f"• {item}", font=("Helvetica", 12), background="#4e4e4e", foreground="#ffffff")
            item_label.pack(anchor="w", padx=20)

    def add_to_history(self, entry):
        """Add an entry to the calculation history and update the display."""
        self.history.append(entry)
        self.toggle_info("history")  # Update the display to show the latest history

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

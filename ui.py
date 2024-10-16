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

import tkinter as tk

def create_gui(calculate_callback):
    """Create and return the main GUI window."""
    root = tk.Tk()
    root.title("Voice-Activated Calculator")

    # Create a label to display results
    result_label = tk.Label(root, text="", font=("Helvetica", 16))
    result_label.pack(pady=20)

    # Create a button to trigger voice command recognition
    calculate_button = tk.Button(root, text="Speak Command", command=calculate_callback, font=("Helvetica", 14))
    calculate_button.pack(pady=10)

    return root, result_label  # Return both root and result_label

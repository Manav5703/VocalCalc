import tkinter as tk
from tkinter import ttk

def create_gui(calculate_callback):
    """Create and return the main GUI window."""
    # Create the main window
    root = tk.Tk()
    root.title("Voice-Activated Calculator")
    root.geometry("500x300")  # Set a larger window size
    root.configure(bg="#f0f0f0")  # Set a light background color

    # Create a frame for the content
    frame = ttk.Frame(root, padding=5)
    frame.pack(expand=True, fill=tk.BOTH)

    # Create a label to display results
    result_label = tk.Label(frame, text="", font=("Helvetica", 24), bg="#f0f0f0")
    result_label.pack(pady=20)

    # Create a button to trigger voice command recognition
    calculate_button = ttk.Button(frame, text="Speak Command", command=calculate_callback)
    calculate_button.pack(pady=10)

    # Customize the button's style
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 16), padding=10)
    
    # Add an info label
    info_label = tk.Label(frame, text="Press the button and speak your command.", font=("Helvetica", 12), bg="#f0f0f0")
    info_label.pack(pady=10)

    # Add a quit button
    quit_button = ttk.Button(frame, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    return root, result_label

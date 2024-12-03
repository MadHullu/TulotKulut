import tkinter as tk

# Function to handle button click events
def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)  # Evaluates the expression entered by the user
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        entry.insert(tk.END, button_text)  # Add the button text to the entry field

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Create an Entry widget (where the user can see and type the expression)
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, 
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()

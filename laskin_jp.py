import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def create_calculator():
    root = tk.Tk()
    root.title("Basic Calculator")
    center_window(root, 600, 250)

    global entry
    entry = tk.Entry(root, width=35, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
    ]

    for (text, row, col) in buttons:
        if text == 'C':
            button = tk.Button(root, text=text, padx=20, pady=20, command=button_clear)
        elif text == '=':
            button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal)
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t))
        button.grid(row=row, column=col)

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
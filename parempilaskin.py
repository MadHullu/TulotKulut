import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Virhe", "Virheellinen lauseke")
        entry.delete(0, tk.END)

def clear_entry():
    entry.delete(0, tk.END)

def append_to_entry(value):
    entry.insert(tk.END, value)

def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Virhe", "Virheellinen syöte neliöjuurelle")

def log():
    try:
        value = float(entry.get())
        if value > 0:
            result = math.log10(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            messagebox.showerror("Virhe", "Logaritmi vaatii positiivisen luvun")
    except Exception:
        messagebox.showerror("Virhe", "Virheellinen syöte logaritmille")

def trig_function(func):
    try:
        angle = float(entry.get())
        radians = math.radians(angle)
        if func == "sin":
            result = math.sin(radians)
        elif func == "cos":
            result = math.cos(radians)
        elif func == "tan":
            result = math.tan(radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Virhe", f"Virheellinen syöte funktiolle {func}")

root = tk.Tk()
root.title("Toiminnallinen Laskin")

entry = tk.Entry(root, width=30, font=("Arial", 16), bd=8, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('Tyhjennä', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 11),
                       command=lambda t=text: append_to_entry(t) if t != 'Tyhjennä' else clear_entry())
    button.grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), bg="lightblue",
          command=calculate).grid(row=5, column=3, padx=5, pady=5)

tk.Button(root, text="neliöjuuri", width=8, height=2, font=("Arial", 14), bg="lightgreen",
          command=sqrt).grid(row=5, column=0, padx=5, pady=5)

tk.Button(root, text="log", width=5, height=2, font=("Arial", 14), bg="lightgreen",
          command=log).grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="sin", width=5, height=2, font=("Arial", 14), bg="lightyellow",
          command=lambda: trig_function("sin")).grid(row=6, column=0, padx=5, pady=5)

tk.Button(root, text="cos", width=5, height=2, font=("Arial", 14), bg="lightyellow",
          command=lambda: trig_function("cos")).grid(row=6, column=1, padx=5, pady=5)

tk.Button(root, text="tan", width=5, height=2, font=("Arial", 14), bg="lightyellow",
          command=lambda: trig_function("tan")).grid(row=6, column=2, padx=5, pady=5)

root.mainloop()

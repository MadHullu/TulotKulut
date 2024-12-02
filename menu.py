import tkinter as tk
import subprocess

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def start_kirjanpito():
    subprocess.Popen(['python', 'TulotMenot.py'])

def start_laskin():
    subprocess.Popen(['python', 'laskin_jp.py'])

def start_salasanat():
    subprocess.Popen(['python', 'teesalat.py'])

def create_main_window():
    root = tk.Tk()
    root.title("Application Menu")
    center_window(root, 600, 250)

    frame = tk.Frame(root)
    frame.pack(expand=True)

    kirjanpito_button = tk.Button(frame, text="Kirjanpito", command=start_kirjanpito)
    kirjanpito_button.pack(pady=10)

    laskin_button = tk.Button(frame, text="Laskin", command=start_laskin)
    laskin_button.pack(pady=10)

    salasanat_button = tk.Button(frame, text="Salasanat", command=start_salasanat)
    salasanat_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
import tkinter as tk
from tkinter import messagebox
import importlib

def tuo_tulotmenot():
    TulotMenot = importlib.import_module('TulotMenot')
    TulotMenot.main()

def main():
    # Luo pääikkuna
    root = tk.Tk()
    root.title("Tulot ja Menot")

    # Lisää käyttöliittymäelementtejä
    aloi = tk.Label(root, text="Tervetuloa Tulot ja Menot -ohjelmaan!")
    aloi.pack()

    # Lisää tekstilaatikko
    tekstilaatikko = tk.Text(root, width=40, height=10)
    tekstilaatikko.pack()

    # Lisää TulotMenot-moduulin tuomispainike
    tulotmenot_painike = tk.Button(root, text="Tuo TulotMenot", command=tuo_tulotmenot)
    tulotmenot_painike.pack()

    # Lisää sulkupainike
    #sulje_painike = tk.Button(root, text="Sulje", command=root.quit)
    #sulje_painike.pack()

    # Käynnistä pääsilmukka
    root.mainloop()

if __name__ == "__main__":
    main()
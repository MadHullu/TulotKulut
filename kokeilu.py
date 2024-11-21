import tkinter as tk
from tkinter import messagebox
import TulotMenot  # Tuo TulotMenot-moduuli

def avaa_tulotmenot_ikkuna():
    TulotMenot.main()

def main():
    # Luo pääikkuna
    root = tk.Tk()
    root.title("Kokeilu")

    # Lisää käyttöliittymäelementtejä
    aloi = tk.Label(root, text="Tervetuloa Kokeilu-ohjelmaan!")
    aloi.pack()

    # Lisää tekstilaatikko
    tekstilaatikko = tk.Text(root, width=40, height=10)
    tekstilaatikko.pack()

    # Lisää TulotMenot-ikkunan avaamispainike
    tulotmenot_painike = tk.Button(root, text="Avaa TulotMenot", command=avaa_tulotmenot_ikkuna)
    tulotmenot_painike.pack()

    # Lisää sulkupainike
    sulje_painike = tk.Button(root, text="Sulje", command=root.quit)
    sulje_painike.pack()

    # Käynnistä pääsilmukka
    root.mainloop()

if __name__ == "__main__":
    main()
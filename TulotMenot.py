import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, scrolledtext
from datetime import datetime
import sqlite3
import TallennusLataus
import LisaaPoista

def poista_tyhjat_rivit(teksti_kentta):
    rivit = teksti_kentta.get("1.0", tk.END).splitlines()
    teksti_kentta.delete("1.0", tk.END)
    for rivi in rivit:
        if rivi.strip():
            teksti_kentta.insert(tk.END, rivi + "\n")

def paivita_summa_tekstit(*args):
    try:
        tulot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in tulot_text.get("1.0", tk.END).splitlines() if line.strip())
        menot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in menot_text.get("1.0", tk.END).splitlines() if line.strip())
        tulot_menot_arvo = tulot_sum + menot_sum  # Korjattu laskemaan tulot ja menot yhteen oikein

        tulot_sum_text.set(f"{tulot_sum:.2f}".replace('.', ',') + "€")
        menot_sum_text.set(f"{menot_sum:.2f}".replace('.', ',') + "€")
        tulot_menot_text.set(f"{tulot_menot_arvo:.2f}".replace('.', ',') + "€")
    except ValueError:
        messagebox.showerror("Virhe", "Syötetyt arvot eivät ole kelvollisia numeroita.")

def lataa_tiedot():
    TallennusLataus.lataa_tiedot(tulot_text, menot_text, tavoite_text)
    paivita_summa_tekstit()

def tallenna_tiedot():
    TallennusLataus.tallenna_tiedot(tulot_text, menot_text, tavoite_text)

def kysy_tietokanta():
    vastaus = messagebox.askyesno("Tietokanta", "Haluatko ladata olemassa olevan tietokannan?")
    if vastaus:
        tiedosto = filedialog.askopenfilename(title="Valitse tietokanta", filetypes=(("SQLite files", "*.db"), ("All files", "*.*")))
        if tiedosto:
            return tiedosto
    else:
        return "tumeti.db"

def main():
    global tietokanta, tulot_text, menot_text, tulot_menot_text, tulot_sum_text, menot_sum_text, tavoite_text, tavoite_ero_text

    tietokanta = kysy_tietokanta()

    # Yhdistä SQLite-tietokantaan (tai luo se, jos sitä ei ole)
    conn = sqlite3.connect(tietokanta)

    # Luo kursori tietokannan käsittelemiseksi
    cursor = conn.cursor()

    # Luo taulu, jos sitä ei ole
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tulotmenot (
        id INTEGER PRIMARY KEY,
        tulo REAL,
        menot REAL,
        tulo_menot REAL,
        tavoite REAL,
        pvm TEXT,
        nimi TEXT
    )
    ''')

    # Tallenna muutokset ja sulje yhteys
    conn.commit()
    conn.close()

    root = tk.Tk()
    root.title("Tulot ja Menot")
    root.config(bg="lightblue")  # Aseta ikkunan taustaväriksi vaaleansininen

    # Luo valikkopalkki
    menubar = tk.Menu(root, font=("Helvetica", 14))

    # Luo alasvetovalikko
    menu = tk.Menu(menubar, tearoff=0, font=("Helvetica", 14))

    menu.add_command(label="Lataa", command=lataa_tiedot)
    menu.add_command(label="Tallenna", command=tallenna_tiedot)
    menu.add_command(label="Ohje", command=lambda: messagebox.showinfo("Ohje", "Ohje toiminto valittu"))

    # Lisää alasvetovalikko valikkopalkkiin
    menubar.add_cascade(label="...", menu=menu)

    # Aseta valikkopalkki ikkunaan
    root.config(menu=menubar)

    # Luo kehys tekstilaatikoille
    frame = tk.Frame(root, bg="lightblue")  # Aseta kehyksen taustaväriksi vaaleansininen
    frame.pack(pady=10, padx=10)

    # Luo otsikot
    tulot_label = tk.Label(frame, text="Tulot", bg="lightblue")
    tulot_label.grid(row=0, column=0, padx=40, pady=5)

    menot_label = tk.Label(frame, text="Menot", bg="lightblue")
    menot_label.grid(row=0, column=1, padx=40, pady=5)

    tulot_menot_label = tk.Label(frame, text="Tulot-Menot", bg="lightblue")
    tulot_menot_label.grid(row=0, column=2, padx=40, pady=5)

    # Luo tekstilaatikot
    tulot_text = scrolledtext.ScrolledText(frame, height=10, width=50, bg="white", state="normal")
    tulot_text.grid(row=1, column=0, padx=40, pady=5)

    menot_text = tk.Text(frame, height=10, width=50, bg="white", state="normal")
    menot_text.grid(row=1, column=1, padx=40, pady=5)

    tulot_menot_text = tk.StringVar()
    tulot_menot_label = tk.Label(frame, textvariable=tulot_menot_text, bg="white", width=20)
    tulot_menot_label.grid(row=1, column=2, padx=40, pady=5)
    tulot_menot_text.set("0,00€")

    # Luo yhteensä tekstikentät
    tulot_sum_label = tk.Label(frame, text="Yhteensä Tulot", bg="lightblue")
    tulot_sum_label.grid(row=2, column=0, padx=40, pady=5)

    menot_sum_label = tk.Label(frame, text="Yhteensä Menot", bg="lightblue")
    menot_sum_label.grid(row=2, column=1, padx=40, pady=5)

    tulot_sum_text = tk.StringVar()
    tulot_sum_entry = tk.Label(frame, textvariable=tulot_sum_text, bg="white", width=20)
    tulot_sum_entry.grid(row=3, column=0, padx=40, pady=5)
    tulot_sum_text.set("0,00€")

    menot_sum_text = tk.StringVar()
    menot_sum_entry = tk.Label(frame, textvariable=menot_sum_text, bg="white", width=20)
    menot_sum_entry.grid(row=3, column=1, padx=40, pady=5)
    menot_sum_text.set("0,00€")

    # Luo Tavoite-otsikko ja tekstikenttä tulot_menot-sarakkeeseen
    tavoite_label = tk.Label(frame, text="Tavoite", bg="lightblue")
    tavoite_label.grid(row=2, column=2, padx=40, pady=5)

    tavoite_text = tk.Text(frame, height=1, width=20, bg="white", state="normal")
    tavoite_text.grid(row=3, column=2, padx=40, pady=5)
    tavoite_text.config(state="normal")
    tavoite_text.insert(tk.END, "0,00€")
    tavoite_text.config(state="disabled")

    # Luo Tavoite-ero otsikko ja tekstikenttä
    tavoite_ero_label = tk.Label(frame, text="Tavoiteesta:", bg="lightblue")
    tavoite_ero_label.grid(row=5, column=2, padx=40, pady=5)

    tavoite_ero_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    tavoite_ero_text.grid(row=6, column=2, padx=40, pady=5)
    tavoite_ero_text.config(state="normal")
    tavoite_ero_text.insert(tk.END, "0,00€")
    tavoite_ero_text.config(state="disabled")

    def paivita_tavoite_ero():
        try:
            tavoite_arvo = float(tavoite_text.get("1.0", tk.END).strip().replace('€', '').replace(',', '.'))
            tulot_menot_arvo = float(tulot_menot_text.get().replace('€', '').replace(',', '.'))
            tavoite_ero = tulot_menot_arvo - tavoite_arvo
            tavoite_ero_text.config(state="normal")
            tavoite_ero_text.delete("1.0", tk.END)
            tavoite_ero_text.insert(tk.END, f"{tavoite_ero:.2f}".replace('.', ',') + "€")
            tavoite_ero_text.config(state="disabled")
        except ValueError:
            tavoite_ero_text.config(state="normal")
            tavoite_ero_text.delete("1.0", tk.END)
            tavoite_ero_text.insert(tk.END, "0,00€")
            tavoite_ero_text.config(state="disabled")

    # Luo Aseta tavoite -painike
    def aseta_tavoite():
        tavoite_arvo_str = simpledialog.askstring("Aseta tavoite", "Anna tavoitteen arvo (numeraalinen):")
        if tavoite_arvo_str is not None:
            try:
                tavoite_arvo = float(tavoite_arvo_str.replace(',', '.'))
                tavoite_text.config(state="normal")
                tavoite_text.delete("1.0", tk.END)
                tavoite_text.insert(tk.END, f"{tavoite_arvo:.2f}".replace('.', ',') + "€")
                tavoite_text.config(state="disabled")
                paivita_tavoite_ero()
            except ValueError:
                messagebox.showerror("Virhe", "Syötetty arvo ei ole kelvollinen numero.")

    aseta_tavoite_painike = tk.Button(frame, text="Aseta tavoite", command=aseta_tavoite, bg="lightblue")
    aseta_tavoite_painike.grid(row=4, column=2, padx=40, pady=5)

    # Lisää kysymys-painike
    kysymys_painike = tk.Button(frame, text="Lisää Tulo tai Meno", command=lambda: LisaaPoista.kysy_ja_lisaa_teksti(tulot_text, menot_text, tietokanta, paivita_summa_tekstit), bg="lightblue")
    kysymys_painike.grid(row=0, column=0, padx=40)

    # Lisää poista-painike
    poista_painike = tk.Button(frame, text="Poista Tulo tai Meno", command=lambda: LisaaPoista.poista_tulo_tai_meno(tulot_text, menot_text, tietokanta, paivita_summa_tekstit), bg="lightblue")
    poista_painike.grid(row=0, column=1, padx=40)

    # Lisää sulkupainike oikeaan alakulmaan
    sulje_painike = tk.Button(root, text="Sulje", command=root.destroy, bg="lightblue")
    sulje_painike.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)

    # Lisää jäljitys tekstikentille
    tulot_text.bind("<<Modified>>", lambda event: paivita_summa_tekstit())
    menot_text.bind("<<Modified>>", lambda event: paivita_summa_tekstit())

    # Käynnistä pääsilmukka 
    root.mainloop()

if __name__ == "__main__":
    main()
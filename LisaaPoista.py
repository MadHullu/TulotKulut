import tkinter as tk
from tkinter import simpledialog, messagebox
import sqlite3
from datetime import datetime

def kysy_ja_lisaa_teksti(tulot_text, menot_text, tietokanta, paivita_summa_tekstit):
    nimi = simpledialog.askstring("Syötä nimi", "Anna tulojen tai menojen nimi:")
    arvo_str = simpledialog.askstring("Syötä arvo", "Anna tulojen tai menojen(-) arvo:")
    if nimi is not None and arvo_str is not None:
        try:
            arvo = float(arvo_str.replace(',', '.'))
            arvo_str = f"{arvo:.2f}".replace('.', ',') + "€"
            paivays = datetime.now().strftime("%d.%m.")
            if arvo < 0:
                menot_text.config(state="normal")
                menot_text.insert(tk.END, f"{paivays} {nimi}: {arvo_str}\n")
                menot_text.config(state="disabled")
            else:
                tulot_text.config(state="normal")
                tulot_text.insert(tk.END, f"{paivays} {nimi}: {arvo_str}\n")
                tulot_text.config(state="disabled")
            paivita_summa_tekstit()

            # Tallenna tietokantaan
            conn = sqlite3.connect(tietokanta)
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO tulotmenot (tulo, menot, tulo_menot, pvm, nimi)
            VALUES (?, ?, ?, ?, ?)
            ''', (arvo if arvo >= 0 else 0, -arvo if arvo < 0 else 0, arvo, paivays, nimi))
            conn.commit()
            conn.close()
        except ValueError:
            messagebox.showerror("Virhe", "Syötetty arvo ei ole kelvollinen numero.")

def poista_tulo_tai_meno(tulot_text, menot_text, tietokanta, paivita_summa_tekstit):
    valinta = simpledialog.askstring("Poista", "Anna poistettavan tulojen tai menojen nimi:")
    if valinta is not None:
        tulot_rivit = tulot_text.get("1.0", tk.END).splitlines()
        menot_rivit = menot_text.get("1.0", tk.END).splitlines()
        tulot_text.config(state="normal")
        menot_text.config(state="normal")
        tulot_text.delete("1.0", tk.END)
        menot_text.delete("1.0", tk.END)
        tulot_poistettavat = [rivi for rivi in tulot_rivit if valinta in rivi]
        menot_poistettavat = [rivi for rivi in menot_rivit if valinta in rivi]
        for rivi in tulot_rivit:
            if rivi not in tulot_poistettavat:
                tulot_text.insert(tk.END, rivi + "\n")
        for rivi in menot_rivit:
            if rivi not in menot_poistettavat:
                menot_text.insert(tk.END, rivi + "\n")
        tulot_text.config(state="disabled")
        menot_text.config(state="disabled")
        paivita_summa_tekstit()

        # Poista tietokannasta
        conn = sqlite3.connect(tietokanta)
        cursor = conn.cursor()
        cursor.execute('''
        SELECT id FROM tulotmenot WHERE nimi = ? AND (tulo != 0 OR menot != 0)
        ''', (valinta,))
        rows = cursor.fetchall()
        if len(rows) > 1:
            valinta_teksti = "\n".join([f"{i+1}. ID: {row[0]}" for i, row in enumerate(rows)])
            rivinumero = simpledialog.askinteger("Poista", f"Anna poistettavan rivin numero:\n{valinta_teksti}")
            if rivinumero is not None and 1 <= rivinumero <= len(rows):
                id_poistettava = rows[rivinumero - 1][0]
                cursor.execute('''
                DELETE FROM tulotmenot WHERE id = ?
                ''', (id_poistettava,))
        elif len(rows) == 1:
            cursor.execute('''
            DELETE FROM tulotmenot WHERE id = ?
            ''', (rows[0][0],))
        conn.commit()
        conn.close()

def paivita_summa_tekstit(tulot_text, menot_text, tulot_menot_text):
    try:
        tulot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in tulot_text.get("1.0", tk.END).splitlines() if line.strip())
        menot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in menot_text.get("1.0", tk.END).splitlines() if line.strip())
        tulot_menot_arvo = tulot_sum - menot_sum

        tulot_menot_text.config(state="normal")
        tulot_menot_text.delete("1.0", tk.END)
        tulot_menot_text.insert(tk.END, f"{tulot_menot_arvo:.2f}".replace('.', ',') + "€")
        tulot_menot_text.config(state="disabled")
    except ValueError:
        messagebox.showerror("Virhe", "Syötetyt arvot eivät ole kelvollisia numeroita.")
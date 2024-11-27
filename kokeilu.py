import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    root = tk.Tk()
    root.title("Tulot ja Menot")
    root.config(bg="lightblue")  # Aseta ikkunan taustaväriksi vaaleansininen

    # Luo valikkopalkki
    menubar = tk.Menu(root, font=("Helvetica", 14))

    # Luo alasvetovalikko
    menu = tk.Menu(menubar, tearoff=0, font=("Helvetica", 14))
    menu.add_command(label="Lataa", command=lambda: messagebox.showinfo("Lataa", "Lataa toiminto valittu"))
    menu.add_command(label="Tallenna", command=lambda: messagebox.showinfo("Tallenna", "Tallenna toiminto valittu"))
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
    tulot_label.grid(row=0, column=0, padx=5, pady=5)

    menot_label = tk.Label(frame, text="Menot", bg="lightblue")
    menot_label.grid(row=0, column=1, padx=5, pady=5)

    tulot_menot_label = tk.Label(frame, text="Tulot-Menot", bg="lightblue")
    tulot_menot_label.grid(row=0, column=2, padx=5, pady=5)

    # Luo tekstilaatikot
    tulot_text = tk.Text(frame, height=10, width=20, bg="white", state="disabled")
    tulot_text.grid(row=1, column=0, padx=5, pady=5)

    menot_text = tk.Text(frame, height=10, width=20, bg="white", state="disabled")
    menot_text.grid(row=1, column=1, padx=5, pady=5)

    tulot_menot_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    tulot_menot_text.grid(row=1, column=2, padx=5, pady=5)
    tulot_menot_text.config(state="normal")
    tulot_menot_text.insert(tk.END, "0,00€")
    tulot_menot_text.config(state="disabled")

    # Luo yhteensä tekstikentät
    tulot_sum_label = tk.Label(frame, text="Yhteensä Tulot", bg="lightblue")
    tulot_sum_label.grid(row=2, column=0, padx=5, pady=5)

    menot_sum_label = tk.Label(frame, text="Yhteensä Menot", bg="lightblue")
    menot_sum_label.grid(row=2, column=1, padx=5, pady=5)

    tulot_sum_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    tulot_sum_text.grid(row=3, column=0, padx=5, pady=5)
    tulot_sum_text.config(state="normal")
    tulot_sum_text.insert(tk.END, "0,00€")
    tulot_sum_text.config(state="disabled")

    menot_sum_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    menot_sum_text.grid(row=3, column=1, padx=5, pady=5)
    menot_sum_text.config(state="normal")
    menot_sum_text.insert(tk.END, "0,00€")
    menot_sum_text.config(state="disabled")

    # Luo Tavoite-otsikko ja tekstikenttä tulot_menot-sarakkeeseen
    tavoite_label = tk.Label(frame, text="Tavoite", bg="lightblue")
    tavoite_label.grid(row=2, column=2, padx=5, pady=5)

    tavoite_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    tavoite_text.grid(row=3, column=2, padx=5, pady=5)
    tavoite_text.config(state="normal")
    tavoite_text.insert(tk.END, "0,00€")
    tavoite_text.config(state="disabled")

    # Luo Tavoite-ero otsikko ja tekstikenttä
    tavoite_ero_label = tk.Label(frame, text="Tavoiteesta:", bg="lightblue")
    tavoite_ero_label.grid(row=5, column=2, padx=5, pady=5)

    tavoite_ero_text = tk.Text(frame, height=1, width=20, bg="white", state="disabled")
    tavoite_ero_text.grid(row=6, column=2, padx=5, pady=5)
    tavoite_ero_text.config(state="normal")
    tavoite_ero_text.insert(tk.END, "0,00€")
    tavoite_ero_text.config(state="disabled")

    def paivita_tavoite_ero():
        try:
            tavoite_arvo = float(tavoite_text.get("1.0", tk.END).strip().replace('€', '').replace(',', '.'))
            tulot_menot_arvo = float(tulot_menot_text.get("1.0", tk.END).strip().replace('€', '').replace(',', '.'))
            tavoite_ero = tavoite_arvo - tulot_menot_arvo
            tavoite_ero_text.config(state="normal")
            tavoite_ero_text.delete(1.0, tk.END)
            tavoite_ero_text.insert(tk.END, f"{tavoite_ero:.2f}".replace('.', ',') + "€")
            tavoite_ero_text.config(state="disabled")
        except ValueError:
            tavoite_ero_text.config(state="normal")
            tavoite_ero_text.delete(1.0, tk.END)
            tavoite_ero_text.insert(tk.END, "0,00€")
            tavoite_ero_text.config(state="disabled")

    # Luo Aseta tavoite -painike
    def aseta_tavoite():
        tavoite_arvo_str = simpledialog.askstring("Aseta tavoite", "Anna tavoitteen arvo (numeraalinen):")
        if tavoite_arvo_str is not None:
            try:
                tavoite_arvo = float(tavoite_arvo_str.replace(',', '.'))
                tavoite_text.config(state="normal")
                tavoite_text.delete(1.0, tk.END)
                tavoite_text.insert(tk.END, f"{tavoite_arvo:.2f}".replace('.', ',') + "€")
                tavoite_text.config(state="disabled")
                paivita_tavoite_ero()
            except ValueError:
                messagebox.showerror("Virhe", "Syötetty arvo ei ole kelvollinen numero.")

    aseta_tavoite_painike = tk.Button(frame, text="Aseta tavoite", command=aseta_tavoite, bg="lightblue")
    aseta_tavoite_painike.grid(row=4, column=2, padx=5, pady=5)

    # Funktio, joka kysyy käyttäjältä tulojen tai menojen nimen ja arvon ja lisää ne tekstikenttään
    def kysy_ja_lisaa_teksti():
        nimi = simpledialog.askstring("Syötä nimi", "Anna tulojen tai menojen nimi:")
        if nimi:
            root.after(1, lambda: root.focus_force())
            root.after(1, lambda: root.focus_get().focus_set())
        arvo_str = simpledialog.askstring("Syötä arvo", "Anna tulojen tai menojen(-) arvo:")
        if arvo_str:
            root.after(1, lambda: root.focus_force())
            root.after(1, lambda: root.focus_get().focus_set())
        if nimi is not None and arvo_str is not None:
            try:
                arvo = float(arvo_str.replace(',', '.'))
                arvo_str = f"{arvo:.2f}".replace('.', ',') + "€"
                if arvo < 0:
                    menot_text.config(state="normal")
                    menot_text.insert(tk.END, f"{nimi}: {arvo_str}\n")
                    menot_text.config(state="disabled")
                else:
                    tulot_text.config(state="normal")
                    tulot_text.insert(tk.END, f"{nimi}: {arvo_str}\n")
                    tulot_text.config(state="disabled")
                try:
                    tulot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in tulot_text.get("1.0", tk.END).splitlines() if line.strip())
                    menot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in menot_text.get("1.0", tk.END).splitlines() if line.strip())
                    tulot_menot_text.config(state="normal")
                    tulot_menot_text.delete(1.0, tk.END)
                    tulot_menot_text.insert(tk.END, f"{tulot_sum + menot_sum:.2f}".replace('.', ',') + "€")
                    tulot_menot_text.config(state="disabled")
                    tulot_sum_text.config(state="normal")
                    tulot_sum_text.delete(1.0, tk.END)
                    tulot_sum_text.insert(tk.END, f"{tulot_sum:.2f}".replace('.', ',') + "€")
                    tulot_sum_text.config(state="disabled")
                    menot_sum_text.config(state="normal")
                    menot_sum_text.delete(1.0, tk.END)
                    menot_sum_text.insert(tk.END, f"{menot_sum:.2f}".replace('.', ',') + "€")
                    menot_sum_text.config(state="disabled")
                    paivita_tavoite_ero()
                except ValueError:
                    messagebox.showerror("Virhe", "Syötetyt arvot eivät ole kelvollisia numeroita.")
            except ValueError:
                messagebox.showerror("Virhe", "Syötetty arvo ei ole kelvollinen numero.")

    # Funktio, joka poistaa valitun tulon tai menon
    def poista_tulo_tai_meno():
        valinta = simpledialog.askstring("Poista", "Anna poistettavan tulojen tai menojen nimi:")
        if valinta:
            root.after(1, lambda: root.focus_force())
            root.after(1, lambda: root.focus_get().focus_set())
        if valinta:
            tulot_rivit = tulot_text.get("1.0", tk.END).splitlines()
            menot_rivit = menot_text.get("1.0", tk.END).splitlines()
            tulot_text.config(state="normal")
            menot_text.config(state="normal")
            tulot_text.delete("1.0", tk.END)
            menot_text.delete("1.0", tk.END)
            tulot_poistettavat = [rivi for rivi in tulot_rivit if rivi.startswith(valinta)]
            menot_poistettavat = [rivi for rivi in menot_rivit if rivi.startswith(valinta)]
            if len(tulot_poistettavat) > 1 or len(menot_poistettavat) > 1:
                valinta_teksti = "\n".join([f"{i+1}. {rivi}" for i, rivi in enumerate(tulot_poistettavat + menot_poistettavat)])
                rivinumero = simpledialog.askinteger("Poista", f"Anna poistettavan rivin numero:\n{valinta_teksti}")
                if rivinumero is not None:
                    root.after(1, lambda: root.focus_force())
                    root.after(1, lambda: root.focus_get().focus_set())
                    if rivinumero <= len(tulot_poistettavat):
                        tulot_poistettavat.pop(rivinumero - 1)
                    elif rivinumero <= len(tulot_poistettavat) + len(menot_poistettavat):
                        menot_poistettavat.pop(rivinumero - len(tulot_poistettavat) - 1)
            for rivi in tulot_rivit:
                if rivi not in tulot_poistettavat:
                    tulot_text.insert(tk.END, rivi + "\n")
            for rivi in menot_rivit:
                if rivi not in menot_poistettavat:
                    menot_text.insert(tk.END, rivi + "\n")
            try:
                tulot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in tulot_text.get("1.0", tk.END).splitlines() if line.strip())
                menot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in menot_text.get("1.0", tk.END).splitlines() if line.strip())
                tulot_menot_text.config(state="normal")
                tulot_menot_text.delete(1.0, tk.END)
                tulot_menot_text.insert(tk.END, f"{tulot_sum + menot_sum:.2f}".replace('.', ',') + "€")
                tulot_menot_text.config(state="disabled")
                tulot_sum_text.config(state="normal")
                tulot_sum_text.delete(1.0, tk.END)
                tulot_sum_text.insert(tk.END, f"{tulot_sum:.2f}".replace('.', ',') + "€")
                tulot_sum_text.config(state="disabled")
                menot_sum_text.config(state="normal")
                menot_sum_text.delete(1.0, tk.END)
                menot_sum_text.insert(tk.END, f"{menot_sum:.2f}".replace('.', ',') + "€")
                menot_sum_text.config(state="disabled")
                paivita_tavoite_ero()
            except ValueError:
                messagebox.showerror("Virhe", "Syötetyt arvot eivät ole kelvollisia numeroita.")
            tulot_text.config(state="disabled")
            menot_text.config(state="disabled")

    # Luo kehys painikkeille
    button_frame = tk.Frame(root, bg="lightblue")
    button_frame.pack(pady=10)

    # Lisää kysymys-painike
    kysymys_painike = tk.Button(button_frame, text="Lisää Tulo tai Meno", command=kysy_ja_lisaa_teksti, bg="lightblue")
    kysymys_painike.grid(row=0, column=0, padx=5)

    # Lisää poista-painike
    poista_painike = tk.Button(button_frame, text="Poista Tulo tai Meno", command=poista_tulo_tai_meno, bg="lightblue")
    poista_painike.grid(row=0, column=1, padx=5)

    # Lisää sulkupainike oikeaan alakulmaan
    sulje_painike = tk.Button(root, text="Sulje", command=root.destroy, bg="lightblue")
    sulje_painike.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)

    # Käynnistä pääsilmukka 
    root.mainloop()

if __name__ == "__main__":
    main()
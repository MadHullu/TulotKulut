import tkinter as tk
from tkinter import simpledialog, messagebox

#jos painetaan cancel, niin lisää if lauseke, joka tarkistaa onko nimi ja arvo None, jos on niin ei tee mitään
#Etsi virhe, mikä aiheuttaa pääohjelman lopettamisen, kun tämä ohjelma suljetaan


def main():
    root = tk.Tk()
    root.title("Tulot ja Menot")

    # Luo kehys tekstilaatikoille
    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10)

    # Luo otsikot
    tulot_label = tk.Label(frame, text="Tulot")
    tulot_label.grid(row=0, column=0, padx=5, pady=5)

    menot_label = tk.Label(frame, text="Menot")
    menot_label.grid(row=0, column=1, padx=5, pady=5)

    tulot_menot_label = tk.Label(frame, text="Tulot-Menot")
    tulot_menot_label.grid(row=0, column=2, padx=5, pady=5)

    # Luo tekstilaatikot
    tulot_text = tk.Text(frame, height=10, width=20)
    tulot_text.grid(row=1, column=0, padx=5, pady=5)

    menot_text = tk.Text(frame, height=10, width=20)
    menot_text.grid(row=1, column=1, padx=5, pady=5)

    tulot_menot_text = tk.Text(frame, height=1, width=20)
    tulot_menot_text.grid(row=1, column=2, padx=5, pady=5)

    # Luo yhteensä tekstikentät
    tulot_sum_label = tk.Label(frame, text="Yhteensä Tulot")
    tulot_sum_label.grid(row=2, column=0, padx=5, pady=5)

    menot_sum_label = tk.Label(frame, text="Yhteensä Menot")
    menot_sum_label.grid(row=2, column=1, padx=5, pady=5)

    tulot_sum_text = tk.Text(frame, height=1, width=20)
    tulot_sum_text.grid(row=3, column=0, padx=5, pady=5)

    menot_sum_text = tk.Text(frame, height=1, width=20)
    menot_sum_text.grid(row=3, column=1, padx=5, pady=5)

    # Funktio, joka kysyy käyttäjältä tulojen tai menojen nimen ja arvon ja lisää ne tekstikenttään
    def kysy_ja_lisaa_teksti():
        nimi = simpledialog.askstring("Syötä nimi", "Anna tulojen tai menojen nimi:")
        arvo_str = simpledialog.askstring("Syötä arvo", "Anna tulojen tai menojen arvo (menot miinus merkillä):")
        if nimi is not None and arvo_str is not None:
            try:
                arvo = float(arvo_str.replace(',', '.'))
                arvo_str = f"{arvo:.2f}".replace('.', ',') + "€"
                if arvo < 0:
                    menot_text.insert(tk.END, f"{nimi}: {arvo_str}\n")
                else:
                    tulot_text.insert(tk.END, f"{nimi}: {arvo_str}\n")
                try:
                    tulot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in tulot_text.get("1.0", tk.END).splitlines() if line.strip())
                    menot_sum = sum(float(line.split(": ")[1].replace('€', '').replace(',', '.')) for line in menot_text.get("1.0", tk.END).splitlines() if line.strip())
                    tulot_menot_text.delete(1.0, tk.END)
                    tulot_menot_text.insert(tk.END, f"{tulot_sum + menot_sum:.2f}".replace('.', ',') + "€")
                    tulot_sum_text.delete(1.0, tk.END)
                    tulot_sum_text.insert(tk.END, f"{tulot_sum:.2f}".replace('.', ',') + "€")
                    menot_sum_text.delete(1.0, tk.END)
                    menot_sum_text.insert(tk.END, f"{menot_sum:.2f}".replace('.', ',') + "€")
                except ValueError:
                    messagebox.showerror("Virhe", "Syötetyt arvot eivät ole kelvollisia numeroita.")
            except ValueError:
                messagebox.showerror("Virhe", "Syötetty arvo ei ole kelvollinen numero.")

    # Lisää kysymys-painike
    kysymys_painike = tk.Button(root, text="Lisää tuloja tai menoja", command=kysy_ja_lisaa_teksti)
    kysymys_painike.pack()

    # Lisää sulkupainike
    sulje_painike = tk.Button(root, text="Sulje", command=root.destroy)
    sulje_painike.pack()

    # Käynnistä pääsilmukka 
    root.mainloop()

if __name__ == "__main__":
    main()
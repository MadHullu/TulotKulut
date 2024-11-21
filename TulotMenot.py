import tkinter as tk

# Luo pääikkuna
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

# Lisää sulkupainike
sulje_painike = tk.Button(root, text="Sulje", command=root.destroy)
sulje_painike.pack()


# Käynnistä pääsilmukka 
root.mainloop()


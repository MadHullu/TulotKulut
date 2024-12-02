import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import getpass
from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt a password
def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# Decrypt a password
def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# Create a new database and user table
def create_database():
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 user_name TEXT PRIMARY KEY,
                 user_password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sites (
                 site_name TEXT,
                 site_url TEXT,
                 site_username TEXT,
                 site_password TEXT)''')
    conn.commit()
    conn.close()
    
# Generate a strong password
def generate_strong_password():
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    return password

# Add a new user
def add_user(user_name, user_password):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (user_name, user_password) VALUES (?, ?)", (user_name, user_password))
    conn.commit()
    conn.close()

# Add a new site
def add_site(site_name, site_url, site_username, site_password):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute("INSERT INTO sites (site_name, site_url, site_username, site_password) VALUES (?, ?, ?, ?)",
              (site_name, site_url, site_username, site_password))
    conn.commit()
    conn.close()

# List all sites
def list_sites():
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sites")
    sites = c.fetchall()
    conn.close()
    return sites

# Delete a site by name
def delete_site(site_name):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute("DELETE FROM sites WHERE site_name = ?", (site_name,))
    conn.commit()
    conn.close()

# Verify user credentials
def verify_user(user_name, input_password, key):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute("SELECT user_password FROM users WHERE user_name = ?", (user_name,))
    result = c.fetchone()
    conn.close()
    if result:
        stored_encrypted_password = result[0]
        stored_password = decrypt_password(key, stored_encrypted_password)
        return stored_password == input_password
    return False


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Sites Manager")
        self.center_window(600, 250)
        
        self.key = None
        if not os.path.exists('key.key'):
            self.create_user_interface()
        else:
            self.login_interface()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_user_interface(self):
        self.clear_interface()
        tk.Label(self.root, text="Enter new user name:").pack()
        self.new_user_name = tk.Entry(self.root)
        self.new_user_name.pack()
        tk.Label(self.root, text="Enter new user password:").pack()
        self.new_user_password = tk.Entry(self.root, show="*")
        self.new_user_password.pack()
        tk.Button(self.root, text="Create User", command=self.create_user).pack()

    def login_interface(self):
        self.clear_interface()
        tk.Label(self.root, text="Enter user name:").pack()
        self.user_name = tk.Entry(self.root)
        self.user_name.pack()
        tk.Label(self.root, text="Enter user password:").pack()
        self.user_password = tk.Entry(self.root, show="*")
        self.user_password.pack()
        tk.Button(self.root, text="Login", command=self.login).pack()

    def main_interface(self):
        self.clear_interface()
        tk.Button(self.root, text="Add site info", command=self.add_site_interface).pack()
        tk.Button(self.root, text="List existing sites", command=self.list_sites_interface).pack()
        tk.Button(self.root, text="Delete site", command=self.delete_site_interface).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def clear_interface(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_user(self):
        user_name = self.new_user_name.get()
        user_password = self.new_user_password.get()
        self.key = generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)
        encrypted_password = encrypt_password(self.key, user_password)
        add_user(user_name, encrypted_password)
        messagebox.showinfo("Success", "User created successfully.")
        self.login_interface()

    def login(self):
        user_name = self.user_name.get()
        user_password = self.user_password.get()
        with open('key.key', 'rb') as key_file:
            self.key = key_file.read()
        if verify_user(user_name, user_password, self.key):
            messagebox.showinfo("Success", "Login successful.")
            self.main_interface()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def add_site_interface(self):
        self.clear_interface()
        tk.Label(self.root, text="Enter site name:").pack()
        self.site_name = tk.Entry(self.root)
        self.site_name.pack()
        tk.Label(self.root, text="Enter site URL:").pack()
        self.site_url = tk.Entry(self.root)
        self.site_url.pack()
        tk.Label(self.root, text="Enter site username:").pack()
        self.site_username = tk.Entry(self.root)
        self.site_username.pack()
        tk.Label(self.root, text="Enter site password:").pack()
        tk.Label(self.root, text="or leave password empthy to create strong password automatically").pack()
        self.site_password = tk.Entry(self.root, show="*")
        self.site_password.pack()
        tk.Button(self.root, text="Add Site", command=self.add_site).pack()
        tk.Button(self.root, text="Back", command=self.main_interface).pack()

    def add_site(self):
        site_name = self.site_name.get()
        site_url = self.site_url.get()
        site_username = self.site_username.get()
        site_password = self.site_password.get()
        if site_password == "":
            site_password = generate_strong_password()
        encrypted_username = encrypt_password(self.key, site_username)
        encrypted_password = encrypt_password(self.key, site_password)
        add_site(site_name, site_url, encrypted_username, encrypted_password)
        messagebox.showinfo("Success", f"Site added successfully with password: {site_password}")
        self.main_interface()

    def list_sites_interface(self):
        sites = list_sites()

        # Create a frame for the list of sites
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas and scrollbar for the frame
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add headers
        headers = ["Site Name", "URL", "Username", "Password"]
        for col, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, font=('bold')).grid(row=0, column=col, padx=10, pady=5)

        # Add site details
        for row, site in enumerate(sites, start=1):
            decrypted_username = decrypt_password(self.key, site[2])
            decrypted_password = decrypt_password(self.key, site[3])
            site_details = [site[0], site[1], decrypted_username, decrypted_password]
            for col, detail in enumerate(site_details):
            
                entry = tk.Entry(scrollable_frame)
            entry.insert(0, detail)
            entry.config(state='readonly')
            entry.grid(row=row, column=col, padx=10, pady=5)

        tk.Button(self.root, text="Back", command=self.main_interface).pack()
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add headers
        headers = ["Site Name", "URL", "Username", "Password"]
        for col, header in enumerate(headers):
            tk.Label(scrollable_frame, text=header, font=('bold')).grid(row=0, column=col, padx=10, pady=5)

        # Add site details
        for row, site in enumerate(sites, start=1):
            decrypted_username = decrypt_password(self.key, site[2])
            decrypted_password = decrypt_password(self.key, site[3])
            site_details = [site[0], site[1], decrypted_username, decrypted_password]
            for col, detail in enumerate(site_details):
                entry = tk.Entry(scrollable_frame)
                entry.insert(0, detail)
                entry.config(state='readonly')
                entry.grid(row=row, column=col, padx=10, pady=5)

        tk.Button(self.root, text="Back", command=self.main_interface).pack()

    def delete_site_interface(self):
        self.clear_interface()
        tk.Label(self.root, text="Enter the site name to delete:").pack()
        self.delete_site_name = tk.Entry(self.root)
        self.delete_site_name.pack()
        tk.Button(self.root, text="Delete Site", command=self.delete_site).pack()
        tk.Button(self.root, text="Back", command=self.main_interface).pack()

    def delete_site(self):
        site_name = self.delete_site_name.get()
        delete_site(site_name)
        messagebox.showinfo("Success", f"Site {site_name} deleted successfully.")
        self.main_interface()

if __name__ == "__main__":
    create_database()
    root = tk.Tk()
    app = App(root)
    root.mainloop()

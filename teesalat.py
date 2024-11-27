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

# Add a new user
def add_user(user_name, user_password):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    key = generate_key()
    encrypted_password = encrypt_password(key, user_password)
    c.execute('INSERT INTO users (user_name, user_password) VALUES (?, ?)', (user_name, encrypted_password))
    conn.commit()
    conn.close()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Verify user credentials
def verify_user(user_name, user_password):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute('SELECT user_password FROM users WHERE user_name = ?', (user_name,))
    result = c.fetchone()
    conn.close()
    if result:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        encrypted_password = result[0]
        decrypted_password = decrypt_password(key, encrypted_password)
        return decrypted_password == user_password
    return False

# Add a new site
def add_site(site_name, site_url, site_username, site_password):
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute('INSERT INTO sites (site_name, site_url, site_username, site_password) VALUES (?, ?, ?, ?)',
              (site_name, site_url, site_username, site_password))
    conn.commit()
    conn.close()

# List all sites
def list_sites():
    conn = sqlite3.connect('secure_sites.db')
    c = conn.cursor()
    c.execute('SELECT site_name, site_url, site_username, site_password FROM sites')
    sites = c.fetchall()
    conn.close()
    return sites

# Generate a strong password
def generate_strong_password():
    import string
    import random
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(16))
    return password

# Main function
def main():
    create_database()
    if not os.path.exists('key.key'):
        user_name = input('Enter new user name: ')
        user_password = getpass.getpass('Enter new user password: ')
        add_user(user_name, user_password)
        print('User created successfully.')
    else:
        user_name = input('Enter user name: ')
        user_password = getpass.getpass('Enter user password: ')
        if verify_user(user_name, user_password):
            print('Login successful.')
            while True:
                print('1. Add site info')
                print('2. List existing sites')
                print('3. Exit')
                choice = input('Enter your choice: ')
                if choice == '1':
                    site_name = input('Enter site name: ')
                    site_url = input('Enter site URL: ')
                    site_username = input('Enter site username: ')
                    site_password = generate_strong_password()
                    add_site(site_name, site_url, site_username, site_password)
                    print(f'Site added successfully with password: {site_password}')
                elif choice == '2':
                    sites = list_sites()
                    for site in sites:
                        print(f'Site Name: {site[0]}, Site URL: {site[1]}, Site Username: {site[2]}, Site Password: {site[3]}')
                elif choice == '3':
                    print('Exiting program.')
                    break
                else:
                    print('Invalid choice.')
        else:
            print('Invalid user name or password.')

if __name__ == '__main__':
    main()

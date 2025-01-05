import argparse
import random
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import hashlib

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    if length < 8 or length > 128:
        raise ValueError("Length must be between 8 and 128 characters.")
    
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character category must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def evaluate_password_security(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    return score

def check_password_pwned(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    hashes = (line.split(':') for line in response.text.splitlines())
    return any(suffix == hash_suffix for hash_suffix, count in hashes)

def generate_multiple_passwords(count, length, use_uppercase, use_digits, use_special_chars):
    return [generate_password(length, use_uppercase, use_digits, use_special_chars) for _ in range(count)]

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument('--length', type=int, default=12, help='Length of the password (8-128)')
    parser.add_argument('--no-uppercase', dest='use_uppercase', action='store_false', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', dest='use_digits', action='store_false', help='Exclude digits')
    parser.add_argument('--no-special-chars', dest='use_special_chars', action='store_false', help='Exclude special characters')
    parser.add_argument('--batch', type=int, help='Generate multiple passwords')
    parser.add_argument('--output', type=str, help='Output file to save passwords')

    args = parser.parse_args()

    if args.batch:
        passwords = generate_multiple_passwords(args.batch, args.length, args.use_uppercase, args.use_digits, args.use_special_chars)
        if args.output:
            save_passwords_to_file(passwords, args.output)
            print(f"Passwords saved to {args.output}")
        else:
            for password in passwords:
                print(password)
    else:
        password = generate_password(args.length, args.use_uppercase, args.use_digits, args.use_special_chars)
        print("Generated Password:", password)

def create_gui():
    def on_generate():
        try:
            length = int(length_var.get())
            use_uppercase = uppercase_var.get()
            use_digits = digits_var.get()
            use_special_chars = special_chars_var.get()
            password = generate_password(length, use_uppercase, use_digits, use_special_chars)
            password_entry.delete(0, tk.END)
            password_entry.insert(0, password)

            # Évaluer la sécurité du mot de passe
            score = evaluate_password_security(password)
            if score <= 2:
                security_label.config(text="Weak", fg="red")
            elif score == 3:
                security_label.config(text="Medium", fg="orange")
            else:
                security_label.config(text="Strong", fg="green")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    root = tk.Tk()
    root.title("Password Generator")

    tk.Label(root, text="Length:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    length_var = tk.StringVar(value="12")  # Spinbox pour la longueur
    tk.Spinbox(root, from_=8, to=128, textvariable=length_var, width=5).grid(row=0, column=1, padx=5, pady=5, sticky="w")

    uppercase_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, columnspan=2)

    digits_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2)

    special_chars_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).grid(row=3, column=0, columnspan=2)

    tk.Button(root, text="Generate", command=on_generate).grid(row=4, column=0, columnspan=2)

    security_label = tk.Label(root, text="Security: ", font=("Arial", 10))
    security_label.grid(row=6, column=0, columnspan=2)


    password_entry = tk.Entry(root, width=50)
    password_entry.grid(row=5, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:  # Si des arguments sont passés, utiliser la ligne de commande
        main()
    else:  # Sinon, lancer l'interface graphique
        create_gui()

# password_generator.py

import argparse
import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars, secure_mode):
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

    if secure_mode:
        while (not any(c.isupper() for c in password) or
               not any(c.isdigit() for c in password) or
               not any(c in string.punctuation for c in password)):
            password = ''.join(random.choice(character_pool) for _ in range(length))

    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument('--length', type=int, default=12, help='Length of the password (8-128)')
    parser.add_argument('--no-uppercase', action='store_false', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_false', help='Exclude digits')
    parser.add_argument('--no-special-chars', action='store_false', help='Exclude special characters')
    parser.add_argument('--secure', action='store_true', help='Enable secure password mode')

    args = parser.parse_args()

    password = generate_password(args.length, args.no_uppercase, args.no_digits, args.no_special_chars, args.secure)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()# password_generator.py
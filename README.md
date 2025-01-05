# Password Generator

A simple and secure password generator written in Python. This tool allows users to generate random passwords with customizable options, ensuring that the generated passwords meet specific security criteria.

## Features

- Generate random passwords with a configurable length (8 to 128 characters).
- Customize character inclusion:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- Secure password mode that guarantees at least one uppercase letter, one digit, and one special character.
- Command-line interface for easy configuration of options.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Reeperc/password-generator
   cd password-generator
   ```

2. Install any required libraries (if applicable):
   ```
   pip install -r requirements.txt
   ```

## Usage

To generate a password, run the following command in your terminal (it's just an exmeple):

```
python3 password_generator.py --length 16 --no-digits
```

### Command-Line Options

- `--length <length>`: Set the length of the password (default is 12).
- `--no-uppercase`: Exclude uppercase letters from the password.
- `--no-digits`: Exclude digits from the password.
- `--no-special-chars`: Exclude special characters from the password.

## Error Handling

If no character categories are selected, the program will display an error message indicating that at least one category must be included.

## Output

Generated passwords can be displayed directly in the terminal or saved to a file (e.g., `passwords.txt`).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
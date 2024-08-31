import random, string, secrets, argparse, sys, pyperclip
from typing import List, Optional

"""
A small (enhanced) utility to help  you generate passwords locally using command line, through randomly generated characters or a passphrase. This can be used offline. Passphrase generation is done through a publicly available EFF wordlist.

Location for eff wordlist: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
"""

def generate_password(length: int, n_digits: int, n_special: int) -> str:
    if n_digits + n_special > length:
        raise ValueError("The sum of digits and special characters exceeds the password length.")
    
    password = []
    password.extend(secrets.choice(string.digits) for i in range(n_digits))
    password.extend(secrets.choice(string.punctuation) for i in range(n_special))
    password.extend(secrets.choice(string.ascii_letters) for i in range(length - n_digits - n_special))
    
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def read_wordlist(filepath: str) -> List[str]:
    try:
        with open(filepath, 'r') as file:
            return [line.split()[1] for line in file]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{filepath}' not found.")
        sys.exit(1)
        
def generate_passphrase(wordlist: List[str], n_words: int, separator: str, n_digits: int, n_special: int) -> str:
    passphrase = separator.join(secrets.choice(wordlist) for i in range (n_words))
    extras = ''.join(secrets.choice(string.digits) for i in range(n_digits)) + \
             ''.join(secrets.choice(string.punctuation) for i in range(n_special))
             
    positions = sorted(secrets.randbelow(len(passphrase) + len(extras)) for i in range(len(extras)))
    for pos, char in zip(positions, extras):
        passphrase = passphrase[:pos] + char + passphrase[pos:]
        
    return passphrase

def get_user_input(prompt: str, validator=None, error_message: str = "Invalid input. Please try again."):
    while True:
        user_input = input(prompt)
        if validator is None or validator(user_input):
            return user_input
        print(error_message)
        
def interactive_mode():
    mode = get_user_input("Choose mode (password/passphrase): ",
                          lambda x: x.lower() in ["password", "passphrase"])
    
    if mode.lower() == "password":
        length = int(get_user_input("Enter password length: ", lambda x: x.isdigit() and int(x) > 0))
        n_digits = int(get_user_input("Enter number of digits: ", lambda x: x.isdigit() and int(x) >= 0))
        n_special = int(get_user_input("Enter number of special characters: ", lambda x: x.isdigit() and int(x) >= 0))
        
        try:
            password = generate_password(length, n_digits, n_special)
            print(f"Generated password: {password}")
            pyperclip.copy(password)
            print("Password copied to clipboard.")
        except ValueError as e:
            print(f"Error: {e}")
            
    else: # passphrase mode
        wordlist = read_wordlist("eff_large_wordlist.txt")
        n_words = int(get_user_input("Enter number of words: ", lambda x: x.isdigit() and int(x) > 0))
        separator = input("Enter word separator (press Enter for space): ") or " "
        n_digits = int(get_user_input("Enter number of digits: ", lambda x: x.isdigit() and int(x) >= 0)) 
        n_special = int(get_user_input("Enter number of special characters: ", lambda x: x.isdigit() and int(x) >= 0))
        
        passphrase = generate_passphrase(wordlist, n_words, separator, n_digits, n_special)
        print(f"Generated passphrase: {passphrase}")
        pyperclip.copy(passphrase)
        print("Passphrase copied to clipboard.")
        
def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords or passphrases.")
    parser.add_argument("--mode", choices=["password", "passphrase"],help="Generation mode")
    parser.add_argument("--length", type=int, help="Password length")
    parser.add_argument("--n-digits", type=int, help="Number of digits")
    parser.add_argument("--n-special", type=int, help="Number of special characters")
    parser.add_argument("--n-words", type=int, help="Number of words for passphrase")
    parser.add_argument("--separator", help="Word separator for passphrase")
    parser.add_argument("--wordlist", default="eff_large_wordlist.txt", help="Path to wordlist file")
    args = parser.parse_args()
    
    # Check if any argument other than the default wordlist is provided
    if all(value is None for key, value in vars(args).items() if key != 'wordlist'):
        interactive_mode()
    else:
        try:
            if args.mode == "password":
                if not all([args.length, args.n_digits is not None, args.n_special is not None]):
                    raise ValueError("Password mode requires --length, --n-digits, and --n-special")
                password = generate_password(args.length, args.n_digits, args.n_special)
                print(f"Generated password: {password}")
                pyperclip.copy(password)
                print("Password copied to clipboard.")
            elif args.mode == "passphrase":
                if not all([args.n_words, args.n_digits is not None, args.n_special is not None]):
                    raise ValueError("Passphrase mode requires --n-words, --n-digits, and --n-special")
                wordlist = read_wordlist(args.wordlist)
                separator = args.separator or " "
                passphrase = generate_passphrase(wordlist, args.n_words, separator, args.n_digits, args.n_special)
                print(f"Generated passphrase: {passphrase}")
                pyperclip.copy(passphrase)
                print("Passphrase copied to clipboard.")
            else:
                raise ValueError("Please specify --mode as either 'password' or 'passphrase'")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
            
if __name__ == "__main__":
    main()
    
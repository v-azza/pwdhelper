import random, string

#Location for eff wordlist: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

#function to convert the password string into list, then apply random.shuffle from random module to prevent min_digit_index and min_punctuation_index outputs from being added sequentially into the final password output
def randomize_password(password): 
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)


def generate_password_characters(n_of_digits, n_punctuation_char, n_passwords, password_length):
    char = string.ascii_letters #define the usable set of characters for password from string module
    passwords = []

    for password_index in range(n_passwords):
        password = []

        for min_digit_index in range(n_of_digits):
            password.append(random.choice(string.digits))

        for min_punctuation_index in range(n_punctuation_char):
            password.append(random.choice(string.punctuation))

        for index in range(password_length - n_of_digits - n_punctuation_char):
            password.append(random.choice(char))

        passwords.append(randomize_password(password))    

    return passwords


def create_standard_password(): #function to generate password for OPTION 1, for given user inputs
    
    n_of_digits =  int(input("How many numbers 0-9 does each of your passwords require? "))
    n_punctuation_char = int(input("How many special characters does each of your passwords require? "))
    n_passwords = int(input("How many passwords do you require? "))
    password_length = int(input("Please give the password length required: "))
    
    if n_of_digits + n_punctuation_char > password_length:
        print("Error: The sum of digits and special characters exceeds the password length.")
        return None
    else:
        passwords = generate_password_characters(n_of_digits, n_punctuation_char, n_passwords, password_length)
        for index, password in enumerate(passwords):
            print(f"Password {index + 1} generated: {password}")
        return passwords


def create_passphrase(): #function to generate passphrase for OPTION 2
    print("Passphrase function!")

# Main function to handle user choices
def main():
    
    last_generated_passwords = None 

    while True:
        print("")
        print("\n1. Create standard password")
        print("2. Create passphrase")
        print("3. Print last password(s) generated")
        print("4. Copy password(s) generated to your clipboard")
        print("5. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            last_generated_passwords = create_standard_password()
        
        elif choice == "2":
            create_passphrase()
            
        elif choice == "3":
            if last_generated_passwords:
                for index, password in enumerate(last_generated_passwords):
                    print(f"Password {index + 1} generated: {password}")
            else:
                print("No passwords generated yet.")
            
        elif choice == "4":
            print("Not built yet.")
            
        elif choice == "5":
            print("Quitting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
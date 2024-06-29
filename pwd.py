import random, string

#function to convert the password string into list, then apply random.shuffle from random module to prevent min_digit_index and min_punctuation_index outputs from being added sequentially into the final password output
def randomize_password(password): 
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

n_of_digits = 3
n_punctuation_char = 2
char = string.ascii_letters + string.digits + string.punctuation #define the usable set of characters for password from string module

n_passwords = int(input("How many passwords do you require? "))
password_length = int(input("Please give the password length required: "))

for password_index in range(n_passwords):
    password = ""

    for min_digit_index in range(n_of_digits):
        password = password + random.choice(string.digits)

    for min_punctuation_index in range(n_punctuation_char):
        password = password + random.choice(string.punctuation)

    for index in range(password_length - n_of_digits - n_punctuation_char):
        password = password + random.choice(char)

    #print("Password {} generated: {}".format(password_index, randomize_password(password))) #print the password(s)
    print(f"Password {password_index} generated: {randomize_password(password)}") #print the password(s) generated  


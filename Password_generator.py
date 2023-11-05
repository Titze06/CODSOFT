import random
import string

# Taking user input for password length
print("Desired length of the password? :")
user_input = input("")

# Setting password length
password_len = user_input

def generate_password(user_input):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    # Use random.choices to generate a random password
    for i in range(int(user_input)):
        password += random.choice(characters) 
    
    return password

# Generate and print the password
generated_password = generate_password(password_len)
print("Your Password is :", generated_password )

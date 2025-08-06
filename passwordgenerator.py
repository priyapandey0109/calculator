import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password
try:
    user_input = int(input("Enter desired password length: "))
    password = generate_password(user_input)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
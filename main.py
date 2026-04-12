import random
import string

try:
    while True:
    length = int(input("Enter password length (min 4): "))
    if length >= 4:
        break
    print("Password must be at least 4 characters long.")
    count = int(input("How many passwords to generate: "))
except ValueError:
    print("Please enter numbers only.")
    exit()

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print("Your secure password:", password)

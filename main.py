import random
import string

try:
    length = int(input("Enter password length: "))
    count = int(input("How many passwords to generate: "))
except ValueError:
    print("Please enter numbers only.")
    exit()

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print("Generated password:", password)

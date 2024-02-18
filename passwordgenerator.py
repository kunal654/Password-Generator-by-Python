import random
import string

length = int(input("Enter the length of the password: "))
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'
use_special=input("Include special character? (yes/no): ").lower() == 'yes'

characters = ''
if use_lowercase:
    characters += string.ascii_lowercase
if use_uppercase:
    characters += string.ascii_uppercase
if use_digits:
    characters += string.digits
if use_punctuation:
    characters += string.punctuation
if use_special:
    characters +=("! @ # $ % ^ & *  _")

if not characters:
    print("Please select at least one character type.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

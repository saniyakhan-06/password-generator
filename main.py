import random
import string
include_letters = input("Include letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()

length = int(input("How long your password should be? "))

chars = ""
if include_letters == 'y':
    chars += string.ascii_letters
if include_numbers == 'y':
    chars += string.digits
if include_symbols == 'y':
    chars += string.punctuation
if chars:
    password = ''.join(random.choices(chars, k=length))
    print("Your password is:", password)
else:
    print("You must select at least one character type!")

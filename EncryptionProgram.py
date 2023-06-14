import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(chars)
# print(key)

#encryption
plain_text = input("Enter a message tro encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

cipher_text = input("Enter a message tro Decrypt: ")
Decry_msg = ""

for letter in cipher_text:
    index = key.index(letter)
    Decry_msg += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {Decry_msg}")
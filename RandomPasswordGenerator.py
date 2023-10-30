import secrets
import random 
import string
while True: 
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation

  alphabet = letters + digits + special_chars

  pwd_length = int(input("Enter the password length: "))

  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  print(pwd)  
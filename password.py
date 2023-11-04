import string
import random

#function to generate random password
def  passwordGenerator(length):
    password=''
    for i in range(length):
        password+=random.choice(characters)
    print(f"The password generated is: {password}")

#storing all the characters as a single string

letters=string.ascii_letters  #storing all the ascii letters
digits=string.digits  #storing all the digits
punctuation=string.punctuation  #storing the symbols
characters=letters+digits+punctuation

length=int(input("Enter the password length:"))
if length<=0:
    print("Password should be of a valid length")
else:
    passwordGenerator(length)

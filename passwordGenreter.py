import random
import string
len = int(input("Enter password length: "))
charecter= input("you have any charecter on your password?...yes or no: ") == 'yes'
number = input("you have any digits on your password?...yes or no: ") == 'yes'
specials = input("you have any symboll on your password?...yes or no: ") == 'yes'

words = ''
if charecter:
    words += string.ascii_letters
if number:
    words += string.digits
if specials:
    words += string.punctuation
if not words:
    print("something is wrong")
else:
    password = ''.join(random.choice(words) for _ in range(len))
    print("Generated Password:", password)



import re

password = input("Enter the password: ")

if (6 <= len(password) <= 16 and 
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[$#@]", password)) :
    print("Your password is valid")
else :
    print("Your password is invalid")
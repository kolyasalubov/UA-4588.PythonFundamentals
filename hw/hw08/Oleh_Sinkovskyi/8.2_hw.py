import re

password = input("Password: ")

if ( 
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and 
    re.search(r"[$#@]", password) and 
    6 <=len(password) <= 16
):
    print("Password is valid")
else:
    print("Password is invalid")
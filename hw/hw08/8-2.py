import re 

passwd = input()
if  6 <= len(passwd) <= 16 and re.search("[a-z]",passwd) and re.search("[A-Z]",passwd) and re.search(r"\d", passwd) and re.search("[$#@]", passwd):
    print("Password is valid")
else:
    print("Password is invalid")
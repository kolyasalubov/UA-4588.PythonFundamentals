import re

password = input()  
def pass_validation(password):
        if 6 <= len(password) <= 16 and \
           re.search(r"[A-Z]", password) and \
           re.search(r"[a-z]", password) and \
           re.search(r"[0-9]", password) and \
           re.search(r"[$@#]", password):
                return "Valid password"
        else:      
                return "Invalid password"
print(pass_validation(password))   
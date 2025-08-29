import re

def check_password(password: str) -> bool:
    
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search(r"[a-z]", password):
        return False
    
    if not re.search(r"[A-Z]", password):
        return False
    
    if not re.search(r"[0-9]", password):
        return False
  
    if not re.search(r"[$#@]", password):
        return False
    
    return True

password = input("Enter your password(you need 1 small letter, 1 big letter, 1 number and 1 of this simbols: $#@): ")
if check_password(password):
    print("Password is valid!")
else:
    print("Password is invalid!")

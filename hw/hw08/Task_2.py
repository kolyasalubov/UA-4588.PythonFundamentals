### Task 2
def chek_password(password):
    import re
    if len(password) < 6:
        return False
    elif len(password) > 16:
        return False
    elif not re.search(r'[A-Z]', password):
        return False
    elif not re.search(r'[a-z]', password):
        return False
    elif not re.search(r'\d', password):
        return False
    elif not re.search(r'[$#@]', password):
        return False
    return True

password = input("Enter your password: ")

print("Your password is correct" if chek_password(password) else "Your password is incorrect")
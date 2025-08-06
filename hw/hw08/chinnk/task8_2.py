import re

def is_valid_password(password):
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

while True:
    user_input = input("Enter your password: ")

    if is_valid_password(user_input):
        print("✅ Password is valid.")
        break
    else:
        print("❌ Password is invalid. Try again.")

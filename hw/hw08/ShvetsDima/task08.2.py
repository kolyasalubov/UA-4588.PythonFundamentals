import re

password = input("Enter your password: ")

if len(password) < 6 or len(password) > 16:
    print("Invalid password: length must be between 6 and 16 characters.")
elif not re.search(r"[a-z]", password):
    print("Invalid password: must contain at least one lowercase letter.")
elif not re.search(r"[A-Z]", password):
    print("Invalid password: must contain at least one uppercase letter.")
elif not re.search(r"[0-9]", password):
    print("Invalid password: must contain at least one digit.")
elif not re.search(r"[$#@]", password):
    print("Invalid password: must contain at least one special character ($, #, @).")
else:
    print("Valid password.")
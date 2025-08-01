import re

def is_valid_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return False

    # Check for at least one special character from [$#@]
    if not re.search(r"[$#@]", password):
        return False

    # All conditions met
    return True

# Get input from the user
user_password = input("Enter your password: ")

# Validate password
if is_valid_password(user_password):
    print("Valid password!")
else:
    print("Invalid password.")

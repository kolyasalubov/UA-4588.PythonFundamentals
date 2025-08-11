import re

valid_password_condition = """
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters
"""
valid_password_change = "\nPlease change password to this recommendation:"

def valid_password(password):
    """
    Function that check valid ot not user password.
    """
    if len(password) > 16:
        print(f"Your password is too long.{valid_password_change}{valid_password_condition}")
    elif len(password) < 6:
        print(f"Your password is too short.{valid_password_change}{valid_password_condition}")
    elif not re.search(r"[A-Z]", password):
        print(f"Your password should have at least 1 uppercase letter.{valid_password_change}{valid_password_condition}")
    elif not re.search(r"[a-z]", password):
        print(f"Your password should have at least 1 lowercase letter.{valid_password_change}{valid_password_condition}")
    elif not re.search(r"\d", password):
        print(f"Your password should have at least 1 number.{valid_password_change}{valid_password_condition}")
    elif not re.search(r"[$#@]", password):
        print(f"Your password should have at least 1 of this symbol $, # or @.{valid_password_change}{valid_password_condition}")
    else:
        print("Your password is valid")
    
valid_password(input(f"Enter new password.\nIt should be:{valid_password_condition}"))
# Task 8.2
# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# import re

# user_passwd = input("Write your password: ")

# def check_password(user_password):
#     passwd_pattern = r"^(?=.*\d)(?=.*[$,#,@])(?=.*[a-z])(?=.*[A-Z]).{6,16}$"
#     if re.match(passwd_pattern, user_password):
#         return print(f"Your password is valid")

#     return print(f"Check your password")

# check_password(user_passwd)

# ---------------------------------------------------------------------------------


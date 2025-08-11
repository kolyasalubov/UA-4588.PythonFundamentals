import re

pswd = input("Please enter your password: ")

lower_letters = re.findall(r"[a-z]", pswd)
upper_letters = re.findall(r"[A-Z]", pswd)
numbers = re.findall(r"[0-9]", pswd)
special_chars = re.findall(r"[$#@]", pswd)

is_valid = lower_letters and upper_letters and numbers and special_chars and 6 <= len(pswd) <= 16

print("Your password is valid" if is_valid else "Your password is invalid :c")

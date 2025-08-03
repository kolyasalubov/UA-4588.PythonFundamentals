import re

password = input("Enter password: ")

if (6 <= len(password) <= 16 and
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[$#@]", password)):
    print("Valid password")
else:
    print("Invalid password")

# Or:

# import re

# password = input("Enter password: ")

# lowercase = re.findall(r"[a-z]", password)
# uppercase = re.findall(r"[A-Z]", password)
# digits = re.findall(r"[0-9]", password)
# special = re.findall(r"[$#@]", password)

# if (6 <= len(password) <= 16 and
#     lowercase and
#     uppercase and
#     digits and
#     special):
#     print("Valid password")
# else:
#     print("Invalid password")

import re

# def correct_password(password):
#     if len(password) < 6 or len(password) > 16:
#         return False
#     if not re.search(r'[a-z]', password):
#         return False
#     if not re.search(r'[A-Z]', password):
#         return False
#     if not re.search(r'[0-9]', password):
#         return False
#     if not re.search(r'[$#@]', password):
#         return False
#     return True

# # def correct_password(password):
# #     length_ok = 6 <= len(password) <= 16
# #     has_lower = bool(re.search(r'[a-z]', password))
# #     has_upper = bool(re.search(r'[A-Z]', password))
# #     has_digit = bool(re.search(r'[0-9]', password))
# #     has_special = bool(re.search(r'[$#@]', password))

# #     return length_ok and has_lower and has_upper and has_digit and has_special


def correct_password(password):
    if 6 <= len(password) <= 16:
        if re.search(r'[a-z]', password):
            if re.search(r'[A-Z]', password):
                if re.search(r'[0-9]', password):
                    if re.search(r'[$#@]', password):
                        return True
    return False


password = input("Enter pasword: ")

if correct_password(password):
    print("Password accepted")
else:
    print("Password rejected")

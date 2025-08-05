import re

def is_valid_password(password):

    """
        VALIDATION RULES:
        At least 1 letter between [a-z] and 1 letter between [A-Z]
        At least 1 number between [0-9]
        At least 1 character from [$#@]
        Minimum length 6 characters
        Maximum length 16     characters
    """

    if (len(password) < 6 or len(password) > 16):
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[$#@]", password): 
        return False
    return True
    
print(is_valid_password(password="Ronevych1@"))
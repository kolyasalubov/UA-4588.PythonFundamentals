import re

def validatePassword(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[$#@]', password):
        return False

    return True


######### Test ##########

# print(f'Test - "Ab1#": {validatePassword("Ab1#")}')
# print(f'Test - "1234567890123Af#gg": {validatePassword("1234567890123Af#gg")}')
# print(f'Test - "Abcdef1@a": {validatePassword("Abcdef1@a")}')
# print(f'Test - "Abcdef1@aA": {validatePassword("Abcdef1@aA")}')


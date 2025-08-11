# __________________________ Check the validity of a password _____________________

import re

def check_valid_pass(password:str) -> bool:
    '''
    Function which check the validity of a password
    '''

    len_pass = len(password)

    if len_pass < 6:
        print(f'Your password contains {len_pass} symbols, but must be longer than 6 symbols')
        return False

    elif len_pass > 16:
        print(f'Your password contains {len_pass} symbols, but must be smaller than 16 symbols')
        return False

    else:
        if not re.search(r'[a-z]', password):
            print('Your password doesn\'t contain eny char of the range letters a-z')
            return False
        
        if not re.search(r'[A-Z]', password):
            print('Your password doesn\'t contain eny char of the range letters A-Z')
            return False
        
        if  not re.search(r'\d', password):
            print('Your password doesn\'t contain eny number of the range digits 0-9')
            return False
        
        if not re.search(r'[$#@]', password):
            print('Your password doesn\'t contain eny character of those $#@')
            return False
        
        print('Your password containing all necessary parameters')
        return True 


# ------------------------------------- Tests -------------------------------------------------
def test_passwords() -> str:
    '''
    Function for test default passwords
    '''
    passwords_to_test = [
    # True passwords
    "Abc12$",
    "aB3#c9",
    "@Py78k",
    "MyPassword123@",
    "TestPass#42",
    "GeMiNi_AI$9",

    # False passwords
    "Abc1$",                    # Недостатня довжина
    "aB2#",                     # Недостатня довжина
    "ThisPasswordIsTooLong123@",# Занадто велика довжина
    "ReallyReallyLongPassword123#", # Занадто велика довжина
    "PASSWORD123$",             # Відсутня мала літера
    "AB@12345",                 # Відсутня мала літера
    "password123$",             # Відсутня велика літера
    "ab@12345",                 # Відсутня велика літера
    "Abcdefgh$",                # Відсутня цифра
    "MyPass@word",              # Відсутня цифра
    "Abcdefgh12",               # Відсутній спецсимвол
    "MyPassWord123",            # Відсутній спецсимвол
    "Abc12_",                   # Використано '_' замість '$', '#' або '@'
    "abc123",                   # Немає великої літери, немає спецсимволу
    "AbcDef",                   # Немає цифри, немає спецсимволу
    "Abcdefg@",                 # Немає цифри
    "12345678@",                # Немає малих і великих літер
    "ABCDE@FGH"                 # Немає цифри
    ]

    for test_pass in passwords_to_test:
        check_valid_pass(test_pass)
# -------------------------------------------------------------------------------------------


def enter_pass() -> str:
    inp_pass = input('Enter your password to valid or command exit to go out: ')

    if inp_pass == 'exit':
        return
    else:
        check_valid_pass(inp_pass)


# Turn check own password
enter_pass()

# Turn auto test with passwords
# test_passwords()


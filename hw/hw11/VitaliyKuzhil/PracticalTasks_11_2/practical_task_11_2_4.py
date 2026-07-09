'''
With help input obtain from user his age. Age must be natural number.

If user try input incorrect value ask him again. If user typed correct age print this value.

Do not use if in your code, but you can use already created function check_age for validation.
'''

def check_age(age):
    if age <= 0:
        raise ValueError('Incorrect age')


def input_age():
    '''
    Function which get user age
    '''
    return input()


def start():
    try:
        age = int(input_age())
        check_age(age)
    except ValueError:
        start()
    else:
        print(age)

start()

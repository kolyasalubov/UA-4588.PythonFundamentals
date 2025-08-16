'''
Write the function check_odd_even (number) whose input parameter is an integer number. The function checks whether the set number is even or odd:

in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
in the case of an odd number the function should be displayed the corresponding message - "Entered number is odd";
in the case of incorrect data the function should be displayed the message - "You entered not a number."
Note: in the function you must use the try except construct.
'''

def type_of_number(num):
    '''
    Function which check type of number
    '''
    if num % 2 == 0:
        return 'Entered number is even'
    else:
        return 'Entered number is odd'


def check_odd_even(number):
    '''
    Function which compare if number odd or even
    '''
    try:
        number = int(number)
    except ValueError:
        return 'You entered not a number.'
    else:
        return type_of_number(num=number)
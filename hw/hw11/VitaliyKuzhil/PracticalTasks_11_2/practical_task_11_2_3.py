'''
Write the function check_positive(number)whose input parameter is a number. The function checks whether the set number is positive or negative:

in the case of a positive number the function should be displayed the corresponding message - "You input positive number: input parameter of function"
in the case of a negative parameter the function should return the exception of your own class MyError and displayed the corresponding message. "You input negative number: input parameter of function. Try again."
in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
'''

class MyError(Exception):
    pass


def check_positive(number):
    try:
        number = float(number)
        if  number < 0:
            raise MyError(f'You input negative number: {float(number)}. Try again.')
        elif number == 0:
            raise MyError('Number can\'t be zero')
        
    except ValueError:
        return MyError('Error type: ValueError!')
    except MyError as exception:
        return exception
    else:
        return f'You input positive number: {number}'
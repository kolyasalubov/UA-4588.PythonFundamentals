'''
Write the function divide(numerator, denominator) the two input parameters of which are numbers. The function returns the result of dividing two numbers.

in case of correct data the function should be displayed the corresponding message – "Result is numerator / denominator"
in the case of division by zero the function should be displayed the corresponding message – "Oops, numerator / denominator, division by zero is error!!!".
in the case of incorrect data the function should be displayed the message –"Value Error! You did not enter a number!"
Note: in the function you must use the try except construct.
'''

def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return ZeroDivisionError(f'Oops, {numerator}/{denominator}, division by zero is error!!!')
    except TypeError:
        return TypeError('Value Error! You did not enter a number!')
    else:
        return f'Result is {result}'
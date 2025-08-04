# write a function that return the largest number of two numbers

def largest_number(a, b):
    '''
    Returns the largest of two numbers.
    '''
    if a > b:
        num = a
    elif b > a:
        num = b
    else:
        num = "Numbers are equal"
    return num

print(largest_number(12.7, -5))
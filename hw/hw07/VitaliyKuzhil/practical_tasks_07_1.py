# Task 1
num_1, num_2 = int(input('Enter number one: ')), int(input('Enter number two: '))

def max_num_of_two(arg_1: int = 0, arg_2:int = 0) -> int | str:
    '''
    Function which compares two numbers

    Receive:
    arg_1: int
    arg_1: int
    
    Return: int or str
    '''

    if arg_1 == arg_2:
        return 'Number one and number two are equal'
    else:
        return arg_1 if arg_1 > arg_2 else arg_2

print(f'Possessive arg: {max_num_of_two(num_1, num_2)}')
print(f'Name arg: {max_num_of_two(arg_1 = num_1, arg_2 = num_2)}')

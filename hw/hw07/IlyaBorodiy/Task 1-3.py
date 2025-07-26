###   Task 1

num_1 = input('Enter you number: ')
num_2 = input('Enter you number: ')

def my_func(a, b):
    """
    Return the largest number, from to input
    """
    if a > b:
        print(a)
    else:
        print(b)

my_func(num_1, num_2)
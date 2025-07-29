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


# Task 2
import math

user_choice = int(input('What do you want to calculate?\n 1 - rectangle, 2 - triangle, 3 - circle? '))


def area_of_rectangle(len_reg: float, width_reg: float) -> float:
    '''
    Function calculate area of rectangle

    Receive:
    len_reg: float
    width_reg: float

    Return: float
    '''
    return len_reg * width_reg


def area_of_triangle(base_tri:float, height_tri:float) -> float:
    '''
    Function calculate area of triangle

    Receive:
    base_tri: float
    height_tri: float

    Return: float
    '''
    return base_tri * height_tri / 2


def area_of_circle(radius_circ: float) -> float:
    '''
    Function calculate area of circle

    Receive:
    radius_circ: float

    Return: float
    '''
    return math.pi * math.pow(radius_circ, 2)


match user_choice:
    case 1:
        len_rectangle = float(input('Enter length of a rectangle: '))
        width_rectangle = float(input('Enter width of a rectangle: '))
        
        rectangle = area_of_rectangle(len_reg = len_rectangle, width_reg = width_rectangle)
        print(f'The area of the rectangle is: {rectangle}')

    case 2:
        base_triangle = float(input('Enter base of a triangle: '))
        height_triangle = float(input('Enter height of a triangle: '))

        triangle = area_of_triangle(base_tri = base_triangle, height_tri = height_triangle)
        print(f'The area of the triangle is: {triangle}')

    case 3:
        radius_circle = float(input('Enter radius of a circle: '))
        
        circle = area_of_circle(radius_circle)
        print(f'The area of the circle is: {round(circle, 5)} or {circle / math.pi}')

    case _:
        print('You must choice one of tre three choices. Try again!')


# Task 3
user_string = input('Enter your string: ').lower()

def count_chars(chars: str) -> dict:
    '''
    Function calculate the number of characters included in given string

    Receive: 
    chars: string

    Return: 
    result: dict
    '''
    result = {}

    for char in chars:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

print(count_chars(user_string))

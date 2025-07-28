import math

# Task 1
def get_max(a, b):
    '''
    Function that returns the largest number of two numbers
    '''
    return a if a > b else b
# print(get_max(10, 20))
# print(get_max(5.5, 2.3)) 
# print(get_max(1.2, 50)) 

#Task 2
def rectangle_area(length, width):
    '''
    Function that returns the rectangle area
    '''
    return length * width

def triangle_area(base, height):
    '''
    Function that returns the triangle area
    '''
    return 0.5 * base * height

def circle_area(radius):
    '''
    Function that returns the circle area
    '''
    return round(math.pi * radius ** 2, 2)

def main_programm():
    '''
    Function that returns the area of the user's choosen shape
    '''
    user_choice = int(input('Choose which shape do you want to calculate. \nReactagle (choose 1). \nTriangle (choose 2). \nCircle (choose 3). '))
    if user_choice == 1:
        length = float(input('add length of rectangle: '))
        width = float(input('add width of rectangle: '))
        print(f'Area of reactagle with length {length} and width {width} is: {rectangle_area(length, width)}')
    elif user_choice == 2:
        base = float(input('add base of triangle: '))
        height = float(input('add height of triangle: '))
        print(f'Area of triangle with base {base} and height {height} is: {triangle_area(base, height)}')
    elif user_choice == 3:
        radius = float(input('add radius of circle: '))
        print(f'Area of circle with radius {radius} is: {circle_area(radius)}')
    else:
        print("You didn't choose the right number. Try one more time")
        main_programm()

main_programm()

# Task 3
def count_characters(str):
    """
    Function that counts the number of occurrences of each character in a string.
    """
    str = str.lower()
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
# print(count_characters('hello'))
# print(count_characters('dictionary'))
# print(count_characters('Hello World'))
# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).

def get_largest_number(num_one, num_two):
    """
    The function returns the largest of the two given numbers.
    """

    return num_one if num_one > num_two else num_two


# Task2. Write a program that calculates the area of ​a rectangle, triangle and circle 
# (write three functions to calculate the area, and call them in the main program depending on the user's choice).

from math import pi

def get_rectangle_area():
    """
    Calculates the area of a rectangle.
    """
    a = float(input("Please enter the length of side a: "))
    b = float(input("Please enter the length of side b: "))
    return a * b

def get_triangle_area():
    """
    Calculates the area of a triangle.
    """
    base = float(input("Please enter the length of the base: "))
    h = float(input("Please enter the length of the height: "))
    return base * h * 0.5

def get_circle_area():
    """
    Calculates the area of a circle.
    """
    r = float(input("Please enter the length of the radius: "))
    return pi * r ** 2

user_shape_choice = int(input("Please input the number to calculate the area for: 1 - rectangle, 2 - triangle, 3 - circle: "))

match user_shape_choice:
    case 1:
        print(get_rectangle_area())
    case 2:
        print(get_triangle_area())
    case 3:
        print(get_circle_area())
    case _:
        print("Invalid input")


# Task3. Write a function that calculates the number of characters included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def get_string_chars_number(string: str):
    """
    Calculates the number of characters included in a given string
    """
    values = {}
    string = string.lower()
    for char in string:
        if char not in values:
            values[char] = string.count(char)
    
    return values
    

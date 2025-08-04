from math import pi, pow

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
    return pi * pow(r, 2)
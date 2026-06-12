import math

def rectangle_area() :
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length * width

def triangle_area() :
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def circle_area() :
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * math.pow(radius, 2)
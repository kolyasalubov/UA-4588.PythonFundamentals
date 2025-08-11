import math

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
    return round(math.pi * math.pow(radius, 2), 2)

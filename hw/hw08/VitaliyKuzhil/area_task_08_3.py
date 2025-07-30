import math


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

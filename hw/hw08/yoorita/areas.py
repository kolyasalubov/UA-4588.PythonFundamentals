from math import pow, pi

figures = {
    "1": {
        "name": "Triangle",
        "elements": ["height", "base"]
    },
    "2": {
        "name": "Circle",
        "elements" : ["radius"]
    },
    "3": {
        "name": "Rectangle",
        "elements": ["A side", "B side"]
    }
}

def triangle_area(h: float, b: float):
    """This function calculates the area of the triangle from base and height."""
    return (h * b) / 2


def rectangle_area(a: float, b: float):
    """This function calculates the area of the rectangle."""
    return a * b


def circle_area(r: float):
    """This function calculates the area of the circle."""
    return pi * pow(r, 2)


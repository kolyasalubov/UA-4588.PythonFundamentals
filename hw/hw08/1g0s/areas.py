"""
Area calculation module for various geometric shapes.

This module provides functions to calculate areas of:
- Rectangle
- Triangle 
- Circle

Uses the math module for mathematical constants and functions.
"""

import math


def rectangle_area(a: float, b: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        a (float): Length of the rectangle
        b (float): Width of the rectangle
        
    Returns:
        float: Area of the rectangle (a * b)
    """
    return a * b


def triangle_area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle.
    
    Args:
        a (float): Base length of the triangle
        h (float): Height of the triangle
        
    Returns:
        float: Area of the triangle (0.5 * a * h)
    """
    return 0.5 * a * h


def circle_area(r: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        r (float): Radius of the circle
        
    Returns:
        float: Area of the circle (π * r²)
    """
    return math.pi * math.pow(r, 2)
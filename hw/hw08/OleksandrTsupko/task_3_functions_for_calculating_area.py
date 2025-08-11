import math


def calculating_area_of_rectangle():
    """
    Calculates the area of a rectangle by taking user-entered 
    length and width
    """
    length_rectangle = float(input("Enter the length of the rectangle: "))
    width_rectangle = float(input("Enter the width of the rectangle: "))
    print(f"The area of the rectangle is equal to " +
          f"{length_rectangle * width_rectangle: .2f}")
    
def calculating_area_of_triangle():
    """
    Calculates the area of a triangle by taking user-entered 
    base and height
    """
    base_triangle = float(input("Enter the base of the triangle: "))
    height_triangle = float(input("Enter the height of the triangle: "))
    print("The area of the triangle is equal to" +
          f"{1/2 * base_triangle * height_triangle: .2f}")
    
def calculating_area_of_circle():
    """
    Calculates the area of a rectangle by taking user-entered radius
    """
    radius_circle = float(input("Enter the radius of the circle: "))
    print("The area of the circle is equal to" +
          f"{math.pi * math.pow(radius_circle, 2): .2f}")

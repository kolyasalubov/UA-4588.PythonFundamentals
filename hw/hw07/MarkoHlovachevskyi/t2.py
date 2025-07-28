import math

def calculating_area_of_rectangle():
    """
    Calculates the area of a rectangle by taking user-entered 
    length and width.
    """
    length_rectangle = float(input("Enter the length of the rectangle: "))
    width_rectangle = float(input("Enter the width of the rectangle: "))
    area = length_rectangle * width_rectangle
    print(f"The area of the rectangle is equal to {area:.2f}")

def calculating_area_of_triangle():
    """
    Calculates the area of a triangle by taking user-entered 
    base and height.
    """
    base_triangle = float(input("Enter the base of the triangle: "))
    height_triangle = float(input("Enter the height of the triangle: "))
    area = 0.5 * base_triangle * height_triangle
    print(f"The area of the triangle is equal to {area:.2f}")

def calculating_area_of_circle():
    """
    Calculates the area of a circle by taking user-entered radius.
    """
    radius_circle = float(input("Enter the radius of the circle: "))
    area = math.pi * radius_circle ** 2
    print(f"The area of the circle is equal to {area:.2f}")

# --- Main Program ---
shape_choosing = int(input("Please choose a shape to calculate the area:\n"
                           "1 - Rectangle\n"
                           "2 - Triangle\n"
                           "3 - Circle\n"
                           "Your choice: "))

match shape_choosing:
    case 1:
        calculating_area_of_rectangle()
    case 2:
        calculating_area_of_triangle()
    case 3:
        calculating_area_of_circle()
    case _:
        print("Wrong input!")
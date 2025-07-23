import math


def calculating_area_of_rectangle():
    """
    Calculates the area of a rectangle by taking user-entered 
    length and width
    """
    length_rectangle = float(input("Enter the length of the rectangle: "))
    width_rectangle = float(input("Enter the width of the rectangle: "))
    print(f"The area of the rectangle is equal to " +
          f"{round(length_rectangle * width_rectangle, 2)}")
    
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
          f"{math.pi * radius_circle ** 2: .2f}")

shape_choosing = int(input("Please choose a shape for which you need to calculate the area:\n \
Push '1' button for a rectangle\n \
Push '2' button for a triangle\n \
Push '3' button for a circle\n"))

match shape_choosing:
    case 1:
        calculating_area_of_rectangle()
    case 2:
        calculating_area_of_triangle()
    case 3:
        calculating_area_of_circle()
    case _:
        print("Wrong input!")


#=====================================================
# Solving the task using function with required arguments
# def calculating_area_of_rectangle(length_rectangle, width_rectangle):
#     print("The area of the rectangle is equal to " +
#           f"{round(length_rectangle * width_rectangle, 2)}")
    
# def calculating_area_of_triangle(base_triangle, height_triangle):
#     print("The area of the triangle is equal to" +
#           f"{1/2 * base_triangle * height_triangle: .2f}")
    
# def calculating_area_of_circle(radius_circle):
#     print("The area of the circle is equal to" +
#           f"{math.pi * radius_circle ** 2: .2f}")
    
# calculating_area_of_rectangle(3.5, 7.2)
# calculating_area_of_triangle(9.8, 6.4)
# calculating_area_of_circle(8.75)

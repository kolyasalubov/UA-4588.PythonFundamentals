def areaOfRectangle(length, width):
    """
    Calculate the area of a rectangle.
    
    :param length: Length of the rectangle.
    :param width: Width of the rectangle.
    :return: Area of the rectangle.
    """

    return length * width

def areaOfCircle(radius):
    """
    Calculate the area of a circle.
    
    :param radius: Radius of the circle.
    :return: Area of the circle.
    """
    
    return 3.14 * (radius ** 2)

def areaOfTriangle(base, height):
    """
    Calculate the area of a triangle.
    
    :param base: Base of the triangle.
    :param height: Height of the triangle.
    :return: Area of the triangle.
    """
    
    return 0.5 * base * height


while True:
    option = int(input("\nPlease select the shape to calculate the area:\n1. Rectangle\n2. Circle\n3. Triangle\n0. Exit\n\nYour choice: "))
    if option in [1, 2, 3]:
        if option == 1:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"The area of the rectangle is: {areaOfRectangle(length, width)}")
        elif option == 2:
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is: {areaOfCircle(radius)}")
        elif option == 3:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print(f"The area of the triangle is: {areaOfTriangle(base, height)}")
    else:
        break
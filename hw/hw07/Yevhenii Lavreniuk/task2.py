import math  

# Function to calculate area of rectangle
def rectangle_area(length, width):
    """
    Calculates and returns the area of a rectangle.
    
    :param length: The length of the rectangle
    :param width: The width of the rectangle
    :return: Area of rectangle
    """
    return length * width

# Function to calculate area of triangle
def triangle_area(base, height):
    """
    Calculates and returns the area of a triangle.
    
    :param base: The base of the triangle
    :param height: The height of the triangle
    :return: Area of triangle
    """
    return 0.5 * base * height

# Function to calculate area of circle
def circle_area(radius):
    """
    Calculates and returns the area of a circle.
    
    :param radius: The radius of the circle
    :return: Area of circle
    """
    return math.pi * radius ** 2

print("Choose a shape to calculate its area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {area:.2f}")

elif choice == "2":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
    print(f"The area of the triangle is: {area:.2f}")

elif choice == "3":
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area:.2f}")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
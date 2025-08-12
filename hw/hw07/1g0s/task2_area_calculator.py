def area_rectangle(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
    """
    return length * width


def area_triangle(base, height):
    """
    Calculate the area of a triangle.
    
    Parameters:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
        
    Returns:
        float: The area of the triangle.
    """
    return (base * height) / 2


def area_circle(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    return 3.14159 * radius**2


def main():
    """Main program to interact with the user and calculate areas."""
    print("Area Calculator")
    print("Choose a shape: rectangle, triangle, circle")
    
    shape = input("Enter your choice: ").lower().strip()
    
    if shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = area_rectangle(length, width)
        print(f"Area = {area}")
        
    elif shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = area_triangle(base, height)
        print(f"Area = {area}")
        
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        area = area_circle(radius)
        print(f"Area = {area}")
        
    else:
        print("Invalid choice. Please choose rectangle, triangle, or circle.")


if __name__ == "__main__":
    main()
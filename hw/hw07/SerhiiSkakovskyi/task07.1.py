#Task1. 
#Write a function that returns the largest number of two
#numbers (use DocStrings documentation strings in the function). 

def max_of_two(a, b):
    """
    Повертає більше з двох чисел.

    Args:
        a (int or float): перше число
        b (int or float): друге число

    Returns:
        int or float: більше з двох переданих чисел
    """
    return a if a > b else b

#Task2. 
#Write a program that calculates the area of a rectangle, 
#triangle and circle (write three functions to calculate the area, 
#and call them in the
#main program depending on the user's choice).

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
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", area_rectangle(length, width))
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of triangle:", area_triangle(base, height))
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print("Area of circle:", area_circle(radius))
    else:
        print("Invalid choice.")


#Task3. 
#Write a function that calculates the number of characters
#included in a given string
#• input: "hello"
#• output: {"h":1, "e":1,"l":2,"o":1}


def count_characters(s):
    """
    Count the number of occurrences of each character in a string.

    Parameters:
    s (str): The input string.

    Returns:
    dict: A dictionary where keys are characters and values are their counts.
    """
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


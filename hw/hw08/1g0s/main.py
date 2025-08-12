"""
Main program for area calculator.

This program allows users to calculate areas of different geometric shapes:
- Rectangle
- Triangle
- Circle

Uses the areas module for calculations.
"""

import areas


def get_positive_number(prompt: str) -> float:
    """
    Get a positive number from user input with validation.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        float: A positive number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """Main program function."""
    print("Area Calculator")
    print("===============")
    
    while True:
        print("\nChoose a shape to calculate the area:")
        print("1. rectangle")
        print("2. triangle")
        print("3. circle")
        print("4. exit")
        
        choice = input("\nEnter your choice (rectangle/triangle/circle/exit): ").lower().strip()
        
        if choice == "exit" or choice == "4":
            print("Goodbye!")
            break
        elif choice == "rectangle" or choice == "1":
            print("\nRectangle Area Calculator")
            a = get_positive_number("Enter the length: ")
            b = get_positive_number("Enter the width: ")
            area = areas.rectangle_area(a, b)
            print(f"The area of the rectangle is: {area}")
            
        elif choice == "triangle" or choice == "2":
            print("\nTriangle Area Calculator")
            a = get_positive_number("Enter the base length: ")
            h = get_positive_number("Enter the height: ")
            area = areas.triangle_area(a, h)
            print(f"The area of the triangle is: {area}")
            
        elif choice == "circle" or choice == "3":
            print("\nCircle Area Calculator")
            r = get_positive_number("Enter the radius: ")
            area = areas.circle_area(r)
            print(f"The area of the circle is: {area}")
            
        else:
            print("Invalid choice. Please enter 'rectangle', 'triangle', 'circle', or 'exit'.")


if __name__ == "__main__":
    main()
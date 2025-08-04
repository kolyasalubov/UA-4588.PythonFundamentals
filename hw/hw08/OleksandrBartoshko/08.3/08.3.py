from area_calc import *
choice = input("Choose a shape (circle, rectangle, triangle): ")
def main(choice):
    match choice:
        case "circle":
            radius = float(input("Enter the radius: "))
            area = circle_area(radius)
            print(f"The area of the circle is: {area}")
        case "rectangle":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            area = rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
        case "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            area = triangle_area(base, height)
            print(f"The area of the triangle is: {area}")
        case _:
            print("Invalid shape choice.")
            
if __name__ == "__main__":
    main(choice)            
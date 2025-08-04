from Task3module import rectangle_area, triangle_area, circle_area

shape = input("Enter the shape (rectangle, triangle, circle): ").strip().lower()

if shape == "rectangle":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    print(f"The area of the rectangle is: {rectangle_area(a, b)}")

elif shape == "triangle":
    a = float(input("Enter the base length a: "))
    h = float(input("Enter the height h: "))
    print(f"The area of the triangle is: {triangle_area(a, h)}")

elif shape == "circle":
    r = float(input("Enter the radius r: "))
    print(f"The area of the circle is: {circle_area(r)}")

else:
    print("Invalid shape selected.")

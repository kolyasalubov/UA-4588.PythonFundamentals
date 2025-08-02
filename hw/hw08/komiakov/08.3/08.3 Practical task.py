import area

while True:
    choice = int(input("\nPlease select the shape to calculate the area:\n1. Circle\n2. Rectangle\n3. Triangle\nYour choice: "))
    
    if choice == 1:
        radius = float(input("Please enter the radius of the circle: "))
        print(f"The area of the circle is: {area.areaOfCircle(radius)}")
    elif choice == 2:
        length = float(input("Please enter the length of the rectangle: "))
        width = float(input("Please enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area.areaOfRectangle(length, width)}")
    elif choice == 3:
        base = float(input("Please enter the base of the triangle: "))
        height = float(input("Please enter the height of the triangle: "))
        print(f"The area of the triangle is: {area.areaOfTriangle(base, height)}")
    else:
        break

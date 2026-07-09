def rectangle_area(a, b):
    return a * b

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

choice = int(input("Choose what do you want: 1 - area of rectangle; 2 - area of triangle; 3 - area of circle;"))
if choice == 1:
    a = int(input("Enter the first side of the rectangle: "))
    b = int(input("Enter the second side of the rectangle: "))
    if a>0 and b>0:
        print("The area of your rectangle is: " , rectangle_area(a, b))
    else:
        print("Wrong size of side")
elif choice == 2:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    if base > 0 and height > 0:
        print("The are aof your triangle is: " , triangle_area(base, height))
    else:
        print("Wrong size of base or heihgt")
elif choice == 3:
    radius = int(input("Enter the radius of the circle:"))
    if radius > 0:
        print("The radius of your circle is: " , circle_area(radius))
    else:
        print("Wrong size of radius")
else:
    print("Wrong choice :/")
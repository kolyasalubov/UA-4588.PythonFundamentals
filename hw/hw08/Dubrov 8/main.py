import areas

print("Choose the figure to calculate area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    if a > 0 and b > 0:
        print("Area of rectangle:", areas.rectangle_area(a, b))
    else:
        print("Wrong size of side")

elif choice == "2":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    if h>0 and a>0:
        print("Area of triangle:", areas.triangle_area(h, a))
    else:
        print("Wrong sise of height or base")

elif choice == "3":
    r = float(input("Enter radius r: "))
    if r > 0:
        print("Area of circle:", areas.circle_area(r))
    else:
        print("Wrong size of radius")
else:
    print(" Invalid choice!")

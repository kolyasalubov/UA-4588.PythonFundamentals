import areas

print("Choose the figure to calculate area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area of rectangle:", areas.rectangle_area(a, b))

elif choice == "2":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    print("Area of triangle:", areas.triangle_area(h, a))

elif choice == "3":
    r = float(input("Enter radius r: "))
    print("Area of circle:", areas.circle_area(r))

else:
    print(" Invalid choice!")

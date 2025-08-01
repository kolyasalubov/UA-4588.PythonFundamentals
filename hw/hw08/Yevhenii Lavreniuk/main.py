from area_module import rectangle_area, triangle_area, circle_area

print("Choose shape to calculate area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    a = float(input("Enter length a: "))
    b = float(input("Enter width b: "))
    print("Area of rectangle:", rectangle_area(a, b))

elif choice == "2":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    print("Area of triangle:", triangle_area(h, a))

elif choice == "3":
    r = float(input("Enter radius r: "))
    print("Area of circle:", circle_area(r))

else:
    print("Invalid choice.")

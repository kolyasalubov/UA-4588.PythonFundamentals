import area_module

choice = input("Choose a figure (rectangle/triangle/circle): ").strip().lower()

if choice == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area of rectangle:", area_module.rectangle_area(a, b))

elif choice == "triangle":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    print("Area of triangle:", area_module.triangle_area(h, a))

elif choice == "circle":
    r = float(input("Enter radius r: "))
    print("Area of circle:", area_module.circle_area(r))

else:
    print("Unknown figure.")

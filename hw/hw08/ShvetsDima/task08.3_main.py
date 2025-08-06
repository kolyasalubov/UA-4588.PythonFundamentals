import task08.3 as area_module

figure = input("Enter the figure (rectangle, triangle, circle): ").lower()

if figure == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area of rectangle:", area_module.rectangle_area(a, b))

elif figure == "triangle":
    h = float(input("Enter height h: "))
    a = float(input("Enter base a: "))
    print("Area of triangle:", area_module.triangle_area(h, a))

elif figure == "circle":
    r = float(input("Enter radius r: "))
    print("Area of circle:", area_module.circle_area(r))

else:
    print("Unknown figure")
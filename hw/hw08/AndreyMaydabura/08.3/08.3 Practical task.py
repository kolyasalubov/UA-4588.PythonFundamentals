import square

figure = input(
    "What figure? (rectangle / triangle / circle): ").strip().lower()

if figure == "rectangle":
    a = float(input("Enter side rectangle: "))
    b = float(input("Enter another side rectangle: "))
    print("Rectangle square:", square.s_rectangle(a, b))

elif figure == "triangle":
    a = float(input("Enter base of a triangle: "))
    h = float(input("Enter high triangle: "))
    print("Triangle square:", square.s_triangle(a, h))

elif figure == "circle":
    r = float(input("Enter radius: "))
    print("Circle square:", square.s_circle(r))

else:
    print("Try again")

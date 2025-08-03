import functions

ask_figure = input("Choose the figure: Rectangle/Triangle/Circle - ").capitalize().strip()

if ask_figure == "Rectangle":
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    area = functions.rectangle(a, b)
    print(f"The area is: {area:.2f}")

elif ask_figure == "Triangle":
    a = float(input("Enter the length of a base: "))
    h = float(input("Enter the height: "))
    area = functions.triangle(h, a)
    print(f"The area is: {area:.2f}")

elif ask_figure == "Circle":
    r = float(input("Enter the radius: "))
    area = functions.circle(r)
    print(f"The area is: {area:.2f}")

else:
    print("Please try again")
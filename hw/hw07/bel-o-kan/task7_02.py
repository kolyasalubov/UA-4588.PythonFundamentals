PI =3.14

def get_rectangle_area():
    a = float(input("Please enter the length of side a: "))
    b = float(input("Please enter the length of side b: "))
    return a * b

def get_triangle_area():
    base = float(input("Please enter the length of the base: "))
    h = float(input("Please enter the length of the height: "))
    return base * h * 0.5

def get_circle_area():
    r = float(input("Please enter the length of the radius: "))
    return PI * r ** 2

user_shape_choice = int(input("Please input the number to calculate the area for: 1 - rectangle, 2 - triangle, 3 - circle: "))

match user_shape_choice:
    case 1:
        print(get_rectangle_area())
    case 2:
        print(get_triangle_area())
    case 3:
        print(get_circle_area())
    case _:
        print("Invalid input")


def s_rectangle(a, b):
    """
    Calculates the area of a rectangle

    a - length
    b - width
    """
    return a * b


def s_triangle(a, b):
    """
    Calculates the area of a triangle

    a - base
    b - height
    """
    return 0.5 * a * b


def s_circle(a):
    """
    Calculates the area of a circle

    a - radius
    """
    return 3.14 * a ** 2


print("What figure's area will we calculate?")
print("If rectangle - press 1")
print("If triangle - press 2")
print("If circle - press 3")

user_select = input("Make a choice: ")

if user_select == "1":
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    print("Area of a rectangle:", s_rectangle(a, b))

elif user_select == "2":
    c = float(input("Enter base: "))
    d = float(input("Enter height: "))
    print("Area of a triangle:", s_triangle(c, d))

elif user_select == "3":
    r = float(input("Enter radius: "))
    print("Area of a circle:", s_circle(r))

else:
    print("Incorrect chose. Try again.")

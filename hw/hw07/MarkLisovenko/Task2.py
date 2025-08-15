def rectangle_area() :
    """This function asks user to enter length and width of the rectangle and calculates its area"""
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    AreaOfTheRectangle = length * width
    print(f"Area of the rectangle is equal to {AreaOfTheRectangle}")

def triangle_area() :
    """This function asks user to enter base and height of the triangle and calculates its area"""
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    AreaOfTheTriangle = base * height / 2
    print(f"Area of the triangle is equal to {AreaOfTheTriangle}")

def circle_area() :
    """This function asks user to enter radius of the circle and calculates its area"""
    PI = 3.14
    radius = float(input("Enter the radius of the circle: "))
    AreaOfTheCircle = PI * radius ** 2
    print(f"Area of the circle is equal to {AreaOfTheCircle}")


####################################################################################################################### 


figure = input("Which figure of the following you want to calculate area of?\n"
               "1 - Rectangle\n"
               "2 - Triangle\n"
               "3 - Circle\n"
               "Choose a figure: ")

match figure :
    case "1" :
        rectangle_area()
    case "2" :
        triangle_area()
    case "3" :
        circle_area()
    case _ :
        print("There is no such figure")
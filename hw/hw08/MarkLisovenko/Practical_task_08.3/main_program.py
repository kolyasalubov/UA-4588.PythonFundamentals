import area

figure = input("Which figure of the following you want to calculate area of?\n"
               "1 - Rectangle\n"
               "2 - Triangle\n"
               "3 - Circle\n"
               "Choose a figure: ")

match figure :
    case "1" :
        print("Area of the rectangle is equal to", area.rectangle_area())
    case "2" :
        print("Area of the triangle is equal to", area.triangle_area())
    case "3" :
        print("Area of the circle is equal to", area.circle_area())
    case _ :
        print("There is no such figure")
import module_area_8_3

choice  = input("Calculate Area for\n1 - Rectangle\n2 - Triangle\n3 - Circle\n")

match choice :
    case "1":
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        print("Rectangle area:", module_area_8_3.rectangle(l,w))
    case "2": 
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
        print("Triangle area:", module_area_8_3.triangle(h,b))
    case "3":
        r = int(input("Enter radius: "))
        print("Circle area:", module_area_8_3.circle(r))
    case _:
        print("Invalid choise")
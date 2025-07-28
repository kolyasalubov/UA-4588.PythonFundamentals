# Task1
def get_max(num1, num2):
    """This function returns the largest number of two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2

print(get_max(5,3))
print(get_max(1,3))

# Task2
PI = 3.14

def rectangle_area(l,w):
    return l*w

def triangle_area(h,b):
    return h*b/2

def circle_area(r):
    return PI*r**2

choice  = input("Calculate Area for\n1 - Rectangle\n2 - Triangle\n3 - Circle\n")
match choice :
    case "1":
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        print("Rectangle area:", rectangle_area(l,w))
    case "2": 
        b = int(input("Enter base: "))
        h = int(input("Enter height: "))
        print("Triangle area:",triangle_area(h,b))
    case "3":
        r = int(input("Enter radius: "))
        print("Circle area:",circle_area(r))
    case _:
        print("Invalid choise")


# Task3
def chars_count(string):
    output_dict = {}
    for char in string:
        if not char in output_dict:
            output_dict.update({char: string.count(char)})
    print(output_dict)

chars_count("hello")
from figure_area import rectangle_area, triangle_area, circle_area

def main(): 
    print("Choose figure to find the area:")
    print("1) Rectangle")
    print("2) Triangle")
    print("3) Circle")
    
    choice = input("Choose option between 1-3: ")
    
    if choice == "1":
        length = input("Input length of the Rectangle: ")
        width = input("Input width of Rectangle: ")
        area = rectangle_area(length, width)
        print(f"The area of Rectangle with width = {width} and length = {length} is {area}")
        
    elif choice == "2":
        base = input("Input base of Triangle: ")
        height = input("Input height of Triangle: ")
        area = triangle_area(base, height)
        print(f"The area of your triangle with base = {base} and height = {height} is {area}")
        
    elif choice == "3":
        radius = input("Enter radius of your triangle: ")
        area = circle_area(radius)
        print(f"The area of your triangle witd radius = {radius} is {area}")
        
    else:
        print("Wrong option number!")
        
if __name__ == "__main__" :
    main()
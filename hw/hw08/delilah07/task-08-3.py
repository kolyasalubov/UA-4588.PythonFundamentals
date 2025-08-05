import module

def main_programm():
    '''
    Function that returns the area of the user's choosen shape
    '''
    user_choice = int(input('Choose which shape do you want to calculate. \nReactagle (choose 1). \nTriangle (choose 2). \nCircle (choose 3).\n'))
    if user_choice == 1:
        length = float(input('add length of rectangle: '))
        width = float(input('add width of rectangle: '))
        print(f'Area of reactagle with length {length} and width {width} is: {module.rectangle_area(length, width)}')
    elif user_choice == 2:
        base = float(input('add base of triangle: '))
        height = float(input('add height of triangle: '))
        print(f'Area of triangle with base {base} and height {height} is: {module.triangle_area(base, height)}')
    elif user_choice == 3:
        radius = float(input('add radius of circle: '))
        print(f'Area of circle with radius {radius} is: {module.circle_area(radius)}')
    else:
        print("You didn't choose the right number. Try one more time")
        main_programm()

main_programm()
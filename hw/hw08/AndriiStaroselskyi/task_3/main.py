import calculator as calc

input_prompt = """
Please input the number to calculate the area for: 
1 - rectangle 
2 - triangle 
3 - circle

0 - to exit

"""

while True:
    user_selection = int(input(input_prompt))
    if user_selection == 0:
        break 
    elif user_selection == 1:
        result = calc.get_rectangle_area()
    elif user_selection == 2:
        result = calc.get_triangle_area()
    elif user_selection == 3:
        result = calc.get_circle_area()
    else:
        print("Invalid input. Please try again \n")
        continue

    print(f"\nThe value of the area is {result}")
    
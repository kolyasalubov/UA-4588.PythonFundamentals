#TASK 1
def largest_numb(num1: int,  num2: int):
    """
    This function determines the largest number
    Parameters
    ----------
    a : int
        first number.
    b : int
        second number.

    Returns
    -------
    int
        The largest number

    str
        But if numbers are equal, function return "The numbers are equal"
    """

    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "The numbers are equal"




#TASK 2
def rectangle_area():
    a = int(input("Enter side a:"))
    b = int(input("Enter side b:"))
    solution = a * b
    print("Rectangle area:", solution)


def triangle_area():
    a = int(input("Enter side a:"))
    b = int(input("Enter side b:"))
    c = int(input("Enter side с:"))
    p = (a + b + c) / 2
    solution = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    rounded_solution = round(solution, 2)
    print("Triangle area:", rounded_solution)

def circle_area():
    radius = float(input("Enter radius:"))
    pi = 3.14
    solution = pi * radius ** 2
    print("Circle area:", solution)


def area():
    s_area = int(input("Rectangle - enter  1\nTriangle- enter  2\nCircle- enter  3\nChoose the area of the shape you want to calculate:"))
    if s_area == 1:
        rectangle_area()

    elif s_area == 2:
        triangle_area()

    elif s_area == 3:
        circle_area()

    else:
        print("Incorrect choice, try again")



#TASK 3
def character_counting():
    user_input = input("Enter a word: ")
    result = {}
    for letter in user_input:
        count_letter = user_input.count(letter)
        result[letter] = count_letter
    print(result)

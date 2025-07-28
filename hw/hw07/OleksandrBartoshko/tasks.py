#task 1   ------------------------------------------------------------------------
def comprasion(a, b):
    """
    Function to compare two numbers and return the larger one
    """
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "equal numbers"
    
print(comprasion(input("enter first number: "), input("enter second number: ")))



#task 2   ------------------------------------------------------------------------
PI = 3.14

def circle_area(radius):
    return PI * radius ** 2

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

choise = input("choose a shape (1:circle, 2:rectangle, 3:triangle): ")

match choise:
    case "1":
        radius = float(input("enter the radius of the circle: "))
        print(f"the area of the circle is: {circle_area(radius)}")
    case "2":
        length = float(input("enter the length of the rectangle: "))
        width = float(input("enter the width of the rectangle: "))
        print(f"the area of the rectangle: {rectangle_area(length, width)}")
    case "3":
        base = float(input("enter the base of the triangle: "))
        height = float(input("enter the height of the triangle: "))
        print(f"the area of the triangle: {triangle_area(base, height)}")
    case _:
        print("invalid choice")





#task 3  ------------------------------------------------------------------------
letter_in_word = list(input("enter a word: "))

def count_every_letter(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
print(count_every_letter(letter_in_word))
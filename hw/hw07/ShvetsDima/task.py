import math

def max_of_two(a, b):
    return a if a > b else b

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def count_characters(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

if __name__ == "__main__":
    print("\nTask 1: Max of Two Numbers")
    print("Max of (10, 7):", max_of_two(10, 7))

    print("\nTask 2: Area Calculation")
    choice = input("Choose shape (rectangle, triangle, circle): ").lower()

    if choice == "rectangle":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("Area of Rectangle:", area_rectangle(l, w))
    elif choice == "triangle":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("Area of Triangle:", area_triangle(b, h))
    elif choice == "circle":
        r = float(input("Radius: "))
        print("Area of Circle:", area_circle(r))
    else:
        print("Invalid choice.")

    print("\nTask 3: Character Frequency")
    test_str = input("Enter a string to analyze: ")
    print(count_characters(test_str))
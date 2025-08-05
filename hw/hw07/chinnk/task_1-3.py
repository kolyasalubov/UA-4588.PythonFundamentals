# Task1
def max_of_two(a, b):
    return a if a > b else b


# Task2
import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

shapes = {
    '1': {
        'name': 'Rectangle',
        'function': area_rectangle,
        'params': ['length', 'width']
    },
    '2': {
        'name': 'Triangle',
        'function': area_triangle,
        'params': ['base', 'height']
    },
    '3': {
        'name': 'Circle',
        'function': area_circle,
        'params': ['radius']
    }
}

print("Choose a shape to calculate the area:")
for key, val in shapes.items():
    print(f"{key}. {val['name']}")

choice = input("Enter your choice (1/2/3): ")

if choice in shapes:
    params = []
    for param_name in shapes[choice]['params']:
        value = float(input(f"Enter {param_name}: "))
        params.append(value)
    result = shapes[choice]['function'](*params)
    print(f"The area of the {shapes[choice]['name'].lower()} is {result:.2f}")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")


# Task3
def count_characters(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(count_characters("hello"))

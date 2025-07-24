# Task 1

# def func(arg1, arg2):
#     """
#     Write a function that returns the largest number of two
#     numbers
#     """
#     if arg1 > arg2:
#         return f"{arg1} is bigger than {arg2}"
#     elif arg2 > arg1:
#         return f"{arg2} is bigger than {arg1}"
#     else:
#         return f"{arg1} is equal to {arg2}"

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(func(num1, num2))




# Task 2

# def rectangle(a, b):
#     area = a * b
#     return area

# def triangle(a, h):
#     area = 0.5 * a * h
#     return area

# def circle(r):
#     PI = 3.14
#     area = PI * r**2
#     return area

# ask = input("Choose a figure you want to work with: Rectangle/Triangle/Circle: ").capitalize()

# if ask == "Rectangle":
#     a = float(input("Enter the length of first side: "))
#     b = float(input("Enter the length of second side: "))
#     print(rectangle(a, b))
# elif ask == "Triangle":
#     a = float(input("Enter the base of Triangle: "))
#     h = float(input("Enter the height of Triangle: "))
#     print(triangle(a, h))
# elif ask == "Circle":
#     r = float(input("Enter the radius of Circle: "))
#     print(circle(r))
# else:
#     print("Unknown shape. Please enter: Rectangle, Triangle or Circle.")




# Task 3

# def calc(ask):
#     result = {}
#     for i in ask:
#         if i in result:
#             result[i] += 1
#         else:
#             result[i] = 1
#     return result

# ask = input("Enter whatever you want: ")
# print(calc(ask))
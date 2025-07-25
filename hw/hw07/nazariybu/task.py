# def arithmetic_mean(*num):
#     '''This function that returns the arithmetic mean
#     of any number of numbers witch function sum() and len()'''
#     result = sum(num) / len(num)
#     return result

# print(arithmetic_mean(1,2,3,4,5))

# def aritmetic_mean(*num):
#     '''
#     This function that returns the arithmetic mean of any number of numbers
#     '''
#     sum = 0
#     count = 0
#     for i in num:
#         sum += i
#         count += 1
#     result = sum / count
#     return result

# print(aritmetic_mean.__doc__)
# print(aritmetic_mean(1,2,3,4,5))

# def largest_number(num1,num2):
#     """
#     This function that returns the largest number of two numbers
#     """
#     if num1 > num2:
#         return (f'{num1} is largest than {num2}')
#     elif num1 == num2:
#         return (f'{num1} is equalet than {num2}')
#     else:
#         return (f'{num2} is largest than {num1}')

# print(largest_number.__doc__)
# print(largest_number(3,3))


# def factorial(in_data):
#     """
#     This is a recursive function 
#     to finde the factorial of an integer
#     """

#     if in_data == 1:
#         return 1
#     else:
#         return factorial(in_data - 1)*in_data

# print(factorial(4))


# my_list = list(range(10))

# new_list = list(map(lambda x: x * 2, my_list))

# print(new_list)

# Task 1.
# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

# def largest_number(num1,num2):
#     """
#     This function that returns the largest number of two numbers
#     """
#     if num1 > num2:
#         return (f'{num1} is largest than {num2}')
#     elif num1 == num2:
#         return (f'{num1} is equalet than {num2}')
#     else:
#         return (f'{num2} is largest than {num1}')

# print(largest_number.__doc__)
# print(largest_number(3,3))


# Task2.
# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program
# depending on the user's choice).

# def rectangle_are(a,b):
#     return a * b

# def triangle_are(a,h):
#     return 0.5*a*h

# def circle_are(r):
#     PI = 3.14
#     return PI * r

# figure = int(input('1 - Rectangle \n2 - Triangle \n3 - Circle \n Select the figure: '))

# if figure == 1:
#     a = int(input('Input a value: '))
#     b = int(input('Input b value: '))
#     print("Are of a rectangle is:", rectangle_are(a,b))
# elif figure == 2:
#     a = int(input('Input a value: '))
#     h = int(input('Input h value: '))
#     print("Are of a tringale is:", int(triangle_are(a,h)))
# elif figure == 3:
#     r = int(input('Input r value: '))
#     print("Are of a circle is:", int(circle_are(r)))
# else:
#     print("Chose the correct option")


# Task3.
# Write a function that calculates the number of characters 
# included in given string
# • input: "hello"
# • output: {"h":l,"e":1,"l":2,"o":1}

# def caunt_characters(user_string):
#     result = {}
#     count = 0
#     for i in user_string:
#         count = user_string.count(i)
#         result.update({i:count})
#     return result

# print(caunt_characters("Hello"))

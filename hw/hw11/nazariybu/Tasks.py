# Task 1.
# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.

# def check_age():
#     try:
#         # Введення тільки цілих чисел
#         age = int(input("Enter your age: ")) 

#         #  Провірка на негативні числа
#         if age < 0:
#             raise ValueError("Age can't be negative!")  

#         # Провірка на парні та непарні
#         if age % 2 == 0:
#             print(f'Your age {age} is even.')
#         else:
#             print(f'Your age {age} is odd.')

#     except ValueError as e:
#         print(e)

# check_age()

# -----------------------------------------------------------------------

# Task 2.
# Write a program that analyzes the entered number and, depending on the number,
# gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday,
# etc.). Take into account cases of entering numbers from 8 and more, as well as cases of
# entering non-numerical data.

def get_day_of_week():
   
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        number = int(input("Enter a number from 1 to 7: "))

        if number in days:
            print(f'{number} is {days[number]}')
        else:
            raise ValueError("Error: Please enter a number between 1 and 7.")
        
    except ValueError as e:
        print(e)


get_day_of_week()
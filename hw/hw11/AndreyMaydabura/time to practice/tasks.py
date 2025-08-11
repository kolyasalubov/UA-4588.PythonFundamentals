# 1. Write a program that prompts the user to enter an integer and determines whether
# the number is even or odd, taking into account the case of entering incorrect data.

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def main():
    user_input = input("Enter an integer: ")

    try:
        number = int(user_input)
        check_even_odd(number)
    except ValueError:
        print("Error: please enter a valid integer.")


if __name__ == "__main__":
    main()
# ________________________________________________________________________________________

# 3. Write a program to calculate the divide of two numbers entered by the user
# sequentially through a comma, to predict the case of division by zero, cases of
# syntactic errors and cases of other exceptional situations. Use the else and finally
# blocks.


def divide_two_numbers():
    user_input = input("Введите два числа через запятую: ")

    num1_str, num2_str = user_input.split(",")
    num1 = float(num1_str.strip())
    num2 = float(num2_str.strip())

    return num1 / num2


def main():

    try:
        result = divide_two_numbers()

    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
    except ValueError:
        print("Ошибка: введите корректные числа, разделённые запятой.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    else:
        print(f"Результат деления: {result}")
    finally:
        print("Выполнение программы завершено.")


if __name__ == "__main__":
    main()

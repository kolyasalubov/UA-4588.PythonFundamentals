try:
    user_input = input("Введіть два числа через кому (наприклад, 24,4): ")
    num1_str, num2_str = user_input.split(",")

    num1 = float(num1_str)
    num2 = float(num2_str)

    result = num1 / num2

except ValueError:
    print("Помилка: потрібно ввести два коректні числа, розділені комою.")

except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе.")

except Exception as e:
    print(f"Несподівана помилка: {e}")

else:
    print(f"Результат ділення {num1} / {num2} = {result}")

finally:
    print("Виконання програми завершено.")
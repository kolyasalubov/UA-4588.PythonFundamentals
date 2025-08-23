try:
    user_input = input("Введіть ціле число: ")
    number = int(user_input)
    if number %2 == 0:
        print("Число парне.")
    else:
        print("Число непарне.")

except ValueError:
    print("Помилка: потрібно ввести ціле число!")
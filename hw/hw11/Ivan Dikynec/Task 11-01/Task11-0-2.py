days = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четверг",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}


user_input = input("Введіть число від 1 до 7: ")

if user_input.isdigit():
    number =int(user_input)


    if 1 <= number <= 7:
        print(f"День {number} - це {days[number]}")
    else:
        print("Помилка: число має бути від 1 до 7.")

else:print("Помилка: число має бути числовим значенням.")
def process_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним!")
    
    if age %2 == 0:
        return "Ваш вік парний."
    else:
        return "Ваш вік непарний."
    

try:
    user_input = input("Введіть свій вік: ")
    age = int(user_input)
    result = process_age(age)
    print(result)

except ValueError as e:
    print(f"Помилка: {e}")

except Exception as e:
    print(f"Сталася несподівана помилка: {e}")
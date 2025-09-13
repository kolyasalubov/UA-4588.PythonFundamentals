def check_age():
    try:
        # Введення тільки цілих чисел
        age = int(input("Enter your age: ")) 

        #  Провірка на негативні числа
        if age < 0:
            raise ValueError("Age can't be negative!")  

        # Провірка на парні та непарні
        if age % 2 == 0:
            print(f'Your age {age} is even.')
        else:
            print(f'Your age {age} is odd.')

    except ValueError as e:
        print(e)

check_age()
import random
def guess_number_game():

    secret_number = random.randint(1, 50)
    attempts = 5

    print("Гра 'Вгадай число'!")
    print("Я загадав число від 1 до 50.")
    print(f"У вас є {attempts} спроб, щоб його знайти!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}: Введіть число: "))
        except ValueError:
            print("❌ Введіть ціле число!")
            continue

        
        if guess == secret_number:
            print(f"🎉 Вітаю! Ви вгадали число {secret_number} за {attempt} спроб(и)!")
            break
        elif guess < secret_number:
            print("📈 Загадане число більше.")
        else:
            print("📉 Загадане число менше.")
        
        if attempt == attempts:
            print(f"😢 Ви використали всі спроби. Загадане число було: {secret_number}")

guess_number_game()
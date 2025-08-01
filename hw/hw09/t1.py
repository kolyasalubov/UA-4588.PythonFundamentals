import random

# Генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)

MAX_ATTEMPTS = 10

print("Вгадай число від 1 до 100. У тебе є 10 спроб!")

for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        guess = int(input(f"Спроба {attempt}: Введи число: "))
    except ValueError:
        print("Будь ласка, введи ціле число.")
        continue

    if guess == secret_number:
        print(f"Вітаю! Ти вгадав число {secret_number} з {attempt} спроби.")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"Спроби закінчились! Загадане число було: {secret_number}")

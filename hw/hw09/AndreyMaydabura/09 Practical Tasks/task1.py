import random

secret_number = random.randint(1, 100)
max_attempts = 10

print("Я загадал целое число от 1 до 100.")
print("У тебя есть 10 попыток, чтобы угадать его.")

for x in range(1, max_attempts + 1):
    guess = input(f"Попытка {x}: Введи число: ")

    if not guess.isdigit():
        print(f"{guess} не целое число!")
        break

    guess = int(guess)

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Ты угадал число {secret_number} с {x}-й попытки!")
        break
else:
    print(f"Ты не угадал. Загаданное число было: {secret_number}")

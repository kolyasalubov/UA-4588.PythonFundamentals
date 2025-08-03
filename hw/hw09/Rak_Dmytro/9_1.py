import random

secret_number = random.randint(1, 100)
attempts = 10

print("🎯 Я загадав число від 1 до 100. У тебе є 10 спроб вгадати його!")

for i in range(1, attempts + 1):
    guess = int(input(f"\nСпроба {i}: Введи число: "))

    if guess == secret_number:
        print(f"🎉 Вітаю! Ти вгадав число {secret_number} за {i} спроб(у)!")
        break
    elif guess < secret_number:
        print("🔼 Моє число більше.")
    else:
        print("🔽 Моє число менше.")

else:
    print(f"\n💥 На жаль, ти не вгадав. Моє число було {secret_number}.")

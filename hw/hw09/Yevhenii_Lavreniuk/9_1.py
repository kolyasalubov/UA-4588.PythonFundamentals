import random

# Генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)

for attempt in range(1, 11):  # 10 спроб
    guess = int(input(f"Attempt {attempt}/10 - Enter your guess (1-100): "))
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempt} tries.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"❌ Sorry, you did not guess the number. It was {secret_number}.")

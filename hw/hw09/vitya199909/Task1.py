
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("Guess number (1-100): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You've guessed the number.")
        break
    elif guess < secret_number:
        print("The secret number is higher.")
    else:
        print("The secret number is lower.")

if attempts == max_attempts:
    print(f"Unfortunately, you didn't guess the number. The secret number was: {secret_number}")

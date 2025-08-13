import random

secret_number = random.randint(1, 100)

print("I have chosen a number between 1 and 100. You have 10 tries to guess it!")

for attempt in range(1, 11):
    while True:
        user_input = input(f"Attempt {attempt}: Enter a number between 1 and 100: ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a whole number.")
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Number out of range. Please choose a number between 1 and 100.")
            continue

        break

    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempt} tries ")
        break
    elif guess < secret_number:
        print("The secret number is higher.")
    else:
        print("The secret number is lower.")
else:
    print(f"Out of tries! The number was {secret_number}. Better luck next time.")

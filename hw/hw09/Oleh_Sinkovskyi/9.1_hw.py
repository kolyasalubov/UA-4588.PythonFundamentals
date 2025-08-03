import random

number_to_guess = random.randint(1, 100)
attempts = 10

print("You have 10 attempts to guess the number in a range of 1 to 100")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt number {attempt}. Enter the number: "))

    if guess < number_to_guess:
        print("My number is bigger")
    elif guess > number_to_guess:
        print("My number is less")
    else:
        print(f"Congratulations! The numeber {guess} is correct!")

else:
    print("Game over. There are no more attempts.")
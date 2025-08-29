import random

unguesed_number = random.randint(1, 100)

print("Try to guess number from 1 to 100. You have 10 attempts to guess!")


for attempt in range(1, 11):
    guess = int(input(f"{attempt} attempt: Enter your number: "))

    if guess == unguesed_number:
        print(f"Congratulations!!! You guessed {unguesed_number} for {attempt} attempt(s)")
        break
    elif guess < unguesed_number:
        print("Number is biger!")
    else:
        print("Number is less!")

else:
    print(f"You used all your 10 attempts, looser. The number was {unguesed_number}.")

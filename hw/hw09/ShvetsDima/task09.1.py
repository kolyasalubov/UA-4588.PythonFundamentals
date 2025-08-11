import random

secret_number = random.randint(1, 100)

max_attempts = 10

print("🎯 Guess the number between 1 and 100!")
print(f"You have {max_attempts} attempts.\n")

for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number in {attempt} tries!")
        break
    elif guess < secret_number:
        print("🔼 Too low!")
    else:
        print("🔽 Too high!")

    if attempt == max_attempts:
        print(f"\n❌ You've used all {max_attempts} attempts.")
        print(f"The correct number was: {secret_number}")
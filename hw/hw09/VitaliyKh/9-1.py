from random import randint

ATTEMPTS = 10
lower = 1
higher = 100
secret = randint(lower,higher)

for i in range(ATTEMPTS):
    attempt = int(input(f"[{i+1}/{ATTEMPTS}] Guess the number between {lower} and {higher}: "))
    if attempt <= lower or attempt >= higher:
        print(f"Guess should be between {lower} and {higher}")
        continue
    if attempt == secret:
        print("Congratulations!!!")
        break
    elif attempt < secret:
        lower = attempt
        print("The secret number is higher")
    else: 
        higher = attempt
        print("The secret number is lower")
else:
    print(f"You lost! The number was: {secret}")
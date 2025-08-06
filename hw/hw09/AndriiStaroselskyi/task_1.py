from random import randint

number_to_guess = randint(1, 100)

try_number = 10

while try_number > 0:
    print(f"\n** {try_number} {"try" if try_number == 1 else "tries"} left **\n")
    
    user_number = int(input("Please enter your number: "))
    
    if user_number == number_to_guess:
        print("Congratulations! You won!")
        break
    elif user_number > number_to_guess:
        print("The number to guess is less than your number")
    else:
        print("The number to guess is greater than your number")

    try_number -= 1

    if try_number == 0:
        print(f"\nSorry, you lost :c \nThe number was {number_to_guess}")

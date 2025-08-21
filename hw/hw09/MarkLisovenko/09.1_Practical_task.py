def guessing(random_number, user_guess) :
    if random_number > user_guess :
            user_guess = int(input("Unfortunately, you didn't guess the number\n"
                               "Number that you need to guess is greater than one you named\n"
                               "Try again: "))
    
    elif random_number < user_guess :
         user_guess = int(input("Unfortunately, you didn't guess the number\n"
                               "Number that you need to guess is less than one you named\n"
                               "Try again: "))
    
    return user_guess


####################---Main Program---####################

import random

random_number = random.randint(1, 101)

user_guess = 0

for i in range(10) :
    if i == 0 :
        user_guess = int(input("Try to guess the number: "))

    else :
        if user_guess != random_number :
            user_guess = guessing(random_number, user_guess)  
    
        else :
            print("You guessed the number! Good job!")
            break

else :
    print(f"Unfortunately, you run out of attempts. The number was {random_number}. See you next time!")
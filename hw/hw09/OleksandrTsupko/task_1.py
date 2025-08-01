import random

print("Hey there! Welcome to the Number Guessing Game! \n" 
      "Here\'s the rules: program is thinking of a secret number, \n"
      "and you've got 10 tries to guess what it is. After each guess, \n"
      "program\'ll tell you if your number was too high or too low. \n"
      "Good luck!")

def compare_numbers(secret_number, users_input):
    '''
    The function compares the guessed number to the user's input 
    and tells the user if their guess was greater or less
    '''

    if users_input > secret_number:
        print("Your entered number is greater than guessed number..")
        return True
    elif users_input < secret_number:
        print("Your entered number is less than guessed number..")
        return True
    else:
        print("Congratulation! You guessed the number!")
        return False


def play_game():
    '''
    Prompts the user to enter numbers and compares each input
    with a pre-determined guessed number.

    This function continues to receive input until the user 
    either correctly guesses the number or exhausts 10 attempts, 
    utilizing the comparing_guessed_and_users_numbers() function 
    for comparison and feedback.
    '''

    secret_number = random.randint(1, 100)

    attempt_number = 1

    while attempt_number <=10:
        user_number = int(input(f"{attempt_number} attempt. Enter your number..\n"))
        
        if compare_numbers(secret_number, user_number):
            attempt_number += 1
        else:
            break

    else:
        print("\nGame Over!\n"
        "How unfortunate! You didn't quite guess the number this time.\n"
        f"The secret number was {secret_number}. "
        "Better luck next time!")

play_game()

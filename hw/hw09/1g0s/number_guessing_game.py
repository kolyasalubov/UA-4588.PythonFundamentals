import random

def number_guessing_game() -> None:
    """
    A number guessing game where the user has 10 attempts to guess a random number between 1 and 100.
    
    The game provides feedback whether the guess is higher or lower than the target number.
    After 10 attempts or a correct guess, the game ends with an appropriate message.
    """
    target_number: int = random.randint(1, 100)
    max_attempts: int = 10
    attempts: int = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    print()
    
    while attempts < max_attempts:
        attempts += 1
        
        try:
            guess: int = int(input(f"Attempt {attempts}/{max_attempts}: Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                attempts -= 1
                continue
                
            if guess == target_number:
                print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts!")
                return
            elif guess < target_number:
                print("Your guess is too low. Try a higher number.")
            else:
                print("Your guess is too high. Try a lower number.")
                
        except ValueError:
            print("Please enter a valid integer.")
            attempts -= 1
            
        print()
    
    print(f"Game over! You've used all {max_attempts} attempts.")
    print(f"The number I was thinking of was {target_number}.")

if __name__ == "__main__":
    number_guessing_game()
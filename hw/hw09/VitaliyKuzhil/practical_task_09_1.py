import random


def random_num() -> int:
    '''
    Function which generate random number from 1 to 100
    '''
    return random.randint(1, 100)


def check_user_input_is_digit(user_str:str) -> bool:
    '''
    Function that checks if the input is number.
    '''
    return True if user_str.isdigit() else False


def check_user_input_range(user_num: int) -> bool:
    '''
    Function that checks is the input in the range from 1 to 100
    '''
    return True if 0 < user_num <= 100 else False 


def input_user_num() -> int:
    '''
    Function which get user number
    '''
    user_input = input('Write your number: ')

    # Check if the input is number
    if check_user_input_is_digit(user_input) is False:
        print('Please enter correct integer number.')
        user_input = input_user_num()
    else:
        user_input = int(user_input)

    # Check if the number in the range from 1 to 100
    if check_user_input_range(user_input) is False:
        print('Enter number of range from 1 to 100.')
        user_input = input_user_num()
    
    return user_input

if __name__ == '__main__':

    def start_game(attempts: int = 10):
        '''
        Function which compare random number with guesses number
        '''
        # Get random number
        rand_num = random_num()
        # print(rand_num)

        # Compare random numbers and guesses number
        while attempts > 0:
            guess_num = input_user_num()
            attempts -= 1
            
            if guess_num  == rand_num:
                print('Congratulation!')
                break
            elif guess_num < rand_num:
                print(f'The number is more than {guess_num}. Try again...')
                continue
            elif guess_num > rand_num:
                print(f'The number is less than {guess_num}. Try again...')
                continue
        else:
            print('Your attempts over')


    def info_about_game():
        '''
        Function in which user get to know rules of game.
        Auto start the game after rules.
        '''
        print('Hi! Let\'s play a game in which you try to guess a number that I chose in the range from 1 to 100.')
        
        # Start a game
        start_game()

    # Run info about game
    info_about_game()

import random

random_num = random.randint(1, 100)
try_num = 10
user_num = 0

while user_num != random_num:
    user_num = int(input('Try to guess number: '))
    try_num -= 1
    try_str = f'{try_num} more tries' if try_num > 1 else f'{try_num} more try'
    
    if try_num < 1:
        print('You loose!')
        break
    else:
        if user_num > random_num:
            print(f'The number is lower! You have {try_str} ')
        elif user_num < random_num:
            print(f'The number is higher! You have {try_str}')
        else:
            print('You win!')
        


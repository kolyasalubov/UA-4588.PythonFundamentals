from random import randint

value = randint(1,100)

print('\nHi!\nI\'ve already thought of a number, try to guess it.')

for attempt in range(10, 0, -1):
    print(f'\nYou have {attempt} attempts left.{value}')
    userAttempt = int(input('Your guess: '))

    if userAttempt == value:
        print(f'You win!\nMy number is {attempt}')
        break
    elif userAttempt > value:
        print('Your number is greater than mine!')
    elif userAttempt < value:
        print('Your number is less than mine!')

else:
    print('Unfortunately you have no attempts left.')


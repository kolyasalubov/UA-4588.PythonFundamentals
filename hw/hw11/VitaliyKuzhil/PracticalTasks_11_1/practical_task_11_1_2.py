days_of_the_week = {1:'Monday',
                    2:'Tuesday',
                    3:'Wednesday',
                    4:'Thursday',
                    5:'Friday',
                    6:'Saturday',
                    7:'Sunday'}


def start_program():
    '''
    Function which show name days of the week
    '''
    try:
        print(days_of_the_week[int(input('Enter number from 1 to 7: '))])
    except ValueError:
        print('You must enter the number')
    except KeyError:
        print('There is no day of the week into this number')
    finally:
        print('-' * 35)
        user_choice()


def user_choice():
    '''
    Function which check if user want to exit
    '''
    match input('Enter "c" to continue or "e" to exit\nMake your choice: '):
            case 'c':
                print('Let\'s continue...')
                start_program()
            case 'e':
                print('See you later!')
            case _ :
                print('Wrong value. Goodbye!')


if __name__ == '__main__':
    print('The program is starting')
    start_program()

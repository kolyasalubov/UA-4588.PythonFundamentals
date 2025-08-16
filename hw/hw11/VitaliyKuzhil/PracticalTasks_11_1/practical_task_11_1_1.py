class NegativeNumber(Exception):
    '''
    Custom Exception (Raise when user enter negative number of age)
    '''
    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return self.age


def user_input_age():
    '''
    Function which get user age
    '''
    return input('Enter your age: ')


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


def check_if_age_is_positive(user_age:int):
    '''
    Function which check if user age is positive
    '''
    if user_age < 0:
        raise NegativeNumber('You must enter positive number of age')


def check_type_of_age(number:int):
    '''
    Function which check type of age
    '''
    if number % 2 == 0:
        return'Your age is even'
    else:
        return'Your age is odd'


def start_program():
    '''
    Main function which start checking user age
    '''
    try:
        # Check if user input number
        user_age = int(user_input_age())

        # Check if user age is positive
        check_if_age_is_positive(user_age=user_age)

    except ValueError:
        print('You entered incorrect value')
    
    except NegativeNumber as exception:
        print(exception)
    
    else:
        print(check_type_of_age(number=user_age))
    
    finally:
        print('-' * 35)
        user_choice()



if __name__ == '__main__':
    print('The program is starting')
    start_program()
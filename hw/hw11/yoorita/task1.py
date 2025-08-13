class LessThanZeroError(Exception):
    def __init__(self, error_data = 'Less than zero value is not allowed'):
        self.data = error_data

    def __str__(self):
        return repr(self.data)


def check_age(user_data: int):
    if user_data < 0:
        raise LessThanZeroError()
    print(f'The age is {'even' if user_data % 2 == 0 else 'odd'} number')


if __name__ == "__main__":
    while True:
        try:
            age = int(input('Please, enter your age: '))
            check_age(age)
        except ValueError:
            print('ValueError: The age should be an integer number!')
        except LessThanZeroError as e:
            print(f'LessThanZeroError: {e.data}')
        else:
            break
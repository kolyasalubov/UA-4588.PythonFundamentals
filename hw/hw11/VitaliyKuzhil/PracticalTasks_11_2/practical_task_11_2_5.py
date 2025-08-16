'''
Write your code bellow to create custom Error named InputError and function check.

The error must save description of error in data attribute.

In data of error must be written:

"Short text error" if length of string less than 3,
"Long text error" if length of string more than 15,
"Type text error" if we try to check not string.
Your function check will be called from function test_input as shown on screenshot.
'''

def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)


class InputError(Exception):
    '''
    Custom Error
    '''
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check(text):
    '''
    Function which check length of text
    '''
    if not isinstance(text, str):
        raise InputError('Type text error')
    else:
        text_length = len(text)
        if text_length < 3:
            raise InputError('Short text error')
        elif text_length > 15:
            raise InputError('Long text error')
    return True

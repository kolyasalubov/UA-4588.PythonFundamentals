#___________________________ Jenny's secret message _______________________________

def greet(name:str) -> str:
    '''
    Function for greeting users. (Special greet for Johnny)
    '''
    return 'Hello, my love!' if name == 'Johnny' else f'Hello, {name}!'

#------------------------------- Tests --------------------------------------------
print(greet('James'))
print(greet('Jane'))
print(greet('Jim'))

print(greet('Johnny'))

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


# ________________ Simple: Find The Distance Between Two Points ___________________

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)
#----------------------------------------------------------------------------------

# distance = lambda x1, y1, x2, y2: round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)

#------------------------------- Tests --------------------------------------------
print(distance(1, 1, 0, 0))

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

def distance(x1:int, y1:int, x2:int, y2:int) -> float:
    '''
    Function which find the distance between two points
    '''
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)
#----------------------------------------------------------------------------------

# distance = lambda x1, y1, x2, y2: round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)

#------------------------------- Tests --------------------------------------------
print(distance(1, 1, 0, 0))


# ____________________________ No yelling! __________________________________________

def filter_words(st:str) -> str:
    '''
    Function which correcting sentence
    '''
    return ' '.join([word.lower() for word in st.split() if word != ' ']).capitalize()

#------------------------------- Tests --------------------------------------------
print(filter_words('HELLO world!'))
print(filter_words('This    will    not    pass '))
print(filter_words('NOW THIS is a VERY EXCITING test!'))
print(filter_words('Extra       white     space     should     also     be     changed   '))

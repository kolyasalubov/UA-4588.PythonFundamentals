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


# ______________________________ Convert a Number to a String! _____________________

def number_to_string(num):
    return str(num)

#------------------------------- Tests --------------------------------------------
print(number_to_string(67))
print(number_to_string(79585))
print(number_to_string(-79585))
print(number_to_string(1+2))
print(number_to_string(1-2))
print(number_to_string(0))



# __________________________ Reversing Words in a String ______________________________

def reverse(st:str) -> str:
    '''
    Function which reversing Words in a String
    '''
    return ' '.join(reversed(st.split()))
# --------------------------------------------------------------------------------------

# def reverse(st:str) -> str:
#     '''
#     Function which reversing Words in a String
#     '''
#     index_ = st.index(' ')
#     return st[index_ + 1:] + ' ' + st[:index_]
# --------------------------------------------------------------------------------------

# reverse = lambda st: ' '.join(st.split()[::-1])

#------------------------------- Tests -------------------------------------------------
print(reverse('Hello World'))
print(reverse('Hi There.'))


# _____________________________ Reverse List Order _____________________________________

def reverse_list(l:list) -> list:
    '''
    Function which reversing list
    '''
    return l[::-1]

#------------------------------- Tests -------------------------------------------------
print(reverse_list([1,2,3,4]))
print(reverse_list([3,1,5,4]))
print(reverse_list([3,6,9,2]))
print(reverse_list([1]))


# ________________________________ Multiples of 3 or 5 __________________________________

def solution(number:int) -> int:
    '''
    Function which multiples all the natural numbers below input number
    '''
    return sum([num for num in range(1, number)
                if num % 3 == 0 or num % 5 == 0]) if number > 0 else 0

#------------------------------- Tests -------------------------------------------------
print(solution(4))
print(solution(6))
print(solution(16))
print(solution(3))
print(solution(5))
print(solution(15))
print(solution(0))
print(solution(-1))
print(solution(10))
print(solution(20))
print(solution(200))


#________________________________ Will you make it? ______________________________________

def zero_fuel(distance_to_pump:int, mpg:int, fuel_left:int) -> bool:
    '''
    Function which calculate possibility should car arrive to pump
    '''
    return True if fuel_left * mpg >= distance_to_pump else False

# ------------------------------- Tests -------------------------------------------------
print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))


# ___________________________________ Are You Playing Banjo? ______________________________

def are_you_playing_banjo(name: str) -> str:
    return name + ' plays banjo' if name.capitalize().startswith('R') else name + ' does not play banjo'

# ----------------------------------- Tests -------------------------------------------------
print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("bravo"))
print(are_you_playing_banjo("rolf"))
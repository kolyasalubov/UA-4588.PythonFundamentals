import math

# Task 1 - Jenny's secret message
def greet(name):
    return "Hello, my love!" if name == 'Johnny' else f"Hello, {name}!"

# Task 2 - Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)

# Task 3 - No yelling!
def filter_words(st):
    new_st = st.capitalize().split() 
    return ' '.join(new_st)

# Task 4 - Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Task 5 - Reversing Words in a String
def reverse(st):
    return ' '.join(st.split(' ')[::-1])

# Task 6 - Reverse List Order
def reverse_list(l):
    return l[::-1]

# Task 7 - Multiples of 3 or 5
def solution(number):
    list = []
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            list.append(num)
    return sum(list)

# Task 8 - Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# Task 9 - Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f'{name} plays banjo' if name[0].lower() == 'r' else f"{name} does not play banjo"

#Task 10 - Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# Task 11 - Counting sheep...
def count_sheeps(sheep):
  return sheep.count(True)

# task 12 - Is this my tail?
def correct_tail(body, tail):
     return True if body[-1] == tail else False

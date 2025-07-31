# Task 1---------------------------------
# Jenny's secret message

def greet(name):
    return "Hello, {name}!".format(name = 'my love' if name == "Johnny" else name)


# Task 2---------------------------------
# Find The Distance Between Two Points

from math import sqrt

def distance(x1, y1, x2, y2):
    return round(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)


# Task 3---------------------------------
# No yelling!

def filter_words(st):
    return ' '.join(st.split()).capitalize()


# Task 4---------------------------------
# Convert a Number to a String!

def number_to_string(num):
    return str(num)


# Task 5---------------------------------
# Reversing Words in a String

def reverse(st):
    return ' '.join(st.split()[::-1])


# Task 6---------------------------------
# Reverse List Order
def reverse_list(l):
    return l[::-1]


# Task 7---------------------------------
# Reverse List Order
def solution(number):
    sum = 0
    for num in range(number):
        if num % 5 == 0 or num % 3 == 0:
            sum += num
    return sum

# Task 8---------------------------------
# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


# Task 9---------------------------------
# Are You Playing Banjo?

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower()[0] == 'r' else f"{name} does not play banjo"


# Task 10---------------------------------
# Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Task 11---------------------------------
# Counting sheep...

def count_sheeps(sheep):
  return sheep.count(True)

# Task 11---------------------------------
# Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail



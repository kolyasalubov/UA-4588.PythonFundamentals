import math

# Jenny's secret message
def greet(name):
    return f"Hello, {"my love" if name == 'Johnny' else name}!"


# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)), 2)


# No yelling!
def filter_words(st: str):
    return " ".join(st.split()).capitalize()


# Convert a Number to a String!
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    return " ".join(st.split()[::-1])


# Reverse List Order
def reverse_list(l):
    return l[::-1]


# Multiples of 3 or 5
def solution(number):
    return sum(i for i in range(0, number) if i % 3 == 0 or i % 5 == 0)


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} {'plays' if name.lower()[0] == 'r' else 'does not play'} banjo"


# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Counting sheep...
def count_sheeps(sheep):
  return sheep.count(True)


# Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail


print(solution(5))
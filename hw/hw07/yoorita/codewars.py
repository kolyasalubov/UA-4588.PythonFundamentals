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
    pass

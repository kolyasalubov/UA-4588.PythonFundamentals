# I. Jenny's secret message
def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"

# II. Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)

# III. No yelling!
def filter_words(st):
    return " ".join(st.lower().capitalize().split())

# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
def reverse(st):
    li = st.split()
    st = " ".join(str(element) for element in li[::-1])
    return st

# VI. Reverse List Order
def reverse_list(l):
  return l[::-1]

# VII. Multiples of 3 or 5
def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo" 
    return name + " does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)

# XII. Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail
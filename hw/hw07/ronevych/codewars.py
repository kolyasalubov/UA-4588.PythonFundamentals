# Jenny's Secret Message!

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else: 
        return f"Hello, {name}!"
    
# Simple: Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 2)

# No yelling!

def filter_words(st):
    st = st.capitalize()
    st = " ".join(st.split())
    return st

# to string

def number_to_string(num):
    return str(num)

# Reversing Words in a String

def reverse(st):
    return " ".join(st.split()[::-1])

# Reverse List Order

def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

# Multiples of 3 or 5

def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0] == 'r' or name[0] =='R':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    

# Convert a Boolean to a String

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
# Counting sheep...

def count_sheeps(sheep):    
    return sheep.count(True)

# Is this my tail?

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
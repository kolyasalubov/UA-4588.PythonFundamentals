# --- Jenny's secret message ---
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


# --- Find The Distance Between Two Points ---
from math import *
def distance(x1, y1, x2, y2):
    distance_variable = sqrt((x2-x1)** 2 + (y2-y1)**2)
    distance_variable = round(distance_variable, 2)
    return distance_variable


# --- No yelling! ---
def filter_words(st):
    st = st.split()
    st = " ".join(st)
    st = st.capitalize()
    
    return st


# --- Convert a Number to a String ---
def number_to_string(num):
    num = str(num)
    
    return num


# --- Reversing Words in a String ---
def reverse(st):
    st = st.split()
    st.reverse()
    st = " ".join(st)
    
    return st


# --- Reverse List Order ---
def reverse_list(l : list):
    l.reverse()
    return l


# --- Multiples of 3 or 5 ---
def solution(number):
    sum = 0
    if number < 0 :
        return 0
    for i in range(number) :
        if i % 3 == 0 and i % 5 == 0 or i % 3 == 0 or i % 5 == 0 :
            sum += i
    
    return sum


# --- Will you make it? ---
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump :
        return True
    else :
        return False
    

# --- Are You Playing Banjo? ---
def are_you_playing_banjo(name):
    if name[0].lower() == "r" :
        name = name + " plays banjo"
    else :
        name = name + " does not play banjo"
        
    return name


# --- Convert boolean values to strings 'Yes' or 'No’ ---
def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"


# --- Counting sheep ---
def count_sheeps(sheep):
    return sheep.count(True)


# --- Is this my tail? ---
def correct_tail(body, tail):
    return True if tail == body[-1] else False
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






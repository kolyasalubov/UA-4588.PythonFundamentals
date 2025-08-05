# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

# II. Find The Distance Between Two Points
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

# III. No yelling!
def filter_word(text):
    words = text.split()
    words = [word.lower().capitalize() for word in words]
    return ' '.join(words)


# IV. Convert a Number to a String
def num_to_str(num):
    return str(num)

# V. Reversing Words in a String

def rev_word(text):
    return ' '.join(text.strip().split()[::-1])

# VI. Reverse List Order

def reverse(l):
    return l[::-1]

# VII. Multiples of 3 or 5

def sum_multiples(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0) if n > 0 else 0

# VIII. Will you make it?

def can_pump(distance, fuel_left, fuel_efficiency):
    max_distance = fuel_left * fuel_efficiency
    return distance <= max_distance

# IX. Are You Playing Banjo?

def banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’

def boolean_to_string(b):
    return 'Yes' if b else 'No'

# XI. Counting sheep

def count_sheep(sheep):
    return sum(1 for s in sheep if s is True)

# XII. Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail

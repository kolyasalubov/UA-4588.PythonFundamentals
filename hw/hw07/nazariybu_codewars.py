# Task I
# Jenny's secret message
# Jenny has written a function that returns a greeting for a user.
#  However, she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
# Can you help her?

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# ------------------------------------------------------------------------------------------
# Task II.
# Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     x = (x2 - x1) ** 2 
#     y = (y2 - y1) ** 2
#     sqrt = (x + y) ** 0.5
#     result = round(sqrt, 2)
#     return result

# print(distance(1,1,0,0))

# ------------------------------------------------------------------------------------------
# Task III. 
# No yelling!
# Write a function taking in a string 
# like WOW this is REALLY          amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. Using re and string is not allowed.

# def filter_words(st):
#    st = st.capitalize()
#    st = " ".join(st.split())
#    return st

# print(filter_words('This    will    not    pass '))
# print(filter_words('HELLO world!'))

# ------------------------------------------------------------------------------------------

# Task IV.
# Convert a Number to a String
# We need a function that can transform a number (integer) into a string.

# def number_to_string(num):
#     return str(num)

# print(number_to_string(123))

# ------------------------------------------------------------------------------------------

# Task V.
# Reversing Words in a String
# You need to write a function that reverses the words in a given string.
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# def reverse(st):
#     st = st.split()
#     st = ' '.join(st[::-1])
#     return st


# print(reverse("Hello World"))

# ------------------------------------------------------------------------------------------

# Task VI. 
# Reverse List Order
# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# def reverse_list(l):
#     return l[::-1]

# print(reverse_list([1, 2, 3, 4]))

# ------------------------------------------------------------------------------------------

###CODEWARS###

# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    x_value = x2 - x1
    y_value = y2 -y1
    result = (x_value * x_value) + (y_value *y_value)
    result = result ** 0.5
    result = round(result, 2)
    return result


#III. No yelling!
def filter_words(st):
    a = st.capitalize()
    b = " ".join(a.split())
    return b


# IV. Convert a Number to a String
def number_to_string(num):
    stringing_num = str(num)
    return stringing_num


# V. Reversing Words in a String
def reverse(st):
    st_list = st.split()
    new_st_list = st_list[::-1]
    st = " ".join(new_st_list)
    return st


# VI. Reverse List Order
def reverse_list(l):
    new_l = l[::-1]
    return new_l


# VII. Multiples of 3 or 5
def solution(number):
    total = 0
    if number <= -1:
        return 0
    else:
        a = range(number)
        for x in a:
            if x % 3 == 0 or x % 5 == 0:
                total += x
    return total


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True

    else:
        return False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    idex_type = bool(boolean)
    if idex_type:
        return "Yes"
    else:
        return "No"

# XI. Counting sheep
def count_sheeps(sheep):
    counter = 0
    for x in sheep:
        if x is True:
            counter += 1
    return counter

# XII. Is this my tail?
def correct_tail(body, tail):
    body = body[-1]
    if body == tail:
        return True
    else:
        return False


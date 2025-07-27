# # I. Jenny's secret message
# # https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python


# def greet(name):

#     if name == "Johnny":
#         return "Hello, my love!"

#     return f"Hello, {name}!"


# # _____________________________________________________________________
# # II. Find The Distance Between Two Points
# # https://www.codewars.com/kata/58b309e4bffc6b0a09000036/train/python


# def distance(x1, y1, x2, y2):
#     return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)


# # _____________________________________________________________________
# # III. No yelling!
# # https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python


# def filter_words(st):
#     sentence = ' '.join(st.lower().split()).capitalize()
#     return sentence


# # _____________________________________________________________________
# # IV. Convert a Number to a String
# # https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python


# def number_to_string(num):
#     return str(num)


# # _____________________________________________________________________
# # V. Reversing Words in a String
# # https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python


# def reverse(s):
#     words = s.strip().split()
#     words.reverse()
#     return ' '.join(words)


# # _____________________________________________________________________
# # VI. Reverse List Order
# # https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python


# def reverse_list(l):
#     return l[::-1]


# # _____________________________________________________________________
# # VII. Multiples of 3 or 5
# # https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


# def solution(number):
#     if number < 0:
#         return 0
#     count = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             count += i
#     return count


# # _____________________________________________________________________
# # VIII. Will you make it?
# # https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return mpg * fuel_left >= distance_to_pump


# # _____________________________________________________________________
# # IX. Are You Playing Banjo?
# # https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python


# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# # _____________________________________________________________________
# # X. Convert boolean values to strings 'Yes' or 'No’
# # https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python


# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"


# # _____________________________________________________________________
# # XI. Counting sheep
# # https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python


# def count_sheeps(sheep):
#     count = 0
#     for x in sheep:
#         if x is True:
#             count += 1
#     return count


# # _____________________________________________________________________
# # XII. Is this my tail?
# # https://www.codewars.com/kata/is-this-my-tail/train/python


def correct_tail(body, tail):
    return body[-1] == tail


def correct_tail(body, tail):
    return body.endswith(tail)

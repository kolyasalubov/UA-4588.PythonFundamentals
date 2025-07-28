#1----------------------------------------------------
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)



#2----------------------------------------------------
# import math

# def distance(x1, y1, x2, y2):
#     result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     return round(result, 2)

# print(distance(1, 1, 2, 2))



#3----------------------------------------------------
# def filter_words(st):
#     words = st.lower().split()
#     return " ".join(words).capitalize()



#4----------------------------------------------------
# def number_to_string(num):
#     return str(num)



#5----------------------------------------------------
# def reverse(st):
#     return " ".join(st.split()[::-2])



#6----------------------------------------------------
# def reverse_list(l):
#     return l[::-1]



#7----------------------------------------------------
# def solution(number):
#     mul = []
    
#     if number < 0:
#         return 0
    
#     for num in range(number):
#         if num % 3 == 0 or num % 5 == 0:
#             mul.append(num)
    
#     suma = sum(mul)
#     return suma



#8----------------------------------------------------
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / mpg <= fuel_left:
#         return True
#     else:
#         return False
    


#9----------------------------------------------------
# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == "r":
#         return f"{name} plays banjo"
#     return f"{name} does not play banjo"



#10----------------------------------------------------
# def bool_to_word(boolean):
#     if boolean is True:
#         return "Yes"
#     return "No"



#11----------------------------------------------------
# def count_sheeps(sheep):
#     return sheep.count(True)



#12----------------------------------------------------
# def correct_tail(body, tail):
#     sub = body[-len(tail):]
#     if sub == tail:
#         return True
#     else:
#         return False
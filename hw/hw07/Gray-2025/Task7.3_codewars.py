##############################
## I. Jenny's secret message

# def greet(name):
    
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# print(greet("Tom"))


###############################
##      II. Find The Distance Between Two Points
 
# import math
# def distance(x1, y1, x2, y2):
#     return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


###############################
##      III. No yelling!

# def filter_words(st):
#     st = st.capitalize()
#     st = st.split()
#     return(" ".join(st))
    
# print(filter_words("TOM       heLLO"))


#################################
##      IV. Convert a Number to a String

# def number_to_string(num):
#     return str(num)


#################################
##      V. Reversing Words in a String

# def reverse(st):
#     st = st.split()
#     st = reversed(st)
#     return(" ".join(st))

# print(reverse("Hello     World   "))


################################
##      VI. Reverse List Order

# def reverse_list(l):
#     'return a list with the reverse order of l'
#     return list(reversed(l))


###############################
##      VII. Multiples of 3 or 5
# Якщо ми перерахуємо всі натуральні числа нижче 10, які є кратними 3 або 5, ми отримаємо 3, 5, 6 та 9.
# Сума цих кратних дорівнює 23.
# Завершіть розв'язок так, щоб він повертав суму всіх чисел, кратних 3 або 5, менших за передане число.
# Крім того, якщо число від'ємне, повертається 0.
# Примітка: Якщо число кратне і 3, і 5, порахуйте його лише один раз .

# def solution(number):
#     if number > 0:
#         index_3and5_lst = []
#         for i in range(0, number, 3):
#             index_3and5_lst.append(i)
        
#         for x in range(0, number, 5):
#             index_3and5_lst.append(x)    

#         index_3and5_set = set(index_3and5_lst)
#         end_list = list(index_3and5_set)
#         return sum(end_list)
#     else:
#         return(0)


################################
##      VIII. Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return fuel_left * mpg >= distance_to_pump
    
# print(zero_fuel(100, 50, 1))


###############################
##      IX. Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0].lower() == "r":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"

 
###############################
##      X. Convert boolean values to strings 'Yes' or 'No’

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"


###############################
##      XI. Counting sheep

# def count_sheeps(sheep):  
#     return sheep.count(True)


################################
##      XII. Is this my tail?

# def correct_tail(body, tail):
#     animal = list(body)
#     # return tail
#     if animal.pop() == tail:
#         return True
#     else:
#         return False
    
# print(correct_tail("Fox", "x"))
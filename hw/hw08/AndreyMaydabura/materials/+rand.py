# random
# The random() method returns a
# random floating number between 0 and 1.
##########################################
# import random

# print(random.random())


############################################
# функція randint(a,b) вибирає
# випадкове ціле число із
# заданого діапазону(a,b)
############################
# import random

# print(random.randint(1,50))
# ##########################
# функція choice()
# вибирає випадковий
# елемент зі списку
#######################
# import random

# colors_list=["red","green","black","white","yellow"]

# print(random.choice(colors_list))
# # # # # #################
# print(dir(random))
# 3
# The sample() method returns a list with
# a randomly selection of a specified
# number of items from a sequnce.

# Note: This method does not change the original sequence.
# 3

# import random

# mylist = ["apple", "banana", "cherry", "melon","watermelon","orange"]

# print(random.sample(mylist, k=3))
# print(mylist)

# ###########################
# функція shuffle() перемішує
# список міняючи його елементи
# місцями
############################
# The shuffle() method takes a sequence
# (list, string, or tuple) and reorganize
# the order of the items.

# Note: This method changes the original list/tuple/string,
# it does not return a new list/tuple/string.
#############################
# import random

# colors_list=["red","green","black","white","yellow"]
# print(colors_list)

# random.shuffle(colors_list)
# print(colors_list)

# random.shuffle(colors_list)
# print(colors_list)


###################
# Модуль sys забезпечує
# доступ до деяких змінних
# і функцій, які взаємодіють
# з інтерпритатором python.
#############################
# sys.argv #ми отримаємо шлях
# до нашого скрипта
########################

# import sys

# print(sys.argv)
#################################
# Recursion layers
########################

# import sys
# print(sys.getrecursionlimit())

######################
# sys.executable
# отримаємо повний шлях
# до інтерпритатора Python
###########################

# import sys

# print(sys.executable)

###################################
# sys.path
# Значення функції path
# модуля sys – це список
# стрічок, які показують
# шлях пошуку для модулів.
# Як правило, дана функція
# показує Python, в яких
# локаціях дивитись, коли
# він намагається імпортувати
# модуль.
# Відповідно до документації Python,
# sys.path ініціалізується з змінною
# оточення PYTHONPATH
##################################
# import sys


# print(sys.path)

###################################
# Дана функція може бути корисною
# при відлагодженні причин, при
# яких модуль не імпортується.
# Ми також можемо змінити шлях.
# Так як дана функція є шляхом
# ми можемо добавляти або видаляти
# шлях з неї:
###########################
# import sys

# sys.path.append("D:/path/to/my/module")

# ######################################
# значення sys.platform – ідентифікатор
# платформи(ОС).
########################################

# import sys
# print(sys.platform)
# 3
# amount references
# work with memory
#############################
# import sys

# l1 = [6, 7, 8]
# l2 = l1
# l3 = l1

# print(sys.getrefcount(l1))

###########################
# import sys

# l1 = [6, 7, 8]
# l1.append(l1)

# print(sys.getrefcount(l1))
# print(l1)
# print(l1 is l1[-1])

#############
# global variable


########################################
# london_co = {'r1': {'hostname': 'london_r1', 'location': '21 New Globe Wal: k', 'vendor': 'Cisco', 'model': '4451',
# 'IOS': '15.4', 'IP': '10.255.0.1'}, 'r2': {'hostname': 'london_r2', 'location': '21 New Globe Walk', 'vendor: ': 'Cisco',
#  'model': '4451', 'IOS': '15.4', 'IP': '10.255.0.2'}, 'sw1': {': hostname': 'london_sw1', 'location': '21 New Globe Walk',
#  'vendor': 'Cisco: ', 'model': '3850', 'IOS': '3.6.XE', 'IP': '10.255.0.101'}}

# print(london_co)
# # # # # # # # # # # ##########################
# from pprint import pprint
# pprint(london_co)

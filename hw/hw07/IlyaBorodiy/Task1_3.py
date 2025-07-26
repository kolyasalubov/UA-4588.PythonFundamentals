###   Task 1

num_1 = input('Enter you number: ')
num_2 = input('Enter you number: ')

def my_func(a, b):
    """
    Return the largest number, from to input
    """
    if a > b:
        print(a)
    else:
        print(b)

my_func(num_1, num_2)


###   Task 2

def rectangle(a, b):
    s_r = a * b
    print("Area of a rectangle: ", s_r)

def triangle(a, b):
    s_t = 0.5 * a * b
    print("Area of a triangle: ", s_t)

def circle(r):
    from math import pi
    s_c = pi * r ** 2
    print("Area of a triangle: ", s_c)

rtc = int(input("Enter num 1 (rectangle), num 2 (triangle) or num 3 (circle ): "))

if rtc == 1:
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    rectangle(a, b)
elif rtc == 2:
    a = float(input("Enter basis: "))
    b = float(input("Enter height: "))
    triangle(a, b)
elif rtc == 3:
    r = float(input("Enter radius: "))
    circle(r)
else:
    print("Error, wrong choice!")


###   Task 3

def str_to_count(s: str):
    counts = {}
    for ch in s.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

s = input("Enter you string: ")
print(str_to_count(s))

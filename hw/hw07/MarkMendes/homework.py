#task 1
print("task 1:")

def compare():
    """compares the first and second number"""

    print("write the first number")
    a = input()
    print("write the second number")
    b = input()

    if(a > b):
        print("first number is bigger")
    else:
        print("second number is bigger")

compare()

#task 2
print("task 2:")

print("write 1 to count rectangle area, 2 for triangle, 3 for circle")

def countRec():
    
    a = int(input())
    b = int(input())

    sum = a * b
    print("Area of this rectangle is: " + str(sum))
def countTria():

    a = int(input())
    va = int(input())

    sum = a * va
    print("Area of this triangle is: " + str(sum))
def countCir():

    r = int(input())
    PI = 3,14

    sum = PI*r*r
    print("Area of this circle is:" + str(sum))

option = int(input())


if(option == 1):
    countRec()
elif(option == 2):
    countTria()
else:
    countCir()

#task 3
print("task 3:")

def count_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts
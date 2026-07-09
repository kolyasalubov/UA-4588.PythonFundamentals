def max_of_two(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return 'Same numbers'

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(max_of_two(a,b))
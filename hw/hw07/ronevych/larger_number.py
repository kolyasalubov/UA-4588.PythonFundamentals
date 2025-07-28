def define_larger_number(a, b):
    
    """
    This function defines a large number.
    
    realises the larger of two numbers.
    If both numbers are equal, it returns a message indicating that.
    
    Параметри:
    a (int): The first number.
    b (int): The second number.
    
    Повертає:
    int or str: The larger number, or a message if both are equal.
    """
    
    if a > b:
        large_number = a
    elif a < b:
        large_number = b
    else:
        large_number = "Both numbers are equal"
    return large_number

a, b = input("Enter two numbers separated by a space: ").split()
a = int(a)
b = int(b)
result = define_larger_number(a, b)
print(f"The larger number is: {result}")
# print(help(define_larger_number))  
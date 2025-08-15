def largest_number(num1 : int | float = 0, num2 : int | float = 0) :
    """This function returns the largest number of two numbers"""
    if num1 > num2 :
        return num1
    else : 
        return num2
    
print(largest_number(5, 10)) # Output : 10
print(largest_number(-7, -49)) # Output : -7
print(largest_number(-88)) # Output : 0
print(largest_number(6.3, 9.8)) # Output : 9.8
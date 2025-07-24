def maxNumber(num1, num2):
    """
    This function takes two numeric arguments and returns the larger of the two.
    If either argument is not a numeric data type (int or float), it returns an error
    """

    if type(num1) == int or type(num1) == float: 
        if type(num2) == int or type(num2) == float: 
            return num1 if num1 > num2 else num2
        else:
            return "The second argument is not a numeric data type."
    else:
        return "The first argument is not a numeric data type."


############  Test  #############

# print(maxNumber(12, 23))
# print(maxNumber(23, 23))
# print(maxNumber(23, 12))
# print(maxNumber("23", 12))
# print(maxNumber("Number", 12))
# print(maxNumber(23, "Number"))
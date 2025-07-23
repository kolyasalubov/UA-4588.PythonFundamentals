def comparing_two_numbers(number1, number2):
    """
    This function returns the largest number of two given numbers
    """
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        print("Numbers are equal")
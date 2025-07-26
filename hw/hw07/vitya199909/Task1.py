def max_of_two_numbers(a, b):
    """
    Find the maximum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The maximum of the two numbers.
    """
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Both numbers are equal"
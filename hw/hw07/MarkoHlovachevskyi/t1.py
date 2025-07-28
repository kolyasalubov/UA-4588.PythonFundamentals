def max_of_two(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: The larger number
    """
    return a if a > b else b
print(max_of_two(10, 20))  # Виведе: 20
print(max_of_two(-5, -1))  # Виведе: -1

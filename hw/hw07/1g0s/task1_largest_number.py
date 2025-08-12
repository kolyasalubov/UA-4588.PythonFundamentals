def largest_number(num1, num2):
    """
    Function to return the largest of two numbers.

    Parameters:
        num1 (int or float): First number.
        num2 (int or float): Second number.

    Returns:
        int or float: The larger number between num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2


if __name__ == "__main__":
    # Test the function
    print(largest_number(10, 5))    # Output: 10
    print(largest_number(3.5, 7.2))  # Output: 7.2
    print(largest_number(-5, -10))   # Output: -5
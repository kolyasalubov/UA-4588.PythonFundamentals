def largest_of_two(first: int | float, second: int | float):
    """This function returns the largest number of two numbers"""
    return first if first >= second else second

# Test function
print(largest_of_two(3, 5))
print(largest_of_two(-4, 2.9))
print(largest_of_two(9.8, -4.5))
def get_largest_number(num_one, num_two):
    """
    The function returns the largest of the two given numbers.
    """

    return num_one if num_one > num_two else num_two

print(get_largest_number(20, 5))
print(get_largest_number.__doc__)

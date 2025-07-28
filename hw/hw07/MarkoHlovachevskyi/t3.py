def count_characters(s):
    """
    Count the number of each character in a string.

    Parameters:
    s (str): Input string

    Returns:
    dict: Dictionary with character counts
    """
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

# Example usage
print(count_characters("hello"))
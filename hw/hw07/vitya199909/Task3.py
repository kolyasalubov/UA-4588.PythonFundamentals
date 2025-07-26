def count_characters(input_string):
    """Counts the occurrences of each character in the input string.

    Args:
        input_string (str): The input string.

    Returns:
        dict: A dictionary where the key is a character and the value is its count in the string.
    """
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


input_string = input("Enter a string: ")
print(count_characters(input_string))
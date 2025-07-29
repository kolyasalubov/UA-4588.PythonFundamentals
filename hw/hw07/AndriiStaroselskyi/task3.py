def get_string_chars_number(string: str):
    """
    Calculates the number of characters included in a given string
    """
    values = {}
    string = string.lower()
    for char in string:
        if char not in values:
            values[char] = string.count(char)
    
    return values
    
print(get_string_chars_number("hello"))

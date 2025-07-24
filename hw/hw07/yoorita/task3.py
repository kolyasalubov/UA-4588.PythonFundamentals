def calculate_chars(string: str):
    result = {}
    for char in set(string):
        result[char] = string.count(char)
    return result

# Test
print(calculate_chars("hello"))
print(calculate_chars("entered some text here to test"))
def get_string_chars_number(string: str) :
    values = {}
    string = string.lower()
    for char in string :
        if char not in values :
            values[ char ] = string.count(char)
    print(values)
    return values

get_string_chars_number("HeLLo")
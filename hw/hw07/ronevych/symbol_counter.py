user_input = input(str("Write down your word: "))

def symb_counter(string: str):
    result = {}
    for char in set(string):
        result[char] = string.count(char)
    return result


print(symb_counter(user_input))
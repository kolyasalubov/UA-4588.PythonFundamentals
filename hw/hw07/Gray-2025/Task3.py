def counts_characters(words):
    '''
    Function takes a string and returns the numbers of letters in it.
    '''
    result = {}
    for char in words.lower():
        result[char] = result.get(char, 0) + 1
    return result

# Test example
print(counts_characters("heLlo WOrld"))
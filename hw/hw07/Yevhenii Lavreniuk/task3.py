def count_characters(text):
    """
    This function counts how many times each character appears in a string.
    
    """
    result = {}  

    for char in text:
        if char in result:
            result[char] += 1  
        else:
            result[char] = 1  

    return result
word = "google"
char_count = count_characters(word)
print(char_count)
def char_frequency(text):
    """
    Count the frequency of each character in a string.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency


if __name__ == "__main__":
    # Test the function
    test_string = "hello"
    result = char_frequency(test_string)
    print(f"Input: '{test_string}'")
    print(f"Output: {result}")
    
    # Additional test cases
    print("\nAdditional test cases:")
    print(char_frequency("Hello World!"))  # With spaces and punctuation
    print(char_frequency("aAaA"))          # Case sensitivity test
    print(char_frequency(""))              # Empty string test
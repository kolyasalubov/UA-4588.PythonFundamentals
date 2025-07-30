def amountLetters(string):
    """
    This function takes a string and returns the number of letters in it.
    """

    string = string.lower()
    lettersDict = {}
    
    for char in string:
        if char.isalpha(): 
            if char in lettersDict:
                lettersDict[char] = lettersDict[char] + 1
            else:
                lettersDict[char] = 1

    return lettersDict
    

###########  Test  #############
# print(amountLetters("Hello"))
# print(amountLetters("Hello, World!"))
# print(amountLetters("Python Programming 123!"))
# print(amountLetters("1234567890!@#$%^&*()"))    
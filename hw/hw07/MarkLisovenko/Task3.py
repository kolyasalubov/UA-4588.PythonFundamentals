def amount_of_letter(word : str) :
    word = word.lower()
    WORD = word
    word = list(word)
    for letter in word :
        if word.count(letter) != 1 :
            while word.count(letter) != 1 :
                word.remove(letter)

    letters_and_amounts = {}.fromkeys(tuple(word), 0)

    for key in letters_and_amounts.keys() :
        letters_and_amounts[key] = WORD.count(key)
    print(letters_and_amounts)


#######################################################################################################################


amount_of_letter("Hello")
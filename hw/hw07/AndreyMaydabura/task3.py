def count_characters(your_word):
    my_dict = {}
    for x in your_word:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    return my_dict

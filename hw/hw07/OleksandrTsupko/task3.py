def calculating_number_of_caracters(given_string):
    """
    This function calculates the number of characters included in
    given string
    """
    result = {}
    for i in given_string:
        if result.get(i) == None:
            result[i] = given_string.count(i)
            
    print(result)
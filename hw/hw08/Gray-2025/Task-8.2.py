def password(validity):
    
    import string
    number = list(string.digits)
    lower_letters = list(string.ascii_lowercase)
    capital_letters = list(string.ascii_uppercase)
    symbols = ['#', '$', '@']
    count = len(validity)

    if any(char in validity for char in number)\
        and\
        any(char in validity for char in lower_letters)\
        and\
        any(char in validity for char in capital_letters)\
        and\
        any(char in validity for char in symbols)\
        and\
        6 <= count <= 16:
        return "Password is validity"
    else:
        return "Password is not validity"

# Test example        
print(password("ytgtgtgtgtgT@a1"))
def char_count(s):
    coutns = {}
    for char in s:
        if char in coutns:
            coutns[char] += 1
        else:
            coutns[char] = 1
    return coutns

result = char_count("hello")
print(result)
def solution(number):
    numbers = []
    if number < 0:
        return 0
    else:
        for num in range(1, number):
            if num % 3 == 0 or num % 5 == 0:
                numbers.append(num)
    
    sum = 0
    for i in numbers:
        sum += i
    
    return sum
class MyError(Exception):
    pass

def ageEvenOrOdd(number):
    try:
        if isinstance(number, float):
            raise ValueError
        number = int(number)
        if number < 0:
            return MyError(f"{number} less then 0")
        elif number % 2 == 0:
            return f'{number} is Even'
        else:
            return f'{number} is Odd'
    except ValueError:
        return MyError(f"{number} is not integer")

######### Tests ############

# print(ageEvenOrOdd(18.5))
# print(ageEvenOrOdd(18))
# print(ageEvenOrOdd(21))
# print(ageEvenOrOdd(-3))
# print(ageEvenOrOdd("18"))
# print(ageEvenOrOdd("aaa"))
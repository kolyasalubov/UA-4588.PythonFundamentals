def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age % 2 == 0:
        return "The age is even"
    elif age % 2 != 0:
        return "The age is odd"

try:
    age = int(input("Please enter the age: "))
    check_result = check_age(age)
except Exception as e:
    print(e)
else:
    print(check_result)

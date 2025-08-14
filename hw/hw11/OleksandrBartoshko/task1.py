def check(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    if age % 2 == 0:
        return "your age is even."
    else:
        return "your age is odd."

try:
    user_age = int(input("enter your age: "))
    result = check(user_age)
    print(result)
except ValueError as e:
    print("ERROR", e)

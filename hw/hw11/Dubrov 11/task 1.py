def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")  
    if age % 2 == 0:
        return f"Your age {age} is even."
    else:
        return f"Your age {age} is odd."
        


try:
    age = int(input("Enter your age: "))
    print(process_age(age))
except ValueError as e:
    print(" Error:", e)

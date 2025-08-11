def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")


def main():
    user_input = input("Enter your age: ")
    try:
        age = int(user_input)
        process_age(age)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number in days:
        return f"{number} is {days[number]}"
    else:
        return "Error: number must be between 1 and 7."


def main():
    user_input = input("Enter a number (1-7): ")

    try:
        number = int(user_input)
        result = get_day_of_week(number)
        print(result)
    except ValueError:
        print("Error: please enter a valid number.")


if __name__ == "__main__":
    main()

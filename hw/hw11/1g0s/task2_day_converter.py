class InvalidDayError(Exception):
    """Custom exception raised when day number is not in valid range (1-7)."""
    def __init__(self, day_number: int) -> None:
        super().__init__(f"Invalid day number: {day_number}. Please enter a number between 1 and 7.")
        self.day_number = day_number


def get_day_of_week(number: int) -> str:
    """
    Converts a number (1-7) to corresponding day of the week.
    
    Args:
        number: Day number (1=Monday, 2=Tuesday, ..., 7=Sunday)
        
    Returns:
        str: Name of the day
        
    Raises:
        InvalidDayError: If number is not in range 1-7
    """
    if number < 1 or number > 7:
        raise InvalidDayError(number)
    
    days = {
        1: "Monday",
        2: "Tuesday", 
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    return days[number]


def main() -> None:
    """Main program that handles user input and exception handling."""
    try:
        number_input = input("Enter a number (1-7) to get the day of the week: ")
        number = int(number_input)
        
        day_name = get_day_of_week(number)
        print(f"Day {number} is {day_name}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except InvalidDayError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
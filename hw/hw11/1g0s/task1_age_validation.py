class NegativeAgeError(Exception):
    """Custom exception raised when age is negative."""
    def __init__(self, age: int) -> None:
        super().__init__(f"Age cannot be negative. You entered: {age}")
        self.age = age


def process_age(age: int) -> str:
    """
    Validates age and determines if it's even or odd.
    
    Args:
        age: The age to validate and check
        
    Returns:
        str: "even" or "odd"
        
    Raises:
        NegativeAgeError: If age is negative
    """
    if age < 0:
        raise NegativeAgeError(age)
    
    return "even" if age % 2 == 0 else "odd"


def main() -> None:
    """Main program that handles user input and exception handling."""
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)
        
        result = process_age(age)
        print(f"Your age is {result}")
        
    except ValueError:
        print("Error: Please enter a valid number for your age.")
    except NegativeAgeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()